unit = input("What unit are you using? ")
temp = input("What temperapture is the water? ")

farenheight = 212
celsius = 100
kelvin = 373

if unit == "Farenheight" or unit == "farenheight" or unit == "f":
    if float(temp) < farenheight:
        print(f"Your water is not boiling, it is {farenheight - float(temp)} below boiling point")
    else:
        print("Your water is boiling")
elif unit == "Celsius" or unit == "celsius" or unit == "c":
    if float(temp) < celsius:
        print(f"Your water is not boiling, it is {celsius - float(temp)} below boiling point")
    else:
        print("Your water is boiling")
elif unit == "Kelvin" or unit == "kelvin" or unit == "k":
    if float(temp) < kelvin:
        print(f"Your water is not boiling, it is {kelvin - float(temp)} below boiling point")
    else:
        print("Your water is boiling")
else:
    print("I don't know those units")