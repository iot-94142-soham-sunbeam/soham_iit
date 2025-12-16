prices = [105, 110, 108, 112, 115, 116, 114]

rolling_avg = []

for i in range(len(prices) - 2):
    avg = sum(prices[i:i+3]) / 3
    rolling_avg.append(round(avg, 2))

print(rolling_avg)
[107.67, 110.0, 111.67, 114.33, 115.0]
