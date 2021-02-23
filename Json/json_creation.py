import json

def create_person():
    new_person = {"First Name": "Anna",
                    "Last Name": "Ables",
                    "Age": 35,
                    "Visits": ["1/1/2020", "2/3/2020", "3/15/2020"]}
    return new_person

# Approach 1
def output_json(my_dict):
    filename = "my_booleans.json"
    out_file = open(filename, 'w')
    json.dump(my_dict, out_file)
    out_file.close()

# Approach 2
def output_json_with(output_data):
    filename = "my_output.txt"
    with open(filename, 'w') as out_file:
        json.dump(output_data, out_file)
    print("the output is finished")


def create_list():
    return [True, False, True]


if __name__ == "__main__":
    data_to_output = create_list()
    output_json(data_to_output)

#if __name__ == "__main__":
#    person = create_person()
#    print(person)
#    output_json(person)