def sma(values, period):
    if period <= 0:
        raise ValueError("Period must be positive")

    if len(values) < period:
        return []

    return [
        sum(values[i - period + 1:i + 1]) / period
        for i in range(period - 1, len(values))
    ]
