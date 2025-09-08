name = input("请输入公司名: ")
stock_price = float(input("请输入当前股价: "))
stock_code = input("请输入股票代码: ")
stock_price_daily_growth_factor = float(input("请输入股票每日增长系数: "))
growth_days = int(input("请输入增长天数: "))
print(
    f"公司: {name}, 股票代码: {stock_code}, 当前股价{stock_price}\n每日增长系数是: %.1f, 经过%d天后的增长后, 股价达到了: %.2f" % (
        stock_price_daily_growth_factor, growth_days, stock_price * stock_price_daily_growth_factor ** growth_days))
