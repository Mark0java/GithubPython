print("Hello world")

mas1=[]

def Func1(num1, num2):
    test=True
    if (num1<0 or num2<0):
        raise ValueError('number must be non-negative')
    if (num1%num2!=0):
        test=False
    return test

print("Function 1: ")
print(Func1(int(input("enter first number: ")), int(input("enter second number: "))))

def Func2(num1, num2):
    if(num1 < 0 or num2 < 0):
        raise ValueError('number must be non-negative')
    mas1=[]
    ertest=False
    for i in range(num1, num2+1):
        test = True
        for j in range(2, int(i/2+1)):
            if(Func1(i, j)):
                test=False
        if(test):
            mas1.append(i)
            ertest=True
    if(ertest):
        return mas1
    else:
        raise ValueError('no simple digits')

print("Function 2: ")
print(Func2(int(input("enter first number: ")), int(input("enter second number: "))))

mas2=['a', ['c', 1, 3], ['f', 7, [4, ['4']]], [{'lalala': 111}]]
print(mas2)

mas3=[]

def Func3(spysok):
    for i in range(0, len(spysok)):
        if(isinstance(spysok[i], list)):
            Func3(spysok[i])
        else:
            mas3.append(spysok[i])

Func3(mas2)

print(mas3)