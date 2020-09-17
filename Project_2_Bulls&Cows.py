# '''
# author = Vitek Kral
# '''
def generate_nums():
    import random
    num_set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    rnd_num_list = []

    rnd = random.randint(1, 9)      # prvni cislice nesmi byt nula
    temp_val = num_set.pop(rnd)
    rnd_num_list.append(temp_val)

    for i in range(1, 4, 1):
        rnd = random.randint(0, 8-i)        # doplneni dalsich trech unikatnich cislic
        temp_val = num_set.pop(rnd)
        rnd_num_list.append(temp_val)

    return rnd_num_list


def conv_to_int(num_in):
    temp_str = ""
    num_in_int = 0
    for i in num_in:
        temp_str += str(i)
        num_in_int = int("".join(temp_str))
    return num_in_int


def conv_to_list(int_in):
    num_in_list = []
    for i in str(int_in):
        if i.isdigit():
            num_in_list.append(int(i))
    return num_in_list


def number_evaluation(attempt_in):      # vyhodnoceni platnosti zadaneho cisla 0000-9999
    if attempt_in.isdecimal() is not True:
        return False
    elif (int(attempt_in) <= -1) or (int(attempt_in) > 9999):
        return False
    elif len(attempt_in) is not 4:
        return False
    else:
        return True


def comparison(gener_num_in, attempt_in):       # porovnani seznamu generovaneho cisla a hadaneho
    bulls = cows = 0
    used_numbers = []  # pouzita cisla - vyloucení opakujicich se cislic v zadani napr. 0011
    comparison_result = []
    for i in range(1, 5, 1):
        if attempt_in[i - 1] == gener_num_in[i - 1]:
            used_numbers.append(attempt_in[i - 1])
            bulls += 1


    for i in range(1, 5, 1):
        if attempt_in[i-1] not in used_numbers:
            if (attempt_in[i - 1] in gener_num_in) and (attempt_in[i - 1] != gener_num_in[i - 1]):
                used_numbers.append(attempt_in[i - 1])
                cows += 1

    comparison_result.append(bulls)
    comparison_result.append(cows)
    return comparison_result


def evaluation(guess_no_in):           # zaverecne slovni hodnoceni
    eval_str = ""
    if guess_no_in < 9:
        eval_str = "AMAZING!!! :)"
    elif guess_no_in < 13:
        eval_str = "GOOD!"
    elif guess_no_in < 17:
        eval_str = "average."
    elif guess_no_in >= 17:
        eval_str = "just useless..."

    return eval_str


def main():
    print("\n ---=== BULLS & COWS ===---\n")
    print("Hi there\nI've generated a random 4 digit number for you.\nLet's play a bulls and cows game.\n")
    generated_number = generate_nums()
    # print("The secret number is: {}\n".format(conv_to_int(generated_number)))     # ZOBRAZENI VYGENEROVANEHO CISLA
    result = [0]
    guess_no = 1

    while result[0] != 4:
        attempt = input("Enter 4-digit number (guess no.{}): ".format(guess_no))
        while number_evaluation(attempt) is False:
            print("Invalid entry!")
            attempt = input("Enter 4-digit number (guess no.{}): ".format(guess_no))
        attempt_to_list = conv_to_list(attempt)
        result = comparison(generated_number, attempt_to_list)
        print("Bulls: {} Cows: {}".format(result[0], result[1]))
        guess_no += 1

    print("\n---=== YOU WIN! ===---\n\nCorrect, you've guessed the right number in {} guesses!".format(guess_no-1))
    print("That's {}".format(evaluation(guess_no)))
    exit()


main()
