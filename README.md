# Algorithmic Trading

Django momentum trading app using [Massive](https://massive.com) for market data, [SnapTrade](https://snaptrade.com) for brokerage access, and [Alpaca](https://alpaca.markets) for paper trading.

Followed [this tutorial](https://www.youtube.com/watch?v=zH2Mg782XhA) to learn SnapTrade integrations.

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- API keys for Massive and SnapTrade
- Alpaca paper trading account

## Setup

### 1. Create virtual environment

```bash
uv venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
uv pip install -r requirements.txt
```

### 3. Configure environment variables

```bash
cp .env.example .env
```

Add API keys to `.env`.

### 4. Set up database

```bash
python manage.py migrate
```

### 5. Run server

```bash
python manage.py runserver
```
