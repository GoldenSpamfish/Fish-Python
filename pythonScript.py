script = open("pythonScriptFile.txt", "r")
code = script.read()
lines = code.split(">")

data = []
variables = {}

# removes unnecessary \n
for i in range(0, len(lines)):
    lines[i] = lines[i].strip()
lines.pop(0)


# the print function
def psPrint(data_in):
    if data_in[0] == "@":
        data_in.pop(0)
        return " ".join(data_in)

    elif data_in[0] == "&":
        print(data_in)
        return variables[data_in[1]]


def variableDef(data_in):
    # for number variables

    if data_in.pop(0) == "number":
        data_in.pop(1)
        variables[data[0]] = eval(data_in[1])
        del data_in[:2]


# splits lines into list "data"
for line in lines:
    data = line.split(" ")

    # variable definition
    if data[0] == "&":
        data.pop(0)
        variableDef(data)

    # for running functions
    elif data[0] == "$":
        data.pop(0)

        # print function
        if data.pop(0) == "print":
            print(psPrint(data))
    # for loops
    elif data[0] == "*":
        data.pop(0)

        # for repeat loops (effectively for loops)
        if data.pop(0) == "repeat":
            repeats = eval(data.pop(0))

            # repeated printing
            if data.pop(0) == "print":
                toPrint = psPrint(data)

                for i in range(repeats):
                    print(toPrint)
