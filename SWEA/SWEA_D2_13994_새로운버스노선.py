
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    station = [0]*1001

    for _ in range(N):
        bus, start, end = map(int, input().split())

        if bus == 1:
            for a in range(start, end+1):
                station[a] += 1

        elif bus == 2:
            for b in range(start, end+1, 2):
                station[b] += 1
            if start % 2 and not end % 2:
                station[end] += 1
            if not start % 2 and end % 2:
                station[end] += 1

        else:
            if start % 2:
                for c in range(start, end+1):
                    if (not c%3) and c%10: 
                        station[c] += 1
                    if c == start and not ((not c%3) and c%10):
                        station[start] += 1
                    if c == end and not ((not c%3) and c%10):
                        station[end] += 1
            else:
                for c in range(start, end+1):
                    if not c%4: 
                        station[c] += 1
                    if c == start and c%4:
                        station[start] += 1
                    if c == end and c%4:
                        station[end] += 1
        print(station)

    max_value = station[0]
    for s in station:
        if max_value < s:
            max_value = s
    
    print('#{}'.format(tc), max_value)
    
