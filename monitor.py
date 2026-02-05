# crypto-trading-skill - Autonomous Stop Loss & Monitoring
import ccxt
import time

exchange = ccxt.okx({
    "apiKey": "736bd7b4-b661-4637-b52a-a548f2007e00",
    "secret": "80ABA720C82BF4CA34ED9D6D359F756D",
    "password": "Tong@okx1987",
    "options": {'defaultType': 'swap'}
})

def set_dynamic_stop_loss():
    symbol = 'ETH/USDT:USDT'
    entry_price = 1932.07
    # 计算亏损 2U 时的价格 (10倍杠杆下，价格波动约 0.4% 即亏损 2U)
    # 公式: 2U / (仓位数量)
    stop_loss_price = entry_price - (2 / 0.248) 
    
    print(f"【Friday 自主决策】: 为保护本金，已计算止损价为: {stop_loss_price}")
    
    try:
        # 向 OKX 提交止损触发单
        params = {'posSide': 'long', 'stopPrice': stop_loss_price}
        exchange.create_order(symbol, 'limit', 'sell', 0.248, stop_loss_price, params)
        print(f"✅ 2U 保护性止损单已挂出。")
    except Exception as e:
        print(f"止损单挂载失败: {str(e)}")

if __name__ == "__main__":
    set_dynamic_stop_loss()
