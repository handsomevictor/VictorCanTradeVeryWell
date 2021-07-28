# 执行这个程序，调用时可以自动在logging_records中记录想要记录的日志信息
# 这里direction需要传入根目录的方式来调用
# 调用这个方法后，只需要传入想要的文件名，txt地址和信息，即可以追加的方式记录信息

def logging_records(file_name, direction, message):
    import datetime
    import os

    today = datetime.date.today()
    current_time = datetime.datetime.now().__format__('%Y-%m-%d-%H-%M-%S')
    today_string = today.__format__('%Y-%m-%d')

    # file_direction = os.path.abspath('..') + '\\data\\a_share\\all_ticker_data\\' + file_name
    # 在日志文件中添加操作
    #
    file_final_name = direction + file_name + '.txt'
    # if not os.path.exists(direction):  # 如果某个目录不存在，则创建
    #     os.mkdir(file_final_name)

    # 创建完目录之后要开始记录日志
    f = open(file_final_name, 'a')

    f.write(message + ' @ ' + current_time + '\n')
    f.close()
