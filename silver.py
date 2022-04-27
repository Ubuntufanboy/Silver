import playsound
valid = ["1","2","3","4","5","6","7","8","9","0","print", "+", "-", "*", "/", "play", "stop"]
operands = ["+", "-", "*", "/"]

def is_number(test):
        try:
            tmp = myfloat = float(test)
            return True
        except:
            return False

def is_file(job):
    if job.startswith("\""):
        return True
    else:
        return False

while True:
    command = input("silver>>>  ")

    jobs = command.split()


    for job in jobs:
        if job in valid or is_number(job) or is_file(job):
            pass # This just means that the keywork is valid
        else:
            print(f"Silver !>> error {job} is not a valid command!")
            exit()
    # Only run this if there is a number or operand in the command

    def needs_math():
        for tas in jobs:
            if tas in operands:
                return True
            elif is_number(tas):
                return True
    if needs_math():   
        # Number logic
        needs_calc = True
        # If a single number is given return the number back

        if is_number(jobs[0]) and len(jobs) == 1:
            print(jobs[0])
            needs_calc = False

        # If 2 numbers are given with no operation return an error

        if is_number(jobs[0]) and is_number(jobs[1]):
            print("Silver !>>Invalid syntax")
            exit()

        # if dividing by zero return error

        if jobs[1] == "/" and jobs[2] == "0":
            print("Silver !>> Divide by zero error!")
            exit()

        # if 2 operands are given return invalid syntax

        if jobs[1] in operands and jobs[2] in operands:
            print("Silver !>> Invalid syntax")
            exit()

        # this might help fix some logic

        def is_odd(num):
            if num % 2 == 0:
                return False

        for i in range(len(jobs)):
            if is_odd(i) and jobs[i] not in operands:
                print("Silver !>> Invalid syntax")
                exit()
            
            if is_odd(i) and is_number(jobs[i]):
                print("Silver !>> Invalid syntax")
                exit()
        
        # if number is bigger than 9 allow it

        ###########################
        # Actually doing the math #
        ###########################

        if needs_calc:
            print(eval(command))
    else:
        print("We need to play some audio")

        ###################
        # Error detection #
        ###################

        # If multiple "play" is given return error

        playcount = 0
        for job in jobs:
            if job == "play":
                playcount += 1
            if playcount == 2:
                print("Silver !>> Invalid syntax")
        
        # Try to play the file but if the file does not exist return an error

        try:
            to_play = jobs[1]
            to_play = list(to_play)
            to_play.pop(0)
            to_play.pop(-1)

            new_to_play = ""

            for item in to_play:
                new_to_play += item
            
            to_play = new_to_play
            playsound.playsound(to_play)
        except:
            print(f"Silver !>> {to_play} is not a valid filepath")