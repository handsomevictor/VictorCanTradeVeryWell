from .Dashboard_content import LimitRelated

# a = LimitRelated()
from VictorCanTradeVeryWell.login.login_account import login_account

username = '13070162357'
password = '1234567890Sos'

if not login_account(username, password):
    print('login error')
