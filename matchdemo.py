Week = 'Day3dd'

match Week:
    case 'Day1':
        print("Today is Monday")
    case 'Day2':
        print("Today is Tuesday")
    case 'Day3':
        print("Today is Wednesday")
    case 'Day4':
        print("Today is Thursday")  
    case 'Day5':
        print("Today is Friday")    
    case 'Day6':
        print("Today is Saturday")
    case 'Day7':
        print("Today is Sunday")
    case _:
        print("Invalid day")