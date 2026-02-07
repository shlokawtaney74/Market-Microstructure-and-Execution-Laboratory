# strategies.py
from orderbook import Order

# time weighted avg price strat/mmech
def twap(order_book, side, total_quantity, steps, price=None):
    """
    Time-Weighted Average Price
    Splits total quantity into equal chunks over 'steps' time intervals.
    
    side: "BUY" or "SELL"
    total_quantity: total units to trade
    steps: number of intervals
    price: optional limit price (None for market order)
    """
    quantity_per_step = total_quantity // steps

    for _ in range(steps):
        if price is None:
            # market order
            if side == "BUY":
                order_book.market_buy(quantity_per_step)
            else:
                order_book.market_sell(quantity_per_step)
        else:
            # limit order
            order = Order(side, price, quantity_per_step)
            order_book.add_limit_order(order)


# volume weighted avg price strat/mech
def vwap(order_book, side, total_quantity, market_volumes, price=None):
    """
    Volume-Weighted Average Price
    Trade more when market volume is high, less when low.
    
    market_volumes: list of simulated market volumes per step
    """
    total_volume = sum(market_volumes)
    for vol in market_volumes:
        # calculates proportion of ttl quantity based on vol
        quantity_step = int(total_quantity * (vol / total_volume))
        if quantity_step == 0:
            continue

        if price is None:
            if side == "BUY":
                order_book.market_buy(quantity_step)
            else:
                order_book.market_sell(quantity_step)
        else:
            order = Order(side, price, quantity_step)
            order_book.add_limit_order(order)