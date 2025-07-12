#Problem: Lists

if __name__ == '__main__':
    N = int(input())
    lst = []
    for x in range(N):
        inpt = input().split()
        op = inpt[0]
        match op:
            case "insert":
                i = int(inpt[1])
                e = int(inpt[2])
                lst.insert(i, e)
            case "print":
                print(lst)
            case "remove":
                e = int(inpt[1])
                lst.remove(e)
            case "append":
                e = int(inpt[1])
                lst.append(e)
            case "sort":
                lst.sort()
            case "pop":
                lst.pop()
            case "reverse":
                lst.reverse()
                
