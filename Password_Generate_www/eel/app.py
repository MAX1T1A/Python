import eel
import random


eel.init("web")

all_symbol = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!№;%:?*())_+/'



@eel.expose
def password_(length, name):
	if (length == 0) and (name == ''):
		print('FILL IN THE FIELDS')
	else:
		password = "".join(random.sample(all_symbol, length))
		print(password)


		password_file = open ('password.txt', 'a+')
		return password_file.write(f'[ {password} ] <===> [ {name} ]\n')


eel.start("index.html", size = (500, 500))
