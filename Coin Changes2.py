''' available coins are in the denominations that are powers of c, i.e., the denominations are c0, c1, ...., ck for some integers c>1 and k>= 1.'''

n = int(input("Enter the amount in Cents: "))
denNumber = int(input("Enter how many denominations you want to enter: "))

print("Enter the denominations: ")
denominations = [int(input()) for i in range(denNumber)] 
denominations = sorted(denominations, reverse=True)      
numbers = []

for i in range(len(denominations)):
    numbers.append(int(n/denominations[i]))
    n = n%denominations[i]

print("Denomination in Descending order:                             ",denominations)
print("Number of times each denomination is occuring correpondingly: ",numbers)
