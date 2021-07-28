

if __name__ == '__main__':
    from VictorCanTradeVeryWell.general_processing.only_for_login import for_login
    import datetime
    import jqdatasdk as jq
    today = datetime.date.today()
    two_days_ago = today - datetime.timedelta(4)
    for_login()

    # print(jq.get_index_stocks)
    print(jq.get_industries(name='zjw', date=today))
