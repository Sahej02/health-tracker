import os
from helper import *
global name, sex, age, weight, height, itype

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

def basic_details():
    global name, sex, age, weight, height, bmi
    print("Welcome to your HEALTH TRACKER APP\n\nPlease provide the following details:\n")
    name = input("Your name: ")
    sex  = input("\nYour sex: ")
    age  = int(input("\nYour age in years: "))
    try:
        metric = input("\nUse Metric System? Y or N\n")

        if metric.lower() == "n":
            print("\nUsing FPS for weight and height")
            weight  = int(input("\nYour weight in pounds: "))
            height  = int(input("\nYour height in inches: "))

            weight = int(weight * 0.453592)
            height = int(height * 2.54)

        elif metric.lower() == "y":
            print("\nUsing Metric System")
            weight  = int(input("\nYour weight in kg: "))
            height  = int(input("\nYour height in cm: "))

        else:
            assert(False)

        height = height/100
        assert(weight != 0)
        assert(height != 0)
    except:
        print("\nPlease enter valid height and weight input. TRY AGAIN\n\n")
        basic_details()

    bmi = round(weight/(height)**2, 2)
    choose_input_type()

def choose_input_type():
    global itype
    print("\n\nDo you wish to enter weekly(w), monthly(m), or quarter-yearly(q) data?")
    itype = input("Please choose either w, m or q as above.\n")
    
    if (itype not in ["w", "m", "q"]):
        print("\nPlease enter valid input")
        choose_input_type()


def print_basic():
    global name, bmi
    cls()
    print(f"Hello {name}")
    print(f"\nYour BMI is {bmi}")

    if bmi <= 18.5:
        print("\nPlease gain some weight")

    elif bmi >= 24.9:
        print("\nPlease lose some weight")

    else:
        print("\nYour BMI is healthy!")

def weekly():

    dist_in_metres, time_in_seconds, check = read_file("w")
    
    if check == False:
        print("\nPlease make sure complete data according to the chosen option is present in input.txt")
        print("\nCorrect input and restart the program")
        exit()

    metrics, award = week_stats(dist_in_metres, time_in_seconds)
    
    print_basic()
    print("\n*****************************************\n")
    print("Your weekly achievement is as follows:")
    print(f"\nYour fastest speed: { metrics['max_speed'] * 18/5} km/h")
    print(f"\nYour slowest speed: { metrics['min_speed'] * 18/5} km/h")
    print(f"\nYour longest distance: { metrics['max_dist']/1000} km")
    print(f"\nYour shortest distance: { metrics['min_dist']/1000} km")
    print(f"\nYour average speed: { metrics['avg_speed'] * 18/5} km/h")
    print(f"\nYour weekly average distance is: { metrics['avg_dist']/ 1000} km")

    if award == 0:
        print("\nCongratulations! You have achieved a 7/7 award this week!\n")

    else:
        print("\nSorry, no awards for you this week because you missed a day!\n")


def monthly():
    
    dist_in_metres, time_in_seconds, check = read_file("m")
    
    if check == False:
        print("\nPlease make sure complete data according to the chosen option is present in input.txt")
        print("\nCorrect input and restart the program")
        exit()
        

    weeks_list = []

    for i in range(4):
        week_dist = dist_in_metres[i*7: i*7 + 7]
        week_time = time_in_seconds[i*7: i*7 + 7]
        weeks_list.append(week_stats(week_dist, week_time))

    metrics, award, result = month_stats(weeks_list)
    print_basic()
    print("\n*****************************************\n")
    print("Your monthly achievement is as follows:")
    print(f"\nYour fastest speed: { metrics['max_speed'] * 18/5} km/h")
    print(f"\nYour slowest speed: { metrics['min_speed'] * 18/5} km/h")
    print(f"\nYour longest distance: { metrics['max_dist']/1000} km")
    print(f"\nYour shortest distance: { metrics['min_dist']/1000} km")
    print(f"\nYour average speed: { metrics['avg_speed'] * 18/5} km/h")
    print(f"\nYour weekly average distance is: { metrics['avg_dist']/ 1000} km")

    if award:
        print(f"\nCongratulations! You had a consecutive streak of {result} 7/7 weeks, with a break of 1-2 days allowed in one week\n")
    else:
        print(f"\nThere is no award this month, since you had no consecutive 7/7 weeks\n")

def quarterly():

    dist_in_metres, time_in_seconds, check = read_file("q")
    
    if check == False:
        print("\nPlease make sure complete data according to the chosen option is present in input.txt")
        print("\nCorrect input and restart the program")
        exit()

    months_list = []

    for i in range(4):
        month_dist = dist_in_metres[i*28: i*28 + 28]
        month_time = time_in_seconds[i*28: i*28 + 28]
        weeks_list = []
        for i in range(4):
            week_dist = dist_in_metres[i*7: i*7 + 7]
            week_time = time_in_seconds[i*7: i*7 + 7]
            weeks_list.append(week_stats(week_dist, week_time))

        months_list.append(month_stats(weeks_list))

    metrics, award, result = quarter_stats(months_list)
    print_basic()
    print("\n*****************************************\n")
    print("Your quarterly achievement is as follows:")
    print(f"\nYour fastest speed: { metrics['max_speed'] * 18/5} km/h")
    print(f"\nYour slowest speed: { metrics['min_speed'] * 18/5} km/h")
    print(f"\nYour longest distance: { metrics['max_dist']/1000} km")
    print(f"\nYour shortest distance: { metrics['min_dist']/1000} km")
    print(f"\nYour average speed: { metrics['avg_speed'] * 18/5} km/h")
    print(f"\nYour weekly average distance is: { metrics['avg_dist']/ 1000} km")

    if award:
        print(f"\nCongratulations! You had a consecutive streak of {result} M/M months, with a break of 1-2 days in a week\n")
    else:
        print(f"\nThere is no award this quarter, since you had no consecutive M/M months\n")


if __name__ == "__main__":
    try:
        basic_details()

    except:
        print("\nSorry, you have provided invalid input, please try again\n")
        basic_details()

    if itype == "w":
        weekly()

    elif itype == "m":
        monthly()

    elif itype == "q":
        quarterly()