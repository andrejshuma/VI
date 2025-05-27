import os

from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier

os.environ['OPENBLAS_NUM_THREADS'] = '1'
#from submission_script import *
from zad1_dataset import dataset
#from zad1_dataset import dataset

# Во оваа верзија користете ги само класите 0 и 1.
# Од податочното множество отстранете ги најмалку важните k карактеристики
# (вредноста k се чита од стандарден влез). Потоа тренирајте втор класификатор со истите параметри како првиот.
# Испечатете точност, прецизност и одзив.
#
# прецизност = TP / (TP + FP)
#
# одзив = TP / (TP + FN)

def remove_classes(dataset):
    return [row for row in dataset if row[-1]==1 or row[-1]==0]


def remove_columns(dataset, to_be_removed):
    new_dataset = []
    for row in dataset:
        new_row = []
        for i in range(len(row)):
            if i not in to_be_removed:
                new_row.append(row[i])
        new_dataset.append(new_row)

    return new_dataset


def remove_least_importances(feature_importances, k):
    dictionary = {idx: val for idx, val in enumerate(feature_importances)}

    sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[1])
    to_be_removed = [item[0] for item in sorted_dictionary[:k]]
    new_dataset = remove_columns(dataset, to_be_removed)
    return new_dataset


def calculate(predictions, test_Y):
    tp, fp, tn, fn = 0, 0, 0, 0
    for true,pred in zip(test_Y, predictions):
        if true == 1:
            if pred == 1:
                tp+=1
            else:
                fn+=1
        else:
            if pred == 0:
                fp+=1
            else:
                tn+=1

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    return precision, recall


if __name__ == '__main__':
    # Vashiot kod tuka
    X = float(input())
    X /= 100
    criterion = input()
    k=int(input())
    dataset = remove_classes(dataset)
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
    feature_importances = classifier.feature_importances_

    dataset =remove_least_importances(feature_importances,k)

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
    
    predictions = classifier.predict(test_X)
    precision,recall = calculate(predictions,test_Y)
    print(precision)
    print(recall)

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    #submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    #submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    #submit_classifier(classifier)

    # submit na encoderot
    #submit_encoder(encoder)
