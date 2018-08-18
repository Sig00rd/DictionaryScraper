def get_requested_word_from_user_input():
    input_word = input("Szukane słowo: ")
    return input_word


def print_words(words):
    for i in range(len(words)):
        print("{:2}: {}".format(i, words[i]))


def get_word_numbers_from_user_input():
    print("Proszę podać numery słów do zapisu oddzielając je spacjami.")
    user_input = input()
    return to_int_list(user_input)


def to_int_list(space_separated_ints):
    result_list = [int(number) for number in space_separated_ints.split()]
    return result_list

