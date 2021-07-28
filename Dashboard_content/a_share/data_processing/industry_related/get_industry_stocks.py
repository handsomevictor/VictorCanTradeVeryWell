# 运行本代码可以生成一个DataFrame，里面包含了所有行业的所有的股票

def get_industry_stocks():
    import jqdatasdk as jq
    from VictorCanTradeVeryWell.Dashboard_content.a_share.data_processing.industry_related.get_all_industry import get_all_industry
    import datetime
    import pandas as pd

    today = datetime.date.today()
    all_industry = get_all_industry(today)
    industry_code_list = all_industry[1]
    industry_name_list = all_industry[0]

    # 返回每个industry所包含的股票代码
    target_df = {}
    for i in industry_code_list:
        target_df[i] = jq.get_industry_stocks(i)

    # 做DataFrame
    first_column = industry_name_list
    second_column = target_df.values()
    third_column = target_df.keys()
    zip_df = zip(first_column, second_column)
    df = pd.DataFrame(list(zip_df))
    df.columns = ['industry_name', 'industry_companies']
    df['industry_code'] = list(third_column)
    df = df.set_index('industry_code')

    return df

if __name__ == '__main__':
    from VictorCanTradeVeryWell.general_processing.only_for_login import for_login
    import datetime
    import jqdatasdk as jq
    today = datetime.date.today()

    for_login()

    print(get_industry_stocks())
