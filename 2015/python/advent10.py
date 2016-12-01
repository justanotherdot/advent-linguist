test_input = '3113322113'

def look_and_say(val):
	val = str(val)
	curr_c = list(val)[0]
	curr_cnt = 0
	string = ''
	for c in list(val):
		if curr_c != c:
			string += str(curr_cnt) + curr_c
			curr_cnt = 1
			curr_c = c
		else:
			curr_cnt += 1
	string += str(curr_cnt) + curr_c
	return string

res = look_and_say(test_input)
for i in xrange(0,39):
	res = look_and_say(res)

print len(res)
