# Cash Register System

A lightweight, beginner-friendly Python application that simulates a cash register. This project demonstrates Object-Oriented Programming (OOP) concepts such as class initialization, property encapsulation with getters and setters, item management, discount application, and transaction history voiding.

---

## Features

- **Encapsulated Discount Property**: Ensures discount percentages are integers between `0` and `100` inclusive. Invalid entries automatically default to `0` and print a helpful error message.
- **Dynamic Item Management**: Add individual or bulk items with custom prices and quantities.
- **Transaction History**: Keeps track of cart items, current total, and individual transaction objects in memory.
- **Percentage Discounts**: Deducts a percentage off the overall cart total.
- **Transaction Voiding**: Reverts the most recent transaction, updating the total price and cart contents accurately.

## Requirements & Setup
Prerequisites
Python 3.x installed on your system.

### Installation
Clone the repository:

### Bash
git clone <your-repository-url>
cd python-cash-register

## Usage
To run the interactive demonstration, execute cash_register.py in your terminal:

### Bash
python3 cash_register.py