history = {
    "+":[],
    "-":[],
    "*":[],
    "/":[]
}
while True:
    try:
        a = int(input("Введите первое число "))
        b = int(input("Введите второе число "))
        c = str(input("Введите математическую операцию "))
        
        if c=="+":
            result = a + b
            print(result)
            history["+"].append(f"{a}+{b}={result}")
        elif c=="-":
            result = a - b
            print(result)
            history["-"].append(f"{a}-{b}={result}")
        elif c=="/":
            result = a / b
            print(result)
            history["/"].append(f"{a}/{b}={result}")
        elif c=="*":
            result = a * b
            print(result)
            history["*"].append(f"{a}*{b}={result}")
        else:
            print("такой операции нет")
        
        
        for operation, operations_list in history.items():
            print(f"{operation} {operations_list}")
                
    except ValueError:
        print("Ошибка: введите корректные числа!")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")

    


