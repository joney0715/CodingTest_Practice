import sys

sys.stdin = open('imput.txt', 'r')
input = sys.stdin.readline

change = [
    '0001101', 
    '0011001', 
    '0010011', 
    '0111101', 
    '0100011', 
    '0110001',
    '0101111', 
    '0111011', 
    '0110111', 
    '0001011'
    ]
    
hex2bin = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111',
}


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    

    for _ in range(N):
        row = input()
        if int(row) != 0:
            row = str(int(row[::-1]))

            code_list = []
            for i in range(8):
                code = change.index(row[7*i : 7*i+7][::-1])
                code_list.append(code)

