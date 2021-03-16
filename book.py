#!/usr/bin/env python3

class Order:
    def __init__(self, order_type, number, price, order_id):
        self.order_type = order_type
        self.number = number
        self.price = price
        self.id = order_id

class Book:
    def __init__(self, book_name):
        self.name = book_name
        self.buys = list()
        self.sells = list()
        self.current_id = 0

    def insert_buy(self, number, price):
        self.current_id += 1
        order_type = "BUY"
        order = Order(order_type, number, price, self.current_id)
        self.buys.append(order)
        self.print_book(order)
    
    def insert_sell(self, number, price):
        self.current_id += 1
        order_type = "SELL"
        order = Order(order_type, number, price, self.current_id)
        self.sells.append(order)
        self.print_book(order)

    def print_sell(self):
        self.sells.sort(key = lambda x: x.id)
        self.sells.sort(key = lambda x: x.price, reverse=True)
        for sell in self.sells:
            print(f"{sell.order_type} {sell.number}@{sell.price} id={sell.id}")

    def print_buy(self):
        self.buys.sort(key = lambda x: x.id)
        self.buys.sort(key = lambda x: x.price, reverse=True)
        for buy in self.buys:
            print(f"{buy.order_type} {buy.number}@{buy.price} id={buy.id}")

    def print_book(self, order):
        print(f"--- Insert {order.order_type} {order.number}@{order.price} id={order.id} on {self.name}")
        print(f"Book on {self.name}")
        self.print_sell()
        self.print_buy()
        print("------------------------")

