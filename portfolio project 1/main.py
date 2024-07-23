import string

morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
letter_count = dict((key, n) for (key,n) in zip(string.ascii_lowercase, morse_code))
print(letter_count)

def morse_text(input_text, direction):
    empty_str = ""
    if direction == "encrypt":
        for letter in input_text:
            if letter not in letter_count and letter != " ":
                empty_str += letter + " "
            elif letter != " ":
                empty_str += letter_count[letter] + " "
            else:
                empty_str += "/" + " "
        final_text = empty_str[:-1]
    if direction == "decrypt":
        input_text = input_text.split(" ")
        for n in input_text:
            if n not in letter_count.values() and n != "/":
                empty_str += n
            elif n != "/":
                for key, value in letter_count.items():
                    if n == value:
                        empty_str += key
            else:
                empty_str += " "

        final_text = empty_str[0].capitalize() + empty_str[1:]

    print(f"The {direction} text is: {final_text}")


game_is_on = True
while game_is_on:
    direction = input("Do you want to encrypt or decrypt a text?").lower()
    user_input = input("Please enter a string/morse_code to be converted").lower()
    morse_text(user_input, direction)

    reset = input("Would like to try again? Type 'YES' or 'NO'").upper()
    if reset == "NO":
        print("Good Bye")
        game_is_on = False

