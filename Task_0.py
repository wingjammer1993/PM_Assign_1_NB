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
