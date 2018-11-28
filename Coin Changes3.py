''' O(nk)-time algorithm that makes change for any set of k different coin denominations'''
# Assumption: Any of the entered denominations should be penny.

n = int(input("Enter the amount in Cents: "))
denNumber = int(input("Enter how many denominations you want to enter: "))

print("Enter the denominations: ")
denominations = [int(input()) for i in range(denNumber)] #Taking the input of each denominationnumbers
denominations = sorted(denominations, reverse=True)      # Sorting all the denominations in decreasing order.
numbers = []                                             # This list will store number of times each denomination occurinng.

for i in range(denNumber):                               # Iterate through k times i.e through denomination list
    numbers.append(0)
    while(n >= denominations[i]):
        n -= denominations[i]
        numbers[i]+=1
print("Denomination in Descending order:                             ",denominations)
print("Number of times each denomination is occuring correpondingly: ",numbers)


