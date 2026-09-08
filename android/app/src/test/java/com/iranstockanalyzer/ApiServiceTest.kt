package com.iranstockanalyzer

import com.iranstockanalyzer.data.api.ApiService
import kotlinx.coroutines.runBlocking
import org.junit.Test
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import org.junit.Assert.assertEquals

class ApiServiceTest {

    @Test
    fun healthCheck_returnsOk() = runBlocking {
        val api = Retrofit.Builder()
            .baseUrl("http://10.0.2.2:8000/")
            .addConverterFactory(GsonConverterFactory.create())
            .build()
            .create(ApiService::class.java)

        val result = api.healthCheck()

        assertEquals("ok", result["status"])
    }
}
