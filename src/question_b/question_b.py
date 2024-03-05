def get_bonus_pay(sales):
    if sales < 0 or sales > 1999:
        return "Error: Invalid Argument"
    elif sales >= 0 and sales <= 499:
        return sales * 0.05
    elif sales >= 500 and sales <= 999:
        return sales * 0.06
    elif sales >= 1000 and sales <= 1499:
        return sales * 0.07
    elif sales >= 1500 and sales <= 1999:
        return sales * 0.08