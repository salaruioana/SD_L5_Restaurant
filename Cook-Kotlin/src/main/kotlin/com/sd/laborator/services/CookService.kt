package com.sd.laborator.services

import com.sd.laborator.interfaces.Cook
import com.sd.laborator.models.Dish
import com.sd.laborator.models.Order

import org.springframework.stereotype.Service
import java.sql.DriverManager.println

// the CookService represents the concept of a chef that prepares a dish in the kitchen
@Service
class CookService(): Cook {
    private val longId = java.util.UUID.randomUUID().toString()
    private val idUnique: String="Cook_"+longId.subSequence(0,4)
    override fun Cook(order: Order): Dish {
        when(order.typeMenu) {
            1 -> Thread.sleep(1000)
            2 -> Thread.sleep(2000)
            3 -> Thread.sleep(3000)
            4 -> Thread.sleep(4000)
            5 -> Thread.sleep(5000)
            else -> println("Unknown menu ordered")
        }
        return Dish(order.idOrder,idUnique,order.typeMenu)
    }
}