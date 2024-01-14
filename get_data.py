# get_data.py

from datetime import datetime
from itertools import product
from get_filtered_data import add_word_variations

def get_person_information():
    # Initialize empty lists to store person and additional information
    persons = []
    additional_info = []

    # Ask the user for the number of persons
    num_persons = int(input("Enter the number of persons:"))

    # Gather information for each person
    for i in range(num_persons):
        print(f"\nEnter information for person {i + 1}:")

        # Ask for name, last name, and birthdate
        name = input("Enter name:")
        last_name = input("Enter last name:")
        birthdate_str = input("Enter birthdate (DD-MM-YYYY), leave blank if not available:")

        # Check if the user provided a birthdate
        if birthdate_str.lower() == '':
            day, month, full_year, last_two_digits = '', '', '', ''
        else:
            # Convert birthdate string to datetime object
            birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")

            # Extract day, month, and year components
            day, month, full_year = str(birthdate.day).zfill(2), str(birthdate.month).zfill(2), str(birthdate.year)
            last_two_digits = full_year[-2:]

        # Add person information to the persons list
        person_info = [name, last_name, day, month, full_year, last_two_digits]
        persons.extend(person_info)

        # Ask for the number of additional information
        num_additional_info = int(input("Enter the number of additional information for this person:"))

        # Gather additional information for each person
        additional_info_for_person = []
        for j in range(num_additional_info):
            info = input(f"Enter additional information {j + 1} for {name}:")
            additional_info_for_person.append(info)

        # Add additional information to the additional_info list
        additional_info.extend(additional_info_for_person)

    # Generate case variants after gathering all information
    full_persons = generate_case_variants([persons])
    full_additional_info = generate_case_variants([additional_info])

    # Remove duplicate words
    full_persons = remove_duplicates([full_persons])
    full_additional_info = remove_duplicates([full_additional_info])

    # Flatten the lists
    full_persons  = [item for sublist in full_persons for item in sublist]
    full_additional_info = [item for sublist in full_additional_info for item in sublist]

    data_persons, data_additional_info = add_word_variations(full_persons, full_additional_info)

    full_data = []
    full_data.extend(full_persons)
    full_data.extend(full_additional_info)
    full_data.extend(data_persons)
    full_data.extend(data_additional_info)


    return full_data

def remove_duplicates(data):
    unique_data = []

    for item in data:
        # Flatten the nested list
        flat_item = [element for sublist in item for element in sublist]
        unique_item = tuple(set(flat_item))
        unique_data.append(list(unique_item))

    return unique_data

def generate_case_variants(persons_info):
    case_variants = []

    for person_info in persons_info:
        case_variant_upper = [value.upper() for value in person_info]
        case_variant_lower = [value.lower() for value in person_info]

        case_variants.append(case_variant_upper)
        case_variants.append(case_variant_lower)

    return case_variants

def write_to_file(combination, file_path):
    with open(file_path, 'w') as file:
        file.write(combination + '\n')

def generate_combinations(persons_info, additional_info, file_path):
    all_words = persons_info + additional_info

    for r in range(2, len(all_words) + 1):
        for combination in product(*all_words, repeat=r):
            # Join the combination into a single string
            combined_string = ''.join(combination)

            # Check the length criteria
            if 6 <= len(combined_string) <= 13:
                # Write the combination to the file immediately
                write_to_file(combined_string, file_path)
