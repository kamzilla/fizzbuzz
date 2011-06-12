def get_input():
    print "Enter in a number or 'exit' when done"
    response = raw_input("> ")
    input_check(response)
    
def input_check(response):
    if response.isdigit():
        number = int(response)
        fizz_buzz(number)
    elif response.isalpha() and not response == "exit":
        print "please enter a number, not a word"
        get_input()
    elif response == "exit":
        print "thanks for playing"
        return
    else: 
        print "WTF!?!"
        get_input()
        
def fizz_buzz(number):
    if number%15 == 0:
        print "fizzbuzz"
    elif number%3 == 0:
	        print "fizz"
    elif number%5 == 0:
        print "buzz"
    else:
        print number
        print "this number is not divisible by 3 and 5"    
    get_input()

def run():
    get_input()

run()
