i = 30
while i >= 0 and 30:
    print(i)
    i = i - 1   #eerste opdracht

print ("------------------")

m = 0
while m < 24:
    if m <= 11:
        print (str(m) + ' AM')
    if m >= 12 and m <= 24:
        print (str(m) + " PM")
    m = m + 1                   #tweede opdracht

print ("------------------")

x = 20
while x >= 20 and x <=50:
    print(x)
    x = x + 2       #derde opdracht

print ("------------------")

dag = input ("geef een dag van ma,di,wo,do,vr,za,zo op ")
if dag == "ma":
    d = 1
elif dag == "di":
    d = 2
elif dag == "wo":
    d = 3
elif dag == "do":
    d = 4
elif dag == "vr":
    d = 5
elif dag == "za":
    d = 6
elif dag == "zo":
    d = 7

while d >= 0:
    if d == 1:
        print("maandag")
    elif d == 2:
        print ("dinsdag")
    elif d == 3:
        print ("woensdag")
    elif d == 4:
        print ("donderdag")
    elif d == 5:
        print ("vrijdag")
    elif d == 6:
        print ("zaterdag")
    elif d == 7:
        print ("zondag")
    d =  d - 1

print ("--------------------")

while True:
    gok = input("raad wat voor woord ik in mijn hoofd heb ")
    if gok == "quit":
        break
    else:
        print("Dat is niet waar ik aandacht.")      #vijfde opdracht
    
print ("------------------")

teller = 50
som = 0
while som <= 1000:
    som = som + teller
    teller = teller + 1
    print (str(teller)+ " zoveel keer")