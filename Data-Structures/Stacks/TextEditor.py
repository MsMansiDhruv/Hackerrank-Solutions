from collections import deque

S = ""
previousState = deque()
for _ in range(int(input())):
    line = input().split()
    # print(line)
    if line[0] == '1':
        previousState.append(S)
        S += line[1]
        # print(previousState)
    elif line[0] == '2':
        previousState.append(S)
        S = S[:-int(line[1])]   
    elif line[0] == '3':
        print(S[int(line[1])-1])
    elif line[0] == '4':
        S = previousState.pop()
        # print(S)
    
