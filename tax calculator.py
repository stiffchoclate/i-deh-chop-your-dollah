# a tax calculators
#uses map and iterable to calcuklate the taxes neessary in the uk
#enter income tax, and donation etc
#xtensions; figure out how to add in tax breaks

#plan
    #1. calculate tax
"""take income and income type(pre-conditions). store in a 2d array (do recursively until no more sources required.)
make it robust (e.g. use while loop to get correct data types(this is data validation)). 
use map function to apply the correct tax bracket to each income source and return tax tb paid. add deductions at the end. 
store all of this is another array that relates. could this be done ++ efficiently using a relational DB.
at the end display to  the user all the income sources and their according taxes;

 """
    #2. incl tax write offs

"""execution: first imma write the tax function. 
second, the func for taking input.
third, the functional part; acc mapping each income source to the necessary tax functions e.g  def tax(income, source)"""

#assume inputs are valid rn
def tax(income, source):
    valid = False
    if source == "capital gains":
        while valid != True:
            try:
                real_estate = float(input("How much of it is from residential: £"))
            except:
                print("Error: Data Type invlaid")
                tax(income, source) #when this line is changed to return tax(...), it no longer returns an exception
            valid = True
            sub_tax = 0.2*(income-real_estate) - 0.28*real_estate
        print(sub_tax)#need to round numbers afterwards

    elif source == "salary" or source == "income":
        print("")
    elif source == "shares" or source == "dividends":
        print("")
    else:
        print("")
    print(real_estate)

    
tax(124123, "capital gains")