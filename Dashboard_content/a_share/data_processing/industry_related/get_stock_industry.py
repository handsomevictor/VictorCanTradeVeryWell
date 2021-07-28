# 使用这个方法可以将输入的公司的所属板块找到
# 默认值为zjw行业
# 注意，这个不能一次传多个值

def get_stock_industry(stock_name):
    import jqdatasdk as jq
    import datetime

    today2 = datetime.date.today()

    industry = jq.get_industry(stock_name, date=today2)[stock_name]['sw_l1']

    return industry


if __name__ == '__main__':
    from VictorCanTradeVeryWell.general_processing.only_for_login import for_login
    import datetime
    import jqdatasdk as jq
    today = datetime.date.today()
    from VictorCanTradeVeryWell.data_preparation.get_a_share_all_tickers import get_a_share_all_tickers

    for_login()
    ticker_list = get_a_share_all_tickers().index

    print(get_stock_industry(ticker_list[2]))
