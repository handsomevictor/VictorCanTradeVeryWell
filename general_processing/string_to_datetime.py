# 这里date的格式应该是'2020-11-11'
def change_string_to_datetime(date_string):
    from datetime import date

    return date.fromisoformat(date_string)

if __name__ == "__main__":
    print(change_string_to_datetime('2020-11-12'))
