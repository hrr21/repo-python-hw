import json

result = []
with open('text_77_L5.json', 'w') as f:
    with open('text_7_L5.txt', encoding='utf-8') as f_obj:
        profit = {}
        for line in f_obj:
            profit[line.split(' ')[0]] = int(line.split(' ')[2]) - int(line.split(' ')[3])
        average_profit = sum([int(i) for i in profit.values() if int(i) > 0]) / len(
            [int(i) for i in profit.values() if int(i) > 0])
        result.append(profit)
        result.append({'average_profit': round(average_profit)})
    json.dump(result, f)