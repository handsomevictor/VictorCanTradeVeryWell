# 请先在JoinQuant中注册您的账号，再使用账号和密码登录本模块

def login_account(account_username, account_password):
    import jqdatasdk

    jqdatasdk.auth(account_username, account_password)
    is_auth_ok = jqdatasdk.is_auth()

    if is_auth_ok is True:
        return True
    else:
        return False

if __name__ == "__main__":
    username = '13070162357'
    password = '1234567890Sos'

    print(login_account(username, password))

