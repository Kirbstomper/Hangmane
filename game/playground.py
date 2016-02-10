## Just a place to test some code and loopz

guess = ['e','l','l','a','g','p']
word = "legal"
buildin = []
brokenword = list(word)

for c in guess:
    if c in brokenword:
        print(c)
        brokenword.pop(brokenword.index(c))
        print(brokenword)
    else:
        print("Words not equal")
        break

