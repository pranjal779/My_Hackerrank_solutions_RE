if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    score = []
    for arrs in arr:
        if arrs not in score:
            score.append(arrs)
            
    score_card = sorted(score)
    print(score_card[-2]) 
