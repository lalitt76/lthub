print ("Hello Monitor")

FName = "Lalit"
LName = "Tyagi"

Name = FName + " " + LName
print (Name)

Odd = [1,3,5,7,9]
Even = [2,4,6,8]

print len(FName)

Age = 40

if FName == "Lalit1" and Age == 40:
    print("Your Name is " + FName)
elif FName == "Lalit" and Age == 40: 
     print("Your Correct Name is " + FName)
else:
    print("Wrong Name")

if FName in ["Lalit", "Chris"] and Age == 40:
    print ("Correct Answer " + FName)
else:
    print ("Wrong Answer")
    
#Loops    
    
for number in Odd:
    print number
    
count = 0
while count < 5:
    print (count)
    count += 1
#Loops End

#Function
def MyAddFunction(a,b):
    if a != b:
        return a + b
    else:
        return a - b
    
Result = MyAddFunction(3,3)

print "Outcome of function is %s" %(Result)

#Function End

#Class
class NewClass:

    def CarValue(n):
        if n == "Acura":
            return 10000
        elif n == "Honda":
            return 5000
        else:
            return 100
    
    CarName = "Acura"
    CarPrice = CarValue(CarName)
        
myCar = NewClass()

print "My Car name is %s and price is %d" % (myCar.CarName, myCar.CarPrice)

#Class End

#Dictionaries

YellowBook = {}
YellowBook['Lalit'] = 6316815644
YellowBook['Chris'] = 6316818888

for name, number in YellowBook.items():
 print("Phone number of %s is %d" % (name, number))
    
print YellowBook['Lalit']
print(YellowBook)

Contacts = {
    'Brian' : 6316819876,
    'Marc' : 651678888,
    'Mike' : 7891239999
}

print(Contacts)

Contacts['Brian'] = 9998886666

del Contacts['Mike']

print(Contacts)

print(Contacts)

if "Mike" not in Contacts:
    print("Mike is not listed in the Contacts")    

if "Brian" in Contacts:
    print("Brian is in the contacts")


