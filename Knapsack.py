objects = int(input("Enter Number of objects "))

print("Enter profits for each input")
profits = [int(input()) for i in range(objects)]

print("Enter weights for each objects")
weights = [int(input()) for i in range(objects)]

#x = [0 for i in range(objects)]
limit = int(input("Enter maximum capacity of bag "))

priority = [profits[i]/weights[i] for i in range(objects)]

totalProfit = 0

for i in range(1, len(priority)):
    key = priority[i]
    key1 = profits[i]
    key2 = weights[i]
    j = i-1
    while j >=0 and key > priority[j]:
        priority[j+1] = priority[j]
        profits[j+1] = profits[j]
        weights[j+1] = weights[j]
        j = j-1
    priority[j+1] = key
    profits[j+1] = key1
    weights[j+1] = key2

for i in range(objects):
    if(limit > weights[i]):
        limit -= weights[i]
        totalProfit += profits[i]
    else:
        break
    
if(limit != 0):
    totalProfit += ((limit/weights[i])*(profits[i]))
print("Total Profit is: ",totalProfit)
    






    
