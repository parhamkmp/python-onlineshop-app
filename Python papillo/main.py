try:
	try:
		# ----- IMPORTS -----
		import os
		from time import sleep
		os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/inf.png" "Checking modules install" "wait for Just a moment!"')
		sleep(1)
		os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/su2.png" "Imported modules is ok" "Have good time"')

	except ModuleNotFoundError:
		os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/inf.png" "Checking modules install" "wait for Just a moment!"')
		sleep(1)
		os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/err.png" "os or time module is not install" "terminal: pip3 install module-name"')

		# ----- CLASSES -----
	class OnlineShop:
			def __init__(self, name=None, lastname=None, username=None, password=None, age=None, email=None, bank_name=None, bank_card_inventory='0$'):
				# Self variables
				self.name = name
				self.lname = lastname
				self.uname = username
				self.pword = password
				self.age = age
				self.email = email
				self.usr_inf = {
					'name' : name,
					'lastname' : lastname,
					'username' : username,
					'password' : password,
					'age' : age,
					'email' : email
				}
				self.logS = False
				self.bankName = bank_name
				self.inventory = bank_card_inventory # please type just number

			# ----- FUNCTIONS -----
			def Start(self):
				try:
					self.login(input('[Enter] Username: '), input('[Enter] Password: '))
					while True:
						if self.logS == True:
							print('[ Help ]: login=1 ~ user-info=2 ~ buy-product=3 ~ logout=4 ~ clear-terminal=5 ~ exit=6')
							req_input = input('[ Enter ] your request >>> ')

							if req_input == '1':
								if self.logS == True:
									os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/inf2.png" "You logined !!!!" "Thanks you"')
								elif self.logS == False:
									self.login(input('[Enter] Username: '), input('[Enter] Password: '))


							elif req_input == '2':
								self.user_info()

							elif req_input == '3':
								self.Buy_Product()

							elif req_input == '4':
								continue_inp = input('Do you want to continue? [Y/n] ')
								if continue_inp.lower() == 'y':
									self.logS = False
									os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/bye.png" "Ok! you logouted" "have good time"')
								elif continue_inp.lower() == 'n':
									os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/cancel_logout.png" "You canceled the logout!" "Thanks you!"')


							elif req_input == '5':
								os.system('clear')
								os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/cls.png" "terminal cleared" "Have good time"')


							elif req_input == '6':
								continue_inp = input('Do you want to continue? [Y/n] ')
								if continue_inp.lower() == 'y':
									os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/bye.png" "Ok! you exited" "good bye"')
									break
								elif continue_inp.lower() == 'n':
									os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/cancel_logout.png" "You canceled the exit!" "Thanks you!"')
						

							else:
								os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/err.png" "Not defined function for this !" "have good time"')

						else:
							self.login(input('[Again] Username: '), input('[Again] Password: '))

				except KeyboardInterrupt:
					os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/err.png" "Please do not press ctrl + c" "thanks"')
					os.system('clear')
					papill.Start()


			def login(self, user_input, pass_input):
				Username = self.uname
				Password = self.pword
				if user_input == Username and pass_input == Password:
					os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/login.png" "Your login success" "welcome"')
					self.logS = True
					return True
				else:
					os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/err.png" "Your login unsuccess" "try type username and password"')
					self.logS = False
					return False



			def user_info(self):
				def print_info():
					if self.logS == True:
						os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/su1.png" "User info printed" "in editor or terminal !"')
						print('-----------------------------')
						for key, value in self.usr_inf.items():
							print(f'[ {key} : {value} ]')
						print(f'[ You Bank inventory: {self.inventory} ]')
						print(f'[ Your bank name: {self.bankName} ]')
						print('-----------------------------')

				if self.logS == False:
					self.login(input('[Enter] Username: '), input('[Enter] Password: '))
					return print_info()

				else:
					return print_info()



			def Buy_Product(self):
				def inner():
					if self.logS == True:
						product_list = {
							'2255' : {'name' : 'Patch Cord', 'model' : 'SC->SC', 'color' : 'yellow', 'price' : '100', 'code' : '2255'},
							'1122' : {'name' : 'HDMI CABLE', 'model' : '15M', 'color' : 'black-red', 'price' : '450', 'code' : '1122'},
							'3215' : {'name' : 'Terminal Kerone', 'model' : '10pair orginal', 'color' : 'white-gray', 'price' : '253', 'code' : '3215'},
							'7788' : {'name' : 'Connector', 'model' : 'CAT-7', 'color' : 'white', 'price' : '500', 'code' : '7788'},
							'1254' : {'name' : 'Module electoronic', 'model' : '8PORT', 'color' : 'white-black', 'price' : '600', 'code' : '1254'},
							'2001' : {'name' : 'Patch Cord', 'model' : 'LC->LC', 'color' : 'yellow', 'price' : '900', 'code' : '2001'},
							'3002' : {'name' : 'Patch Cord', 'model' : 'FC->FC', 'color' : 'yellow', 'price' : '900', 'code' : '3002'},
							'5001' : {'name' : 'Patch Cord', 'model' : 'FC->SC', 'color' : 'yellow', 'price' : '900', 'code' : '5001'},
							'1401' : {'name' : 'Patch Cord', 'model' : 'FC->LC', 'color' : 'yellow', 'price' : '900', 'code' : '1401'},
							'1235' : {'name' : 'Captcher', 'model' : 'TV', 'color' : 'black', 'price' : '2000', 'code' : '1235'}
						}


						print('[ Product lists ]:')
						for i in product_list:
							print(f'[ {product_list[i]["name"]}  code: {product_list[i]["code"]} ]')

						product_input = input('[ Enter ] product CODE: ')

						try:
							os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/search.png" "Searching please wait !" "Just a moment!"')
							sleep(3)
							os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/addChart.png" "Product added to chart!" "please check console or terminal"')
							num_bandCard = input(f'[ Enter ] your number bank card (Price: {product_list[product_input]["price"]}$ ): ')
							os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/inf2.png" "Checking card num!" "Just a moment!"')
							sleep(3)
							try:
								if int(num_bandCard) == type(int(num_bandCard)):
									sleep(3)
									os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/err.png" "Card number is incorrect" "please check"')
									return False
								if len(num_bandCard) > 16 or len(num_bandCard) < 16 or num_bandCard == ' ':
									sleep(3)
									os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/err.png" "Card number is incorrect" "Must be 16 digits"')
									return False
							except:
								os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/err.png" "please just type num" "please check"')
								return False

							if int(self.inventory) <= int(product_list[product_input]["price"]):
								os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/price.png" "your bank card inventory not enough" "Please check the value of the last argument of the Online Shop class in the codes"')
								os.system(f'notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/inf2.png" "your bank card inventory: {self.inventory}" "Thanks you !"')
								return False


							os.system(f'notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/su2.png" "Ok! Your Buyed product" "goodbye {self.name} {self.lname}"')
							self.inventory = int(self.inventory) - int(product_list[product_input]["price"])

							print('------------------')
							print('[ Buy info] :')
							for i in product_list[product_input]:
								print(f'[ {i} : {product_list[product_input][i]} ]')
							print(f'[ You Bank inventory: {self.inventory}$ ]')
							print(f'[ Your bank name: {self.bankName} ]')
							print('[ Currency: $ Dollars ]')
							print('------------------')


						except:
							os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/search.png" "Searching please wait !" "Just a moment!"')
							sleep(6)
							os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/err.png" "The product undifined !" "sorry ! try again"')

				if self.logS == False:
					self.login(input('[Enter] Username: '), input('[Enter] Password: '))
					return inner()

				else:
					return inner()


	papill = OnlineShop('parham', 'kmp', 'parham', '1386', 15, 'mail@domain.com', 'pasargad', '200')
	papill.Start()



except KeyboardInterrupt:
	os.system('notify-send -i "/home/parham/Documents/01-programming/projects/Python papillo/icn/err.png" "Please do not press ctrl + c" "thanks"')
	os.system('clear')
	papill.Start()
	

