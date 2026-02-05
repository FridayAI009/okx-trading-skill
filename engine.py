# crypto-trading-skill - Conservative Short Strategy
import ccxt

exchange = ccxt.okx({
    "apiKey": "736bd7b4-b661-4637-b52a-a548f2007e00",
    "secret": "80ABA720C82BF4CA34ED9D6D359F756D",
    "password": "Tong@okx1987",
    "options": {'defaultType': 'swap'}
})

def check_and_short():
    symbol = 'ETH-USDT-SWAP'
    trigger_price = 1924.0 # 跌破此价开空
    try:
        ticker = exchange.fetch_ticker(symbol)
        current_price = ticker['last']
        print(f"【监控中】: ETH 当前价 {current_price} | 触发价 {trigger_price}")
        
        if current_price < trigger_price:
            print("【信号触发】: 跌破 1924，正在以 5X 杠杆开空...")
            # 5X 杠杆，15U 本金
            amount = (15 * 5) / current_price
            params = {'posSide': 'short', 'tdMode': 'cross'}
            order = exchange.create_market_sell_order(symbol, amount, params)
            print(f"【成功】: 5X 空单已成交，订单号: {order['id']}")
            return True
        return False
    except Exception as e:
        print(f"监控异常: {str(e)}")
        return False

if __name__ == "__main__":
    check_and_short()
