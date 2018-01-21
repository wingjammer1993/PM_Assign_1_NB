import csv


# Function to create counts of all the keys
def generate_stats(filename, separator):
    data_joint_probabilites = {}
    with open(filename, 'r') as file_obj:
        for line in csv.reader(file_obj, delimiter=separator, skipinitialspace=True, quoting=csv.QUOTE_NONE):
            if line:
                tup = (line[0], line[1], line[2], line[3])
                if tup in data_joint_probabilites:
                    data_joint_probabilites[tup] = data_joint_probabilites[tup] + 1
                else:
                    data_joint_probabilites[tup] = 1

    length = sum(data_joint_probabilites.values())
    for i in data_joint_probabilites:
        data_joint_probabilites[i] = data_joint_probabilites[i]/length
    return data_joint_probabilites


if __name__ == "__main__":
    training = 'Dataset.data'
    delim = ' '
    data_stats = generate_stats(training, delim)


# Function to read the input file as a csv
# def read_input(filename, separator):
#     data_frame = {}
#     index = 0
#     with open(filename, 'r') as file_obj:
#         for line in csv.reader(file_obj, delimiter=separator, skipinitialspace=True, quoting=csv.QUOTE_NONE):
#             if line:
#                 data_line = {'class': line[0], 'age': line[1], 'gender': line[2], 'survived': line[3]}
#                 data_frame[index] = data_line
#                 index = index + 1
#     return data_frame

