from models.market_data import DailyMarketData


data = DailyMarketData(
    symbol="فملی",
    name="ملی صنایع مس ایران",
    ins_code="TEST",
    date="20260907",
    open_price=10000,
    high_price=10500,
    low_price=9900,
    close_price=10300,
    last_price=10400,
    yesterday_price=10000,
    volume=1000000,
    value=10300000000,
    trade_count=5000
)


print("=== Daily Market Data ===")
print(data)

print("\nSymbol:", data.symbol)
print("Close:", data.close_price)
print("Volume:", data.volume)
