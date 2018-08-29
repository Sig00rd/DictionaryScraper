def get_requested_words_from_user_input():
    input_word = input("Wpisz szukane wyrażenia oddzielając je przecinkami: ")
    return to_words_list(input_word)


def to_words_list(comma_separated_words):
    result_list = [word for word in comma_separated_words.split(",")]
    return result_list


def print_words(words):
    for i in range(len(words)):
        print("{:2}: {}".format(i, words[i]))


def get_word_numbers_from_user_input():
    print("Podaj numery słów do zapisu oddzielając je spacjami:")
    user_input = input()
    return to_int_list(user_input)


def to_int_list(space_separated_ints):
    result_list = [int(number) for number in space_separated_ints.split()]
    return result_list
