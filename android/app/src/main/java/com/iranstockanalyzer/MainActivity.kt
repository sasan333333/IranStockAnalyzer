package com.iranstockanalyzer

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.LinearLayout
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

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

            result.text = if (symbol.isEmpty()) {
                "Enter symbol"
            } else {
                "Analyzing: $symbol"
            }
        }
    }
}
