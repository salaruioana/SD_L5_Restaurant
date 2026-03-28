package com.sd.laborator.models

//Waiters send object Order to the queue where they are taken and prepared
data class Order(
    val idOrder: Int,
    val idWaiter: String,
    val typeMenu: Int //the preparation time depends on the order type
)
