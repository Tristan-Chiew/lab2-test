print("This is a bs lab excerise")

input_values = []
usable_values = []
def display_main_menu():
    input_values = input("Enter some numbers seperated by commas")

def get_user_input():
    usable_values = input_values.split(,)   

def calc_avg():
    total = 0
    sum = 0
    for i in usable_values:
        total += i
        sum += 1
    return total/sum

def find_min_max():
    return min(usable_values), max(usable_values)

def sort_temp():
    print("dummy")

def calc_median():
    print("dummy")