#This program returns pig latin word of the english  word


vowels="aeiou"
def igpay (engWord):
    word=engWord.lower()
    firstLetter = word[0]
    if firstLetter in vowels :
        
        print (engWord + "{}".format("way"))
    else :       
        for l in engWord :   
            if l in vowels :
                pos=engWord.find(l)
                pre=engWord[:pos]
                w= engWord[pos:]
                print (w + pre +"{}".format("ay"))
                break
       
igpay("apple")
