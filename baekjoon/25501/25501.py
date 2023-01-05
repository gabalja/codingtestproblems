'''
재귀의 귀재 python 풀이
https://doctcoder.tistory.com/entry/%EC%9E%AC%EA%B7%80%EC%9D%98-%EA%B7%80%EC%9E%AC-%ED%92%80%EC%9D%B4
'''
def recursion(s, l, r):
	global cnt
	cnt+=1
	if l >= r: return 1
	elif s[l] != s[r]: return 0
	else: return recursion(s, l+1, r-1)

def isPalindrome(s):
  return recursion(s, 0, len(s)-1)

n=int(input())
for i in range(n):
	inp=input()
	cnt=0
	print(isPalindrome(inp),cnt)
