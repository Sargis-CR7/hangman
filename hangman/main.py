# import random

# from hangman_words import word_list
# from hangman_art import logo
# from hangman_art import stages
# print(logo)

# chosen_word=random.choice(word_list)
# worth_lenght=len(chosen_word)

# end_of_game=False
# lives=6

# while not end_of_game:
#     x=input("guess a letter")
#     if x in chosen_word:
#         print(stages[lives])
#     else:
#         lives-=1
#         print(stages[lives])



# display=[]
# for i in range(worth_lenght):
#     display+="_"     

# while not end_of_game:
#     guess=input("guess a letter:" ).lower()
#     if guess in display:
#         print(f"yove alredy guessd {guess}")
    
#     for i in range(worth_lenght):
#         letters=chosen_word[i]

#         if letters==guess:
#             display[i]=letters
    
#     if guess not in chosen_word:
#         print(f"you guessed {guess},thats not in the word.you lose a life.")

#         lives-=1
#         if lives==0:
#             end_of_game=True
#             print("you lose")
        
#         print(f"{' '.join(display)}")

#         if "_" not in display:
#             end_of_game=True
#             print("you win")

#     print(stages[lives])







