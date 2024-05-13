from random import randint

#def uzvares_serija():
#	for k in range(5, 0, -1):
#		if k == 0:


def parbaudit_kas_uzvare():
	if datora_izvele == 1:
		print('akmens_dators')
		if lietotaja_izvele == 1:
			print('akmens_lietotajs')
			print("Neizšķirts!")
		elif lietotaja_izvele == 2:
			print('skeres_lietotajs')
			print('Uzvar dators!')
		else:
			print('papirs_lietotajs')
			print('Uzvar lietotājs!')
	elif datora_izvele == 2:
		print('skeres_dators')
		if lietotaja_izvele == 1:
			print('akmens_lietotajs')
			print("Uzvar lietotājs!")
		elif lietotaja_izvele == 2:
			print('skeres_lietotajs')
			print('Neizšķirts!')
		else:
			print('papirs_lietotajs')
			print('Uzvar dators!')
	else:
		print('papirs_dators')
		if lietotaja_izvele == 1:
			print('akmens_lietotajs')
			print("Uzvar dators!")
		elif lietotaja_izvele == 2:
			print('skeres_lietotajs')
			print('Uzvar lietotājs!')
		else:
			print('papirs_lietotajs')
			print('Neizšķirts')


while True:

	serija = [0, 0, 0, 0, 0]

	print('''
	   Šaja dator spēle jūs spēlejat ar datoru PAPĪRS-ŠĶĒRES-AKMENTIŅŠ
	   Ievadiet
	   1 - Sākt spēli
	   2 - Apskatīt labakas uzvares sērijas
	   3 - Iziet no spēles
	   ''')
	menu = int(input())

	if menu == 1:
		while True:		   
			print('''
			
			Ievadiet savu izvēli no piedāvatiem:
			1 - Akmens
			2 - Šķēres
			3 - Papīrs ''')

			datora_izvele = randint(1,3)

			while True:
				izvele = input("Jūsu izvelē: ")

				if izvele == '1':
					lietotaja_izvele = 1
					break
				elif izvele == '2':
					lietotaja_izvele = 2
					break
				elif izvele == '3':
					lietotaja_izvele = 3
					break
				else:
					print('''Kļūdā! Ievadiet jūsu izveli no piedāvatiem variantiem
					1 - Akmens
					2 - Šķēres
					3 - Papīrs ''')
					continue

			# akmens_pacelts_dators | akmens_pacelts_lietotajs
			# 1 akmens_dators | akmens_dators
			# 2 skeres_dators | skeres_lietotajs
			# 3 papirs_dators | papirs_lietotajs

			parbaudit_kas_uzvare()
					
			velreiz = input('Vēlaties uzspēlet velreiz? y/n')

			if velreiz == 'y' or 'Y':
				continue
			else:
				break
		
	elif menu == 2:
		print('tabula vēl izstrādajuma')
		# izvada masiva rezultāts
		continue
	else:
		break