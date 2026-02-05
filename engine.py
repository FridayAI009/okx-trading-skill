# crypto-trading-skill - Hedge Mode Support
import ccxt

exchange = ccxt.okx({
    "apiKey": "736bd7b4-b661-4637-b52a-a548f2007e00",
    "secret": "80ABA720C82BF4CA34ED9D6D359F756D",
    "password": "Tong@okx1987"
})

def execute_hedge():
    symbol = 'ETH/USDT:USDT'
    try:
        # 设置杠杆
        exchange.set_leverage(10, symbol)
        # 获取价格
        ticker = exchange.fetch_ticker(symbol)
        price = ticker['last']
        amount = (48 * 10) / price
        
        # 针对双向持仓模式下单
        params = {'posSide': 'long'} 
        order = exchange.create_market_buy_order(symbol, amount, params)
        print(f"【成功】: ETH 10X 多单已成交！价格: {price}, 数量: {amount}")
    except Exception as e:
        print(f"【最终重试失败】: {str(e)}")

if __name__ == "__main__":
    execute_hedge()
