import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

dataset = [
    [14.23, 1.71, 2.43, 15.6, 127, 2.8, 3.06, .28, 2.29, 5.64, 1.04, 3.92, 1065, 0],
    [13.2, 1.78, 2.14, 11.2, 100, 2.65, 2.76, .26, 1.28, 4.38, 1.05, 3.4, 1050, 0],
    [13.16, 2.36, 2.67, 18.6, 101, 2.8, 3.24, .3, 2.81, 5.68, 1.03, 3.17, 1185, 0],
    [14.37, 1.95, 2.5, 16.8, 113, 3.85, 3.49, .24, 2.18, 7.8, .86, 3.45, 1480, 0],
    [13.24, 2.59, 2.87, 21, 118, 2.8, 2.69, .39, 1.82, 4.32, 1.04, 2.93, 735, 0],
    [14.2, 1.76, 2.45, 15.2, 112, 3.27, 3.39, .34, 1.97, 6.75, 1.05, 2.85, 1450, 0],
    [14.39, 1.87, 2.45, 14.6, 96, 2.5, 2.52, .3, 1.98, 5.25, 1.02, 3.58, 1290, 0],
    [14.06, 2.15, 2.61, 17.6, 121, 2.6, 2.51, .31, 1.25, 5.05, 1.06, 3.58, 1295, 0],
    [14.83, 1.64, 2.17, 14, 97, 2.8, 2.98, .29, 1.98, 5.2, 1.08, 2.85, 1045, 0],
    [13.86, 1.35, 2.27, 16, 98, 2.98, 3.15, .22, 1.85, 7.22, 1.01, 3.55, 1045, 0],
    [14.1, 2.16, 2.3, 18, 105, 2.95, 3.32, .22, 2.38, 5.75, 1.25, 3.17, 1510, 0],
    [14.12, 1.48, 2.32, 16.8, 95, 2.2, 2.43, .26, 1.57, 5, 1.17, 2.82, 1280, 0],
    [13.75, 1.73, 2.41, 16, 89, 2.6, 2.76, .29, 1.81, 5.6, 1.15, 2.9, 1320, 0],
    [14.75, 1.73, 2.39, 11.4, 91, 3.1, 3.69, .43, 2.81, 5.4, 1.25, 2.73, 1150, 0],
    [14.38, 1.87, 2.38, 12, 102, 3.3, 3.64, .29, 2.96, 7.5, 1.2, 3, 1547, 0],
    [13.63, 1.81, 2.7, 17.2, 112, 2.85, 2.91, .3, 1.46, 7.3, 1.28, 2.88, 1310, 0],
    [14.3, 1.92, 2.72, 20, 120, 2.8, 3.14, .33, 1.97, 6.2, 1.07, 2.65, 1280, 0],
    [13.83, 1.57, 2.62, 20, 115, 2.95, 3.4, .4, 1.72, 6.6, 1.13, 2.57, 1130, 0],
    [14.19, 1.59, 2.48, 16.5, 108, 3.3, 3.93, .32, 1.86, 8.7, 1.23, 2.82, 1680, 0],
    [13.64, 3.1, 2.56, 15.2, 116, 2.7, 3.03, .17, 1.66, 5.1, .96, 3.36, 845, 0],
    [12.37, .94, 1.36, 10.6, 88, 1.98, .57, .28, .42, 1.95, 1.05, 1.82, 520, 1],
    [12.33, 1.1, 2.28, 16, 101, 2.05, 1.09, .63, .41, 3.27, 1.25, 1.67, 680, 1],
    [12.64, 1.36, 2.02, 16.8, 100, 2.02, 1.41, .53, .62, 5.75, .98, 1.59, 450, 1],
    [13.67, 1.25, 1.92, 18, 94, 2.1, 1.79, .32, .73, 3.8, 1.23, 2.46, 630, 1],
    [12.37, 1.13, 2.16, 19, 87, 3.5, 3.1, .19, 1.87, 4.45, 1.22, 2.87, 420, 1],
    [12.17, 1.45, 2.53, 19, 104, 1.89, 1.75, .45, 1.03, 2.95, 1.45, 2.23, 355, 1],
    [12.37, 1.21, 2.56, 18.1, 98, 2.42, 2.65, .37, 2.08, 4.6, 1.19, 2.3, 678, 1],
    [13.11, 1.01, 1.7, 15, 78, 2.98, 3.18, .26, 2.28, 5.3, 1.12, 3.18, 502, 1],
    [12.37, 1.17, 1.92, 19.6, 78, 2.11, 2, .27, 1.04, 4.68, 1.12, 3.48, 510, 1],
    [13.34, .94, 2.36, 17, 110, 2.53, 1.3, .55, .42, 3.17, 1.02, 1.93, 750, 1],
    [12.21, 1.19, 1.75, 16.8, 151, 1.85, 1.28, .14, 2.5, 2.85, 1.28, 3.07, 718, 1],
    [12.29, 1.61, 2.21, 20.4, 103, 1.1, 1.02, .37, 1.46, 3.05, .906, 1.82, 870, 1],
    [13.86, 1.51, 2.67, 25, 86, 2.95, 2.86, .21, 1.87, 3.38, 1.36, 3.16, 410, 1],
    [13.49, 1.66, 2.24, 24, 87, 1.88, 1.84, .27, 1.03, 3.74, .98, 2.78, 472, 1],
    [12.99, 1.67, 2.6, 30, 139, 3.3, 2.89, .21, 1.96, 3.35, 1.31, 3.5, 985, 1],
    [11.96, 1.09, 2.3, 21, 101, 3.38, 2.14, .13, 1.65, 3.21, .99, 3.13, 886, 1],
    [11.66, 1.88, 1.92, 16, 97, 1.61, 1.57, .34, 1.15, 3.8, 1.23, 2.14, 428, 1],
    [13.03, .9, 1.71, 16, 86, 1.95, 2.03, .24, 1.46, 4.6, 1.19, 2.48, 392, 1],
    [11.84, 2.89, 2.23, 18, 112, 1.72, 1.32, .43, .95, 2.65, .96, 2.52, 500, 1],
    [12.33, .99, 1.95, 14.8, 136, 1.9, 1.85, .35, 2.76, 3.4, 1.06, 2.31, 750, 1],
    [12.7, 3.87, 2.4, 23, 101, 2.83, 2.55, .43, 1.95, 2.57, 1.19, 3.13, 463, 1],
    [12, .92, 2, 19, 86, 2.42, 2.26, .3, 1.43, 2.5, 1.38, 3.12, 278, 1],
    [12.72, 1.81, 2.2, 18.8, 86, 2.2, 2.53, .26, 1.77, 3.9, 1.16, 3.14, 714, 1]
]


