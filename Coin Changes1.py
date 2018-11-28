''' greedy algorithm to make change consisting of quarters, dimes, nickels, and pennies'''

n = int(input("Enter the values in cents: "))
coins = [25,10,5,1]
numbers = []
for i in range(len(coins)):
    numbers.append(int(n/coins[i]))
    n = n%coins[i]
print("Denomination in Descending order:                             ",coins)
print("Number of times each denomination is occuring correpondingly: ",numbers)
