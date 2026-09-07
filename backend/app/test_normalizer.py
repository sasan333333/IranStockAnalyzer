from providers.normalizer import normalize_history


sample_data = [
    {
        "dEven": 20260907,
        "priceFirst": 10000,
        "priceMax": 10500,
        "priceMin": 9900,
        "pClosing": 10300,
        "pDrCotVal": 10400,
        "priceYesterday": 10000,
        "qTotTran5J": 1000000,
        "qTotCap": 10300000000,
        "zTotTran": 5000
    }
]


result = normalize_history(
    raw_history=sample_data,
    symbol="فملی",
    name="ملی صنایع مس ایران",
    ins_code="TEST"
)


print("Records:", len(result))

for item in result:
    print(item)
    print("Symbol:", item.symbol)
    print("Date:", item.date)
    print("Close:", item.close_price)
    print("Volume:", item.volume)
