data_file = open('chiru_data.csv', 'r')
data = data_file.readlines()
data_file.close()

data = data[3:]

answer_key = [
    0, 1, 0, 1, 0,
    1, 0, 1, 0, 1,
    0, 1, 0, 1, 0,
    1, 1, 1, 0, 1,
    1, 1
]

for i, person_data in enumerate(data):
    responses = person_data.split(',')[7:29]
    score = 0
    for j, response in enumerate(responses):
        if (answer_key[j] and response == 'Yes') or ((not answer_key[j]) and response == 'No'):
            score += 1
    data[i] = person_data[:-2] + ',' + str(score) + '\r\n'
