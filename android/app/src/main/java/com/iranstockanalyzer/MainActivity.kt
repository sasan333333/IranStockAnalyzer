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

        val symbolInput = EditText(this)
        symbolInput.hint = "Symbol"

        val button = Button(this)
        button.text = "Analyze"

        val result = TextView(this)

        layout.addView(symbolInput)
        layout.addView(button)
        layout.addView(result)

        setContentView(layout)

        button.setOnClickListener {
            val symbol = symbolInput.text.toString().trim()

            if (symbol.isEmpty()) {
                result.text = "Enter symbol"
                return@setOnClickListener
            }

            result.text = "Loading..."

            CoroutineScope(Dispatchers.Main).launch {
                try {
                    val data = RetrofitClient.apiService.marketData(symbol)

                    result.text = """
                        Symbol: ${data["symbol"] ?: "-"}
                        Last Price: ${data["last_price"] ?: "-"}
                        Close Price: ${data["close_price"] ?: "-"}
                        Volume: ${data["volume"] ?: "-"}
                    """.trimIndent()

                } catch (e: Exception) {
                    result.text = "Error: ${e.message}"
                }
            }
        }
    }
}
