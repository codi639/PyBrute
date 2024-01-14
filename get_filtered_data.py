# get_filtered_data.py

def add_word_variations(persons_info, additional_info):
    updated_persons_info = add_persons_variations_to_array(persons_info)
    updated_additional_info = add_additional_variations_to_array(additional_info)

    return updated_persons_info, updated_additional_info


def add_persons_variations_to_array(data_array):
    updated_array = []

    for item in data_array:
        # print(f"item {item}")
        updated_item = []

        if item.isalpha() and not item.isdigit():
            updated_item_one_letters = item[0]
            updated_item_two_letters = item[:2]
            updated_item_three_letters = item[:3]
            updated_array.append(updated_item_one_letters)
            updated_array.append(updated_item_two_letters)
            updated_array.append(updated_item_three_letters)

    return updated_array

def add_additional_variations_to_array(data_array):
    updated_array = []

    for item in data_array:
        # print(f"item {item}")
        updated_item = []

        if item.isalpha() and not item.isdigit():
            updated_item_one_letters = item[0]
            # updated_item_two_letters = item[:2]
            # updated_item_three_letters = item[:3]
            updated_array.append(updated_item_one_letters)
            # updated_array.append(updated_item_two_letters)
            # updated_array.append(updated_item_three_letters)

    return updated_array