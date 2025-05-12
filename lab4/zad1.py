import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
#from zad1_dataset import dataset


if __name__ == '__main__':
    # Vashiot kod tuka
    X = float(input())
    X /= 100
    criterion = input()

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[int(len(dataset) * (1.0 - X)):]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]
    train_X = encoder.transform(train_X)

    test_set = dataset[:int(len(dataset) * (1.0 - X))]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]
    test_X = encoder.transform(test_X)

    classifier = DecisionTreeClassifier(criterion=criterion, random_state=0)
    classifier.fit(train_X, train_Y)
    accuracy = classifier.score(test_X, test_Y)
    feature_importances = classifier.feature_importances_

    print(f"Depth: {classifier.get_depth()}")
    print(f"Number of leaves: {classifier.get_n_leaves()}")
    print(f"Accuracy: {accuracy}")
    featire_importances = classifier.feature_importances_
    max_idx = max(list(featire_importances))
    min_idx = min(list(featire_importances))

    for i, importance in enumerate(featire_importances):
        if importance == max_idx:
            print("Most important feature: " + str(i))
        if importance == min_idx:
            print("Least important feature: " + str(i))

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    submit_classifier(classifier)

    # submit na encoderot
    submit_encoder(encoder)
