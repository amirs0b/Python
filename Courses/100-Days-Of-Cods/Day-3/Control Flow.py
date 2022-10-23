print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm ? "))

pay = 0

if height > 120:
    print("You can ride the rollercoaster !")
    age = int(input("What is your age ? "))
    if age < 12:
        print("Child tickets are  $5.")
        pay += 5
    elif age <= 18:
        print("Youth tickets are $7.")
        pay += 7
    else:
        print("Adult tickets are $12.")
        pay += 12

    wants_photo = input("Do you want a photo taken? Y or N. ").lower()

    if wants_photo == "y":
        pay += 3

    print(f"Your final bill is {pay}")


else:
    print("Sorry, you have to grow aller before you can ride.")
