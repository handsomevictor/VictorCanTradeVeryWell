# 这是用于存储所有上市公司名字，代码，上市时间，四字母代码等
# 文件保存到../data/a_share/all_ticker_data中
# 本方法返回的是标准DataFrame，不是list
import jqdatasdk as jq
import datetime
import os
import pandas as pd
from VictorCanTradeVeryWell.logging_records import logging_address
# 导入存储日志的direction
from VictorCanTradeVeryWell.logging_records.logging_tool import logging_records
# 导入自动保存数据的方法
from VictorCanTradeVeryWell.general_processing.save_csv_file import save_csv_file

def get_a_share_all_tickers():

    today = datetime.date.today()
    today_string = today.__format__('%Y-%m-%d')
    all_ticker_data = jq.get_all_securities(types=[], date=None)

    # 如果在data文件中没有这个数据，则自动创建csv文件并储存
    file_name = today_string + '_all_ticker_data.csv'
    save_file_direction = 'data\\a_share\\all_ticker_data'

    save_csv_file(all_ticker_data, save_file_direction, file_name)

    # 在logging_records里面记录日志信息
    message = 'Downloaded all tickers data'
    logging_records(today_string, logging_address(), message)

    return all_ticker_data

if __name__ == '__main__':
    from VictorCanTradeVeryWell.general_processing.only_for_login import for_login
    for_login()

    print(get_a_share_all_tickers().index)

