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
        self.print_insert(order)
        self.buys.append(order)
        self.print_book(order)

    def insert_sell(self, number, price):
        self.current_id += 1
        order_type = "SELL"
        order = Order(order_type, number, price, self.current_id)
        self.print_insert(order)
        self.process_sell(order)
        self.print_book(order)

    def print_sell(self): 
        self.sells.sort(key = lambda x: x.id)
        self.sells.sort(key = lambda x: x.price, reverse=True)
        for sell in self.sells:
            print(f"\t{sell.order_type} {sell.number}@{sell.price} id={sell.id}")

    def print_buy(self):
        self.buys.sort(key = lambda x: x.id)
        self.buys.sort(key = lambda x: x.price, reverse=True)
        for buy in self.buys:
            print(f"\t{buy.order_type} {buy.number}@{buy.price} id={buy.id}")

    def remove_buy(self, buy_to_remove):
        for buy in buy_to_remove:
            del self.buys[self.buys.index(buy)]

    def process_sell(self, order):
        buy_to_remove = list()
        for buy in self.buys:
            if order.price <=buy.price and order.number > 0:
                if order.number < buy.number:
                    buy.number -=order.number
                    print(f"Execute {order.number} at {buy.price} on {self.name}")
                    order.number = 0
                elif order.number > buy.number:
                    order.number -=buy.number
                    print(f"Execute {buy.number} at {buy.price} on {self.name}")
                    buy_to_remove.append(buy)
                else:
                    buy_to_remove.append(buy)
        if order.number > 0:
            self.sells.append(order)
        self.remove_buy(buy_to_remove)

    def remove_sell(self,sell_to_remove):
        for sell in sell_to_remove:
            del self.sells[self.sells.index(buy)]

    def process_buy(self, order):
        sell_to_remove =list()
        for sell in self.sells:
            if order.price <= sell.price and order.number > 0:
                if order.number < sell.number:
                    sell.number -= order.number
                    print(f"Execute {order.number} at {sell.price} on {self.name}")
                    order.number = 0
                elif order.number > sell.number:
                    order.number -= sell.number
                    print(f"Execute {sell.number} at {sell.price} on {self.name}")
                    buy_to_remove.append(sell)
                else:
                    buy_to_remove.append(sell)
        if order.number > 0:
            self.buys.append(order)
        self.remove_sell(sell_to_remove)

    def print_insert(self, order):
        print(f"--- Insert {order.order_type} {order.number}@{order.price} id={order.id} on {self.name}")

    def print_book(self, order):
        print(f"Book on {self.name}")
        self.print_sell()
        self.print_buy()
        print("------------------------")


