from time import process_time
import random
myList = []

# Checks if list is ordered
def isOrdered(myList):
    N = len(myList)
    for n in range(0,N-1):
        if myList[n] > myList[n+1]:
            return False
    return True

# Shuffles list by just swapping two elements
def shuffle(myList):
    N = len(myList)
    i = random.randint(0,N-1)
    j = random.randint(0,N-1)
    t = myList[i]
    myList[i] = myList[j]
    myList[j] = t

# Generates random list
for n in range(10):
    myList.append(random.randint(1,100))

# Print list unordered
print(myList)

# Shuffle order
print("Shuffle sort....")
t1 = process_time()
while isOrdered(myList) == False:
    shuffle(myList)
t2 = process_time()
print(myList)

# Result
print("This took", t2-t1, "seconds to SHUFFLE sort.")

#Quit
quit()