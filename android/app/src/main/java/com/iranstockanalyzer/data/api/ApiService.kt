package com.iranstockanalyzer.data.api

import retrofit2.http.GET

interface ApiService {

    @GET("health")
    suspend fun health(): Map<String, String>

    @GET("market-data")
    suspend fun marketData(): Map<String, Any>
}
