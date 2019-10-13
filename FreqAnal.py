#CMPE132 Frequency Analysis program
#Author: Sowmya Bijjala
#Find out the number of occurances of each letter, compare that with frequent english letters

freq = []
freq2 = []
order = ["E","T",'A','O','I','N','S','H','R','D','L','U','C','M','W','F','Y','G','P','V','K','X','J','Q','Z']
ciphertext = ""
ciphertext2 = ""

def calc_Freq(p,f):
	#Calculates the frequency of the letters
	from string import ascii_lowercase
	for c in ascii_lowercase:
		count = p.count(c)
		f.append((c,count))

def convert_o2(p): #deciphers o2.txt 
	p = p.replace("f","E")
	p = p.replace("i","T")
	p = p.replace("z","H")
	p = p.replace("q","A")
	p = p.replace("n","R")
	p = p.replace("x","K")
	p = p.replace("b","W")
	p = p.replace("o","M")
	p = p.replace("y","N")
	p = p.replace("v","I")
	p = p.replace("m","L")
	p = p.replace("j","S")
	p = p.replace("l","F")
	p = p.replace("a","D")
	p = p.replace("s","O")
	p = p.replace("k","P")
	p = p.replace("u","G")
	p = p.replace("e","C")
	p = p.replace("h","U")
	p = p.replace("w","B")
	p = p.replace("g","V")
	p = p.replace("r","Y")
	p = p.replace("p","X")
	p = p.replace("d","J")
	p = p.replace("t","Z")
	#2 more lines
	
	print (p)
	
def convert(p): #deciphers ciphertext.txt
	p = p.replace("n","E")
	p = p.replace("y","T")
	p = p.replace("t","H")
	p = p.replace("u","N")
	p = p.replace("m","I")
	p = p.replace("q","S")
	p = p.replace("r","G")
	p = p.replace("h","R")
	p = p.replace("v","A")
	p = p.replace("b","F")
	p = p.replace("x","O")
	p = p.replace("d","Y")
	p = p.replace("c","M")
	p = p.replace("a","C")
	p = p.replace("i","L")
	p = p.replace("z","U")
	p = p.replace("p","D")
	p = p.replace("g","B")
	p = p.replace("l","W")
	p = p.replace("e","P")
	p = p.replace("s","K")
	p = p.replace("f","V")
	p = p.replace("k","X")
	p = p.replace("j","Q")
	p = p.replace("w","M")
	p = p.replace("o","J")
	#1 more lines
	
	print (p)

def main():
	#opens encrypted text and loads it into a string, then calls calc_freq to calculate 
	#the # of occurences of a character, then displays this list sorted in decending order.
	f = open("input.txt", "r")
	if f.mode == 'r':
		ciphertext = f.read()
	calc_Freq(ciphertext,freq)
	freq.sort(key=lambda tup: tup[1], reverse=True)
	print("FREQUENCY OF o2 CIPHERTEXT:")
	print(*freq, sep = "\n")
	convert_o2(ciphertext)

	f = open("cipher.txt", "r")
	if f.mode == 'r':
		ciphertext2 = f.read()
	calc_Freq(ciphertext2,freq2)
	freq2.sort(key=lambda tup: tup[1], reverse=True)
	print("\n FREQUENCY OF CIPHERTXT CIPHERTEXT:")
	print(*freq2, sep = "\n")
	convert(ciphertext2)


if __name__ == '__main__':
	main()