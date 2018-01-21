import csv
import itertools


# Function to create counts of all the keys
def generate_stats(filename, separator):
    data_frame = {}
    with open(filename, 'r') as file_obj:
        for line in csv.reader(file_obj, delimiter=separator, skipinitialspace=True, quoting=csv.QUOTE_NONE):
            if line:
                for index in range(0, 4):
                    if line[index] in data_frame:
                        data_frame[line[index]] = data_frame[line[index]] + 1
                    else:
                        data_frame[line[index]] = 1
    return data_frame


# Function to generate the probabilities of all keys
def generate_probability(statistics):
    data_probability = {}
    den_class = statistics['1st']+statistics['2nd']+statistics['3rd']+statistics['crew']
    data_probability['1st'] = statistics['1st']/den_class
    data_probability['2nd'] = statistics['2nd']/den_class
    data_probability['3rd'] = statistics['3rd']/den_class
    data_probability['crew'] = statistics['crew']/den_class
    den_gender = statistics['male']+statistics['female']
    data_probability['male'] = statistics['male']/den_gender
    data_probability['female'] = statistics['female']/den_gender
    den_survival = statistics['yes']+statistics['no']
    data_probability['yes'] = statistics['yes']/den_survival
    data_probability['no'] = statistics['no']/den_survival
    den_age = statistics['adult']+statistics['child']
    data_probability['adult'] = statistics['adult']/den_age
    data_probability['child'] = statistics['child']/den_age
    return data_probability


# Function to generate the joint probabilities for the key truth table
def generate_joint(probabilities):
    data_joint_probabilites = {}
    table = list(itertools.product(['male', 'female'], ['adult', 'child'], ['yes', 'no'],
                                   ['1st', '2nd', '3rd', 'crew'], repeat=1))
    for i in table:
        data_joint_probabilites[i] = probabilities[i[0]]*probabilities[i[1]]*probabilities[i[2]]*probabilities[i[3]]
    return data_joint_probabilites


if __name__ == "__main__":
    training = 'Dataset.data'
    delim = ' '

    data_stats = generate_stats(training, delim)
    data_prob = generate_probability(data_stats)
    data_joint = generate_joint(data_prob)
    summation = sum(data_joint.values())
    print(data_joint)
    print(summation)


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

