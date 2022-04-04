# 以后调用这个结果就能直接返回所有行业名
# 调用的时候第一个是行业名，第二个是行业代码
import jqdatasdk as jq

def get_all_industry(date):
    industry_classification_data = jq.get_industries(name='sw_l1', date=date)
    return list(industry_classification_data.iloc[:, 0]), list(industry_classification_data.index)


if __name__ == '__main__':
    from VictorCanTradeVeryWell.general_processing.only_for_login import for_login
    import datetime
    import jqdatasdk as jq
    today = datetime.date.today()
    two_days_ago = today - datetime.timedelta(4)
    for_login()

    print(get_all_industry(date=today))
