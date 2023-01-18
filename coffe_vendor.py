#IMport repl libraries

from replit import clear


#logo for the coffe vendor

logo = '''



===========================================================================
                        |                          |
   ~-_ Steamin'         |  ((     ___              | Let us not forget our
  _-~    Hot            |   ))  \___/_  Bottomless | tea-drinking sisters
c|_|    JAVA!           |  |~~| /~~~\ \ cup o'     | and brothers, of whom
                        | C|__| \___/   coffee     | I was one, long ago...
 - - - - - - - - - - -  |       `'`'`              |
                        | And, if anyone's up to   |          ((  Mmmm...
 _-~  I like coffee, I  | animating their brew...  |        .-.))
~-_   like tea...A cup, |               __         |        :|:~~|_
(| |  a cup, a cup, a   |         )) /\<_          |        ;|() |_)
 `-'  cup, a cup....    |         ((/ /  \         |     [].'|___|
                        |          __/~~~/         |
 - - - - - - - - - - -  |        ,(  \__/          | The ASCII Cafe', by
                        |        "`                | Dan Strychalski (dski@
 (   Demitasse,         |      _|  |               | cameonet.cameo.com.tw)
  )  s'il vous          |     (_|~~|               | Tools: WordPerfect 5.1
c[]  plait...           |       `--'               | WordStar 3.3, Toshiba
                        |             `'`'`        | T2000SXe. Unbeatable!
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

'''



#Dictnnory for machine

machin_dict={
	'capcity':{
		'milk':1000,
		'sugar':100,
		'water':600
		}
	}
#dictnory for coffee

coffe_dict = {
	#Three type of cofee in there
	'capachino':{
		'milk':200,
		'sugar':7,
		'water':100,
		'money':50
		},
	'cold_coffee':{
		'milk':200,
		'sugar':6,
		'water':50,
		'money':25
		},
	'filter_coffee':{
		'milk':300,
		'sugar':10,
		'water':150,
		'money':50
		}
	}


#Function for all the coffe type and its evaluvating the capacity...

def choose_coffee():
	for coffe in coffe_dict:
		print(f'\n{coffe}')
	use_choice_cofee = input('\nChoose your coffee : ').lower()
	if use_choice_cofee == 'capachino':
		return 'capachino'
	elif use_choice_cofee == 'cold_coffee':
		return 'cold_coffee'
	elif use_choice_cofee == 'filter_coffee':
		return 'filter_coffee'
	else:
		print('\nCheck the spelling....')
		exit()

#function for calculating the user_packet and the cost of the coffee

#user ahve only 300 rs.
user_packet = 300
#checking wheather user like coffe or not
#and the cofee vendor main part of coding

is_machine_start = True
while is_machine_start:
	#Asking user to would you like coffee or wouldn't
	have_coffee = input("\nWould you like to have some coffee : type yes or no  : ").lower()

	if have_coffee == 'yes' or have_coffee == 'y':
		clear()
		print(logo)
		print(f"\nThe availability of coffe vendor machine {machin_dict['capcity']} in grams and litres....\n")
		print(f"There is {user_packet} rs. in your account...")
		type_cofee = choose_coffee()
		print(f'\nYou have only {user_packet} rs.')
		if type_cofee == 'capachino':
			pay = input(f"\nYou have to pay {coffe_dict['capachino']['money']} rs. for the coffee. Is it ok or not : ").lower()
			if pay == 'ok':
				if user_packet < coffe_dict[type_cofee]['money']:
					print(f"\nInsufficient money in your account. The coffe cost is {coffe_dict[type_cofee]['money']} but you have {user_packet}")
					is_machine_start = False
					exit()
				elif machin_dict['capcity']['milk'] < coffe_dict[type_cofee]['milk'] or machin_dict['capcity']['water'] < coffe_dict[type_cofee]['water'] or machin_dict['capcity']['sugar'] < coffe_dict[type_cofee]['sugar']:
						print(f"\nThere is no more availability in the vendor machine. Machine have : {machin_dict['capcity']}\nThe choosed coffee want : {coffe_dict[type_cofee]}")
						print("\nOut of Stack")
						break
				print(f"\nEnjoy ! your {type_cofee} .....\n")
				user_packet -= coffe_dict['capachino']['money']
				for item in machin_dict['capcity']:
					machin_dict['capcity'][item] -= coffe_dict[type_cofee][item]
			else:

				clear()
				print('\nThank you for using !')
		elif type_cofee == 'cold_coffee':
			pay = input(f"\nYou have to pay {coffe_dict['cold_coffee']['money']} rs. for the coffee. Is it ok or not : ").lower()
			if pay == 'ok':
				if user_packet < coffe_dict[type_cofee]['money']:
					print(f"\nInsufficient money in your account. The coffe cost is {coffe_dict[type_cofee]['money']} but you have {user_packet}")
					is_machine_start =False
					exit()
				elif machin_dict['capcity']['milk'] < coffe_dict[type_cofee]['milk'] or machin_dict['capcity']['water'] < coffe_dict[type_cofee]['water'] or machin_dict['capcity']['sugar'] < coffe_dict[type_cofee]['sugar']:
						print(f"\nThere is no more availability in the vendor machine. Machine have : {machin_dict['capcity']}\nThe choosed coffee want : {coffe_dict[type_cofee]}")
						print("\nOut of Stack")
						break
				print(f"\nEnjoy ! your {type_cofee} .....\n")
				user_packet -= coffe_dict[type_cofee]['money']
				for item in machin_dict['capcity']:
					machin_dict['capcity'][item] -= coffe_dict[type_cofee][item]
			else:
				clear()
				print('\nThank you for using !')
		elif type_cofee == 'filter_coffee':
			pay = input(f"\nYou have to pay {coffe_dict['filter_coffee']['money']} rs. is it ok or not : ").lower()
			if pay == 'ok':
				if user_packet < coffe_dict[type_cofee]['money']:
					print(f"\nInsufficient money in your account. The coffe cost is {coffe_dict[type_cofee]['money']} but you have {user_packet}")
					is_machine_start =False
					exit()
				elif machin_dict['capcity']['milk'] < coffe_dict[type_cofee]['milk'] or machin_dict['capcity']['water'] < coffe_dict[type_cofee]['water'] or machin_dict['capcity']['sugar'] < coffe_dict[type_cofee]['sugar']:
						print(f"\nThere is no more availability in the vendor machine. Machine have : {machin_dict['capcity']}\nThe choosed coffee want : {coffe_dict[tye_cofee]}")
						print("Out of Stack")
						break
				print(f"\nEnjoy ! your {type_cofee} ....\n")
				user_packet -= coffe_dict[type_cofee]['money']
				for item in machin_dict['capcity']:
					machin_dict['capcity'][item] -= coffe_dict[type_cofee][item]
			else:
				clear()
				print('\nThank you for using!')
		print(f"\nNow you have {user_packet} rs. in your account...")
		print(f"\nThe balance availablity of the machine have {machin_dict['capcity']} in grams and litres..")
	else:
		print('\nThank you')
		break
		exit()
