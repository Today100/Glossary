import numexpr
equation = input()

characters = "1234567890+-*/^)."

letter = {}
count = 0

for x in equation:
    if x not in characters:
        letter[x] = ""
        if x == "(":
            if equation[count-1] not in "+-/" and count != 0:
                letter[x] = "*("
            else:
                letter[x] = "("
            # print("here")
            # print(letter)
    count += 1
        

equation.replace("(", "*(")
# print(equation)
# print("))))))")

for letters in letter.keys():
    if letters == "(":
        pass
    else:
        get = input(str(letters) + " = ")
        letter[letters] = get

for letters in letter.keys():
    equation = equation.replace(letters, letter[letters])



print(letter)
print(equation)
print(equation, "=", numexpr.evaluate(str(equation)))