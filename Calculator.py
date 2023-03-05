calculation = input("Input: ")
operations = ["+","-","/","*", "**", "^"] #add brackets later
calc = [char for char in calculation.replace(" ","")] #other way to prevent spaces?


#plan:
#number one
#operation
#number two
#put together

while calc[0] in operations:
    print("Invalid calculation. Try again.")
    calculation = input("Input: ")
    calc = [char for char in calculation.replace(" ","")]
try:
    a = int(calc[0])
except:
    try:
        a = float(calc[0])
    except:
        print("Invalid calculation. Try again.")
        calculation = input("Input: ")
        calc = [char for char in calculation.replace(" ","")]
try:
    b = int(calc[2])
except:
    try:
        b = float(calc[2])
    except:
        print("Invalid calculation. Try again.")
        calculation = input("Input: ")
        calc = [char for char in calculation.replace(" ","")]
finally:
    c = calc[1]
    ops = {"+": a + b, "-": a-b, "/": a/b, "*": a*b, "**": a**b, "^": a**b}
    total = ops[c]
    print("Answer:", total)
