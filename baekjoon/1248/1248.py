'''
맞춰봐 python 풀이
https://doctcoder.tistory.com/entry/%EB%A7%9E%EC%B6%B0%EB%B4%90-%ED%92%80%EC%9D%B4
'''
n = int(input())
data = input()
k = 0
s = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        if data[k] == '0':
            s[i][j] = 0
        elif data[k] == '-':
            s[i][j] = -1
        else:
            s[i][j] = 1
        k += 1
 
 
def check(index):
    total = 0
    for i in range(index, -1, -1):
        total += answer[i]
        if total == 0 and s[i][index] != 0:
            return False
        elif total < 0 and s[i][index] != -1:
            return False
        elif total > 0 and s[i][index] != 1:
            return False
    return True
 
 
def dfs(index):
    if index == n:
        return True
 
    if s[index][index] == 0:
        answer[index] = 0
        return dfs(index + 1)
 
    for i in range(1, 11):
        answer[index] = s[index][index] * i
        if check(index) and dfs(index + 1):
            return True
            
    return False
 
 
answer = [0] * n
dfs(0)
print(' '.join(map(str, answer)))
