def sma(values, period):
    if period <= 0:
        raise ValueError("Period must be positive")

    if len(values) < period:
        return []

    return [
        sum(values[i - period + 1:i + 1]) / period
        for i in range(period - 1, len(values))
    ]


def ema(values, period):
    if period <= 0:
        raise ValueError("Period must be positive")

    if len(values) < period:
        return []

    multiplier = 2 / (period + 1)

    result = [sum(values[:period]) / period]

    for price in values[period:]:
        result.append(
            (price - result[-1]) * multiplier + result[-1]
        )

    return result
    ]
