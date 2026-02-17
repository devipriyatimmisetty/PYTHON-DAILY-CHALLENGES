full_name="DEVI PRIYA TIMMISETTY"
n=int(input("enter no. of resource requests:"))
requests=[]
for i in range(n):
    request =int(input(f"enter request no. {i+1}:"))
    requests.append(request)

valid_requests=0
low_demand=[]
no_demand=0
moderate_demand=[]
high_demand=[]
invalid_requests=[]

for request in requests:
    if request<0:
        print(request, "-->Invalid request")
        invalid_requests.append(request)
    else:
        valid_requests += 1
        if request==0:
            print(request,"-->No demand")
            no_demand+=1

        elif request<=20:
            print(request, "-->Low demand")
            low_demand.append(request)

        elif request<=50:
            print(request, "-->Moderate demand")
            moderate_demand.append(request)

        else:
            print(request, "-->High demand")
            high_demand.append(request)

print("Before personalization:")
print("Invalid Requests",invalid_requests)
print("Low Demand",low_demand)
print("Moderate Demand",moderate_demand)
print("High Demand",high_demand)
print("Total Valid Students:",valid_requests)

print("After personalisation:")
l=0
removed_requests=0
for ch in full_name:
    if ch!=" ":
        l=l+1
PLI=l%3
print("length of name:",l)
print("PLI value:",PLI)
if PLI==0:
    print("Applied Rule: A -Low Demand Removed")
    removed_requests=len(low_demand)
    low_demand=[]
elif PLI==1:
    print("Applied Rule: B -High Demand Removed")
    removed_requests=len(high_demand)
    high_demand=[]
else:
    print("Applied Rule: C -Only Keep Moderate Demand")
    removed_requests=len(low_demand)+len(high_demand)+no_demand+len(invalid_requests)
    low_demand=[]
    high_demand=[]
    invalid_requests=[]

print("Total Requests Removed Due to PLI:",removed_requests)
print("Invalid requests:",invalid_requests)
print("Low Demand",low_demand)
print("Moderate Demand",moderate_demand)
print("High Demand",high_demand)







