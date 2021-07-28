# 写一个function，调用的时候可以直接将目标文件保存到data中的某个目录中
# 传入的参数示例：save_csv_file(data, full_direction, 'file_name_for_all_ticker')
# 注意，这里的direction应该是相对路径！从项目根目录开始！比如: direction = 'data/a_share/...'

def save_csv_file(file, direction, file_name_in_data):
    import os
    root_path = os.path.abspath(os.path.dirname(__file__)).split('VictorCanTradeVeryWell')[0]

    full_direction = root_path + 'VictorCanTradeVeryWell\\' + direction + '\\' + file_name_in_data
    file.to_csv(full_direction, encoding='utf-8')
