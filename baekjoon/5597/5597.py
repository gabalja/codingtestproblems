'''
과제 안 내신 분..? python 풀이
https://doctcoder.tistory.com/entry/%EA%B3%BC%EC%A0%9C-%EC%95%88-%EB%82%B4%EC%8B%A0-%EB%B6%84-%ED%92%80%EC%9D%B4
'''
stu=[i+1 for i in range(30)]
for i in range(28):
	stu.remove(int(input()))
print(stu[0])
print(stu[1])
