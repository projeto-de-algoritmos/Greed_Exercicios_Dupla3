n = int(input())

prog = []
math = []
pe = []

i = 1
gifts = input().split(' ')
for gift in gifts:
    gift = int(gift)
    if gift == 1:
        prog.append(i)
    if gift == 2:
        math.append(i)
    if gift == 3:
        pe.append(i)

    n -= 1
    i += 1

lowest = min([len(prog), len(math), len(pe)])

count = 0
teams = []

while count < lowest:
    teams.append((prog[count], math[count], pe[count]))
    count += 1

print(str(count))
for team in teams:
    print(f"{team[0]} {team[1]} {team[2]}")

