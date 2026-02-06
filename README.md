# Order Book Simulator – Algorithmic Trading Systems Project

## Overview

This project implements a **limit order book simulator** that models how real electronic exchanges match buy and sell orders. The system allows limit and market orders to be placed, matches them using price priority, supports partial fills, and records executed trades for later analysis.

The simulator is designed as a **systems and algorithms project**, focusing on correctness, transparency, and explainability rather than raw performance. It provides a controlled environment to test and compare execution strategies such as TWAP and VWAP.

---

## Core Features

* Limit buy and sell orders
* Market buy and sell orders
* Price-priority matching engine
* Partial order fills
* Trade execution recording
* Clean, modular Python design

---

## Order Book Design

### Data Structures

The order book is split into two lists:

* `buy_orders`: sorted by **descending price** (highest bid first)
* `sell_orders`: sorted by **ascending price** (lowest ask first)

Each order is represented by an `Order` object containing:

* `side` (“BUY” or “SELL”)
* `price`
* `quantity`

### Design Rationale

Sorted Python lists were chosen instead of more complex structures (e.g. trees or heaps) in order to:

* prioritise correctness and clarity
* make the matching logic easy to verify and explain
* allow rapid debugging and iteration

While more advanced data structures could improve performance, the chosen approach is efficient enough for simulation-scale workloads and better suited for demonstrating algorithmic reasoning.

---

## Matching Engine Logic

The matching engine repeatedly compares:

* the highest-priced buy order
* the lowest-priced sell order

A trade occurs when:

```
best_buy_price ≥ best_sell_price
```

When this condition is met:

* the trade quantity is the minimum of the two order quantities
* the trade executes at the seller’s price
* both orders are reduced accordingly
* fully filled orders are removed from the order book

The engine continues matching until no further price overlap exists.

This logic closely mirrors how real electronic exchanges operate.

---

## Market Orders

Market orders bypass price constraints and instead consume the best available liquidity from the opposite side of the order book.

* A market buy consumes the cheapest sell orders
* A market sell consumes the highest buy orders

This allows immediate execution while still respecting price priority.

---

## Trade Recording and Metrics

Each executed trade is recorded with:

* execution price
* traded quantity

This enables later analysis of:

* execution quality
* slippage
* strategy performance
* stability under changing market conditions

---

## Extensibility

The simulator is intentionally modular and can be extended with:

* execution strategies (TWAP, VWAP, volatility-based)
* slippage measurement
* runtime benchmarking
* simulated volatility spikes
* alternative order book data structures

---

## Limitations

* No time-priority handling for orders at the same price
* No latency or network delay modelling
* No real-time data integration
* Optimised for clarity over maximum speed

These trade-offs were made deliberately to keep the system transparent and explainable.

---

## Why This Project Matters

This project demonstrates:

* algorithmic thinking
* data structure selection and justification
* system modelling
* real-world abstraction
* iterative engineering design
