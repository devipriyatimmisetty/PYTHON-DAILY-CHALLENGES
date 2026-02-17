student_id=input("Enter Student ID: ")
email=input("Enter Email: ")
password=input("Enter Password: ")
referral=input("Enter Referral: ")
if( len(student_id) == 7 and student_id[0] == "C" and student_id[1] == "S" and student_id[2] == "E" and student_id[3] == "-"):
    if(student_id[-1].isdigit() == True and student_id[-2].isdigit() == True and student_id[-3].isdigit() == True):
        if(email.count("@") == 1 and email.count(".") == 1):
            if(email[0] != "@" and email[-1] != "@" and email[-1] == "u" and email[-2] == "d" and email[-3] == "e" and email[-4] =="."):
                if(len(password) >= 8 and password[0].isupper() == True and password.count("0")+password.count("1")+password.count("2")+password.count("3")+password.count("4")+password.count("5")+password.count("6")+password.count("7")+password.count("8")+password.count("9") > 0):
                    if(len(referral) == 6 and referral[0] == "R" and referral[1] == "E" and referral[2] == "F" and referral[3].isdigit() ==True and referral[4].isdigit() == True and referral[-1] == "@"):
                        print("APPROVED")
                    else:
                        print("REJECTED")
                else:
                    print("REJECTED")
            else:
                print("REJECTED")
        else:
            print("REJECTED")
    else:
        print("REJECTED")
else:
    print("REJECTED")