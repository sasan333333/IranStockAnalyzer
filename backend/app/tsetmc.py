from providers.tsetmc_provider import TSETMCProvider


provider = TSETMCProvider()

symbol = "فملی"

print(f"Searching for: {symbol}")

results = provider.search_symbol(symbol)

if not results:
    print("Symbol not found.")
    raise SystemExit(1)

print("\nSearch results:")

for item in results[:5]:
    print(
        item.get("lVal18AFC"),
        "|",
        item.get("lVal30"),
        "|",
        item.get("insCode")
    )

instrument = results[0]

ins_code = instrument["insCode"]

print("\nSelected instrument:")
print("Symbol:", instrument.get("lVal18AFC"))
print("Name:", instrument.get("lVal30"))
print("InsCode:", ins_code)

history = provider.get_history(ins_code)

print("\nHistory records:", len(history))

if history:
    print("\nFirst record:")
    print(history[0])
