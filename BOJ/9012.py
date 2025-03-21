num = int(input()) 

def vpsTest(arr) :
    stack = []
    for i in arr :
        if i == "(" :
            stack.append(i)
        elif i == ")" :
            if len(stack) == 0 :
                print("NO")
                return
            else :
                stack.pop() 
    if len(stack) == 0 :
        print("YES")
    else :
        print("NO") 


for _ in range(num) :
    arr = list(input()) 
    vpsTest(arr)
