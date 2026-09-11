package com.iranstockanalyzer

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.LinearLayout
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.github.mikephil.charting.charts.LineChart
import com.github.mikephil.charting.data.Entry
import com.github.mikephil.charting.data.LineData
import com.github.mikephil.charting.data.LineDataSet
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

        val chart = LineChart(this)

        layout.addView(symbolInput)
        layout.addView(button)
        layout.addView(result)
        layout.addView(chart)

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
                    val data = RetrofitClient.apiService.marketHistory(symbol)

                    val entries = data.mapIndexed { index, item ->
                        Entry(
                            index.toFloat(),
                            (item["close_price"] as? Number)?.toFloat() ?: 0f
                        )
                    }

                    val dataSet = LineDataSet(entries, symbol)

                    chart.data = LineData(dataSet)
                    chart.invalidate()

                    result.text = "History: ${data.size} records"

                } catch (e: Exception) {
                    result.text = "Error: ${e.message}"
                }
            }
        }
    }
}
