import random
import json


def load_words() -> list:
    """
    Function will load the word dictionary file and return a set of all words.
    :rtype: list[str]
    """
    with open('./words_dictionary.json') as word_file:
        valid_words = list(json.load(word_file).keys())
    return valid_words


def random_symbol(num: int = 1, seed=None) -> list:
    """
    Function will return a list of random symbols from the following set:

    ['!', '@', '#', '$', '%', '^', '&, '*' ,'(', ')', '-', '_', '=', '+', '`', '~]

    :param num:  Number of symbols to return
    :type num: int
    :param seed: Random seed (Optional)
    :rtype: list
    """
    symbols = "~`!@#$%^&*()_-+="
    random.seed(a=seed)
    result = []
    while num > 0:
        rand_index = random.randint(0, len(symbols) - 1)
        result.append(symbols[rand_index])
        num = num - 1
    return result


def random_word(num: int = 1, seed=None) -> list:
    """
    Function will return a list of random words.

    :param num: Number of words to return
    :type num: int
    :param seed: Random seed (Optional)
    :rtype: list[str]
    """
    word_list = load_words()
    result = []
    random.seed(a=seed)
    while num > 0:
        rand_index = random.randint(0, len(word_list) - 1)
        while len(word_list[rand_index]) >= 8:
            rand_index = random.randint(0, len(word_list) - 1)
        result.append(word_list[rand_index])
        num = num - 1
    return result


def lambda_handler(event, context):
    # TODO implement
    words = random_word(2)
    symbols = random_symbol(2)
    password = "{word1}{word2}{num1}{num2}{sym1}{sym2}".format(word1=words[0].capitalize(),
                                                               word2=words[1].capitalize(),
                                                               num1=random.randint(0,9),
                                                               num2=random.randint(0, 9),
                                                               sym1=symbols[0],
                                                               sym2=symbols[1])
    return {
        "statusCode": 200,
        "body": json.dumps(password)
    }
