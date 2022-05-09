#law of large number

#초기값 입력
n, m ,k = map(int, input().split())

#m이 k보다 크거나 같다는 조건하에 n의 내부 값 입력
if m >= k:
    n_list = list(map(int, input().split()[ :n]))

else:
    print("please enter M lager than K")
    exit()

#n값을 내림차순으로 정렬
n_list.sort(reverse = True)
first = n_list[0]
second = n_list[1]

#가장 큰 값과 두 번째로 큰 값이 사용되는 패턴을 수식화
count_first = int(m/(k+1))*k + m%(k+1)
count_second = m - count_first

largest_number = first * count_first + second * count_second

#결과값 출력
print(largest_number)
