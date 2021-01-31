
romToInt = {
    'i': 1,
    'v':5,
    'x':10,
    'l':50,
    'c':100,
    'm':1000 }

def romanToInteger(roman):
    total=0
    length=len(roman)
    roman=roman.lower()
    try:
        
        for c,i  in enumerate(roman) :
            if length == c+1 :
                total=total+romToInt[i] 
                break        
            if romToInt[i] >= romToInt[roman[c+1]] :
                total = total +romToInt[i] 
           
            elif (romToInt[i]) < romToInt[roman[c+1]]:
                total = total -romToInt[i] 
              
        return total
    except:
        print("invalid input")

    
rNumeral = input ("Enter Roman numeral: ")
result=romanToInteger(rNumeral)
print ("Integer = "+ str(result))
