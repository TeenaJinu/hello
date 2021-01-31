# To print list of cards in a stack

cardNames=["Spade","Club","Hearts","Diamond"]
cardNos= range(1,14)
cards=[]
for n in cardNames:
    for num in cardNos:
        print (num)
        cards.append("{0}  {1}".format(n,num))
        
print (cards)



 