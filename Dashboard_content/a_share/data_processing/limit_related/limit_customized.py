# 本文件返回为符合要求的股票代码list
# 输入参数为涨跌幅与方向（高于这个涨幅或者低于这个涨幅）
# 本方法需要取两天的值，所以调用两次get_ticker_price_information
# date输入格式为datetime，percentage输入格式为0.07，direction输入格式为'higher'或 'lower'

def limit_customized_df(date, percentage, direction):
    from VictorCanTradeVeryWell.data_preparation.general_data_for_use import get_ticker_price_information
    from VictorCanTradeVeryWell.data_preparation.get_a_share_all_tickers import get_a_share_all_tickers
    import datetime
    import numpy as np

    # 定义date和date的前一天
    date_today = date
    date_yesterday = date_today - datetime.timedelta(1)

    # 将昨天和今天的数据拿出来
    all_tickers = list(get_a_share_all_tickers().index)

    today_all_price_information = get_ticker_price_information(stock_list=all_tickers, start_date=date_today,
                                                               end_date=date_today, frequency='daily')
    yesterday_all_price_information = get_ticker_price_information(stock_list=all_tickers, start_date=date_yesterday,
                                                                   end_date=date_yesterday, frequency='daily')

    # 拿到昨天今天的数据后，将每个票的涨幅计算出来加入到最后一列
    # 如果有新股而导致的出现nan，则不做任何替换依旧让其为nan，出现nan一般因为停牌或者新股,以后新股可以标注一下
    price_today = np.array(today_all_price_information.close)
    price_yesterday = np.array(yesterday_all_price_information.close)
    price_change_rate = price_today / price_yesterday - 1

    # 替换nan
    # price_change_rate[np.isnan(price_change_rate)] = 0

    # 保留两位小数
    price_change_rate = price_change_rate.round(4)

    # 添加列
    today_all_price_information['price_change_rate'] = price_change_rate

    # 调用stock_data_add_company_name.py来添加一列中文
    def add_chinese(data):
        from VictorCanTradeVeryWell.general_processing.stock_data_add_company_name import stock_data_add_company_name
        all_data = stock_data_add_company_name(data)
        return all_data

    # 返回高于这个涨幅的所有票
    if direction == 'higher':
        higher_df = today_all_price_information[today_all_price_information.price_change_rate >= percentage]

        # 加中文名
        higher_df = add_chinese(higher_df)

        return higher_df

    # 返回低于这个涨幅的所有票
    elif direction == 'lower':
        lower_df = today_all_price_information[today_all_price_information.price_change_rate <= percentage]

        # 加中文名
        lower_df = add_chinese(lower_df)

        return lower_df

if __name__ == '__main__':
    from VictorCanTradeVeryWell.general_processing.only_for_login import for_login
    for_login()
    import datetime
    import warnings
    warnings.filterwarnings('ignore')
    today = datetime.date.today()

    print(limit_customized_df(date=today, percentage=-0.09, direction='lower'))
