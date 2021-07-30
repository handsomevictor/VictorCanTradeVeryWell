# VictorCanTradeVeryWell

A Python open source package that can help people better monitor and analyze the financial market.

This version is for test and it was uploaded on test.pypi.org. It has some basic functions and one can write something like the following:



**First install the package:**

```python
pip install -i https://test.pypi.org/simple/ VictorCanTradeVeryWell==0.0.2
```



**Then write something like this:**

```python
Import the packages
import datetime
import VictorCanTradeVeryWell as vtw

today = datetime.date.today()
yesterday = today - datetime.timedelta(1)

vtw.LimitRelated(choice='customize', date=yesterday, direction='higher', percentage=0.09).result
```

**Now you can see directly what A-share stocks skyrocketed by 9% yesterday and their corresponding industries (in DataFrame type).**



I will add many more functions & integrated strategies & demo backtesting system & a dashboard (for users to plan all things that he wants to see) and update the depository before September.
