'''
사분면 고르기 python 풀이
https://doctcoder.tistory.com/entry/%EC%82%AC%EB%B6%84%EB%A9%B4-%EA%B3%A0%EB%A5%B4%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
x=int(input())
y=int(input())
if(x>0 and y>0): print(1)
if(x<0 and y>0): print(2)
if(x<0 and y<0): print(3)
if(x>0 and y<0): print(4)
