import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
#from submission_script import *
from zad1_dataset import dataset
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB

if __name__ == '__main__':
# Vashiot kod tuka

    encoder=OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set=dataset[:int(len(dataset)*0.75)]
    test_set=dataset[int(len(dataset)*0.75):]

    train_X=[row[:-1] for row in train_set]
    train_Y=[row[-1] for row in train_set]

    test_X=[row[:-1] for row in test_set]
    test_Y=[row[-1] for row in test_set]

    train_X=encoder.transform(train_X)
    test_X=encoder.transform(test_X)

    classifier=CategoricalNB()
    classifier.fit(train_X,train_Y)

    accuracyEasy = classifier.score(test_X,test_Y)

    # accuracy=0
    # for i in range(len(test_set)):
    #     predicted_class=classifier.predict([test_X[i]])[0]
    #     true_class=test_Y[i]
    #     if true_class==predicted_class:
    #         accuracy+=1
    #
    # accuracy= accuracy / len(test_set)

    entry=[el for el in input().split(' ')]
    entry=encoder.transform([entry])

    print(accuracyEasy)
    print(classifier.predict(entry)[0])
    print(classifier.predict_proba(entry))

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