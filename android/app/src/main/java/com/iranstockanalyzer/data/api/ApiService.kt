package com.iranstockanalyzer.data.api

import retrofit2.http.GET

interface ApiService {

    @GET("health")
    suspend fun healthCheck(): Map<String, String>
}
