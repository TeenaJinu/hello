freshFruits=["apple","orange","strawberry","plum","grapes","pomegranate"]
driedFruits=["dates","rasins","grapes","mango", "apple","strawberry","banana"]

def intersect ( a, b) :
    commonFruits=[]
    for i in  (a) :
        if i in b :
            commonFruits.append(i)
    return commonFruits     
        

finalList =intersect (freshFruits,driedFruits)
print (finalList)

k=list(set(freshFruits).intersection(driedFruits))
print(k)

for a,b in zip(freshFruits,driedFruits) :
    print (a + " ," +b)