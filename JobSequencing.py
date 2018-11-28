# Assumption that each job is taking 1 unit of time.
jobs = int(input("Enter the number of jobs: "))

print("Enter profits for each jobs: ")
profits = [int(input()) for i in range(jobs)]

print("Enter the Dealines for each job: ")
deadlines = [int(input()) for i in range(jobs)]

for i in range(1, len(profits)):
    key = profits[i]
    key1 = deadlines[i]
    j = i-1
    while j >=0 and key > profits[j]:
        profits[j+1] = profits[j]
        deadlines[j+1] = deadlines[j]
        j = j-1
    profits[j+1] = key
    deadlines[j+1] = key1

jobSequence = [0]*(max(deadlines))
totalProfit = 0

for i in range(jobs):
    if(jobSequence[deadlines[i]-1] == 0):
        jobSequence[deadlines[i]-1] = i+1
        totalProfit+=profits[i]
    else:
        j = deadlines[i]-1
        while(j>=0 and jobSequence[j] != 0):
            j-=1
        if(j>=0):
            jobSequence[j] = i+1
            totalProfit+=profits[i]
    #print(jobSequence)
print("Order of Jobs are: ",jobSequence,"and profit is: ",totalProfit)
        



