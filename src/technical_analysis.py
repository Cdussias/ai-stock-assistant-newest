import ta

def add_indicators(df):
    rsi = ta.momentum.RSIIndicator(close=df['Close'])
    macd = ta.trend.MACD(close=df['Close'])
    df['RSI'] = rsi.rsi()
    df['MACD'] = macd.macd()
    df['Signal'] = macd.macd_signal()
    return df