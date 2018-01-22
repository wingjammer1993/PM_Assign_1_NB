import csv
import itertools
import Task_1

# Function to create counts of all the keys
def generate_tables(filename, separator):
    data_yes = {}
    data_no = {}
    count_yes = 0
    count_no = 0
    with open(filename, 'r') as file_obj:
        for line in csv.reader(file_obj, delimiter=separator, skipinitialspace=True, quoting=csv.QUOTE_NONE):
            if line:
                if line[-1] == 'yes':  # survived
                    for i in range(0, 3):
                        if line[i] in data_yes:
                            data_yes[line[i]] += 1
                        else:
                            data_yes[line[i]] = 1
                    count_yes += 1
                elif line[-1] == 'no':
                    for i in range(0, 3):  # off
                        if line[i] in data_no:
                            data_no[line[i]] += 1
                        else:
                            data_no[line[i]] = 1
                    count_no += 1

    for i in data_yes:
        data_yes[i] = data_yes[i]/count_yes
        data_no[i] = data_no[i]/count_no

    y = count_yes + count_no
    count_yes = count_yes / y
    count_no = count_no / y

    return data_yes, data_no, count_yes, count_no


def generate_nb(prob_yes, prob_no, c_yes, c_no):
    data_nb = {}
    table = list(itertools.product(['1st', '2nd', '3rd', 'crew'], ['adult', 'child'],
                                   ['male', 'female'], repeat=1))
    for i in table:
        a = prob_no[i[0]]*prob_no[i[1]]*prob_no[i[2]]*c_no
        b = prob_yes[i[0]]*prob_yes[i[1]]*prob_yes[i[2]]*c_yes

        data_nb[i] = a / (a + b)

    return data_nb


if __name__ == "__main__":
    training = 'Dataset.data'
    delim = ' '
    dict_yes, dict_no, yes, no = generate_tables(training, delim)
    dict_nb = generate_nb(dict_yes, dict_no, yes, no)
    classification = Task_1.classify(dict_nb)
    print(dict_nb)
    print(classification)


