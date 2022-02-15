intro=input("Enter your introducution: ")
print(intro)
charecterCount=0
wordCount=1
for i in intro: 
    charecterCount=charecterCount+1
    if i == ' ':
        wordCount=wordCount+1

print(wordCount)
print(charecterCount)