drive = input('是否開過車')
if drive != '是' and drive != '否':
	print('請輸入是或否')
	raise SystemExit
age = input('請輸入年齡')
age = int(age)
if drive =='是':
	if age >=18:
		print('考過駕照')
	else:
		print('你怎麼可以開車')
elif drive =='否':
	if age >= 18:	
		print('你可以去考駕照')
	else:
		print('再等等吧')
else:
	print('請輸入是或否')
    	
