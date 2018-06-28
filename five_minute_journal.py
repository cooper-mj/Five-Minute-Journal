import json
import random
import datetime
import sys

'''
Loads in a series of quotes from 'quotes.json', returns a random quote
and its author.
'''
def getQuote():

	quotes_data = json.load(open("quotes.json", "r"))
	quote = random.choice(quotes_data)
	return(quote['Quote'] + " - " + quote['Author'] + "\n")

'''
Prompts the user for input, writes prompts and input to the specified 
journal file (passed in as argument).

With the exception of the 'Current thoughts and emotions: ' section, these
prompts follow the format of the Five-Minute Journal's morning section.
'''
def morning_routine(journal):

	journal.write("\n\n")
	journal.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
	journal.write("\n\n")

	print("\nGood morning!\n")

	daily_quote = getQuote()
	print(daily_quote)
	journal.write(daily_quote)

	curr_thoughts = input("\nCurrent thoughts and emotions: \n")
	journal.write("Current thoughts and emotions: \n")
	journal.write(curr_thoughts + "\n\n")

	print("\nThree things I am grateful for: ")
	grateful_1 = input("1. ")
	grateful_2 = input("2. ")
	grateful_3 = input("3. ")

	journal.write("Three things I am grateful for: \n\n")
	journal.write("1. " + grateful_1 + "\n")
	journal.write("2. " + grateful_2 + "\n")
	journal.write("3. " + grateful_3 + "\n\n")

	print("\nWhat would make today amazing?")
	amazing_1 = input("1. ")
	amazing_2 = input("2. ")
	amazing_3 = input("3. ")

	journal.write("What would make today amazing?\n\n")
	journal.write("1. " + amazing_1 + "\n")
	journal.write("2. " + amazing_2 + "\n")
	journal.write("3. " + amazing_3 + "\n\n")

	affirmations = input("\nDaily affirmation(s). I am: ")
	journal.write("Daily affirmation(s). I am: " + affirmations + "\n")

'''
Prompts the user for input, writes prompts and input to the specified 
journal file (passed in as argument).

These prompts follow the format of the Five-Minute Journal's evening 
section.
'''
def evening_routine(journal):

	journal.write("\n")
	journal.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
	journal.write("\n\n")

	print("\nThree wonderful things that happened today: ")
	wonderful_1 = input("1. ")
	wonderful_2 = input("2. ")
	wonderful_3 = input("3. ")

	journal.write("Three wonderful things that happened today: \n\n")
	journal.write("1. " + wonderful_1 + "\n")
	journal.write("2. " + wonderful_2 + "\n")
	journal.write("3. " + wonderful_3 + "\n\n")

	curr_thoughts = input("\nHow could I have made today better? \n")
	journal.write("How could I have made today better? \n\n")
	journal.write(curr_thoughts + "\n\n")

	journal.write("--------------------------------------------------------------------------------")

'''
Prints a message indicating how to run this program correctly (e.g.
arguments to use) from the command line.
'''
def usage_message():

		return("Unidentified command. Usage: $ python3 morningjournal.py [morning | evening]")

'''
Checks for command line argument errors, and if there are none, runs either
the morning or evening routine as directed by the command line argument.
'''
def main():
	
	if len(sys.argv) < 2:
		usage_message()
		return

	journal = open("morningjournal.txt", "a")

	if sys.argv[1] == "morning":
		morning_routine(journal)

	elif sys.argv[1] == "evening":
		evening_routine(journal)

	else:
		print(usage_message())

	journal.close()

if __name__ == '__main__':
	main()