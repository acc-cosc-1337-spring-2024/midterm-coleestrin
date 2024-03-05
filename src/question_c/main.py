from question_c import get_day_of_week

def main():
    

    dayInput = int(input("Day number? (1-7)"))
    print(f"Day of week is {get_day_of_week(dayInput)}")    
    
    quitInput = input("Do you want to quit? (Y/N)")
    if (quitInput == "Y"):
        return
    
    main()

main()