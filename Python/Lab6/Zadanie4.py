import os
from multiprocessing import Pool

def search_in_file(args):
    filepath, phrase = args
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for i, line in enumerate(f, start=1):
                if phrase in line:
                    return f"{filepath} (linia {i}): {line.strip()}"
    except Exception as e:
        return f"{filepath}: Błąd - {e}"
    return None

def find_phrase_in_dir(directory, phrase):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))

    with Pool() as pool:
        results = pool.map(search_in_file, [(path, phrase) for path in file_paths])

    matches = [res for res in results if res]

    if matches:
        for match in matches:
            print(match)
    else:
        print("Nie znaleziono")

if __name__ == "__main__":
    dir_path = input("Podaj ścieżkę do katalogu: ")
    phrase = input("Podaj słowo do wyszukania: ")

    find_phrase_in_dir(dir_path, phrase)
