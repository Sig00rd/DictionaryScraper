def get_requested_expressions_from_user_input():
    input_word = input("Wpisz szukane wyrażenia oddzielając je przecinkami: ")
    return to_words_list(input_word)


def to_words_list(comma_separated_words):
    result_list = [word for word in comma_separated_words.split(",")]
    return result_list


def print_words_or_meanings(message, words):
    print(message)
    for i in range(len(words)):
        print("{:2}: {}".format(i, words[i]))


def get_word_numbers_from_user_input():
    input_list = get_numbers_from_user_input(
        "Podaj numery słów do zapisu oddzielając je spacjami:"
    )
    return input_list


def get_numbers_from_user_input(message):
    print(message)
    user_input = input()
    return to_int_list(user_input)


def get_meaning_numbers_from_user_input():
    input_list = get_numbers_from_user_input(
        "Podaj numery znaczeń do zapisu oddzielając je spacjami:"
    )
    return input_list


def to_int_list(space_separated_ints):
    result_list = [int(number) for number in space_separated_ints.split()]
    return result_list


def print_connection_error_message():
    print("Napotkano błąd połączenia.")


def print_saving_message(word):
    print("Zapisuję słowo: " + word + ".")


def get_numbers_of_words_to_save_from_user(writing_meaning_list):
    print_words_or_meanings(
        "Podaj numery słów do zapisu oddzielając je spacjami:",
        writing_meaning_list
    )
    number_list = to_int_list(input())
    return cut_numbers_above_list_size(number_list, writing_meaning_list)


def cut_numbers_above_list_size(number_list, data_list):
    for number in number_list:
        if number >= len(data_list):
            number_list.remove(number)
    return number_list
