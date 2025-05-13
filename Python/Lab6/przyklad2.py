from math import ceil
from hashlib import sha512
from multiprocessing import Pool

# hash one word using the SHA algorithm
def hash_word(word):
    # create the hash object
    hash_object = sha512()
    # convert the string to bytes
    byte_data = word.encode('utf-8')
    # hash the word
    hash_object.update(byte_data)
    # get the hex hash of the word
    return hash_object.hexdigest()

def main():
    # load a file of words
    path = 'words.txt'
    with open(path) as file:
        words = file.readlines()
    print(f'Loaded {len(words)} words from {path}')

    # create the process pool
    with Pool(4) as pool:
        # create a set of word hashes
        known_words = set(pool.map(hash_word, words))
    print(f'Done, with {len(known_words)} hashes')

if __name__ == '__main__':
    main()
