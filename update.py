from automatiq import update
def update1():
    print("_____________________________________________")
    print("Enter a digit to choose an option")
    print("_____________________________________________")
    print("0. update both BHT-EMR-API and HIS-core")
    print("1. update BHT-EMR-API")
    print("2. update HIS-Core")
    print("_____________________________________________")
    
    option = input()  # Capture user input
    print("_____________________________________________")
    
    if option == "0":
        print("Updating both BHT-EMR-API and HIS-core...")
        print("_____________________________________________")
        update(int(option))
    elif option == "1":
        print("Updating BHT-EMR-API...")
        print("_____________________________________________")
        update(int(option))
    elif option == "2":
        print("Updating HIS-Core...")
        print("_____________________________________________")
        update(int(option))
    else:
        print("Invalid option selected. Please enter a valid option.")


if __name__ == "__main__":
    update1()