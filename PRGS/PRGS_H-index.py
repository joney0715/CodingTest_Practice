def solution(citations):
    for ref in range(10000):
        count = 0
        for i in citations:
            if ref <= i:
                count += 1
        if ref >= count:
            break
            
    return count