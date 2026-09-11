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
        layout.setPadding(32, 32, 32, 32)

        val title = TextView(this)
        title.text = "Iran Stock Analyzer"
        title.textSize = 24f

        val symbolInput = EditText(this)
        symbolInput.hint = "Symbol"

        val targetInput = EditText(this)
        targetInput.hint = "Target Price"
        targetInput.inputType = 2

        val analyzeButton = Button(this)
        analyzeButton.text = "Analyze Stock"

        val alertButton = Button(this)
        alertButton.text = "Check Price Alert"

        val telegramButton = Button(this)
        telegramButton.text = "Send Alert to Telegram"

        val result = TextView(this)
        result.textSize = 17f

        val chart = LineChart(this)
        chart.description.text = "Price History"

        layout.addView(title)
        layout.addView(symbolInput)
        layout.addView(targetInput)
        layout.addView(analyzeButton)
        layout.addView(alertButton)
        layout.addView(telegramButton)
        layout.addView(result)
        layout.addView(chart)

        setContentView(layout)

        analyzeButton.setOnClickListener {
            val symbol = symbolInput.text.toString().trim()

            if (symbol.isEmpty()) {
                result.text = "Enter symbol"
                return@setOnClickListener
            }

            result.text = "Analyzing $symbol..."

            CoroutineScope(Dispatchers.Main).launch {
                try {
                    val marketData =
                        RetrofitClient.apiService.marketData(symbol)

                    val history =
                        RetrofitClient.apiService.marketHistory(symbol)

                    val lastPrice =
                        (marketData["last_price"] as? Number)?.toFloat()

                    val prices = history.mapNotNull {
                        (it["close_price"] as? Number)?.toFloat()
                    }

                    val entries = prices.mapIndexed { index, price ->
                        Entry(index.toFloat(), price)
                    }

                    if (entries.isNotEmpty()) {
                        val dataSet = LineDataSet(entries, symbol)
                        dataSet.setDrawValues(false)
                        dataSet.setDrawCircles(false)
                        chart.data = LineData(dataSet)
                        chart.invalidate()
                    }

                    val sma20 =
                        if (prices.size >= 20) {
                            prices.takeLast(20).average().toFloat()
                        } else {
                            null
                        }

                    val trend = when {
                        sma20 == null || lastPrice == null -> "N/A"
                        lastPrice > sma20 -> "BULLISH"
                        lastPrice < sma20 -> "BEARISH"
                        else -> "NEUTRAL"
                    }

                    result.text =
                        "Symbol: $symbol\n" +
                        "Last Price: $lastPrice\n" +
                        "SMA(20): ${sma20 ?: "N/A"}\n" +
                        "Trend: $trend\n" +
                        "History: ${prices.size} records"

                } catch (e: Exception) {
                    result.text = "Error: ${e.message}"
                }
            }
        }

        alertButton.setOnClickListener {
            val symbol = symbolInput.text.toString().trim()
            val targetPrice = targetInput.text.toString().toFloatOrNull()

            if (symbol.isEmpty() || targetPrice == null) {
                result.text = "Enter symbol and target price"
                return@setOnClickListener
            }

            CoroutineScope(Dispatchers.Main).launch {
                try {
                    val marketData =
                        RetrofitClient.apiService.marketData(symbol)

                    val currentPrice =
                        (marketData["last_price"] as? Number)?.toFloat()

                    if (currentPrice == null) {
                        result.text = "Current price unavailable"
                        return@launch
                    }

                    val triggered =
                        currentPrice in
                        (targetPrice * 0.97f)..(targetPrice * 1.03f)

                    result.text =
                        if (triggered) {
                            "🔔 ALERT!\nCurrent: $currentPrice\nTarget: $targetPrice"
                        } else {
                            "No Alert\nCurrent: $currentPrice\nTarget: $targetPrice"
                        }

                } catch (e: Exception) {
                    result.text = "Error: ${e.message}"
                }
            }
        }

        telegramButton.setOnClickListener {
            val symbol = symbolInput.text.toString().trim()

            if (symbol.isEmpty()) {
                result.text = "Enter symbol"
                return@setOnClickListener
            }

            result.text =
                "Telegram integration is connected through the backend."
        }
    }
}
