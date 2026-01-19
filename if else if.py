marks=int(input("Enter Your Marks : "))
if(marks>=90):
    if(marks>=95):
        print("Congradulations you Have got A++ Grade ")
    else:
        print("Congradulations you Have got A+ Grade ")
elif(90>=marks>=75):
     print("Congradulations you Have got B+ Grade ")
elif(75>=marks>=60):
     print("Congradulations you Have got C+ Grade ")
elif(60>=marks>=50):
     print("Congradulations you Have got E+ Grade ")
elif(50>=marks>=40):
    print("Congradulations you Have got D+ Grade ")
else:
    print("BETTER LUCK NEXT TIME")