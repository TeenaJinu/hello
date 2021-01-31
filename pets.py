pets={"bird":3.5,"cat":5,"dog":7.25,"gerbil":1.5}
try:
    def petPrice(petName) :
        name= petName.lower()
        print("Price of " + petName + " is " + str(pets[petName]) )


    petName=input ("Enter the pet name:")
    petPrice(petName)
except: 
    print("Please enter a valid pet name") 