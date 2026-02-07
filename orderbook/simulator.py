# simulator.py
from orderbook import OrderBook
from strategies import twap, vwap
import random

def simulate_twap():
    book = OrderBook()
    # e.g. twap bbuys 100 units in 5 steps
    twap(book, side="BUY", total_quantity=100, steps=5)
    print("TWAP Trades:", book.trades)

def simulate_vwap():
    book = OrderBook()
    # e.g. stimulates mket vols
    market_volumes = [10, 50, 30, 10]  # arb nums
    vwap(book, side="SELL", total_quantity=100, market_volumes=market_volumes)
    print("VWAP Trades:", book.trades)

def simulate_random_market_orders():
    book = OrderBook()
    # simming some random limit orders
    for _ in range(5):
        side = random.choice(["BUY", "SELL"])
        price = random.randint(90, 110)
        qty = random.randint(1, 20)
        book.add_limit_order(Order(side, price, qty))
    print("Random Market Trades:", book.trades)

if __name__ == "__main__":
    print("=== TWAP Simulation ===")
    simulate_twap()
    print("\n=== VWAP Simulation ===")
    simulate_vwap()
    print("\n=== Random Market Simulation ===")
    simulate_random_market_orders()