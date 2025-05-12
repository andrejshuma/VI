import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

from dataset_script import dataset  # this will import the dataset on coderunner at courses
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler


def main():
    global dataset

    C = int(input())
    P = int(input())

    ...


main()