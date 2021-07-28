from VictorCanTradeVeryWell.login.login_account import login_account
from jqdatasdk import *

username = '13070162357'
password = '1234567890Sos'

if not login_account(username, password):
    print('login error')

data = get_all_securities(types=[], date=None)
