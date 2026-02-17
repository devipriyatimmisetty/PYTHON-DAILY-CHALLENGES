regno="AP24110011665"
d=int(regno[-1])
n=int(input("Enter number of activity scores:"))
scores=[]
for i in range(n):
    s=int(input("Enter activity score:"))
    scores=scores+[s]
print("Registration Num (d):",d)
low_risk=[]
med_risk=[]
high_risk=[]
critic_risk=[]
ignored_count=0
valid_count=0
for i in range(n):
    if(scores[i]<0):
        ignored_count = ignored_count+1
    elif(scores[i]<=30):
        low_risk = low_risk + [scores[i]]
        valid_count = valid_count+1
    elif(scores[i]<=60):
        med_risk = med_risk + [scores[i]]
        valid_count = valid_count+1
    elif(scores[i]<=100):
        high_risk = high_risk + [scores[i]]
        valid_count = valid_count+1
    else:
        critic_risk = critic_risk + [scores[i]]
        valid_count = valid_count+1
print("Low Risk:",low_risk)
print("Medium Risk:",med_risk)
print("High Risk:",high_risk)
print("Critical Risk:",critic_risk)
removed=0
print("After Personalized Filtering:")
removed = len(critic_risk)
critic_risk=[]
print("Low Risk:",low_risk)
print("Medium Risk:",med_risk)
print("High Risk:",high_risk)
print("Critical Risk:",critic_risk)
print("Total Valid Entries:",valid_count)
print("Ignored Entries:",ignored_count)
print("Removed due to personalization:",removed) 