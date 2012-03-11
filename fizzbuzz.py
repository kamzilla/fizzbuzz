def get_input():
    print "Enter in a number or 'exit' when done"
    response = raw_input("> ")
    return response
    
def input_check(response):
    if response.isdigit():
        number = int(response)
        fizz_buzz(number)
        return False
    elif response.isalpha() and not response == "exit":
        print "please enter a number, not a word"
        return False
    elif response == "exit":
        print "thanks for playing"
        return True
    else: 
        print "WTF!?!"
        return False
        
def fizz_buzz(number):
    if number % 15 == 0:
        print "fizzbuzz"
    elif number % 3 == 0:
        print "fizz"
    elif number % 5 == 0:
        print "buzz"
    else:
        print number
        print "this number is not divisible by 3 and 5"

def run():
    ready_to_exit = False
    while (not ready_to_exit):
        ready_to_exit = input_check(get_input())

run()
