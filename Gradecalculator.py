name =input("Enter your name: ")
nep =int(input("Enter nep mark: "))
eng =int(input("Enter eng mark: "))
mat =int(input("Enter mat mark: "))
sci =int(input("Enter sci mark: "))
com =int(input("Enter com mark: "))
total = nep+eng+mat+sci+com
per =total/5
grade=""
if per>35 and per<45:
    print(f"Name:{name} Grade:C")
elif per>45 and per<60:
    print(f"Name:{name} Grade:B")
elif per>60 and per<80:
    print(f"Name:{name} Grade:A")
elif per>80 and per<=100:
    print(f"Name:{name} Grade:A+")
else:
    print(f"Name:{name} Grade:Fail")

