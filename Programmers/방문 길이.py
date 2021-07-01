# https://programmers.co.kr/learn/courses/30/lessons/49994

def reachable(x, y):
    if x < -5 or y < -5 or x > 5 or y > 5:
        return False
    return True

def solution(dirs):
    answer = 0
    dir = {'U': (0,1),
            'D': (0,-1),
            'R': (1,0),
            'L': (-1,0)
           }
    x = 0
    y = 0
    records = []
    for direction in dirs:
        move = dir[direction]    
        dx = x + move[0]
        dy = y + move[1]
        # print(x, y, dx, dy, direction, move)
        
        if reachable(dx, dy):
            new = (x, y, dx, dy)
            new_back = (dx, dy, x, y)
            been = 0
            if new not in records:
                records.append(new)
                been += 1
            if new_back not in records:
                records.append(new_back)
                been += 1
                
            if been > 0:
                answer += 1
            
            x = dx
            y = dy
            
    
    return answer
