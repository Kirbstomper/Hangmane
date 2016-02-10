

# Create your models here.
from django.db import models
import string
# Create your views here.
class Word(models.model):
    phrase = models.charField(max_length=255)
    timesFailed = models.IntegerField()
    timesPassed = models.IntegerField()

class Hangman(Word):
    def __init__(self):
        gameWord = Word.phrase.lower()
        strikes = 0
        letterBank = string.ascii_lowercase[:26]
        usedPile = []
        workingWord = []

    def make_guess(self,guess):
        if any(guess in s for s in self.letterBank):#if the letter has not been used

            if(guess in i for i in self.gameWord):

                self.remove_letter(guess)
                self.add_letter(guess)


        else:
            print("This letter has been used")
        if self.check_equal():
            print("YOU WIN")

    #This function returns true if letters contained in the list are equal or not

    def check_equal(self):
        brokenWord = list(self.phrase)
        for c in self.workingWord:
            if c in brokenWord:
                brokenWord.pop(brokenWord.index(c))
            else:
                return False
        return True


    #Function to remove a letter from the letterlist and add it to the used pille
    def remove_letter(self, letter):
        letter = letter.lower()
        for i in self.letterBank:
            if letter == self.letterBank[i]:
                self.letterBank[i].pop
        return self.usedPile.add(letter)

    #Function to add a letter to the uncompleted word/correct letter list
    def add_letter(self, guess):
        self.workingWord.add[guess]

