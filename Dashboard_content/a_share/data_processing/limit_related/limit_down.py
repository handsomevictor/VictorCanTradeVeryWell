# 本文件返回值为当日全部跌停股票DataFrame，里面code列为股票代码
# 传入的值为datetime格式的date
# 不传入值则默认返回当日值


def limit_down_df(date):
    # 调入当日所有price information
    from VictorCanTradeVeryWell.data_preparation.general_data_for_use import get_ticker_price_information
    from VictorCanTradeVeryWell.data_preparation.get_a_share_all_tickers import get_a_share_all_tickers
    from VictorCanTradeVeryWell.general_processing.stock_data_add_company_name import stock_data_add_company_name
    import datetime

    today2 = datetime.date.today()
    security = list(get_a_share_all_tickers().index)
    all_data = get_ticker_price_information(stock_list=security, start_date=today2, end_date=today2, frequency='daily')

    # 找到当日涨停的，即high_limit==close的
    all_data = all_data[all_data.close == all_data.low_limit]

    # 现在调用stock_data_add_company_name.py来添加一列中文
    all_data = stock_data_add_company_name(all_data)

    return all_data


if __name__ == '__main__':
    from VictorCanTradeVeryWell.general_processing.only_for_login import for_login
    for_login()
    import datetime
    import warnings
    warnings.filterwarnings('ignore')
    today = datetime.date.today()
    print(limit_down_df(today))
