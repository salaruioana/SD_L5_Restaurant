package com.sd.laborator.interfaces

import com.sd.laborator.models.Dish
import com.sd.laborator.models.Order

interface Cook {
    fun Cook(order: Order): Dish
}