print("Please enter marks obtained in the following subject")
English=int(input("English:"))
Maths=int(input("Maths:"))
Science=int(input("Science:"))
Spanish=int(input("Spanish:"))
total=English+Maths+Science+Spanish
avg=total/4
if avg>=91:
    print("Your grade is A+")
elif avg>=81:
    print("Your grade is A")  
elif avg>=71:
    print("Your grade is B+")  
elif avg>=61:
    print("Your grade is B")   
elif avg>=51:
    print("Your grade is C+")         
elif avg>=41:
    print("Your grade is C ")
elif avg>=33:
    print("Your grade is D+")   
elif avg>=22:
    print("Your grade is D")   
else:
    print("You have FAILED")      
        