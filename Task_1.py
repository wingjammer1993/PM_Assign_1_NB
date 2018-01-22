import Task_0
import itertools


def generate_conditional(joint_probabilities):
    data_conditional_probabilities = {}
    table = list(itertools.product(['1st', '2nd', '3rd', 'crew'], ['adult', 'child'],
                                   ['male', 'female'], repeat=1))
    for i in table:
        tup_1 = (i[0], i[1], i[2], 'no')
        tup_2 = (i[0], i[1], i[2], 'yes')
        a = 0
        b = 0

        if tup_1 in joint_probabilities:
            a = joint_probabilities[tup_1]
        if tup_2 in joint_probabilities:
            b = joint_probabilities[tup_2]

        if a > 0 or b > 0:
            denominator = a + b
            data_conditional_probabilities[i] = a / denominator
        else:
            data_conditional_probabilities[i] = 'data not available'
    return data_conditional_probabilities


def classify(table):
    data_classify = {}
    for i in table:
        if table[i] == 'data not available':
            data_classify[i] = 'data not available'
        elif table[i] >= 0.5:
            data_classify[i] = 'D'
        else:
            data_classify[i] = 'S'
    return data_classify


if __name__ == "__main__":
    training = 'Dataset.data'
    delim = ' '

    data_joint = Task_0.generate_stats(training, delim)
    data_conditional = generate_conditional(data_joint)
    classification = classify(data_conditional)
    print(data_conditional)
    print(classification)

