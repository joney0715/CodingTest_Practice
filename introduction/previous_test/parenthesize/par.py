
def function(par):
    answer = []
    #스텍에 추가하기 위한 조건
    input_stack = ["(","{","["]

    #입력된 값에서 괄호 묶음을 하나씩 처리
    for data in par:
        #괄호 묶음을 리스트화
        data = [i for i in data]
        #스텍 초기화
        stack = []
        #괄호 묶음에서 괄호 하나씩 처리
        for i in data:
            #괄호 열기인 경우
            if i in input_stack:
                #두번째 이후 괄호인 경우
                try:
                    #앞 괄호열기와 비교
                    j = abs(ord(i)-100) - abs(ord(stack[len(stack)-1])-100)
                    #앞 괄호와 비교해서 작은 괄호인 경우
                    if j > 0:
                        stack.append(i)
                    #앞 괄호와 비교해서 큰 괄호인경우 : 잘못된 괄호 사용
                    else:
                        answer.append(0)
                        break
                #첫 괄호 열기인 경우
                except:
                    stack.append(i)
            #괄호 닫기인 경우
            else:
                #스텍에 가장 최근에 들어간 괄호와 비교
                try:
                    #처리중인 괄호의 아스키코드 - 스텍에 최근에 추가된 괄호의 아스키코드
                    k = ord(i) - ord(stack[len(stack)-1])
                    #처리중인 괄호와 스텍에 최근에 추가된 괄호가 대응되는 경우, 스텍에서 괄호 삭제
                    if k >= 1 and k <= 2:
                        stack.pop()   
                    #대응이 안되는 경우                 
                    else:
                        answer.append(0)
                        break
                #첫 괄호가 닫기인 경우
                except:
                    answer.append(0)
        #마지막 괄호까지 처리 후에 스텍이 비어있는 경우 1 추가
        if len(stack) == 0:
            answer.append(1)

    return answer

par =["[(){()}]", "[}", "{[]}", "[())]", ")(", "{)"]
answer = function(par)
print(answer)
