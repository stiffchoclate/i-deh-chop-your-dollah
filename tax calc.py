#Author: stiff_chcoclate
#dw u will remember this name
#purpose; tax collector bih

#dope thoughts, dope shit
incomes = [[],[],[]] #amount of income, type, taxes 

def sources(incomes):
    types = ["capital gains", "wages", "salary", "self-employment", "dividends", "commission, bonds", "gifts"]
    print("Please use a valid amount of currency. Please use a valid type [capital gains, wages/salary, self-employment, dividends, commission, bonds, gifts ]")
    
    origin = str(input("What type of income is this."))
    while any(origin.lower() == x for x in types) != True:
        origin = input("Invalid input. \nWhat type of income is this.")
    
    amount = float(input("How much ?"))
    while type(amount) != type(4.5):
        try:
            amount = float(input("Invalid input. \nHow much ?"))
        except:
            None
    
    incomes[0].append(amount)
    incomes[1].append(origin)
    return incomes

sources(incomes)
print(incomes)