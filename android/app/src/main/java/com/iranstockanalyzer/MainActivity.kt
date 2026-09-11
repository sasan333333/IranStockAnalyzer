package com.iranstockanalyzer

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.LinearLayout
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.github.mikephil.charting.charts.LineChart
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
        title.textSize = 24f

        val symbolInput = EditText(this)
        symbolInput.hint = "Enter Symbol"

        val analyzeButton = Button(this)
        analyzeButton.text = "Analyze"

        val result = TextView(this)
        result.textSize = 18f

        val chart = LineChart(this)

        layout.addView(title)
        layout.addView(symbolInput)
        layout.addView(analyzeButton)
        layout.addView(result)
        layout.addView(chart)

        setContentView(layout)

        analyzeButton.setOnClickListener {
            val symbol = symbolInput.text.toString().trim()

            if (symbol.isEmpty()) {
                result.text = "Enter symbol"
                return@setOnClickListener
            }

            result.text = "Loading..."

            CoroutineScope(Dispatchers.Main).launch {
                try {
                    val data = RetrofitClient.apiService.marketHistory(symbol)
                    result.text = "History: ${data.size} records"
                } catch (e: Exception) {
                    result.text = "Error: ${e.message}"
                }
            }
        }
    }
}
