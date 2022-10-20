#vowels and consonants
string = input("enter a word to check number of vowels and consonants : ")
vowel = ""
consonants = ""
for word in string:
	if word in "AaEeIiOoUu":   #new-one
		vowel += word
	else:
		consonants += word
print("number of vowel are %d and vowels are : %s"%(len(vowel),vowel))
print("number of vowel are %d and consonants are : %s"%(len(consonants),consonants))