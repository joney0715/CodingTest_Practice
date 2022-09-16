import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def cook(combi):
    s = 0
    for i in range(N//2):
        for j in range(i+1,N//2):
            s += S_table[combi[i]][combi[j]] + S_table[combi[j]][combi[i]]
    return s


def dfs(n, subset):
    subsets.append(subset)

    for i in range(n, len(ingred_list)):
        dfs(i+1, subset+[ingred_list[i]])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    ingred_list = list(range(N))
    S_table = [list(map(int,input().split())) for _ in range(N)]

   
    subsets = []
    dfs(0, [])
    
    ingreds = []
    for subset in subsets:
        if len(subset) == N//2:
            ingreds.append(subset)

    answer = []
    for ingred in ingreds:
        A_ingred = ingred
        B_ingred = []
        for i in ingred_list:
            if i not in ingred:
                B_ingred.append(i)
        
        A_result = cook(A_ingred)
        B_result = cook(B_ingred)
        
        answer.append(abs(A_result - B_result))
           
    print('#{}'.format(tc), min(answer))


