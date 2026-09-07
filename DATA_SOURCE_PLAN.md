# Iran Stock Analyzer - Data Source Plan

## Architecture

TSETMC
   ↓
Python Data Collector
   ↓
PostgreSQL
   ↓
FastAPI
   ↓
Flutter Android + Telegram Bot

## Important Rule

Flutter and Telegram Bot must NOT connect directly to TSETMC.

Only the backend data collector communicates with market data sources.

## Required Market Data

### Daily OHLCV

- symbol
- instrument name
- ins_code
- date
- open
- high
- low
- close
- last
- yesterday
- volume
- value
- trade_count

### Client Type Data

- date
- individual buy volume
- legal buy volume
- individual sell volume
- legal sell volume
- individual buyer count
- legal buyer count
- individual seller count
- legal seller count

## Data Sources

Primary candidate:

TSETMC CDN API

Possible fallback sources:

- TSETMC Web Gateway
- TSETMC legacy APIs
- Other market-data providers if required

## Network Requirement

The data collector must run from an environment that can reliably access the required TSETMC endpoints.

GitHub Actions is used for testing and CI, not as the permanent market-data collector.

## Provider Design

Market-data access must be isolated behind provider functions.

Initial functions:

- search_symbol()
- get_history()
- get_quote()
- get_client_type_history()

The rest of the application must not depend directly on TSETMC URLs.

## Database

Initial database target:

PostgreSQL

Development may temporarily use SQLite.

## Alert System

Users can define a target price.

Example:

Target price = 10,000

Alert threshold = 3%

Alert when:

9,700 <= current price <= 10,300

Telegram notification will be added later.

## Future Features

- Candlestick charts
- Volume charts
- Individual/legal flow
- Price alerts
- Telegram chart command
- Excel export
- Historical analysis
- Technical indicators
