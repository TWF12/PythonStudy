studs = [{'sid': '103', 'Chinese': 90, 'Math': 95, 'English': 92},
         {'sid': '101', 'Chinese': 80, 'Math': 85, 'English': 82},
         {'sid': '102', 'Chinese': 70, 'Math': 75, 'English': 72}]
scores = {}
for stud in studs:
    sid = stud['sid']
    Chinese = stud['Chinese']
    Math = stud['Math']
    English = stud['English']
    score = [Chinese, Math, English]
    scores[sid] = score
scores = dict(sorted(scores.items(), key=lambda x: x[0]))
for sid, score in scores.items():
    print(f"{sid}: {score}")

