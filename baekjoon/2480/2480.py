'''
주사위 세개 풀이
https://doctcoder.tistory.com/entry/%EC%A3%BC%EC%82%AC%EC%9C%84-%EC%84%B8%EA%B0%9C-%ED%92%80%EC%9D%B4
'''
a,b,c=map(int,input().split())
if(a==b and b==c): print(a*1000+10000)
elif(a==b or a==c): print(a*100+1000)
elif(b==c): print(b*100+1000)
else: print(max(a,b,c)*100)
