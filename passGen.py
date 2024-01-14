# main_script.py

from get_data import get_person_information
from itertools import product


def generate_and_write_combinations(words_list, file_path):
    print(f"\nOppening file: {file_path}")
    with open(file_path, 'w') as f:
        for r in range(2, len(words_list) + 1):
            print(f"Entering outer loop for r={r}")
            for combination in product(words_list, repeat=r):
                combined_string = "".join(combination)

                if 6 <= len(combined_string) <= 13:
                    f.write(combined_string + '\n')
                    # write_combination_to_file(combined_string, file_path)
            print(f"Exiting outer loop for r={r}")
    print(f"Closing file: {file_path}")

def write_combination_to_file(combination, file_path):
    with open(file_path, 'a') as file:  # Use 'a' to append to the file
        file.write(combination + '\n')

def main():
    words_list = get_person_information()
    file_path = 'passGen.txt'
    print(f"Using the words list: {words_list}")
    print(f"Writting to file: {file_path}")
    generate_and_write_combinations(words_list, file_path)
    print(f"Generation completed.")

if __name__ == '__main__':
    main()

