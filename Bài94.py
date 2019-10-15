a = 'quantrimang'
dic = {}
for x in a:
	dic[x] = ""
print(dic)
for k,v in dic.items():
	numb = 0
	for i in a:
		if k == i:
			numb+=1
	dic[k] = str(numb)
print(dic)
