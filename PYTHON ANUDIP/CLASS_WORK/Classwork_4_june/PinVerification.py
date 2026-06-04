correct_pin= 1234
while True:
    pin=int(input("Enter the correct pin: "))
    if(pin==correct_pin):
        print("Access Granted")
        break
    else:
        print("Incorrect pin. Try Again..")