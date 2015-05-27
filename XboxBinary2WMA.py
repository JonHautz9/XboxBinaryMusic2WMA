#Made for Pythoon 3.3
import base64
import binascii
import os
ID = 1
if not os.path.exists('WMA'):			#Checks if a relative WMA directory exists and makes one if not
    os.makedirs('WMA')
for (dirname, dirs, files) in os.walk('.'):
	for filename in files:
		if filename.endswith('.py'): continue
		if filename.endswith('.wma'): continue
		f=filename
		F=open(f,'rb')
		F.seek(13)
		S = 'WMA\\' + str(ID)		#I had some files with the same name (i.e track 1, track 2) this avoids overwriting them
		S = S + '_'
		int(ID)
		for x in range(0,76):		#base64.b16decode() was not converting certain characters at the time, so I had to write the conversions for them
			c = F.read(1)
			i = binascii.hexlify(c)
			if i== b'4a':		#This is one of my first python scripts, please excuse that all this could be converted into a dictionary.
				S=S+ 'J'	
				continue
			if i== b'4b':
				S=S+ 'K'
				continue
			if i== b'4c':
				S=S+ 'L'
				continue
			if i== b'4d':
				S=S+ 'M'
				continue
			if i== b'4e':
				S=S+ 'N'
				continue
			if i== b'4f':
				S=S+ 'O'
				continue
			if i== b'5a':
				S=S+'z'
				continue
			if i== b'6a':
				S=S+'j'
				continue
			if i== b'6b':
				S=S+'k'
				continue
			if i== b'6c':
				S=S+ 'l'
				continue
			if i== b'6d':
				S=S+ 'm'
				continue
			if i== b'6e':
				S=S+ 'n'
				continue	
			if i== b'6f':
				S=S+ 'o'
				continue
			if i== b'7a':
				S=S+ 'z'
				continue
			if (i>b'40'and i<b'5b') or( i>b'60' and i<b'7b'):
					S = S + str(base64.b16decode(i))[2:-1]
			if i==b'20': 
				S=S +' '
			if i== b'30':
				S=S +'0'
			if i==b'31': 
				S=S +'1'
			if i==b'32': 
				S=S +'2'
			if i==b'33': 
				S=S +'3'
			if i==b'34':
				S=S +'4'
			if i==b'35':
				S=S +'5'
			if i==b'36':
				S=S +'6'
			if i==b'37':
				S=S +'7'
			if i==b'38':
				S=S +'8'
			if i==b'39':
				S=S + '9'
		F.seek(3336)
		rest=F.read()
		Fo=open(S+'.wma','wb')
		Fo.write(rest)
		ID +=1
	
