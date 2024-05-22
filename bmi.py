def calc_bmi(h,w):
    print("height = ", h)
    print("weight = ", w)
    bmi = w/(h*h)
    print("BMI = ", bmi)
    if bmi < 18.5:
        status = "Under Weight"
    elif bmi <= 25:
        status = "Normal Weight"
    else:
        status = "Over Weight"
    print("You are ", status)
calc_bmi(1.73,57)
