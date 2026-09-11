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


def rsi(values, period=14):
    if period <= 0:
        raise ValueError("Period must be positive")

    if len(values) <= period:
        return []

    gains = []
    losses = []

    for i in range(1, len(values)):
        change = values[i] - values[i - 1]
        gains.append(max(change, 0))
        losses.append(max(-change, 0))

    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period

    result = []

    for i in range(period, len(gains)):
        avg_gain = ((avg_gain * (period - 1)) + gains[i]) / period
        avg_loss = ((avg_loss * (period - 1)) + losses[i]) / period

        if avg_loss == 0:
            result.append(100.0)
        else:
            rs = avg_gain / avg_loss
            result.append(100 - (100 / (1 + rs)))

    return result
