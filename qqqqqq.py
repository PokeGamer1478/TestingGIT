n = int(input())
k = 1
while k == 1 and (n != 0):
    if (n % 3 != 0):
        k = 0
    n = n//3
    print (n)
    
if (n == k):
    print ("TRUE")
else:
    print ("FALSE")
