full_name = input("Enter your full name: ")
email = input("Enter your email: ")
mobile = input("Enter your mobile number: ")
age = int(input("Enter your age: "))
if (full_name.count(" ") > 0 and full_name[0] != " " and full_name[-1] != " "):
    if (email.count("@") > 0 and email.count(".") > 0 and email[0] != "@"):
        if (len(mobile) == 10 and mobile.isdigit() == True and mobile[0] != "0"):
            if (age >= 18 and age <= 60):
                print("User Profile is Valid")
            else:
                print("User Profile is Invalid")
        else:
            print("User Profile is Invalid")
    else:
        print("User Profile is Invalid")
else:
    print("User Profile is Invalid")
