#Author: stiff_chcoclate
#dw u will remember this name
#purpose; tax collector bih

#dope thoughts, dope shit
incomes = [[],[],[]] #amount of income, type, taxes 

def sources(incomes):
    types = ["capital gains", "wages", "salary", "dividends", "bonds", "gifts"]
    print("Please use a valid amount of currency. Please use a valid type [capital gains, wages/salary, dividends, bonds, gifts ]")
    
    origin = str(input("What type of income is this."))
    while any(origin.lower() == x for x in types) != True:
        origin = input("Invalid input. \nWhat type of income is this.   ")
    
    amount = None
    while type(amount) != type(4.5):
        try:
            amount = float(input("How much ?   "))
        except:
            print("Invalid input.")#data validation
     
    incomes[0].append(amount)
    incomes[1].append(origin)
    cont = None

    while cont != "yes" and cont != "no":
        cont = (input("Woudl u like to add another source? Yes or No \n")).lower()
    if cont == "no":
        return calcs(incomes)
    return sources(incomes)#then calculate the taxes for the user

#types = ["capital gains", "wages", "salary", "dividends", "bonds", "gifts"]

def calcs(incomes):#finished
    print(incomes)
    for n in range(0,len(incomes[0])):
        if incomes[1][n] == "salary" or incomes[1][n] == "wages":
            incomes[2].append(regular(incomes[0][n]))
        elif incomes[1][n] == "gifts":
            incomes[2].append(0)
        elif incomes[1][n] == "capital gains":
            incomes[2].append(incomes[0][n])
        elif incomes[1][n] == "bonds":
            incomes[2].append(0.2*(incomes[0][n]))
        elif incomes[1][n] == "dividends":
            incomes[2].append(dividends(incomes[0][n]))
    return show(incomes)

def show(incomes):#unfin
    for a in range(0,len(incomes[0])):
        incomes[0][a] = round(incomes[0][a], 3)#round to 2dp or 3dp to represent pennies
    for a in range(0,len(incomes[2])):
        incomes[0][a] = round(incomes[0][a], 2)
    
    print(incomes)

    
        

    print(incomes[0], incomes[1], incomes[2])

def regular(k):
    if k>125140:
        t = 0.2*(502700-12570) + 0.4*(125140-50271) + 0.45*(k-125140)
    if k>50270:
        t = 0.2*(502700-12570) + 0.4*(k-50271)
    elif k>12570:
        t =  0.2*(k-12570)
    else:
        t = 0
    return t
def gains(k):
    homes = input("How much came from homes")
    while type(homes) != type(4.5):
        try:
            homes = float(homes)
        except:
            homes = input("Error occured. Enter a number. no symbols")
    t = 0.2*(k-homes) + 0.28*(homes)
    return t
def dividends(k):
    if k>1000:
        t = 0.0875*(k)
    else:
        t = 0
    return t


    
sources(incomes)
