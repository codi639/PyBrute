import argparse
import itertools
import random
import string


def get_person_info(person_number):
    """
    Function to prompt the user for personal information.
    :param person_number: The person number (e.g., Person 1, Person 2)
    :return: A dictionary containing the person's name, last name, and birthdate
    """
    print(f"\nEnter information for Person {person_number}:")
    first_name = input(f"First Name: ")
    last_name = input(f"Last Name: ")
    birth_year = input(f"Birth Year (4 digits): ")
    birth_month = input(f"Birth Month (2 digits): ")
    birth_day = input(f"Birth Day (2 digits): ")

    return {
        'first_name': first_name,
        'last_name': last_name,
        'birth_year': birth_year,
        'birth_month': birth_month,
        'birth_day': birth_day,
    }


def generate_password_variations(person_info, additional_chars, include_special_chars, case_variation, max_combinations, min_r, max_r, range_r):
    """
    Function to generate potential password variations based on a person's information and additional characters.
    :param person_info: The person's info dictionary
    :param additional_chars: List of additional characters (e.g., pet name, favorite number)
    :param include_special_chars: Boolean flag to include special characters
    :param case_variation: Boolean flag to alternate case for each part of the name
    :param max_combinations: The max number of combinations to generate
    :return: List of generated passwords
    """
    passwords = []
    first_name = person_info['first_name']
    last_name = person_info['last_name']
    birth_year = person_info['birth_year']
    birth_month = person_info['birth_month']
    birth_day = person_info['birth_day']

    # Extract first letters of first and last name
    first_initial = first_name[0]
    last_initial = last_name[0]

    # Generate variations by permuting different segments
    name_variations = [
        f"{first_name}{last_name}",
        f"{last_name}{first_name}",
        f"{first_name[0]}{last_name}",
        f"{first_name}{last_name[0]}",
        f"{first_name[0]}{last_name[0]}",
        f"{first_name}{birth_year[-2:]}",
        f"{last_name}{birth_year[-2:]}",
        f"{first_name[0]}{birth_month}{birth_day}",
        f"{first_name}{birth_month}{birth_day}",
        f"{last_name}{birth_month}{birth_day}",
    ]

    # Apply case variations if needed
    if case_variation:
        name_variations.extend([name.lower() for name in name_variations])
        name_variations.extend([name.upper() for name in name_variations])
    
    # Include the first letters (both upper and lower case)
    name_variations.extend([
        f"{first_initial}{last_name}",
        f"{first_name}{last_initial}",
        f"{first_initial}{last_initial}",  # Uppercase first initials
        f"{first_initial.lower()}{last_name}",
        f"{first_name}{last_initial.lower()}",
        f"{first_initial.lower()}{last_initial.lower()}",  # Lowercase first initials
    ])

    # Include additional characters
    for add_char in additional_chars:
        name_variations.append(f"{add_char}{first_name}{birth_year[-2:]}")
        name_variations.append(f"{first_name}{add_char}{birth_year[-2:]}")
        name_variations.append(f"{add_char}{first_name[0]}{birth_month}")
        name_variations.append(f"{first_name[0]}{add_char}{birth_day}")
        
        if include_special_chars:
            name_variations.append(f"{add_char}#{first_name}{birth_year[-2:]}")
            name_variations.append(f"{first_name}{birth_month}#{add_char}")

    # Generate more combinations with special characters
    if include_special_chars:
        name_variations.extend([
            f"{first_name}{birth_year[-2:]}@{last_name}",
            f"{first_name[0]}{birth_year[-2:]}$",
            f"{first_name}{last_name}!{birth_year}",
            f"{first_name}{birth_year}#{birth_day}",
            f"{first_name}{birth_month}{birth_day}*",
            f"{first_name}${last_name}#{birth_year}",
        ])

    # Add random special characters in the middle of names and birthdates
    if include_special_chars:
        for name_variation in name_variations:
            password_with_special_char = insert_special_chars_randomly(name_variation)
            passwords.append(password_with_special_char)

    # Generate permutations for all lengths from min_r to max_r if the flag is set
    r_values = range(min_r, max_r + 1) if range_r else [max_r]

    # Generate permutations of names, dates, and additional characters
    for r in r_values:
        for combination in itertools.permutations([first_name, last_name, birth_year[-2:], birth_month, birth_day, first_initial, last_initial], r):
            passwords.append(''.join(combination))

    # Limit to max combinations if necessary
    return passwords#[:max_combinations]


def insert_special_chars_randomly(base_string):
    """
    Function to randomly insert special characters into a base string.
    :param base_string: The string to modify
    :return: A string with special characters inserted at random positions
    """
    special_chars = string.punctuation  # All special characters
    num_insertions = random.randint(1, 3)  # Randomly insert between 1 and 3 special characters

    for _ in range(num_insertions):
        insert_pos = random.randint(0, len(base_string))  # Random position to insert
        special_char = random.choice(special_chars)  # Random special character
        base_string = base_string[:insert_pos] + special_char + base_string[insert_pos:]
    
    return base_string


def parse_arguments():
    """
    Function to parse command-line arguments using argparse.
    :return: Parsed arguments as a Namespace object
    """
    parser = argparse.ArgumentParser(description="Generate password combinations.")
    
    # Arguments for number of people
    parser.add_argument('-op', '--num_people', type=int, required=True, 
                        help="Number of people for password generation.")
    
    # Arguments for additional characters
    parser.add_argument('-ap', '--num_additional', type=int, default=0, 
                        help="Number of additional characters (e.g., pet name, favorite number).")
    
    # Flag to include special characters
    parser.add_argument('-sc', '--special_chars', action='store_true', 
                        help="Include special characters (e.g., @, #, $, etc.) in the passwords.")
    
    # Argument to control case variations
    parser.add_argument('-cv', '--case_variation', action='store_true', 
                        help="Include case variations (e.g., lowercase, uppercase) in the passwords.")

    # Limit the number of password combinations
    parser.add_argument('-mc', '--max_combinations', type=int, default=500, 
                        help="Max number of passwords to generate (default is 500).")

    # Range for permutations
    parser.add_argument('-mipl', '--min_lenght_permutation', type=int, default=2,
                        help="Minimum length of the permutations (default is 2).")
    parser.add_argument('-mapl', '--max_lenght_permutation', type=int, default=5,
                        help='Maximum length of the permutations (default is 5).')

    # Flag to indicate if the user wants to generate all permutations from min_r to max_r
    parser.add_argument('--range_r', action='store_true', 
                        help="Generate permutations for all lengths from min_r to max_r.")

    return parser.parse_args()


def main():
    # Parse command-line arguments
    args = parse_arguments()

    # Get additional characters (if any)
    additional_chars = []
    if args.num_additional > 0:
        for i in range(args.num_additional):
            additional_char = input(f"Enter additional character {i + 1}: ")
            additional_chars.append(additional_char)
    
    # List to hold all generated passwords
    all_passwords = []

    # Generate passwords for each person
    for person_number in range(1, args.num_people + 1):
        # Get information for each person
        person_info = get_person_info(person_number)

        # Generate the password variations for this person
        passwords = generate_password_variations(person_info, additional_chars, args.special_chars, 
                                                 args.case_variation, args.max_combinations,
                                                 args.min_lenght_permutation, args.max_lenght_permutation, args.range_r)
        
        # Add generated passwords to the main list
        all_passwords.extend(passwords)

    # Output the generated passwords
    print("\nGenerated Passwords:")
    for password in set(all_passwords):  # Using set to remove duplicates
        print(password)


if __name__ == "__main__":
    main()

             
