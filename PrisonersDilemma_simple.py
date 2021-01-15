responses = open("Responses", "r")
resp = responses.read()
rows = resp.split("\n")
items = [[]]
responders = {}


class Person:
    def __init__(self, name, time, betrayed, betrays, perceived, actual):
        self.name = name
        self.time = time
        self.betrayed = betrayed
        self.betrays = betrays
        self.perceived = perceived
        self.actual = actual


for n in range(len(rows)):
    items.append(rows[n].split("\t"))

print()
prisoners = items.pop(1)
prisoners.pop(0)

items.pop(0)

respName = ""
for i in range(len(items)):
    respName = items[i].pop(0)

    responders[respName] = Person(respName, 0, 0, 0, 0.00, 0.00)

for x in range(len(responders)):
    for y in range(len(prisoners)):
        if items[x][y] == "Silent" and items[y][x] == "Silent":
            responders[prisoners[x]].time += 1
        elif items[x][y] == "Betray" and items[y][x] == "Betray":
            responders[prisoners[x]].time += 2
            responders[prisoners[x]].betrays += 1
            responders[prisoners[x]].betrayed += 1

        elif items[x][y] == "Betray" and items[y][x] == "Silent":
            responders[prisoners[x]].time += 0
            responders[prisoners[x]].betrays += 1
        elif items[x][y] == "Silent" and items[y][x] == "Betray":
            responders[prisoners[x]].time += 3
            responders[prisoners[x]].betrayed += 1

for key in responders:
    if not responders[key].betrayed == 0:
        responders[key].perceived = round(len(responders) / responders[key].betrayed, 2)
    else:
        responders[key].perceived = len(responders)

    if not responders[key].betrays == 0:
        responders[key].actual = round(len(responders) / responders[key].betrays, 2)
    else:
        responders[key].actual = len(responders)

    print(key + ":")
    print("time: " + str(responders[key].time))
    print("betrays: " + str(responders[key].betrays))
    print("betrayed: " + str(responders[key].betrayed))
    print("perceived trustworthiness: " + str(responders[key].perceived))
    print("actual trustworthiness: " + str(responders[key].actual))
    print()
