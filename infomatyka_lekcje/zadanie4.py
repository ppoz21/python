class gracz:
    def __init__(self, numer):
        self.x = 0
        self.y = 0
        self.disqualified = False
        self.points = 3
        self.number = numer

    def move(self, side):
        if not self.disqualified:
            if side == "N":
                self.y -= 1
            elif side == "E":
                self.x += 1
            elif side == "S":
                self.y += 1
            elif side == "W":
                self.x -= 1
            if self.x > 19 or self.x < 0 or self.y < 0 or self.y > 19:
                self.disqualified = True
                self.points = -1

    def add_points(self, reward):
        self.points += reward

with open("./dane_2019/plansza.txt") as f:
    plansza = f.read()
with open("./dane_2019/robot.txt") as f:
    ruchy = f.read()

plansza = plansza.split("\n")

plansza_punkty = {}
y = 0
for i in plansza:
    x = 0
    j = i.split()
    for k in j:
        plansza_punkty[f"{x}, {y}"] = int(k)
        x += 1
    y += 1

ruchy = ruchy.split("\n")

gracze = []

numer = 1

for i in ruchy:
    curr_player = gracz(numer)
    gracze.append(curr_player)
    for j in i:
        curr_player.move(j)
        if curr_player.disqualified:
            break
        curr_player.add_points(plansza_punkty[f"{curr_player.x}, {curr_player.y}"])
    numer += 1

zdyskwalifikowani = len([x for x in gracze if x.disqualified])
max_points = max([x.points for x in gracze])
max_points_player_number = [x.number for x in gracze if x.points == max_points][0]

zad_4_3 = []
ruchy_w_jednym_wierszu = 0
max_ruchy_w_jednym_wierszu = 0
number = 1
for i in ruchy:
    for j in i:
        if j in ['W', 'E']:
            ruchy_w_jednym_wierszu += 1
        else:
            ruchy_w_jednym_wierszu = 0
        if ruchy_w_jednym_wierszu > max_ruchy_w_jednym_wierszu:
            max_ruchy_w_jednym_wierszu = ruchy_w_jednym_wierszu
    zad_4_3.append([number, max_ruchy_w_jednym_wierszu])
    max_ruchy_w_jednym_wierszu = 0
    ruchy_w_jednym_wierszu = 0
    number += 1

max_ruchy = max([x[1] for x in zad_4_3])
numery = [x[0] for x in zad_4_3 if x[1] == max_ruchy]
print("Zad 4.1", zdyskwalifikowani)
print("Zad 4.2", max_points_player_number, max_points)
print("Zad 4.3", numery, max_ruchy)

