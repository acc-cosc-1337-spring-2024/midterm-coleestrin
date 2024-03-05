days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_day_of_week(day):
    if (day < 1 or day > 7):
        return "Error: Invalid Number"
    else:
        return days[day - 1]
