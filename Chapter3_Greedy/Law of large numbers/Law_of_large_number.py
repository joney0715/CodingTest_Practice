#law of large number

n, m ,k = map(int, input().split())

if m >= k:
    n_list = list(map(int, input().split()[ :n]))

else:
    print("please enter M lager than K")
    exit()
    
n_list.sort(reverse = True)
first = n_list[0]
second = n_list[1]

count_first = int(m/(k+1))*k + m%(k+1)
count_second = m - count_first

largest_number = first * count_first + second * count_second

print(largest_number)
