'''
골드바흐 파티션 python 풀이
https://doctcoder.tistory.com/entry/%EA%B3%A8%EB%93%9C%EB%B0%94%ED%9D%90-%ED%8C%8C%ED%8B%B0%EC%85%98-%ED%92%80%EC%9D%B4
'''
def get_primary_list(n):
    array = [1 for _ in range(n+1)]

    for i in range(2, int(n ** 0.5) + 1):
        if array[i]:
            j = 2

        while i * j <= n:
            array[i * j] = 0
            j += 1

    return array

T = int(input())
nums = [int(input()) for _ in range(T)]
max_num = max(nums)
primarys = get_primary_list(max_num)

for num in nums:
    result = 0

    for i in range(2, num // 2 + 1):
        if primarys[i] and primarys[num - i]:
            result += 1

    print(result)
