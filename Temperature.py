fah=0
cel=0
print("--------Temperature Converter-----------")
print("1.Fahrenheit to Celsius       2.Celsius to Fahrenheit")
x=int(input("Enter Your choice"))
if x==1:
    fah=float(input("Enter how much degrees"))
    cel=(fah-32)*5/9
    print("The degree in celsius is :" , fah)
    
elif x==2:
    cel=float(input("Enter how much degrees"))
    fah=cel*(9/5)+32
    print("The degree in fahrenheit is :" , fah)

else:
    print("Invalid Input")
    


