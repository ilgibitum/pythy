male = input("Male ")
age = input("Age ")

if (male in ("m", "M", "м", "М")) and (int(age) >= 18) and (int(age) < 50):
    print("Army!")
else:
    print("Relax")
