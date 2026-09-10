package com.iranstockanalyzer

import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.iranstockanalyzer.data.api.RetrofitClient
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val textView = TextView(this)
        textView.text = "Loading Market Data..."
        setContentView(textView)

        CoroutineScope(Dispatchers.Main).launch {
            try {
                val data = RetrofitClient.apiService.marketData()
                textView.text = data.toString()
            } catch (e: Exception) {
                textView.text = "Error: ${e.message}"
            }
        }
    }
}
