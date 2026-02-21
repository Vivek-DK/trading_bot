# Binance Futures Testnet Trading Bot

A small CLI-based Python application that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).  
The project focuses on clean structure, input validation, logging, and error handling.

---

## Features

- Place MARKET and LIMIT orders
- Supports BUY and SELL
- CLI input validation
- Structured logging of requests, responses, and errors
- Separation of client, validation, order logic, and CLI layers

---

## Project Structure
```
trading_bot/
│
├── bot/
│ ├── init.py
│ ├── client.py
│ ├── orders.py
│ ├── validators.py
│ └── logging_config.py
│
├── cli.py
├── requirements.txt
├── logs/
└── README.md
```

---

## Prerequisites

- Python 3.9+
- Binance Futures Testnet account  
  https://testnet.binancefuture.com

Create API keys from Futures Testnet API management.

---

## Setup

Clone repository:

```bash
git clone https://github.com/Vivek-DK/trading_bot.git
cd trading_bot
```

Create virtual environment:

Linux / macOS:

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create .env file in project root:

```bash
BINANCE_API_KEY="your_testnet_key" 
BINANCE_API_SECRET="your_testnet_secret" 
```
---

## Usage

### MARKET order

Minimum position value must be above exchange requirement (~100 USDT).

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

### LIMIT order

Example far price so order stays open:

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 100000
```

### Validation example (expected failure)
```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001
```

### Logging

Logs are written to:

```bash
logs/bot.log
```

Log includes:

order intent

API request payload

API response

validation and runtime errors

order result summary

```bash
INFO Market order -> BTCUSDT BUY 0.002
DEBUG API REQUEST futures_create_order -> {...}
DEBUG API RESPONSE futures_create_order -> {...}
INFO Order result -> id=... status=...
```

---

### Assumptions

```bash
# Binance Futures Testnet keys are used
# Minimum order size rules enforced by exchange
# LIMIT order may remain NEW if price is far from market
```

---

### How to Run Full Test Flow

```bash
rm -f logs/bot.log

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 100000
```

Check logs:
```bash
cat logs/bot.log
```

### Requirements

```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Author

Vivek D K

Frontend Developer
