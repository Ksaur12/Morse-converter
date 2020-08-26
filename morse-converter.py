#Made by Ksaur12 www.github.com/ksaur12

print("Type exit to exit the program\n\n")
c = input('Type 1 to convert alphabets into Morse code: \nType 2 to convert Morse code into alphabets: \n')


out = ""
if c == str(1) :
	while True:
		text = input('Enter the text to be converted into Morse code: ')
		text = text.upper()
		dict1 = {
		'A' : '._ ',
		'B' : '_... ',
		'C' : '_._. ',
		'D' : '_.. ',
		'E' : '. ',
		'F' : '.._. ',
		'G' : '__. ',
		'H' : '.... ',
		'I' : '.. ',
		'J' : '.___ ',
		'K' : '_._ ',
		'L' : '._.. ',
		'M' : '__ ',
		'N' : '_. ',
		'O' : '___ ',
		'P' : '.__. ',
		'Q' : '__._ ',
		'R' : '._. ',
		'S' : '... ',
		'T' : '_ ',
		'U' : '.._ ',
		'V' : '..._ ',
		'W' : '.__ ',
		'X' : '_.._ ',
		'Y' : '_.__ ',
		'Z' : '__.. ',
		' ' : '         '
		}
		
		if text == 'EXIT':
			exit()
		for ch in text:
			out += dict1.get(ch, '!')
		print(out)
		del out
		out = ''
elif c == str(2) :
	while True:
		text = input('Enter Morse code to be converted into text: ')
		text = text.upper()
		dict2 = {
		'._' : 'A',
		'_...' : 'B' ,
		'_._.' : 'C' ,
		'_..' : 'D' ,
		'.' : 'E' ,
		'.._.' : 'F' ,
		'__.' : 'G' ,
		'....' : 'H' ,
		'..' : 'I' ,
		'.___' : 'J' ,
		'_._' : 'K' ,
		'._..' : 'L' ,
		'__' : 'M' ,
		'_.' : 'N' ,
		'___' : 'O' ,
		'.__.' : 'P' ,
		'__._' : 'Q' ,
		'._.' : 'R' ,
		'...' : 'S' ,
		'_' : 'T' ,
		'.._' : 'U' ,
		'..._' : 'V' ,
		'.__' : 'W' ,
		'_.._' : 'X' ,
		'_.__' : 'Y' ,
		'__..' : 'Z' ,
		' ' : '      '
		}
		
		if text == 'EXIT':
			exit()
		
		text = text.split(' ')
		text = list(text)
		for ch in text:
			out += dict2.get(ch, '! ')
		print(out)
		del out
		out = ''
else:
	print('Invalid')
