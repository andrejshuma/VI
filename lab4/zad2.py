import os

from sklearn.ensemble import RandomForestClassifier

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
#from zad2_dataset import dataset


def remove_column(dataset, col_index):
    new_dataset = []
    for row in dataset:
        new_dataset.append([row[i] for i in range(len(row)) if i!=col_index])
    return new_dataset


if __name__ == '__main__':
    # Vashiot kod tuka
    col_index = int(input())
    num_trees = int(input())
    criterion = input()
    entry_line = input().split(" ")
    entry = []

    for i in range(len(entry_line)):
        if i != col_index:
            entry.append(int(entry_line[i]))

    dataset = remove_column(dataset, col_index)

    train_set = dataset[:int(len(dataset)*0.85)]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]

    test_set = dataset[int(len(dataset) * 0.85):]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]

    classifier = RandomForestClassifier(n_estimators=num_trees,criterion=criterion,random_state=0)
    classifier.fit(train_X, train_Y)
    accuracy = classifier.score(test_X, test_Y)

    print(f"Accuracy: {accuracy}")
    print(classifier.predict([entry])[0])
    print(classifier.predict_proba([entry])[0])

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo
    # i klasifikatorot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    submit_classifier(classifier)
