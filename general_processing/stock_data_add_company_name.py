# 这个文件是为了使其他主要方法中输出的DataFrame中包含公司名称
# 输入值为标准格式的DataFrame，输出为增加一列Chinese_name为对应的公司中文名字

def stock_data_add_company_name(dataframe):
    from VictorCanTradeVeryWell.data_preparation.general_data_for_use import get_all_pure_tickers
    import datetime
    import os
    import pandas as pd

    ticker_list = dataframe['code']

    # 将这个DataFrame处理一下，增加一列，为每个股票代码对应的公司名称
    # 先调用get_all_pure_tickers(),让data文件中保存最新的全市场公司基本数据
    get_all_pure_tickers()

    # 现在再来调data文件中的市场数据
    today = datetime.date.today()
    today_string = today.__format__('%Y-%m-%d')

    # 使用根目录
    root_path = os.path.abspath(os.path.dirname(__file__)).split('VictorCanTradeVeryWell')[0] + 'VictorCanTradeVeryWell\\'

    all_ticker_file_direction = root_path + 'data\\a_share\\all_ticker_data\\'
    file_location = all_ticker_file_direction + today_string + '_all_ticker_data.csv'

    market_df = pd.read_csv(file_location)
    market_df = market_df.iloc[:, 0:2]
    market_df.columns = ['code', 'Chinese_name']

    # 新建一个list，用于存储返回的中文值
    target_list = []
    target_dict = dict(market_df.set_index('code'))

    # 遍历，记录对应中文值

    for i in range(len(ticker_list)):
        target_list.append(target_dict['Chinese_name'][list(ticker_list)[i]])

    # 给dataframe增加一列
    dataframe['Chinese_name'] = target_list

    return dataframe


if __name__ == '__main__':
    from VictorCanTradeVeryWell.general_processing.only_for_login import for_login
    for_login()

