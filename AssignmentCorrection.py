import random
otp=random.randint(1,20)
attempt=4
print(otp)

while True:
    try:
        uotp = int(input("enter no. between 1 to 20"))
        if uotp>20 or uotp<0:
            print("Please enter the Otp again between 1 to 20")
            continue
        else:
            if attempt!=0:
                if uotp==otp:
                    print("Otp successful, You may start")
                    break
                else :
                    print("wrong otp")
                    print("you are left with ",attempt-1,"attempts only")
                    attempt = attempt - 1


                    x=input("press yes or no")
                    if x == 'yes':
                        continue
                    elif x == 'no':
                        break
                    else:
                        while True:
                            y = input("wrong input press either yes or no")
                            if y == 'yes':
                                break
                            elif y == 'no':
                                raise SystemExit
                            else:
                                continue
                        continue

            else:
                print("Program crashed!!!! Sorry")

    except SystemExit:
        print("bye bye")
print("ok")


