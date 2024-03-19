def calculate_score(participants):
    scoreboard=[]
    for participant in participants:
        score = participant['chickenwings']*5 + participant['hambugers'] * 3 + participant['hotdog']*2
        scoreboard.append({'name':participant["name"],"score":score})
    scoreboard.sort(key=lambda x: (-x["score"], x["name"]))
    return scoreboard


participants = [
    {'name': "Rafael Leao", 'chickenwings': 4, 'hamburgers': 7, 'hotdogs': 19},
    {'name': "Barella ", 'chickenwings': 10, 'hamburgers': 4, 'hotdogs': 11}
]

result = calculate_score(participants)
print(result)