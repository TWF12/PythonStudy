def check_temperature(temp):
    if temp > 37.5:
        return "发烧, 需要隔离"
    elif temp < 36.0:
        return "体温过低, 需要保暖"
    else:
        return "体温正常"
print(check_temperature(38.5))
