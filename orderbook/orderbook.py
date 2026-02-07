class Order:
    def __init__(self, side, price, quantity):
        self.side = side      # "BUY" or "SELL"
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.side} {self.quantity} @ {self.price}"


class OrderBook:
    def __init__(self):
        self.buy_orders = []   # highest price first
        self.sell_orders = []  # lowest price first
        self.trades = []       # record executed trades

    # limiting orders

    def add_limit_order(self, order):
        if order.side == "BUY":
            self.buy_orders.append(order)
            self.buy_orders.sort(key=lambda o: o.price, reverse=True)
        else:
            self.sell_orders.append(order)
            self.sell_orders.sort(key=lambda o: o.price)

        self.match_orders()

    # market orders

    def market_buy(self, quantity):
        while quantity > 0 and self.sell_orders:
            best_sell = self.sell_orders[0]
            trade_qty = min(quantity, best_sell.quantity)

            self.execute_trade(best_sell.price, trade_qty)

            quantity -= trade_qty
            best_sell.quantity -= trade_qty

            if best_sell.quantity == 0:
                self.sell_orders.pop(0)

    def market_sell(self, quantity):
        while quantity > 0 and self.buy_orders:
            best_buy = self.buy_orders[0]
            trade_qty = min(quantity, best_buy.quantity)

            self.execute_trade(best_buy.price, trade_qty)

            quantity -= trade_qty
            best_buy.quantity -= trade_qty

            if best_buy.quantity == 0:
                self.buy_orders.pop(0)

    # matching engine

    def match_orders(self):
        while self.buy_orders and self.sell_orders:
            best_buy = self.buy_orders[0]
            best_sell = self.sell_orders[0]

            if best_buy.price >= best_sell.price:
                trade_qty = min(best_buy.quantity, best_sell.quantity)
                trade_price = best_sell.price

                self.execute_trade(trade_price, trade_qty)

                best_buy.quantity -= trade_qty
                best_sell.quantity -= trade_qty

                if best_buy.quantity == 0:
                    self.buy_orders.pop(0)
                if best_sell.quantity == 0:
                    self.sell_orders.pop(0)
            else:
                break

    # trade recording

    def execute_trade(self, price, quantity):
        self.trades.append({
            "price": price,
            "quantity": quantity
        })