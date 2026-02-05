# crypto-trading-skill - Enhanced Version (Based on ClawHub)
import ccxt

# 5. OKX Credentials (已从 TOOLS.md 自动加载)
exchange = ccxt.okx({
    "apiKey": "736bd7b4-b661-4637-b52a-a548f2007e00",
    "secret": "80ABA720C82BF4CA34ED9D6D359F756D",
    "password": "Tong@okx1987"
})

def get_balance():
    """【Mini Max-M2.1】: 获取 OKX 账户可用余额"""
    try:
        balance = exchange.fetch_balance()
        return balance['total']
    except Exception as e:
        return f"Error fetching balance: {str(e)}"

def get_market_data(symbol="BTC/USDT"):
    """【Mini Max-M2.1】: 获取实时行情"""
    try:
        ticker = exchange.fetch_ticker(symbol)
        return ticker['last']
    except Exception as e:
        return f"Error fetching ticker: {str(e)}"

if __name__ == "__main__":
    print(f"Friday 交易引擎启动。当前 BTC 价格: {get_market_data()}")
