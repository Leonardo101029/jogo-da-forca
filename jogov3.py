from funcoes import limpartela

palavras = []
tentativas = 0
chances = 5
letrasDigitadas = []

limpartela()

print('*'*35)
print('  Bem vindo ao jogo da forca')
print('  Você tem somente pode errar 5x')
print('*'*35)   

desafiante = input('Desafiante digite seu nome: ')
jogador = input('Jogador digite seu nome: ')
file = open("nomesJogadores.txt" ,"r")
file.write('Desafiante = {}\nJogador = {}'.format(desafiante, jogador))
file.close()

limpartela()

palavraChave = input('Digite a palavra secreta:')
dica = input('Digite uma dica: ')
limpartela()

palavraSecreta = ['*'] *len(palavraChave)

opcao = input('1 para jogar ou 2 para dica: ')

if opcao =='2':
	print(dica)

elif opcao =='1':

	while tentativas < chances:

		letra = input("\nQual letra você quer tentar? ")

	
		while letra in letrasDigitadas:
			print ("Você escolheu uma letra já usada")
			letra = input("Qual letra você deseja tentar? ")

		letrasDigitadas.append(letra)

		if letra in palavraChave:
			print ("Parabéns, você acertou a letra!")
			for l in range(len(palavraChave)):
				if letra == palavraChave[l]:
					palavraSecreta[l] = letra
		else:
			print ("você errou")
			tentativas = tentativas + 1

		print ("Você fez", tentativas, "tentativas erradas e ainda restam", chances-tentativas, "chances de acertar" )
		print (palavraSecreta)

		print ("As letras que você já tentou são:")
		for x in letrasDigitadas:
			print (x)

	if tentativas == chances:
		print ("Você perdeu")
	else:
		print ("Você ganhou, parabéns")
		print ("A palavra era", palavraChave)