def split_data(dataset, X):
    set_0 = [row for row in dataset if row[-1]==0]
    set_1 = [row for row in dataset if row[-1]==1]

    train_set = set_0[:int(len(set_0) * X/100)] + set_1[:int(len(set_1) * X/100)]
    test_set = set_0[int(len(set_0) * X/100):] + set_1[int(len(set_1) * X/100):]

    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]

    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]

    return train_X, train_Y, test_X, test_Y


def recall_final_model(max_classifier, bad_models, test_X, test_Y):
    tp,fp,tn,fn = 0,0,0,0
    for X, Y in zip(test_X, test_Y):
        votes_0 = 0
        votes_1 = 0
        max_pred = max_classifier.predict([X])[0]

        if max_pred == 1:
            votes_1 += 2
        else:
            votes_0 += 2

        for model in bad_models:
            pred = model.predict([X])[0]
            if pred == 1:
                votes_1 += 1
            else:
                votes_0 += 1

        voted_class = 1 if votes_1 > votes_0 else 0

        if Y ==1:
            if voted_class == 1:
                tp += 1
            else:
                fn+=1
        else:
            if voted_class == 0:
                fp += 1
            else:
                tn+=1
    return tp / (tp + fn) if (tp + fn) > 0 else 0

if __name__ == '__main__':
    X = int(input())
    train_X,train_Y,test_X,test_Y = split_data(dataset,X)

    naive_classifier = GaussianNB()
    naive_classifier.fit(train_X, train_Y)
    tree_classifier = DecisionTreeClassifier(criterion="entropy",random_state=0)
    tree_classifier.fit(train_X, train_Y)
    forest_classifier = RandomForestClassifier(n_estimators=4,criterion="entropy",random_state=0)
    forest_classifier.fit(train_X, train_Y)
    neural_classifier = MLPClassifier(10,activation="relu",learning_rate_init=0.001,random_state=0)
    neural_classifier.fit(train_X, train_Y)


    acc1 = naive_classifier.score(test_X, test_Y)
    acc2 = tree_classifier.score(test_X, test_Y)
    acc3 = forest_classifier.score(test_X, test_Y)
    acc4 = neural_classifier.score(test_X, test_Y)

    models = [naive_classifier,tree_classifier,forest_classifier,neural_classifier]
    accuracies = [acc1, acc2, acc3, acc4]

    max_acc = 0
    max_classifier = None

    for model,acc in zip(models,accuracies):
        if acc>max_acc:
            max_acc = acc
            max_classifier = model

    bad_models = []
    if max_classifier == naive_classifier:
        print("Najgolema tocnost ima klasifikatorot Naive Bayes")
        bad_models = [tree_classifier,forest_classifier,neural_classifier]
    elif max_classifier == tree_classifier:
        print("Najgolema tocnost ima klasifikatorot Decision Tree")
        bad_models = [naive_classifier,forest_classifier,neural_classifier]
    elif max_classifier == forest_classifier:
        print("Najgolema tocnost ima klasifikatorot Random Forest")
        bad_models = [tree_classifier,naive_classifier,neural_classifier]
    else:
        print("Najgolema tocnost ima klasifikatorot MLP")
        bad_models = [tree_classifier,forest_classifier,naive_classifier]

    recall = recall_final_model(max_classifier,bad_models,test_X,test_Y)

    print(f"Odzivot na kolekcijata so klasifikatori e {recall}")
