from fileinput import input

parens = input('advent01.in')[0]

floor = 0
for paren in parens:
	if paren == '(':
		floor += 1
	if paren == ')':
		floor -= 1

print(floor)
