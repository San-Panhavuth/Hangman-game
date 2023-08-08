import random
words = ['table','elephant','apple']
clue = ['an object we can put things on', 'a big animal with trunks and fluffy ears','a fruit commonly eaten']
wordselection = random.randint(0,2)
clueselection = wordselection
worduse=wordselection
clueuse = clueselection
storeword=""
for i in words[worduse]:
    if i not in storeword:
        storeword += i
x=len(storeword)
z=3
k=-1
wordexists = ''
while k == -1:
    print('clue: ',clue[clueselection])
    getwords = str(input("enter the a letter you think exist in the word here: "))
    if getwords in storeword:
        x-=1
        print('you have guess right.',x, ' more letters to go.')
        if getwords not in wordexists:
            wordexists += getwords
        print('so far the letters exists are: ', wordexists)
    if getwords not in storeword:
        z-=1
        print('it is not in the list you have ',z," guesses remaining")
    if x == 0:
        print('the word is', words[worduse])
        k=1
    if z == 0:
        k=1