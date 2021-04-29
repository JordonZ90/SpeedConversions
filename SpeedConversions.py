import speed


def display_menu():
    print("MENU")
    print("1. MPH to KPH")
    print("2. KPH to MPH to inches")
    print()


def convert_speed():
    option = int(input("Enter a menu option "))
    if option == 1:
        mph = float(input("Enter speed in MPH "))
        kph = speed.mph_to_kph(mph)
        kph = round(kph, 2)
        print(f"Speed is {kph} kph")
    elif option == 2:
        kph = float(input("Enter speed in KPH "))
        mph = speed.kph_to_mph(kph)
        mph = round(mph, 2)
        print(f"Speed is {mph} mph")
    else:
        print("You must enter a valid menu number ")


def main():
    display_menu()
    again = "y"
    while again.lower() == "y":
        convert_speed()
        print()
        again = input("Convert another measurement? (y|n) ")
        if again == "y".lower():
            display_menu()
        else:
            print()
    print("Goodbye!")


if __name__ == "__main__":
    main()
