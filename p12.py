

PrimeList = []

def initPrimeList(maxN):
    isPrime = [True]*(maxN+1)
    primeSum = 0
    for currNum in range(2, maxN+1):
        if isPrime[currNum]:
            primeSum += currNum
            PrimeList.append(currNum)
            multiples = currNum*2
            while multiples <= maxN:
                isPrime[multiples] = False
                multiples += currNum
def findFactors(num):
    factorList = []
    for prime in PrimeList:
        power = 0
        while num % prime == 0:
            power += 1
        if power > 0:
            factorList.append([prime, power])
    return factorList

def findDivisorCount(num):
    factorList = findFactors(num)
    numDivisors = 1
    for prime, power in factorList:
        numDivisors *= power + 1
    return numDivisors
    
DivisorNumList = [0]
def fillDivisorList(maxDivisor):
    triangle = 1
    DivisorNumList.append(1)
    currDivisor = 2
    print('running fill ')
    for i in range(2, 100):
        triangle += i
        numDiv = findDivisorCount(triangle)
        #print(i, triangle, numDiv, currDivisor)
        if numDiv < currDivisor:
            continue
        while numDiv >= currDivisor:
            DivisorNumList.append(triangle)
            currDivisor += 1
            if currDivisor > maxDivisor:
                return
     
       
'''
'''
        
# Enter your code here. Read input from STDIN. Print output to STDOUT

numList = []
t = int(input().strip())
print('reading ', t)
for a0 in range(t):
    n = int(input().strip())
    numList.append(n)

maxN = max(numList)
print('read', numList)
print("calling with", maxN)

initPrimeList(10**3)
print(PrimeList[:10])

fillDivisorList(maxN)
print(' back in main')
print(DivisorNumList)
#for n in numList:
#    print(DivisorNumList[n])
     
 

# multiples 
# 2 , 3^2 , 5 ^ 3 
# 2, 3, 4 

