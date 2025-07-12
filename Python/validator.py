# Problem: String Validators

if __name__ == '__main__':
    s = input()
    
    hasAlNum = False
    hasAlpha = False
    hasDigit = False
    hasLower = False
    hasUpper = False
    
    for i in s:
        if i.isalnum():
            hasAlNum = True
        if i.isalpha():
            hasAlpha = True
        if i.isdigit():
            hasDigit = True
        if i.islower():
            hasLower = True
        if i.isupper():
            hasUpper = True
            
print(hasAlNum)
print(hasAlpha)
print(hasDigit)
print(hasLower)
print(hasUpper)
            