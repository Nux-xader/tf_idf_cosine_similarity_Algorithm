data = ['aku', 'yang', 'bagaimana', 'seperti itu', 'begini', 'bukan', 'ada', 'data',
		'gak', 'gini', 'mana', 'siapa', 'kenapa', 'latihan', 'belajar', 'jalan', 'halo']


def lowerStrOnList(data):
	result = []
	for i in data: result.append(i.lower())
	return result

def main(data, text):
	text = text.lower()
	if text in data: return text
	dataPrematch = []
	for x in text:
		for y in data:
			if x in y and y not in dataPrematch: dataPrematch.append(y)
	data = dataPrematch
	dataPrematch = []

	for x in data:
		if text[0] == x[0:1] or text[-1] == x[-1]: dataPrematch.append(x)

	data = dataPrematch

	for i in range(len(text)*10):
		for x in text:
			for y in data:
				if x not in y: data.remove(y)

	if len(dataPrematch) > 1:
		dataPrematch = []
		for x in data:
			if text[0] == x[0]: dataPrematch.append(x)

		if len(dataPrematch) == 0:
			dataPrematch = []
			for x in data:
				if text[-1] == x[-1]: dataPrematch.append(x)

		data = dataPrematch

	if len(dataPrematch) > 1:
		dataPrematch = []
		for x in data:
			if text[-1] == x[-1]: dataPrematch.append(x)

		if len(dataPrematch) == 0:
			dataPrematch = []
			for x in data:
				if text[0] == x[0]: dataPrematch.append(x)

		data = dataPrematch

	if len(data) == 0: return False
	return data[0]



listKey = lowerStrOnList(data)
text = str(input('Input : '))
result = main(listKey, text)
if result == text:
	print('Correct')
	exit()
print('Typo detect')
print('Result :',result)