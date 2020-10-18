# This is just a caesar cipher that shifts digits two to the right
# We must shift it two to the left
# Only include alphabet characters

'''
Pseudocode

1. check if the char is alphabetical
2. append or modify current string w/ the new value minus 2
3. print the final output string 
4. replace url http://www.pythonchallenge.com/pc/def/map.html with http://www.pythonchallenge.com/pc/def/string.html
5. or see the result of the printed string

'''

encodedText = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq \
                glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
decodedText = ''
for i in range(len(encodedText)):
    if encodedText[i].isalpha():
        if encodedText[i] == 'y':
            decodedText += 'a'
        elif encodedText[i] == 'z':
            decodedText += 'b'
        else:
            decodedText += chr( ord(encodedText[i]) + 2 )
    else:
        decodedText += encodedText[i]

print(decodedText)

# After working on this, string.makestrans would've worked.
# using this algo on map would make it ocr
print("http://www.pythonchallenge.com/pc/def/ocr.html")

# Now you can go to http://pythonchallenge.com/pcc/def/ocr.html to view solution to level 1 on the wiki