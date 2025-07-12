# Problem: Merge the Tools!

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sub = string[i:i+k]
        
        s = set()
        resSub = ''
        
        for ch in sub:
            if ch not in s:
                resSub += ch
                s.add(ch)
                
        print(resSub)
            

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)