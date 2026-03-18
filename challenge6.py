n = int(input("Enter number of transactions: "))
transactions=[]
for i in range (n):
    t=int(input("enter amount:"))
    transactions.append(t)
categories={"normal":[],
"large":[],
"high_risk":[],
"invalid":[]
}
for t in transactions:
    if t<=0:
        categories["invalid"].append(t)
    elif t<=500:
        categories["normal"].append(t)
    elif t <= 2000:
        categories["large"].append(t)
    else:
        categories["high_risk"].append(t)

valid =[t for t in transactions if t>0]
sum_of_transactions=0
count=0
for v in valid:
     sum_of_transactions+=v
count=len(valid)
num_high_risk=len(categories["high_risk"])


if count > 5:
    frequent_transactions = True
else:
    frequent_transactions = False

if sum_of_transactions > 5000:
    large_spending = True
else:
    large_spending = False

if num_high_risk >= 3:
    suspicious = True
else:
    suspicious = False

if suspicious:
    risk = "High Risk"
elif large_spending or frequent_transactions:
    risk = "Moderate Risk"
else:
    risk = "Low Risk"

summary = (sum_of_transactions, count, num_high_risk)

print("\nCATEGORIES:", categories)
print("TRANSACTION SUMMARY:")
print("TOTAL TRANSACTION VALUE:", summary[0])
print("NUMBER OF TRANSACTIONS:", summary[1])
print("High Risk Count:", summary[2])
print("RISK CLASSIFICATION:", risk)