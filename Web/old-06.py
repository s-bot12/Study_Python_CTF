import base64

def stringTobase64(s) :
	return (base64.b64encode(s.encode('utf-8'))).decode('utf-8')

para = input() #id 또는 password 값

for i in range(20) :
	para = stringTobase64(para)

para = para.replace('1', '!')
para = para.replace('2', '@')
para = para.replace('3', '$')
para = para.replace('4', '^')
para = para.replace('5', '&')
para = para.replace('6', '*')
para = para.replace('7', '(')
para = para.replace('8', ')')

print(para) #최종 encode 값