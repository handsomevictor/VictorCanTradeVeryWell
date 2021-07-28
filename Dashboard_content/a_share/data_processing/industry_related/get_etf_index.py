from VictorCanTradeVeryWell.Dashboard_content.a_share.data_processing.industry_related.get_all_industry import get_all_industry
a = get_all_industry('2021-07-20')
import jqdatasdk as jq
print(a[1][2])

# print(jq.get_price('801750', start_date='2021-07-20', end_date='2021-07-20', frequency='minute', skip_paused=False, fq='pre',))

# jq.get_all_securities(types=['index'], date=None).to_csv('all_index.csv', encoding="utf_8_sig")\
# jq.get_all_securities(types=['etf'], date=None).to_csv('all_etf.csv', encoding="utf_8_sig")
# print(jq.get_all_securities(types=['etf'], date=None))
etf = list(jq.get_all_securities(types=['etf'], date=None).index)[5]
print(etf)
# print(jq.get_price(etf, start_date='2021-07-20', end_date='2021-07-20', frequency='minute', skip_paused=False, fq='pre'))



# 本方法返回的是申万行业指数数据
# 本package用到的所有指数均为ETF指数
#

# 这个方法返回所有etf在当日截至到目前的每分钟的information
def get_etf_index(time):
    import jqdatasdk as jq
    import datetime

    total_etf_index = jq.get_all_securities(types=['etf'], date=None).index
    pass


# 以下方法返回今天截至到目前为止的所有分钟，datetime格式
def get_all_minutes():
    import datetime

    today = datetime.date.today()
    today = today.strftime('%Y-%m-%d %H:%M:%S')
    pass

