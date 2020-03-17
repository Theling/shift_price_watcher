import shift
import datetime as dt
import time
import pandas as pd



def grab_last_pricee(trader, ls):
    pass

def sleep_till_end(trader):
    while True:
        t = trader.get_last_trade_time()
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
    trader = shift.Trader('test001')
    trader.connect('initiator.cfg', 'password')
    trader.sub_all_order_book()

    sym_ls = ['']
    pd.read_csv('sample_last_price.csv')

    