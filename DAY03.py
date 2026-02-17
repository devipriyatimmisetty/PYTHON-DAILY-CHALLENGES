reg_no = 665
last_two =reg_no %100
N = int(input("Enter number of students: "))
marks = []
for i in range(N):
    m = int(input("Enter marks: "))
    marks = marks + [m]
    print(marks)
    valid = 0
    fail = 0
    for m in marks:
        if m < 0 or m > 100:
            print(m, "->Invalid")
        else:
            valid += 1
            if m >= 90:
                print(m, "->Excellent")
            elif m >= 75:
                print(m, "->Very Good")
            elif m >= 60:
                if (m == last_two):
                    m += 5
                print(m, "->Good")
            elif m >= 40:
                print(m, "->Average")
            else:
                print(m, "->Fail")
                fail += 1
    print("Final Summary:")
    print("Total Valid Students:", valid)
    print("Total Failed Students:", fail)