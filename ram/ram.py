print('welcome to general quiz')

player = input('do you want to play? ')

if player.lower() != "yes":
      quit()

print('ok lets play')
score=0

question = input("what is the captial of france? ")
if question.lower() == "paris":
          print('correct')
          score +=1
else:
         print('incorrect')
      
      
question = input("what is the colour of sky? ")
if question.lower() == "blue":
          print('correct')
          score +=1   
else:
         print('incorrect')
      

question = input("who won 2024 t20 world cup? ")
if question.lower() == "india":
          print('correct')
          score +=1
else:
         print('incorrect')
          
print("your score " + str(score))
