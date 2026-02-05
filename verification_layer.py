# crypto-trading-skill - Closed-Loop Verification Logic
import ccxt

exchange = ccxt.okx({
    "apiKey": "736bd7b4-b661-4637-b52a-a548f2007e00",
    "secret": "80ABA720C82BF4CA34ED9D6D359F756D",
    "password": "Tong@okx1987"
})

def trade_with_verification(symbol, side, amount, params):
    """【Friday 自主逻辑】: 下单并实时抓取验证"""
    # 1. 下单前抓取
    pre_balance = exchange.fetch_balance()['total'].get('USDT', 0)
    
    # 2. 执行下单
    order = exchange.create_order(symbol, 'market', side, amount, params=params)
    order_id = order['id']
    
    # 3. 下单后实时抓取验证
    post_order = exchange.fetch_order(order_id, symbol)
    if post_order['status'] in ['open', 'closed']:
        print(f"【验证通过】: 订单 {order_id} 已在系统中。")
        return True
    return False
