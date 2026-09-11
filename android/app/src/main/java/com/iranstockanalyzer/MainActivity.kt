package com.iranstockanalyzer

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.LinearLayout
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.iranstockanalyzer.data.api.RetrofitClient
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val layout = LinearLayout(this)
        layout.orientation = LinearLayout.VERTICAL
        layout.setPadding(32, 32, 32, 32)

        val title = TextView(this)
        title.text = "Iran Stock Analyzer"
        title.textSize = 26f

        val symbolInput = EditText(this)
        symbolInput.hint = "Enter Symbol"

        val analyzeButton = Button(this)
        analyzeButton.text = "Analyze Stock"

        val result = TextView(this)
        result.textSize = 18f
        result.text = "Ready"

        layout.addView(title)
        layout.addView(symbolInput)
        layout.addView(analyzeButton)
        layout.addView(result)

        setContentView(layout)

        analyzeButton.setOnClickListener {
            val symbol = symbolInput.text.toString().trim()

            if (symbol.isEmpty()) {
                result.text = "Enter symbol"
                return@setOnClickListener
            }

            result.text = "Loading $symbol..."

            CoroutineScope(Dispatchers.Main).launch {
                try {
                    val marketData =
                        RetrofitClient.apiService.marketData(symbol)

                    val lastPrice =
                        (marketData["last_price"] as? Number)?.toFloat()

                    val closePrice =
                        (marketData["close_price"] as? Number)?.toFloat()

                    val volume =
                        (marketData["volume"] as? Number)?.toLong()

                    result.text =
                        "Symbol: $symbol\n\n" +
                        "Last Price: ${lastPrice ?: "N/A"}\n" +
                        "Close Price: ${closePrice ?: "N/A"}\n" +
                        "Volume: ${volume ?: "N/A"}"

                } catch (e: Exception) {
                    result.text = "Error: ${e.message}"
                }
            }
        }
    }
}
