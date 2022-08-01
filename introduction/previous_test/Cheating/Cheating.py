
answer_sheet = "53241"
sheets = ["53241","42133","53241","14354"]

def solution(answer_sheet, sheets):
    answer_sheet = list(answer_sheet)
    sheets = [list(sheet) for sheet in sheets]

    for i in range(len(sheets)):
        for j in range(len(answer_sheet)):
            if sheets[i][j] == answer_sheet[j]:
                sheets[i][j] = 0

    ans_list = []
    for i in range(len(sheets)):
        for j in range(i+1, len(sheets)):
            ans = []
            for k in range(len(sheets[j])):
                if sheets[i][k] != 0 and sheets[i][k] == sheets[j][k]:
                    ans.append(1)
                else:
                    ans.append(0)

            count_1 = ans.count(1)
            
            #차라리 스텍을 사용해서 1이면 스텍에 넣고 연속된 숫자 갯수 계산, 0이면 스텍 초기화를 하는거가 직관적
            #stack = []
            #count = []
            #for i in ans:
            #if i == 1:
            #    stack.append(i)
            #    s = sum(stack)
            #    count.append(s)
            #else:
            #    stack = []
            #max_count = max(count)

            max_count = 0
            count = 0
            for x in range(len(ans)):
                if ans[x] == 1:
                    count += 1
                    if max_count < count:
                        max_count = count
                        count = 0
            cal = count_1 + max_count*max_count
            ans_list.append(cal)
    
    answer = max(ans_list)
    return answer

print(solution(answer_sheet, sheets))
