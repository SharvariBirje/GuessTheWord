#api from API Ninjas
import requests

points=0
ch=1
name=input("Enter your name:")
print("Hey,",name,"! Are you ready to dive into the adventure? Let the game begin!")
print("")
while(ch):
    api_url = 'https://api.api-ninjas.com/v1/randomword?length=5'
    response = requests.get(api_url, headers={'X-Api-Key': 'zhqeIN9QuS4XLbiP6IVzUw==j7oPe1CwcleTIhWJ'})
    if response.status_code == requests.codes.ok:
        randomword=response.json()
        word=randomword["word"].lower()
        while len(word) != 5:
            api_url = 'https://api.api-ninjas.com/v1/randomword?length=5'
            response = requests.get(api_url, headers={'X-Api-Key': 'zhqeIN9QuS4XLbiP6IVzUw==j7oPe1CwcleTIhWJ'})
            if response.status_code == requests.codes.ok:
                randomword=response.json()
                word=randomword["word"].lower()
    else:
        print("Error:", response.status_code, response.text)
    print("Guess the word below")
    length=len(word)
    for i in range(length):
        if(i==0 or i==length-1 or i==length//2):
            print(word[i],end=" ")
        else:
            print("_",end=" ")
    print("")
    counter=5
    while(counter>0):
        ans=input("Enter Your Answer: ").lower()
        if(len(ans) > len(word) or not ans.isalpha()):
            print("Invalid input. Please enter only alphabetic characters and a maximum of 5 words.")
            continue
        if(ans==word):
            print("Hurrayyyy! You Guessed It Right")
            print("")
            points+=1
            break
        else:
            print("Oops. You have",counter-1,"chances left")
            counter-=1
    if(counter==0):
        print("")
        print("Don't be Sad. Better Luck Next Time")
        print("The correct answer was:",word)
        print("")
    s=input("Do you wish to continue the game? y/n: ")
    print("")
    if(s=='n'):
        ch=0
        
print("Your Score is:",points)