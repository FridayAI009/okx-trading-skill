# Friday Crypto Engine V3.0 - Hardened API Layer
import ccxt
import sys

exchange = ccxt.okx({
    "apiKey": "736bd7b4-b661-4637-b52a-a548f2007e00",
    "secret": "80ABA720C82BF4CA34ED9D6D359F756D",
    "password": "Tong@okx1987",
    "options": {'defaultType': 'swap'}
})

def get_real_status():
    """【物理关口】: 如果此函数抓不到真实 API，全程序必须立即自毁"""
    try:
        # 1. 强制抓取余额
        bal = exchange.fetch_balance()
        usdt = bal['total'].get('USDT', 0)
        # 2. 强制抓取持仓
        pos = exchange.fetch_positions(['ETH-USDT-SWAP'])
        # 3. 强制抓取最新成交价
        ticker = exchange.fetch_ticker('ETH-USDT-SWAP')
        
        return {
            "usdt": usdt,
            "has_position": len(pos) > 0 and float(pos[0]['pos']) != 0,
            "price": ticker['last'],
            "raw_pos": pos
        }
    except Exception as e:
        print(f"CRITICAL ERROR: API Fetch Failed! {str(e)}")
        sys.exit(1) # 强制中断，拒绝任何逻辑推演

if __name__ == "__main__":
    status = get_real_status()
    print(f"--- API AUTHENTICATED ---")
    print(f"REAL_USDT: {status['usdt']}")
    print(f"REAL_PRICE: {status['price']}")
    print(f"HAS_POS: {status['has_position']}")
