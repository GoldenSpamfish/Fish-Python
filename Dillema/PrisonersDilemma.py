responses = open("Responses", "r")
resp = responses.read()
rows = resp.split("\n")
items = [[]]
responders = {}
for n in range(len(rows)):
    items.append(rows[n].split("\t"))

for i in items:
    print(i)

print()
prisoners = items.pop(1)
prisoners.pop(0)

items.pop(0)

respName = ""
forReduct = []
for i in range(len(items)):
    respName = items[i].pop(0)
    responders[respName] = 0
    forReduct.append(respName)

for i in prisoners:
    if i not in forReduct:
        for n in range(len(items)):
            items[n].pop(prisoners.index(i))
        prisoners.remove(i)

print("Prisoners:")
print(prisoners)
print()

print("Responders:")
print(responders)
print()

for i in items:
    print(i)

for responder in responders:
    for prisoner in prisoners:

        if (items[forReduct.index(responder)][prisoners.index(prisoner)] == "Silent") and \
                (items[prisoners.index(prisoner)][forReduct.index(responder)] == "Silent"):
            responders[responder] += 1
        elif (items[forReduct.index(responder)][prisoners.index(prisoner)] == "Silent") and \
                (items[prisoners.index(prisoner)][forReduct.index(responder)] == "Betray"):
            responders[responder] += 3
        elif (items[forReduct.index(responder)][prisoners.index(prisoner)] == "Betray") and \
                (items[prisoners.index(prisoner)][forReduct.index(responder)] == "Silent"):
            responders[responder] += 0
        elif (items[forReduct.index(responder)][prisoners.index(prisoner)] == "Betray") and \
                (items[prisoners.index(prisoner)][forReduct.index(responder)] == "Betray"):
            responders[responder] += 2

for key in responders:
    print(key + ": " + str(responders[key]))
