#dannie  2018/10/22  17:49  PyCharm

from apscheduler.schedulers.blocking import BlockingScheduler
from f_trans import *

#封装aspcheduler
def f_cron(func_=f_trans, args_=None, trigger_=None, year_=None, month_=None, day_=None, day_of_week_=None, hour_=None, minute_=None,
           second_=None, start_date_=None, end_date_=None):
    scheduler = BlockingScheduler()
    scheduler.add_job(func=func_, args=args_, trigger=trigger_, year=year_, month=month_, day=day_, day_of_week=day_of_week_,
                      hour=hour_, minute=minute_, second=second_, start_date=start_date_,
                      end_date=end_date_)  # cron定时调度（某一定时时刻执行）
    scheduler.start()


def f_interval(func_=f_trans, args_=None, trigger_=None, weeks_=0, days_=0, hours_=0, minutes_=0, seconds_=0, start_date_='2018-01-01',
               end_date_='2018-12-31'):
    scheduler = BlockingScheduler()
    scheduler.add_job(func=func_, args=args_, trigger=trigger_, weeks=weeks_, days=days_, hours=hours_, minutes=minutes_,
                      seconds=seconds_, start_date=start_date_, end_date=end_date_)  # 间隔调度（每隔多久执行）
    scheduler.start()


def f_date(func_=f_trans, args_=None, trigger_=None, run_date_=None):
    scheduler = BlockingScheduler()
    scheduler.add_job(func=func_, args=args_, trigger=trigger_, run_date=run_date_)  # date 定时调度（作业只会执行一次）
    scheduler.start()