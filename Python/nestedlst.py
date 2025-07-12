#Problem: Nested Lists

if __name__ == '__main__':
    students = []
    min = secMin = 101
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        if score < min:
            secMin = min
            min = score
        elif score < secMin and score > min:
            secMin = score
    
    lst = [s[0] for s in students if s[1] == secMin]
            
    lst.sort()
    for i in lst:
        print(i)
        
