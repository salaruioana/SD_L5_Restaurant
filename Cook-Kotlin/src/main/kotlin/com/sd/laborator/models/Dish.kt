package com.sd.laborator.models

// cooks take orders from the queue and prepare them, then send the dishes to be served
// we will consider that any waiter can take any dish to the table as long as each orderId is served to its corresponding table
data class Dish(
    val idOrder: Int, // the dish inherits the id of the order and is taken to the proper table based on it
    val idCook: String,
    val typeMenu: Int // not sure if this is necessary yet but will keep it for traceability
)
