import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
#from zad1_dataset import dataset
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
import numpy as np

if __name__ == '__main__':
# Vashiot kod tuka
    input()
    encoder=OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set=dataset[int(len(dataset)*0.1):]
    test_set=dataset[:int(len(dataset)*0.1)]

    train_X=[row[:-1] for row in train_set]
    train_Y=[row[-1] for row in train_set]

    test_X=[row[:-1] for row in test_set]
    test_Y=[row[-1] for row in test_set]

    train_X=encoder.transform(train_X)
    test_X=encoder.transform(test_X)

    classifier=CategoricalNB()
    classifier.fit(train_X,train_Y)


    accuracy=0
    for i in range(len(test_set)):
        predicted_class=classifier.predict([test_X[i]])[0]
        true_class=test_Y[i]
        if true_class==predicted_class:
            accuracy+=1

    accuracy= accuracy / len(test_set)

    accuracy2 = 0
    for i in range(len(test_set)):
        probas = classifier.predict_proba([test_X[i]])[0]

        probas_with_classes = [(proba, cls) for proba, cls in zip(probas, classifier.classes_)]

        probas_with_classes.sort()

        if test_Y[i] in [cls for _, cls in probas_with_classes[-2:]]:
            accuracy2 += 1

    accuracy2 = accuracy2 / len(test_set)

    print(f"Tochnost: {accuracy}")
    print(f"Tochnost (vtor pristap): {accuracy2}")

    entry = [el for el in input().split(' ')]
    entry = encoder.transform([entry])

    probas_entry = classifier.predict_proba(entry)[0]
    if np.max(probas_entry) > 0.5:
        predicted_class = classifier.classes_[np.argmax(probas_entry)]
    else:
        predicted_class = "UNKNOWN"


    print(f"Predvidena klasa: {classifier.predict(entry)[0]}")
    print(f"Predvidena klasa (vtor pristap): {predicted_class}")


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