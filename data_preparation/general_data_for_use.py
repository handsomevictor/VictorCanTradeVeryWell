# 本文件可以从外部导入很多需要用到的数据集，比如全体股票的代码，市值大于xx的股票代码，市值前35%的代码等
import datetime
import os
import pandas as pd


# 这个方法仅用于获取A股所有纯股票代码，返回值是list格式
def get_all_pure_tickers():
    from VictorCanTradeVeryWell.data_preparation.get_a_share_all_tickers import get_a_share_all_tickers

    today = datetime.date.today()
    today_string = today.__format__('%Y-%m-%d')

    # 使用根目录
    root_path = os.path.abspath(os.path.dirname(__file__)).split('VictorCanTradeVeryWell')[0] + 'VictorCanTradeVeryWell\\'

    all_ticker_file_direction = root_path + 'data\\a_share\\all_ticker_data\\'

    files_in_direction = os.listdir(all_ticker_file_direction)
    file_name = today_string + '_all_ticker_data.csv'

    while True:
        if file_name in files_in_direction:
            file = all_ticker_file_direction + file_name

            # 找到文件并返回股票代码
            all_tickers = pd.read_csv(file)
            current_all_tickers = all_tickers.iloc[:, 0]

            return list(current_all_tickers)
        else:
            get_a_share_all_tickers()
            print('使用了这个！')


# 本函数返回输入的股票代码在某天到某天的价格信息
def get_ticker_price_information(stock_list, start_date, end_date, frequency):
    from VictorCanTradeVeryWell.logging_records.logging_tool import logging_records
    from VictorCanTradeVeryWell.logging_records import logging_address

    import jqdatasdk as jq
    from VictorCanTradeVeryWell.general_processing.save_csv_file import save_csv_file
    import datetime

    field = ['open', 'close', 'low', 'high', 'volume', 'money', 'factor',
             'high_limit', 'low_limit', 'avg', 'pre_close', 'paused',
             'open_interest']

    ticker_price_information = jq.get_price(stock_list,
                                            start_date=start_date,
                                            end_date=end_date,
                                            frequency=frequency,
                                            fields=field,
                                            skip_paused=False,
                                            fq='pre')

    # 将单日的信息记录到本地data文件中
    # 如果已有则不用再记录了
    start_date_string = start_date.__format__('%Y-%m-%d')
    file_name = start_date_string + '_all_ticker_price_information.csv'

    # 根目录
    root_path = os.path.abspath(os.path.dirname(__file__)).split('VictorCanTradeVeryWell')[0] + 'VictorCanTradeVeryWell\\'

    all_ticker_price_information_direction = root_path + 'data\\a_share\\all_ticker_data\\'
    files_in_direction = os.listdir(all_ticker_price_information_direction)

    # 满足这个条件才算将所有值都计入了data中，并输出日志
    if (file_name not in files_in_direction) & (start_date == end_date) & (len(stock_list) > 4520):
        all_price_information = jq.get_price(stock_list,
                                             start_date=start_date,
                                             end_date=end_date,
                                             frequency=frequency,
                                             fields=field,
                                             skip_paused=False,
                                             fq='pre')

        # 记录到data中的csv中
        all_price_information.to_csv(all_ticker_price_information_direction + file_name)

        # 在logging_records里面记录日志信息
        today = datetime.date.today()
        today_string = today.__format__('%Y-%m-%d')
        message = 'Downloaded all tickers price information on date ' + start_date.__format__('%Y-%m-%d')
        logging_records(today_string, logging_address(), message)

    return ticker_price_information


# a_share_ticker_list = get_all_pure_tickers(level=2)

if __name__ == '__main__':
    from VictorCanTradeVeryWell.general_processing.only_for_login import for_login
    import datetime
    today = datetime.date.today()
    two_days_ago = today - datetime.timedelta(4)
    for_login()

    print(get_all_pure_tickers())
    a = get_ticker_price_information(stock_list=get_all_pure_tickers()[:3],
                                     start_date=two_days_ago,
                                     end_date=two_days_ago,
                                     frequency='minute')
    print(a)
    # print(get_all_pure_tickers())
    # print(type(get_all_pure_tickers()))