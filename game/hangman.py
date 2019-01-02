import random

def hangman(list_of_words):
	random_word = random.choice(list_of_words)
	secrate_word = random_word
	available_letters = list("abcdefghijklmnopqrstuvwxyz")
	answer = ''
	replace = ("-" * len(secrate_word))
	list2 = list(replace)
	position_list = []
	message = '''You can't guess same letter again,
please guess letters from available letters list.'''
	print("Welcome to Hangman!")
	print("")
	print(replace)
	while True:
		print("")
		print("Available letters to guess")
		print(available_letters)
		try:
			guess = input("Guess your letter: ")
			if len(guess) == 1:
				position_list = []
				if guess in secrate_word:
					list1 = list(secrate_word)
					counter = 0
					while counter < len(list1):
						if list1[counter] == guess:
							if counter not in position_list:
								position_list.append(counter)
							else:
								position_list.append(counter)
						else:
							pass
						counter+=1

					for numbers in position_list:
						list2[numbers] = guess
						answer = "".join(list2)
					print(answer)

					available_letters.remove(guess)
				else:
					print("Incorrect Guess")
				if answer == secrate_word:
						print("you won the game")
						play_again = input("Do you wnat to play again(y/n): ").lower()
						if play_again == "y":
							continue
						else:
							print("Thanks for playing")
							break
			else:
				print("Please Enter one letter at time")
		except:
			print("")
			print(message)


words = ['mango','apple','london','america','lion','tigher','onion','bus','car','happy','beautiful','ugly']
hangman(words)