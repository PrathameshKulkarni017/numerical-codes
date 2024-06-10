def fibonacci_num(num):
    a = 0
    b = 1
    series = []
    if num<0:
        print("Invalid input")

    elif num ==0:
        series.append(a)
        return series
    
    elif num ==1:
        series.append(b)
        return series
    
    else:
        series.append(a)
        series.append(b)
        for i in range(2,num):
         c = a + b
         a = b
         b = c
         series.append(b)

        return series
    
num = int(input("Enter num: "))
obj = fibonacci_num(num)
print(obj)
for i in obj:
    print(i)
    

    

    
