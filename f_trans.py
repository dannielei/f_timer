#dannie  2018/10/22  17:49  PyCharm

#判断交易日及调用matlab
from jt.utils.calendar.api_calendar import TradeCalendar_api
from win32com.client import Dispatch
import time
import pythoncom

def f_trans(ftype=None,address=None,f_matlab=None,func=None,*args):
    date = time.strftime("%Y%m%d", time.localtime())
    print(date)
    if TradeCalendar_api().is_trading_date(date):
        print('jyr')
        if ftype=='matlab':
            pythoncom.CoInitialize()#多线程
            h = Dispatch("Matlab.application")
            h.execute(address)
            h.execute("ans={}".format(f_matlab))
            print(h.GetVariable("ans", "base"))
        else:
            func(*args)



