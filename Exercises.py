class Exercise:
	def __init__(self):
		self

	def Namaewa(self):
		print('Hello YOu')
		self.n = input('Namaewa?: ')
		print('Nice',self.n)

	def convertToCelsius(degreesFahrenheit):
		Celsius = (degreesFahrenheit - 32) * (5 / 9)
		return Celsius

	def convertToFahrenheit(degreesCelcius):
		Fahrenheit = degreesCelcius * (9 / 5) + 32
		return Fahrenheit

	assert convertToCelsius(0) == -17.77777777777778
	assert convertToCelsius(180) == 82.22222222222223
	assert convertToFahrenheit(0) == 32
	assert convertToFahrenheit(100) == 212
	assert convertToCelsius(convertToFahrenheit(15)) == 15

	def isOdd(number):
		odd = number % 2 == 1
		return odd

	def isEven(number):
		even = number % 2 == 0
		return even

	assert isOdd(42) == False
	assert isOdd(9999) == True
	assert isOdd(-10) == False
	assert isOdd(-11) == True
	assert isOdd(3.1415) == False
	assert isEven(42) == True
	assert isEven(9999) == False
	assert isEven(-10) == True
	assert isEven(-11) == False
	assert isEven(3.1415) == False

	def area(L, W):
		area = L * W
		return area

	def perimeter(L, W):
		perimeter = L + W + L + W
		return perimeter

	def volume(L, W, H):
		volume = L * W * H
		return volume

	def surfaceArea(L, W, H):
		surfacearea = (L * W * 2) + (L * H * 2) + (W * H * 2)
		return surfacearea
		
	assert area(10, 10) == 100
	assert area(0, 9999) == 0
	assert area(5, 8) == 40
	assert perimeter(10, 10) == 40
	assert perimeter(0, 9999) == 19998
	assert perimeter(5, 8) == 26
	assert volume(10, 10, 10) == 1000
	assert volume(9999, 0, 9999) == 0
	assert volume(5, 8, 10) == 400
	assert surfaceArea(10, 10, 10) == 600
	assert surfaceArea(9999, 0, 9999) == 199960002
	assert surfaceArea(5, 8, 10) == 340

	def fizzBuzz(upto):
		for i in range(1, upto):
			if i % 3 == 0 and i % 5 ==0:
				print ("FizzBuzz")
			elif i % 3 == 0:
				print ("Fizz")
			elif i % 5 == 0:
				print("Buzz")
			else:
				if i % 3 != 0 and i % 5 != 0:
					print(i)

	def ordinalSuffix(number):
		numberStr = str(number)

		if numberStr[-2:] in ('11','12','13'):
			return numberStr + 'th'

		if numberStr[-1:] == '1':
			return numberStr + 'st'

		if numberStr[-1:] == '2':
			return numberStr + 'nd'

		if numberStr[-1:] ==  '3':
			return numberStr + 'rd'

		else:
			return numberStr + 'th'

	assert ordinalSuffix(0) == '0th'
	assert ordinalSuffix(1) == '1st'
	assert ordinalSuffix(2) == '2nd'
	assert ordinalSuffix(3) == '3rd'
	assert ordinalSuffix(4) == '4th'
	assert ordinalSuffix(10) == '10th'
	assert ordinalSuffix(11) == '11th'
	assert ordinalSuffix(12) == '12th'
	assert ordinalSuffix(13) == '13th'
	assert ordinalSuffix(14) == '14th'
	assert ordinalSuffix(101) == '101st'
		
	def printASCIITable():
		for i in range(32,126):
				print(i,chr(i))

	# printASCIITable()

	def writeToFile(file, text):
		with open (file ,'w+') as file:
			file.seek(0)
			file.write(str(text)+"\n")
	def appendToFile(file, text):
		with open (file ,'a+') as file:
			file.seek(0)
			file.write(str(text)+"\n")
	def readFromFile(file):
		with open (file , 'r+') as file:
			# file.seek(0)
			return file.read()

	writeToFile('geek.txt', 'wazzaap')
	appendToFile('geek.txt', 'beyyeee')
	assert readFromFile('geek.txt') == "wazzaap\nbeyyeee\n"

	def getChessSquareColor(column, row):

		if column <= 0 or column > 8 or  row < 1 or row > 8:
			return ''

		if column % 2 == row % 2:
			return 'white'
		else:
			return'black'

	assert getChessSquareColor(1, 1) == 'white'
	assert getChessSquareColor(2, 1) == 'black'
	assert getChessSquareColor(1, 2) == 'black'
	assert getChessSquareColor(8, 8) == 'white'
	assert getChessSquareColor(0, 8) == ''
	assert getChessSquareColor(2, 9) == ''

	def findAndReplace(text, oldText, newText):
		# text = "MY DOG JONESY"
		replacedText = ''
		i = 0
		while i < len(text):
			if text[i:i + len(oldText)] == oldText:
				replacedText += newText
				i += len(oldText)
			else:
				replacedText += text[i]
				i += 1
		return replacedText

	assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'
	assert findAndReplace('fox', 'fox', 'dog') == 'dog'
	assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'
	assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'
	assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'

	def getHoursMinutesSeconds(totalSeconds):
		if totalSeconds == 0:
			return '0s'

		hours = 0
		while totalSeconds >= 3600:
			hours += 1
			totalSeconds -= 3600

		day = 0
		while totalSeconds >= 86400:
			day +=1
			totalSeconds -=86400

		minutes = 0 
		while totalSeconds >= 60:
			minutes +=1
			totalSeconds -= 60

		seconds = totalSeconds

		dhms = []
		if day > 0:
			dhms.append(str(day) + 'd')

		if hours > 0:
			dhms.append(str(hours) + 'h') 

		if minutes > 0 :
			dhms.append(str(minutes) + 'm')

		if seconds > 0 :
			dhms.append(str(seconds) + 's')

		return ' '.join(dhms)

	assert getHoursMinutesSeconds(30) == '30s'
	assert getHoursMinutesSeconds(60) == '1m'
	assert getHoursMinutesSeconds(90) == '1m 30s'
	assert getHoursMinutesSeconds(3600) == '1h'
	assert getHoursMinutesSeconds(3601) == '1h 1s'
	assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
	assert getHoursMinutesSeconds(90042) == '25h 42s'
	assert getHoursMinutesSeconds(0) == '0s'

	def getSmallest(numbers):
		if len(numbers) == 0:
			return None
		smallest = numbers[0]
		for number in numbers :
			if number < smallest:
				smallest = number
		return smallest

	assert getSmallest([1, 2, 3]) == 1
	assert getSmallest([3, 2, 1]) == 1
	assert getSmallest([28, 25, 42, 2, 28]) == 2
	assert getSmallest([1]) == 1
	assert getSmallest([]) == None

	def calculateSum(numbers):
		result = 0
		for number in numbers:
			result += number
		return result

	def calculateProduct(numbers):
		result = 1
		for number in numbers:
			result *= number
		return result
	
	assert calculateSum([]) == 0
	assert calculateSum([2, 4, 6, 8, 10]) == 30
	assert calculateProduct([]) == 1
	assert calculateProduct([2, 4, 6, 8, 10]) == 3840

	def average(numbers):
		if len(numbers) == 0:
			return None
		total = 0
		for number in numbers:
			total += number
		return total / len(numbers)

	assert average([1, 2, 3]) == 2
	assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
	assert average([12, 20, 37]) == 23
	assert average([0, 0, 0, 0, 0]) == 0
	import random
	random.seed(42)
	testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]
	for i in range(1000):
		random.shuffle(testData)
		assert average(testData) == 2

	def median(numbers):
		if len(numbers) == 0:
			return None
		numbers.sort()
		middleIndex = len(numbers) // 2
		if len(numbers) % 2 == 0:
			return (numbers[middleIndex] + numbers[middleIndex - 1]) / 2
		else:
			return numbers[middleIndex]

	assert median([]) == None
	assert median([1, 2, 3]) == 2
	assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
	assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6
	import random
	random.seed(42)
	testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
	for i in range(1000):
		random.shuffle(testData)
		assert median(testData) == 6

	def mode(numbers):
		if len(numbers) == 0:
			return None
		numberCount = {}
		mostFreqNumber = None
		mostFreqNumberCount = 0

		for number in numbers:
			if number not in numberCount:
				numberCount[number] = 0
			numberCount[number] += 1
			if numberCount[number] > mostFreqNumberCount:
				mostFreqNumber = number
				mostFreqNumberCount = numberCount[number]
		return mostFreqNumber

	assert mode([]) == None
	assert mode([1, 2, 3, 4, 4]) == 4
	assert mode([1, 1, 2, 3, 4]) == 1


	def rollDice(numberOfDice):
		import random
		total = 0
		for i in range(numberOfDice):
			total += random.randint(1,6)
		return total

	assert rollDice(0) == 0
	assert rollDice(1000) != rollDice(1000)
	for i in range(1000):
		assert 1 <= rollDice(1) <= 6
		assert 2 <= rollDice(2) <= 12
		assert 3 <= rollDice(3) <= 18
		assert 100 <= rollDice(100) <= 600

	def getCostOfCoffee(numberOfCoffee, pricePerCoffee):
		totalPrice = 0
		cupsUntilFreeCoffee = 8

		while numberOfCoffee > 0:
			numberOfCoffee -= 1

			if cupsUntilFreeCoffee == 0:
				cupsUntilFreeCoffee = 8
			else:
				totalPrice += pricePerCoffee
				cupsUntilFreeCoffee -= 1
		return totalPrice

	assert getCostOfCoffee(7, 2.50) == 17.50
	assert getCostOfCoffee(8, 2.50) == 20
	assert getCostOfCoffee(9, 2.50) == 20
	assert getCostOfCoffee(10, 2.50) == 22.50
	for i in range(1, 4):
		assert getCostOfCoffee(0, i) == 0
		assert getCostOfCoffee(8, i) == 8 * i
		assert getCostOfCoffee(9, i) == 8 * i
		assert getCostOfCoffee(18, i) == 16 * i
		assert getCostOfCoffee(19, i) == 17 * i
		assert getCostOfCoffee(30, i) == 27 * i

	def generatePassword(length):
		import random

		LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
		UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		NUMBERS = '1234567890'
		SPECIAL = '~!@#$%^&*()_+'
		ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL
		if length < 12:
			length = 12
		password = []
		password.append(LOWER_LETTERS[random.randint(0, 25)])
		password.append(UPPER_LETTERS[random.randint(0, 25)])
		password.append(NUMBERS[random.randint(0, 9)])
		password.append(SPECIAL[random.randint(0, 12)])

		while len(password) < length:
			password.append(ALL_CHARS[random.randint(0, 74)])
		random.shuffle(password)
		return "".join(password)
	# pw = generatePassword(13)
	# print(pw)

	def isLeapYear(year):
		if year % 400 == 0:
			return True
		elif year % 100 == 0:
			return False
		elif year % 4 == 0:
			return True
		else:
			return False
	assert isLeapYear(1999) == False
	assert isLeapYear(2000) == True
	assert isLeapYear(2001) == False
	assert isLeapYear(2004) == True
	assert isLeapYear(2100) == False
	assert isLeapYear(2400) == True

	def isValidDate(year, month, day):
		import datetime
		def isLeapYear(year):
			if year % 400 == 0:
				return True
			elif year % 100 == 0:
				return False
			elif year % 4 == 0:
				return True
			else:
				return False
		# leapyear = isLeapYear(year)
		if not(1 <= month <= 12):
			return False

		if isLeapYear(year) and month == 2 and day == 29:
			return True

		if month in (1 ,3 ,5 ,7 ,8 ,10 ,12) and not (1 <= day <= 31):
			return False

		elif month in (4 ,6 ,9 ,11) and not (1 <= day <= 30):
			return False

		elif month == 2 and not (1 <= day <= 28):
			return False

		return True

	assert isValidDate(1999, 12, 31) == True
	assert isValidDate(2000, 2, 29) == True
	assert isValidDate(2001, 2, 29) == False
	assert isValidDate(2029, 13, 1) == False
	assert isValidDate(1000000, 1, 1) == True
	assert isValidDate(2015, 4, 31) == False
	assert isValidDate(1970, 5, 99) == False
	assert isValidDate(1981, 0, 3) == False
	assert isValidDate(1666, 4, 0) == False

	def rpsWinner(move1, move2):
		if move1 == 'rock' and move2 == 'paper':
			return "player two"
		elif move1 == 'rock' and move2 == 'scissors':
			return "player one"
		elif move1 == 'paper' and move2 == 'scissors':
			return "player two"
		elif move1 == 'paper' and move2 == 'rock':
			return "player one"
		elif move1 == 'scissors' and move2 == 'rock':
			return "player two"
		elif move1 == 'scissors' and move2 == 'paper':
			return "player one" 
		else:
			return "tie"
	assert rpsWinner('rock', 'paper') == 'player two'
	assert rpsWinner('rock', 'scissors') == 'player one'
	assert rpsWinner('paper', 'scissors') == 'player two'
	assert rpsWinner('paper', 'rock') == 'player one'
	assert rpsWinner('scissors', 'rock') == 'player two'
	assert rpsWinner('scissors', 'paper') == 'player one'
	assert rpsWinner('rock', 'rock') == 'tie'
	assert rpsWinner('paper', 'paper') == 'tie'
	assert rpsWinner('scissors', 'scissors') == 'tie'

	def BottlesOfBeer():
		for numberOfBottles in range(99 ,1 ,-1):
			print(numberOfBottles, 'Bottles Of Beer on the wall,')
			print(numberOfBottles, 'Bottles of Beer,')
			print('Take one down,')
			print('Pass it around,')

			if (numberOfBottles - 1) == 1:
				print('1 bottle of beer on the wall,')
			else:
				print(numberOfBottles - 1, 'Bottles of Beer on the wall,')
		print('1 bottle of beer on the wall,')
		print('1 bottle of beer,')
		print('Take one down,')
		print('Pass it around,')
		print('No more Bottles of beer on the wall!')
	# BottlesOfBeer()

	def Every15Minutes():
		for meridiem in ['am', 'pm']:

			for hour in ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:

				for minutes in ['00', '15', '30', '45']:

					print(hour + ':' + minutes + ' ' + meridiem)
	# Every15Minutes()

	def multiplication():
		print('  |  1   2   3   4   5   6   7   8   9  10')
		print('--+----------------------------------------')

		for column in range(1, 11):
			print(str(column).rjust(2) + '|', end=' ')
			for row in range(1, 11):
				print(str(column * row).rjust(2) + ' ', end=' ')
			print()

	# multiplication()

	def printHandshakes(people):
		handshakes = 0

		for i in range(0, len(people) -1):
			for j in range(i + 1, len(people)):
				print(people[i], "hand shakes with", people[j])
				handshakes +=1
		return handshakes

	# assert printHandshakes(['Alice', 'Bob']) == 1
	# assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
	# assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6

	def drawRectangle(width, height):
		if width < 1 or height < 1:
			return False

		for row in range(height):
			for column in range(width):
				print('#', end='')
			print()
	# drawRectangle(12, 6)

	def drawBorder(width, height):
		if width < 2 or height < 2:
			return False

		print('+' + ('-' * (width - 2)) + '+')
		for i in range(height - 2):
			print('-' + ('-' * (width - 2)) + '-')

		print('+' + ('-' * (width - 2)) + '+')

	# drawBorder(16, 6)

	def drawPyramid(height):

		for row in range(0, height):
			leftsides = ' ' * (height - (row + 1 ))
			pyramidrow = '#'*(row * 2 + 1)
			print(leftsides + pyramidrow)

	# drawPyramid(3)

	def drawBox(size):
		if size < 1:
			return False

		print(' ' * (size + 1) + '+' + '-' * (size * 2) + '+')

		for i in range(size):
			print(' ' * (size - i) + '/' + ' ' * (size * 2) + '/' + ' ' * i + '|')

		print('+' + '-' * (size * 2) + '+' + ' ' * size + '+')

		for i in range(size - 1, -1, -1):
			print('|' + ' ' * (size * 2) + '|' + ' ' * i + '/')

		print('+' + '-' * (size * 2) + '+')

	# for i in range(1, 6):
	# 	drawBox(i)

	def convertIntToStr(integerNum):
		if integerNum == 0:
			return '0'

		DIGITS_INT_TO_STR = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
		if integerNum < 0:
			isNegative = True
			integerNum = -integerNum
		else:
			isNegative = False
		stringNum = ''
		while integerNum > 0:
			onesPlaceDigit = integerNum % 10
			stringNum = DIGITS_INT_TO_STR[onesPlaceDigit] + stringNum
			integerNum //= 10
		if isNegative:
			return '-' + stringNum
		else:
			return stringNum

	for i in range(-10000, 10000):
		assert convertIntToStr(i) == str(i)
	
	def convertStrToInt(stringNum):
		
		DIGITS_STR_TO_INT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

		if stringNum[0] == '-':
			isNegative = True
			stringNum = stringNum[1:]
		else:
			isNegative = False
		integerNum = 0
		for i in range(len(stringNum)):
			digit = DIGITS_STR_TO_INT[stringNum[i]]
			integerNum = (integerNum * 10) + digit
		if isNegative:
			return -integerNum
		else:
			return integerNum

	for i in range(-10000, 10000):
		assert convertStrToInt(str(i)) == i

	def commaFormat(number):
		number = str(number)
		if '.' in number:
			fractionalPart = number[number.index('.'):]
			number = number[:number.index('.')]
		else:
			fractionalPart = ''
		# Create a variable to hold triplets of digits and the
		# comma-formatted string as it is built:
		triplet = ''
		commaNumber = ''
		# Loop over the digits starting on the right side and going left:
		for i in range(len(number) - 1, -1, -1):
		# Add the digits to the triplet variable:
			triplet = number[i] + triplet
		# When the triplet variable has three digits, add it with a
		# comma to the comma-formatted string:
			if len(triplet) == 3:
				commaNumber = triplet + ',' + commaNumber
			# Reset the triplet variable back to a blank string:
				triplet = ''
		# If the triplet has any digits left over, add it with a comma
		# to the comma-formatted string:
		if triplet != '':
			commaNumber = triplet + ',' + commaNumber
		# Return the comma-formatted string:
		return commaNumber[:-1] + fractionalPart

	assert commaFormat(1) == '1'
	assert commaFormat(10) == '10'
	assert commaFormat(100) == '100'
	assert commaFormat(1000) == '1,000'
	assert commaFormat(10000) == '10,000'
	assert commaFormat(100000) == '100,000'
	assert commaFormat(1000000) == '1,000,000'
	assert commaFormat(1234567890) == '1,234,567,890'
	assert commaFormat(1000.123456) == '1,000.123456'

	
	def getUppercase(text):
		LOWER_TO_UPPER = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g':'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O','p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x':'X', 'y': 'Y', 'z': 'Z'}
		uppercaseText = ''
		for character in text:
			if character in LOWER_TO_UPPER:
				uppercaseText += LOWER_TO_UPPER[character]
			else:
				uppercaseText += character
		return uppercaseText

	assert getUppercase('Hello') == 'HELLO'
	assert getUppercase('hello') == 'HELLO'
	assert getUppercase('HELLO') == 'HELLO'
	assert getUppercase('Hello, world!') == 'HELLO, WORLD!'
	assert getUppercase('goodbye 123!') == 'GOODBYE 123!'
	assert getUppercase('12345') == '12345'
	assert getUppercase('') == ''

	def getTitleCase(text):
		titledText = ''
		for i in range(len(text)):
			if i == 0:
				titledText += text[i].upper()
			elif text[i].isalpha() and not text[i - 1].isalpha():
				titledText += text[i].upper()
			else:
				titledText += text[i].lower()
		return titledText

	assert getTitleCase('Hello, world!') == 'Hello, World!'
	assert getTitleCase('HELLO') == 'Hello'
	assert getTitleCase('hello') == 'Hello'
	assert getTitleCase('hElLo') == 'Hello'
	assert getTitleCase('') == ''
	assert getTitleCase('abc123xyz') == 'Abc123Xyz'
	assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'
	assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'
	import random
	random.seed(42)
	chars = list('abcdefghijklmnopqrstuvwxyz1234567890 ,.')
	for i in range(1000):
		random.shuffle(chars)
		assert getTitleCase(''.join(chars)) == ''.join(chars).title()

	def reverseString(text):
		text = list(text)
		for i in range(len(text) // 2):
			mirrorIndex = len(text) - 1 - i
			text[i], text[mirrorIndex] = text[mirrorIndex], text[i]
		return ''.join(text)

	assert reverseString('Hello') == 'olleH'
	assert reverseString('') == ''
	assert reverseString('aaazzz') == 'zzzaaa'
	assert reverseString('xxxx') == 'xxxx'

	def makeChange(amount):
		change = {}
		# If the amount is enough to add quarters, add them:
		if amount >= 25:
			change['quarters'] = amount // 25
			# Reduce the amount by the value of the quarters added:
			amount = amount % 25
			# If the amount is enough to add dimes, add them:
		if amount >= 10:
			change['dimes'] = amount // 10
			# Reduce the amount by the value of the dimes added:
			amount = amount % 10
		# If the amount is enough to add nickels, add them:
		if amount >= 5:
			change['nickels'] = amount // 5
			# Reduce the amount by the value of the nickels added:
			amount = amount % 5
			# If the amount is enough to add pennies, add them:
		if amount >= 1:
			change['pennies'] = amount
		return change

	assert makeChange(30) == {'quarters': 1, 'nickels': 1}
	assert makeChange(10) == {'dimes': 1}
	assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}
	assert makeChange(100) == {'quarters': 4}
	assert makeChange(125) == {'quarters': 5}

	def rShuffle(values):
		import random
		# Loop over the range of indexes from 0 up to the length of the list:
		for i in range(len(values)):
			# Randomly pick an index to swap with:
			swapIndex = random.randint(0, len(values) - 1)
			# Swap the values between the two indexes:
			values[i], values[swapIndex] = values[swapIndex], values[i]

	random.seed(42)
	for i in range(10):
		testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		rShuffle(testData1)
		assert len(testData1) == 10
		assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	testData2 = []
	rShuffle(testData2)
	assert testData2 == []

	def collatz(startingNumber):
		# If the starting number is 0 or negative, return an empty list:
		if startingNumber < 1:
			return []
		# Create a list to hold the sequence, beginning with the starting number:
		sequence = [startingNumber]
		num = startingNumber
		# Keep looping until the current number is 1:
		while num != 1:
		# If odd, the next number is 3 times the current number plus 1:
			if num % 2 == 1:
				num = 3 * num + 1
		# If even, the next number is half the current number:
			else:
				num = num // 2
		# Record the number in the sequence list:
			sequence.append(num)
		# Return the sequence of numbers:
		return sequence

	assert collatz(0) == []
	assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
	assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
	assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
	assert len(collatz(256)) == 9
	assert len(collatz(257)) == 123
	import random
	random.seed(42)
	for i in range(1000):
		startingNum = random.randint(1, 10000)
		seq = collatz(startingNum)
		assert seq[0] == startingNum # Make sure it includes the starting number.
		assert seq[-1] == 1 # Make sure the last integer is 1.

	def mergeTwoLists(list1, list2):
		# Create an empty list to hold the final sorted results:
		result = []
		# Start i1 and i2 at index 0, the start of list1 and list2:
		i1 = 0
		i2 = 0
		# Keeping moving up i1 and i2 until one reaches the end of its list:
		while i1 < len(list1) and i2 < len(list2):
		# Add the smaller of the two current items to the result:
			if list1[i1] < list2[i2]:
		# Add list1's current item to the result:
				result.append(list1[i1])
		# Increment i1:
				i1 += 1
			else:
		# Add list2's current item to the result:
				result.append(list2[i2])
		# Increment i2:
				i2 += 1
		# If i1 is not at the end of list1, add the remaining items from list1:
		if i1 < len(list1):
			for j in range(i1, len(list1)):
				result.append(list1[j])
		# If i2 is not at the end of list2, add the remaining items from list2:
		if i2 < len(list2):
			for j in range(i2, len(list2)):
				result.append(list2[j])
		# Return the merged, sorted list:
		return result

	assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
	assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
	assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
	assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
	assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]
	assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]

	def rot13(text):
		encryptedText = ''
		for character in text:
			if not character.isalpha():
				encryptedText += character
			else:
				rotatedLetterOrdinal = ord(character) + 13
				if character.islower() and rotatedLetterOrdinal > 122:
					rotatedLetterOrdinal -= 26
				if character.isupper() and rotatedLetterOrdinal > 90:
					rotatedLetterOrdinal -= 26
				encryptedText += chr(rotatedLetterOrdinal)
		return encryptedText

	assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
	assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
	assert rot13(rot13('Hello, world!')) == 'Hello, world!'
	assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
	assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'

	def bubbleSort(numbers):
		for i in range(len(numbers) - 1):
			for j in range(i, len(numbers)):
				if numbers[i] > numbers[j]:
					numbers[i] , numbers[j] = numbers[j] ,numbers[i]
		
		return numbers
	assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
	assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]

if __name__ == '__main__':
	Exercise()
