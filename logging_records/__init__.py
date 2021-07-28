# 为了方便，以后所有涉及日志记录的direction目录全部引入这个文件中的logging_direction
import os

def logging_address():
    import os

    root_path = os.path.abspath(os.path.dirname(__file__)).split('VictorCanTradeVeryWell')[0] + 'VictorCanTradeVeryWell\\'

    logging_direction = root_path + 'logging_records\\logging_records\\'
    return logging_direction
