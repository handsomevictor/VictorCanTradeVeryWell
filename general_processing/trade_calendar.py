# 本文件仅限获取交易日历
# 使用说明：
# trade_calendar.get_trade_calendar(False, '2020-11-11', '2020-12-11')
# 中如果输入False，则如果赋值了起始日期和终止日期，则返回区间内的交易日
# 如不赋值则自动返回一年内的所有交易日
# 如果输入True，则自动返回2005至最大可预测的交易日（目前为2023年）

import datetime
from VictorCanTradeVeryWell.login.login_account import login_account

class trade_calendar:
    today = datetime.date.today()
    one_year_ago = today - datetime.timedelta(365)

    def __init__(self, start_date=one_year_ago, end_date=today):
        # self.choice = choice
        self.start_date = start_date
        self.end_date = end_date

    def get_trade_calendar(self=True, start_date=one_year_ago, end_date=today):
        import jqdatasdk as jq

        if self:
            all_days = jq.get_all_trade_days()
            return all_days
        else:
            some_days = jq.get_trade_days(start_date, end_date)
            return some_days


if __name__ == '__main__':
    username = '13070162357'
    password = '1234567890Sos'

    if not login_account(username, password):
        print('login error')
    print(trade_calendar.get_trade_calendar(self=False, start_date='2020-11-11', end_date='2020-12-11'))
