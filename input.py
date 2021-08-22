global name, sex, age, weight, height, itype

def basic_details():
	global name, sex, age, weight, height
	print("Welcome to your HEALTH TRACKER APP\n\nPlease provide the following details:\n")
	name = input("Your name: ")
	sex  = input("\nYour sex: ")
	age  = int(input("\nYour age in years: "))
	weight  = int(input("\nYour weight in kg: "))
	height  = int(input("\nYour height in cm: "))
	choose_input_type()

def choose_input_type():
	global itype
	print("\n\nDo you wish to enter weekly(w), monthly(m), or quarter-yearly(q) data?")
	itype = input("Please choose either w, m or q as above\n")
	
	if (itype not in ["w", "m", "q"]):
		print("\nPlease enter valid input")
		choose_input_type()

	choose_input_method()
	

def choose_input_method():
	print("implement input method\n\n")


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