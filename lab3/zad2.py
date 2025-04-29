import os
from sklearn.naive_bayes import GaussianNB
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset

def convert(dataset):
    dataset_v2=[]
    for row in dataset:
        row2=[float(el) for el in row]
        dataset_v2.append(row2)
    return dataset_v2

if __name__ == '__main__':
    dataset=convert(dataset)

    train_set= dataset[:int(len(dataset) * 0.85)]
    test_set= dataset[int(len(dataset) * 0.85):]

    train_X=[row[:-1] for row in train_set]
    train_Y=[row[-1] for row in train_set]

    test_X=[row[:-1] for row in test_set]
    test_Y=[row[-1] for row in test_set]

    classifier=GaussianNB()
    classifier.fit(train_X,train_Y)

    acc=classifier.score(test_X,test_Y)

    entry=[float(el) for el in input().split(' ')]

    print(acc)
    print(int(classifier.predict([entry])[0]))
    print(classifier.predict_proba([entry]))


    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii
    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    submit_classifier(classifier)

# povtoren import na kraj / ne ja otstranuvajte ovaa linija