from VictorCanTradeVeryWell.general_processing.only_for_login import for_login
import warnings


if __name__ == '__main__':
    from VictorCanTradeVeryWell.Dashboard_content.a_share.data_processing.limit_related.limit_up import limit_up_df
    import datetime
    for_login()
    warnings.filterwarnings("ignore")

    today = datetime.date.today()
    # limit_up_list = limit_up_df(today).Chinese_name
    # print(limit_up_list)

    # import os
    # root_path = os.path.abspath(os.path.dirname(__file__)).split('VictorCanTradeVeryWell')[0]
    # print(root_path)

    import pandas as pd

    import VictorCanTradeVeryWell.Dashboard_content
    a = VictorCanTradeVeryWell.Dashboard_content.LimitRelated(choice='customize', date=today, percentage=-0.08, direction='lower').result
    print(a)
