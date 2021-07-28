from VictorCanTradeVeryWell.Dashboard_content.a_share.data_processing.limit_related.limit_down import limit_down_df
from VictorCanTradeVeryWell.Dashboard_content.a_share.data_processing.limit_related.limit_up import limit_up_df
from VictorCanTradeVeryWell.Dashboard_content.a_share.data_processing.limit_related.limit_customized import limit_customized_df


# 这里定义choice，当用户传入up参数的时候，可以直接做到用up_list = LimitRelated.limit_up_list获取当日涨停股票
# LimitRelated实例化中,传入的参数介绍:
# get_data = LimitRelated(choice='customize', date=today, percentage=0.08, direction='lower').result
# 这里choice只有三种选择,up, down和customize, date传入datetime格式的日期,percentage是小数形式,direction只有higher和lower两种形式

class LimitRelated:
    percentage = 0.09
    direction = 'higher'

    def __init__(self, choice, date, percentage=percentage, direction=direction):
        if choice == 'up':
            self.result = limit_up_df(date)
        elif choice == 'down':
            self.result = limit_down_df(date)
        elif choice == 'customize':
            self.result = limit_customized_df(date, percentage, direction)

        self.date = date
        self.percentage = percentage
        self.direction = direction

    # def limit_up_df(self, date):
    #     return self.result
    #
    # def limit_down_df(self):
    #     return self.result
    #
    # def limit_customized_df(self):
    #     return self.result

if __name__ == '__main__':
    from VictorCanTradeVeryWell.general_processing.only_for_login import for_login
    for_login()
    import datetime
    import warnings
    warnings.filterwarnings('ignore')
    today = datetime.date.today()

    get_data = LimitRelated(choice='customize', date=today, percentage=0.08, direction='lower').result
    print(get_data)
