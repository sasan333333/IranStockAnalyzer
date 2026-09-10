package com.iranstockanalyzer.data.api

import retrofit2.http.GET
import retrofit2.http.Path

interface ApiService {

    @GET("health")
    suspend fun health(): Map<String, String>

    @GET("market-data/{symbol}")
    suspend fun marketData(
        @Path("symbol") symbol: String
    ): Map<String, Any>

    @GET("market-history/{symbol}")
    suspend fun marketHistory(
        @Path("symbol") symbol: String
    ): List<Map<String, Any>>
}
