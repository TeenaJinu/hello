#Double a number starting from 1 till it reach atleast trillion and count the iterations

startNo=1
iterCount=0
while startNo <= 10**12 :
    startNo = startNo*2
    print (startNo) 
    iterCount =iterCount + 1   
print ("No of iterations = " + str(iterCount))      