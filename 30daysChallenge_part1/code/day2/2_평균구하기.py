
N = input()

scores = list(map(int, input().split(" ")))

sum_score = sum(scores)
max_score = max(scores)

N = len(scores)

print((1/N) * 100 + (1/N) * 100/max_score * (sum_score-max_score) )