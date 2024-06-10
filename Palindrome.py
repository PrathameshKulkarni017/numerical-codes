def is_palindrome(num):
    list = [121, 123,133,112]
    if num<0:
        return False
    
    original_num = num
    rev = 0

    while num>0:
        digit = num%10 
        rev = rev *10 + digit
        num = num // 10
    if original_num == rev:
        return f"{original_num} is palindrome"
    else:
        return f"{original_num} is not palindrome"


    

num = int(input("Enter the number"))
print(is_palindrome(num))
