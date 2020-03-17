import shift
import datetime as dt
import time
import pandas as pd



def grab_last_price(trader, ls, header):
    lp, ap, bp, aq, bq = [], [], [], [], []
    for sym in ls:
        lp.append(trader.get_last_price(sym))
        best_price = trader.get_best_price(sym)
        ap.append(best_price.get_ask_price())
        bp.append(best_price.get_bid_price())
        aq.append(best_price.get_ask_size())
        bq.append(best_price.get_bid_size())
    res = [ls, lp, ap, bp, aq, bq]
    return pd.DataFrame(dict(zip(header, res)))

def sleep_till_end(trader):
    while True:
        t = trader.get_last_trade_time()
        t = t.time()
        if t < dt.time(14, 0, 0):
            dt.sleep(60*61)
        elif t < dt.time(15, 00, 0):
            dt.sleep(60*31)
        elif t < dt.time(15, 30, 0):
            dt.sleep(60*16)
        elif t < dt.time(15, 45, 0):
            dt.sleep(60*3)
        elif t < dt.time(15, 55, 0):
            dt.sleep(60*2)
        elif t < dt.time(15, 58, 30):
            dt.sleep(60*1)
        elif t < dt.time(15, 59, 0):
            dt.sleep(10)
        else:
            break
    return True


if __name__=='__main__':
    import os
    print(os.getcwd())
    trader = shift.Trader('test001')
    trader.disconnect()
    trader.connect('initiator.cfg', 'password')
    trader.sub_all_order_book()
    try:
        dat = pd.read_csv("sample_last_price.csv")
        sym_ls = list(dat['Symbol'])
        field_ls = list(dat.columns)
        if sleep_till_end(trader):
            df = grab_last_price(trader, sym_ls, field_ls)
        df.to_csv('last_price.csv')
    except:
        trader.disconnect()
        print('crashed.')

    