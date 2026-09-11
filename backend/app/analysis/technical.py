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


def macd(values, fast_period=12, slow_period=26, signal_period=9):
    if len(values) < slow_period:
        return {
            "macd": [],
            "signal": [],
            "histogram": []
        }

    fast = ema(values, fast_period)
    slow = ema(values, slow_period)

    offset = slow_period - fast_period

    macd_line = [
        fast[i + offset] - slow[i]
        for i in range(len(slow))
    ]

    signal_line = ema(macd_line, signal_period)

    histogram = [
        macd_line[i + signal_period - 1] - signal_line[i]
        for i in range(len(signal_line))
    ]

    return {
        "macd": macd_line,
        "signal": signal_line,
        "histogram": histogram
    }
