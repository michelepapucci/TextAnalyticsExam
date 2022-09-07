import torch


def gender_to_int(row):
    if row['Gender'] == 'M':
        row['Gender'] = 0
    else:
        row['Gender'] = 1
    return row


def gender_to_int_tensor(row):
    if row['Gender'] == 'M':
        row['Gender'] = torch.tensor(0, dtype=torch.int64)
    else:
        row['Gender'] = torch.tensor(1, dtype=torch.int64)
    return row


def topic_to_int(row):
    topics = ['ANIME', 'AUTO-MOTO', 'BIKES', 'CELEBRITIES', 'ENTERTAINMENT', 'MEDICINE-AESTHETICS', 'METAL-DETECTING',
              'NATURE', 'SMOKE', 'SPORTS', 'TECHNOLOGY']
    if row['Topic'] in topics:
        row['Topic'] = topics.index(row['Topic'])
    else:
        print("Error!")
    return row


def topic_to_int_tensor(row):
    topics = ['ANIME', 'AUTO-MOTO', 'BIKES', 'CELEBRITIES', 'ENTERTAINMENT', 'MEDICINE-AESTHETICS', 'METAL-DETECTING',
              'NATURE', 'SMOKE', 'SPORTS', 'TECHNOLOGY']
    if row['Topic'] in topics:
        row['Topic'] = torch.tensor(topics.index(row['Topic']), torch.int64)
    else:
        print("Error!")
    return row


def age_range_to_int(row):
    ages = ["0-19", "20-29", "30-39", "40-49", "50-100"]
    if row['Age'] in ages:
        row['Age'] = ages.index(row['Age'])
    else:
        print("Porcodio")
    return row


def age_range_to_int_tensor(row):
    ages = ["0-19", "20-29", "30-39", "40-49", "50-100"]
    if row['Age'] in ages:
        row['Age'] = torch.tensor(ages.index(row['Age']), torch.int64)
    else:
        print("Porcodio")
    return row
