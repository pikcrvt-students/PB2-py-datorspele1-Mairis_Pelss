from random import randint

while True:		   
	print('''
	Šaja dator spēle jūs spēlejat ar datoru AKMENS-ŠĶĒRES-AKMENTIŅŠ
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
		print('papirs_dators)
		if lietotaja_izvele == 1:
			print('akmens_lietotajs')
			print("Uzvar dators!")
		elif lietotaja_izvele == 2:
			print('skeres_lietotajs')
			print('Uzvar lietotājs!')
		else:
			print('papirs_lietotajs')
			print('Neizšķirts')
			
	velreiz = input('Vēlaties uzspēlet velreiz? y/n')
	if velreiz == 'y' or 'Y':
		continue
	else:
		break