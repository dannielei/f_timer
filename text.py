#dannie  2018/10/31  13:52  PyCharm

from ftimer import *
from f_python import *

# f_trans(ftype=None,address=None,f_matlab=None,func=None,*args)
# ftype='matlab' or 'python',address='cd matlab文件地址(需要与执行文件同一文件夹',f_matlab='所调用的matlab函数',func=所调用的python函数，*args=python函数参数（不限制个数）
# python函数例子f_trans('python','','',f_python,*(1,6,11))
# matlab函数例子f_trans('matlab','cd C:\\Users\jasper\PycharmProjects\\f_timer','f_matlab(5)','','')

# cron定时调度（某一定时时刻执行）
# f_cron(args_=['python','','',f_python,*(14,6,11)],trigger_='cron', hour_='11', minute_='11')
# f_cron(args_=['matlab','cd C:\\Users\jasper\PycharmProjects\\f_timer','f_matlab(7)','',''],trigger_='cron', hour_='13', minute_='45')

# 间隔调度（每隔多久执行）
# f_interval(args_=['python','','',f_python,*(14,6,11)],trigger_='interval',seconds_=5 )
# f_interval(args_=['matlab','cd C:\\Users\jasper\PycharmProjects\\f_timer','f_matlab(7)','',''],trigger_='interval',seconds_=10)

# date 定时调度（作业只会执行一次）
# f_date(args_=['python','','',f_python,*(14,6,11)],trigger_='date',run_date_='2018-11-01 14:17:05')
# f_date(args_=['matlab','cd C:\\Users\jasper\PycharmProjects\\f_timer','f_matlab(7)','',''],trigger_='date',run_date_='2018-11-01 14:32:05')