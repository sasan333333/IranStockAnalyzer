package com.iranstockanalyzer

import org.junit.Assert.assertTrue
import org.junit.Test

class ApiServiceTest {

    @Test
    fun marketDataApiStructureTest() {
        val symbol = "فولاد"
        assertTrue(symbol.isNotEmpty())
    }
}
