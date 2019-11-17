# Convert Time in Number to words

import sys
 

def get_mid(mins):
	if mins < 30:
		text = "past"
	elif mins >= 30:
		text = "to"
	return text


def get_hour(hour,mins):
	if mins < 30:
		hour = hour
	elif mins >= 30:
		hour = hour + 1
	if hour % 12 > 0:
		hour = hour % 12
	return hour


def get_mins(mins):
	if mins < 30:
		res = mins
	elif mins >= 30:
		res = 60 - mins
	return res


def getword(num):
	units = ['','one','two','three','four','five','six','seven','eight','nine']
	teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
	tens =  ['','ten','twenty','thirty','forty','fifty','sixty','seventy', 'eighty','ninety']

	word = ""
	if num < 10:
		word = word + units[num]
	elif num % 10 == 0 :
		word = word + tens[num/10];
	elif num % 10 > 0 and num < 20:
		word = word + teens[num - 10]
	elif num % 10 > 0 and num > 20:
		word = getword(num - (num % 10)) +" "+ units[num % 10]
	return word

def main():
	hour = raw_input("Enter Hours: ")
	mins = raw_input("Enter Minutes: ")
	hour = int(hour)
	mins = int(mins)
	if (hour < 1) or (hour > 12):
		sys.exit("Error! Hours must be greater than or equal to 1 and less than 12")
	if (mins <= 0) or (mins > 60):
		sys.exit("Error! Minutes must be greater than 0 and less than 60")
	mid = get_mid(mins)
	hour = get_hour(hour,mins)
	mins = get_mins(mins)
	hour = getword(hour)
	minutes = getword(mins)
	word_time = minutes+" minutes "+mid+" "+hour
	print word_time.capitalize()


if __name__ == "__main__":
	main()
