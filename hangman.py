import random


def read_file(file_name):
    with open(file_name, 'r') as sw:
        txt = sw.readlines()
        sw.close()
    return txt


def select_random_word(words):
    w_index = random.randint(0, len(words) - 1)
    word = list(words[w_index])
    l_index = random.randint(0, len(word) - 1)

    word[l_index] = '_'
    print("Guess the word: " + "".join(word))
    return words[w_index]


def get_user_input():
    ans = input("Guess the missing letter: ")
    return ans


def run_game(file_name):
    #"""
    #This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    #"""
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

