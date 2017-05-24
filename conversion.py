# 0C = 32F and 1C = 33.8F
def convert(celsius):
	farhenheit = []
	for i in range(len(celsius)):
		if(celsius[i]!=0):
			val = (float(celsius[i])*1.8+32)
			farhenheit.append(val)
		elif(celsius[i]==0): farhenheit.append(32)
	return farhenheit

celsius = ['48','35','28','22', '32', '30', '25']
result = convert(celsius)
print(result)
