import random

intro_string = """Hello,

This software will generate a safe, randomised password for you to use to secure all your important files.
First select your range of characters, then see the usage instructions below for the required options:

-a: Letters in Lowercase
-A: Letters in Uppercase
-1: Numbers
-S: Special Characters

Optionally, you can add them together in the following example:

15 -a -A -n -S

"""

lowerLetters = "qwertyuiopasdfghjklzxcvbnm"
upperLetters = lowerLetters.upper()
numbers = "1234567890"
special_chars = '!@#$%^&*()[]{}/\\'


def main():

    print(intro_string, end="")
    mix = string_range = output = ""
    x = input(">> ")

    for i in x:
        if i != " ":
            string_range = string_range + i
        else:
            break
    string_range = int(string_range)

    if "-a" in x:
        mix = mix + lowerLetters
    if "-A" in x:
        mix = mix + upperLetters
    if "-n" in x:
        mix = mix + numbers
    if "-S" in x:
        mix = mix + special_chars

    for o in range(string_range):
        if mix:
            output = output + random.choice(mix)
        else:
            print("Cannot proceed without additional parameters")
            repeat = input("Restart? (Y/N) ")
            if repeat.upper() == "Y":
                paste_instructions = False
                main()
            elif repeat.upper() == "N":
                print("Thanks for using Password Generator.")
                quit()
            else:
                quit()

    print(f"Generated Password: {output}")
    repeat = input("Generate another password? (Y/N) ")
    if repeat.upper() == "Y":
        main()
    elif repeat.upper() == "N":
        print("Thanks for using Password Generator.")
        quit()
    else:
        quit()


if __name__ == '__main__':
    main()