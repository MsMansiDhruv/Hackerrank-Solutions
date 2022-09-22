from collections import deque
S = ""
undoS = deque()
n = int(input())

#Time complexity: O(n), Space complexity: O(n)
for i in range(n):
    line = input().split()
    
    if line[0]=='1':
        undoS.append(S)
        S += line[1]
    elif line[0]=='2':
        undoS.append(S)
        m = int(line[1])
        S = S[:-m]
    elif line[0]=='3':
        m = int(line[1])-1
        if m < len(S):
            print(S[m])   
    elif line[0]=='4':
        S = undoS.pop()
            
