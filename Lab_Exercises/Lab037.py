today_date=int(input("enter todays date"))

match today_date:
    case 1:
        print("todays date is 1")
    case 2:
        print("todays date is 2")
    case 3:
        print("todays date is 3")
    case 4:
        print("todays date is 4")
    case _:
        print("wrong date")