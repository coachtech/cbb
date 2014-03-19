import random
import time

## Number for Teams
team_1 = set()
team_2 = set()
team_3 = set()
team_4 = set()
team_5 = set()
team_6 = set()
team_7 = set()
team_8 = set()
team_9 = set()
team_10 = set()
team_11 = set()
team_12 = set()
all_teams = set()

## Get Team Names and Create a list for each team
team1 = [input('Which team finished in 1st place? '),False, team_1]
team2 = [input('Which team finished in 2nd place? '), False, team_2]
team3 = [input('Which team finished in 3rd place? '),False, team_3]
team4 = [input('Which team finished in 4th place? '),False, team_4]
team5 = [input('Which team finished in 5th place? '),False, team_5]
team6 = [input('Which team finished in 6th place? '),False, team_6]
team7 = [input('Which team finished in 7th place? '),False, team_7]
team8 = [input('Which team finished in 8th place? '),False, team_8]
team9 = [input('Which team finished in 9th place? '),False, team_9]
team10 = [input('Which team finished in 10th place? '),False, team_10]
team11 = [input('Which team finished in 11th place? '),False, team_11]
team12 = [input('Which team finished in 12th place? '),False, team_12]

allteams = [team1, team2, team3, team4, team5, team6, team7, team8,team9,team10,team11,team12]

### adding new set items to all_teams
def add_to_set(set):
    all_teams.update(set)

## populating the team with random numbers
def populate(team, balls):
    y = 0
    while y < balls:
        x = random.randint(1,78)
        if x not in all_teams:
            team.add(x)
            y += 1
        add_to_set(team)


## Populating Teams with Random Numbers
populate(team_1, 1)
populate(team_2, 2)
populate(team_3, 3)
populate(team_4, 4)
populate(team_5, 5)
populate(team_6, 6)
populate(team_7, 7)
populate(team_8, 8)
populate(team_9, 9)
populate(team_10, 10)
populate(team_11, 11)
populate(team_12, 12)


print (team_1)
print (team_2)
print (team_3)
print (team_4)
print (team_5)
print (team_6)
print (team_7)
print (team_8)
print (team_9)
print (team_10)
print (team_11)
print (team_12)

### Picking Random #s from All Teams
### 

## first pick
firstPick = random.sample(all_teams, 1)
p1 = firstPick[0]
print (p1)

if p1  in team_1:
    all_teams.difference_update(team_1)
    x =  ("The first pick goes to ", team1[0])
elif p1 in team_2:
    all_teams.difference_update(team_2)
    x=  ("The first pick goes to ", team2[0])
elif p1 in team_3:
    all_teams.difference_update(team_3)
    x=  ("The first pick goes to ", team3[0])
elif p1 in team_4:
    all_teams.difference_update(team_4)
    x=  ("The first pick goes to ", team4[0])
elif p1 in team_5:
    all_teams.difference_update(team_5)
    x=  ("The first pick goes to ", team5[0])
elif p1 in team_6:
    all_teams.difference_update(team_6)
    x=  ("The first pick goes to ", team6[0])
elif p1 in team_7:
    all_teams.difference_update(team_7)
    x=  ("The first pick goes to ", team7[0])
elif p1 in team_8:
    all_teams.difference_update(team_8)
    x=  ("The first pick goes to ", team8[0])
elif p1 in team_9:
    all_teams.difference_update(team_9)
    x=  ("The first pick goes to ", team9[0])
elif p1 in team_10:
    all_teams.difference_update(team_10)
    x=  ("The first pick goes to ", team10[0])
elif p1 in team_11:
    all_teams.difference_update(team_11)
    x=  ("The first pick goes to ", team11[0])
else:
    all_teams.difference_update(team_12)
    x =  ("The first pick goes to ", team12[0])

print (all_teams)

## second pick
secondPick = random.sample(all_teams, 1)
p2 = secondPick[0]
print (p2)

if p2  in team_1:
    all_teams.difference_update(team_1)
    y =  ("The second pick goes to ", team1[0])
elif p2 in team_2:
    all_teams.difference_update(team_2)
    y=  ("The second  pick goes to ", team2[0])
elif p2 in team_3:
    all_teams.difference_update(team_3)
    y=  ("The second pick goes to ", team3[0])
elif p2 in team_4:
    all_teams.difference_update(team_4)
    y=  ("The second pick goes to ", team4[0])
elif p2 in team_5:
    all_teams.difference_update(team_5)
    y=  ("The second pick goes to ", team5[0])
elif p2 in team_6:
    all_teams.difference_update(team_6)
    y=  ("The second pick goes to ", team6[0])
elif p2 in team_7:
    all_teams.difference_update(team_7)
    y=  ("The second pick goes to ", team7[0])
elif p2 in team_8:
    all_teams.difference_update(team_8)
    y=  ("The second pick goes to ", team8[0])
elif p2 in team_9:
    all_teams.difference_update(team_9)
    y=  ("The second pick goes to ", team9[0])
elif p2 in team_10:
    all_teams.difference_update(team_10)
    y=  ("The second pick goes to ", team10[0])
elif p2 in team_11:
    all_teams.difference_update(team_11)
    y=  ("The second pick goes to ", team11[0])
else:
    all_teams.difference_update(team_12)
    y =  ("The second pick goes to ", team12[0])

print (all_teams)


## Third pick
thirdPick = random.sample(all_teams, 1)
p3 = thirdPick[0]
print (p3)

if p3  in team_1:
    all_teams.difference_update(team_1)
    z =  ("The third pick goes to ", team1[0])
elif p3 in team_2:
    all_teams.difference_update(team_2)
    z=  ("The third  pick goes to ", team2[0])
elif p3 in team_3:
    all_teams.difference_update(team_3)
    z=  ("The third pick goes to ", team3[0])
elif p3 in team_4:
    all_teams.difference_update(team_4)
    z=  ("The third pick goes to ", team4[0])
elif p3 in team_5:
    all_teams.difference_update(team_5)
    z=  ("The third pick goes to ", team5[0])
elif p3 in team_6:
    all_teams.difference_update(team_6)
    z=  ("The third pick goes to ", team6[0])
elif p3 in team_7:
    all_teams.difference_update(team_7)
    z=  ("The third pick goes to ", team7[0])
elif p3 in team_8:
    all_teams.difference_update(team_8)
    z=  ("The third pick goes to ", team8[0])
elif p3 in team_9:
    all_teams.difference_update(team_9)
    z=  ("The third pick goes to ", team9[0])
elif p3 in team_10:
    all_teams.difference_update(team_10)
    z=  ("The third pick goes to ", team10[0])
elif p3 in team_11:
    all_teams.difference_update(team_11)
    z=  ("The third pick goes to ", team11[0])
else:
    all_teams.difference_update(team_12)
    z =  ("The third pick goes to ", team12[0])

print (all_teams)

time.sleep(2)
print (z)
time.sleep(5)
print (y)
time.sleep(10)
print (x)
