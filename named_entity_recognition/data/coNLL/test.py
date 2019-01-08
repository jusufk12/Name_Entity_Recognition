
path = "C:/Users/jusuf/Desktop/"
file = path+"train.txt"
with open(file) as f:
    lines = f.read().split("\n")


def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""


road = "<START:road> "
city = "<START:city> "
house_number = "<START:houseNumber> "
postal_code = "<START:postalCode> "
state_code = "<START:stateCode> "
END = " <END>"
ROADS = []
CITIES = []
HOUSE_NUMBERS = []
POSTAL_CODES = []
STATE_CODES = []

for item in lines:
    if road in item:
        a = find_between(item, road, END)
        ROADS.append(a)

    if city in item:
        b = find_between(item, city, END)
        CITIES.append(b)

    if house_number in item:
        c = find_between(item, house_number, END)
        HOUSE_NUMBERS.append(c)

    if postal_code in item:
        d = find_between(item, postal_code, END)
        POSTAL_CODES.append(d)

    if state_code in item:
        e = find_between(item, state_code, END)
        STATE_CODES.append(e)

c = []
for i in range(len(CITIES)):
    if CITIES[i] == "":
        c.append(i)
print(len(c))
c = []
for i in range(len(POSTAL_CODES)):
    if POSTAL_CODES[i] == "":
        c.append(i)
print(len(c))
c = []
for i in range(len(HOUSE_NUMBERS)):
    if HOUSE_NUMBERS[i] == "":
        c.append(i)
print(len(c))
c = []
for i in range(len(STATE_CODES)):
    if STATE_CODES[i] == "":
        c.append(i)
print(len(c))
c = []
for i in range(len(ROADS)):
    if ROADS[i] == "":
        c.append(i)
print(len(c))

text_file = open(path+"Output.txt", "w")