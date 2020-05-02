def depositProfit(deposit, rate, threshold):
    money = deposit
    years = 0
    while money < threshold:
        money += (money*(rate/100))
        years += 1
    return years
