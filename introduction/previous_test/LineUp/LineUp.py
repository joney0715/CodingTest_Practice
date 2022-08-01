
student = [0,1,0,0,1,1,0,0,1,1]
k = 1

def solution(student,k):
    if student.count(1) < k:
        answer = 0
    else:
        ans = []
        count = 0
        for i in range(len(student)):
            if i != len(student)-1:
                if student[i] == 0:
                    count += 1
                else:
                    ans.append(count)
                    count = 0
            else:
                if student[i] == 0:
                    count += 1
                    ans.append(count)
                else:
                    ans.append(count)
                    count = 0
                    ans.append(count)
                
    ans = [i+1 for i in ans]


    return ans

print(solution(student,k))
            

        