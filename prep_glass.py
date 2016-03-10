import os
import csv
import sys
import shutil
import numpy as np
from sklearn.datasets.base import Bunch

ri = []
na = []
mg = []
al = []
si = []
k = []
ca = []
ba = []
fe = []
classtype = []


def get_class_type(t):
    if '1' in t:
        return 0.0
    if '2' in t:
        return 1.0
    if '3' in t:
        return 2.0
    if '4' in t:
        return 3.0
    if '5' in t:
        return 4.0
    if '6' in t:
        return 5.0
    if '7' in t:
        return 6.0


def make_data():
    module_path = os.path.dirname(__file__)
    with open(os.path.join(module_path, 'data', 'glass.csv')) as csv_file:
        data_file = csv.reader(csv_file)
        temp = next(data_file)
        n_samples = int(temp[0])
        n_features = int(temp[1])
        target_names = np.array(temp[2:])
        data = np.empty((n_samples, n_features))
        target = np.empty((n_samples,), dtype=np.int)

        for i, ir in enumerate(data_file):
            data[i] = np.asarray(ir[1:-1], dtype=np.float)
            target[i] = np.asarray(ir[-1], dtype=np.int)

        return Bunch(data=data, target=target,
                     target_names=target_names,
                     feature_names=['refractive index', 'sodium',
                                    'magnesium', 'aluminum', 'silicon', 'potassium',
                                    'calcium', 'barium', 'iron'])


def load_glass_training():
    module_path = os.path.dirname(__file__)
    with open(os.path.join(module_path, 'data', 'glass_train.csv')) as csv_file:
        data_file = csv.reader(csv_file)
        temp = next(data_file)
        n_samples = int(temp[0])
        n_features = int(temp[1])
        target_names = np.array(temp[2:])
        data = np.empty((n_samples, n_features))
        target = np.empty((n_samples,), dtype=np.int)

        for i, ir in enumerate(data_file):
            data[i] = np.asarray(ir[1:-1], dtype=np.float)
            target[i] = np.asarray(ir[-1], dtype=np.int)

        return Bunch(data=data, target=target,
                     target_names=target_names,
                     feature_names=['refractive index', 'sodium',
                                    'magnesium', 'aluminum', 'silicon', 'potassium',
                                    'calcium', 'barium', 'iron'])


def load_glass_test():
    module_path = os.path.dirname(__file__)
    with open(os.path.join(module_path, 'data', 'glass_test.csv')) as csv_file:
        data_file = csv.reader(csv_file)
        temp = next(data_file)
        n_samples = int(temp[0])
        n_features = int(temp[1])
        target_names = np.array(temp[2:])
        data = np.empty((n_samples, n_features))
        target = np.empty((n_samples,), dtype=np.int)

        for i, ir in enumerate(data_file):
            data[i] = np.asarray(ir[1:-1], dtype=np.float)
            target[i] = np.asarray(ir[-1], dtype=np.int)

        return Bunch(data=data, target=target,
                     target_names=target_names,
                     feature_names=['refractive index', 'sodium',
                                    'magnesium', 'aluminum', 'silicon', 'potassium',
                                    'calcium', 'barium', 'iron'])


def count():
    module_path = os.path.dirname(__file__)
    with open(os.path.join(module_path, 'data', 'glass.csv')) as csv_file:
        data_file = csv.reader(csv_file)
        temp = next(data_file)
        n_samples = int(temp[0])
        n_features = int(temp[1])
        target_names = np.array(temp[2:])
        data = np.empty((n_samples, n_features))
        target = np.empty((n_samples,), dtype=np.int)

        for i, ir in enumerate(data_file):
            data[i] = np.asarray(ir[1:-1], dtype=np.float)
            target[i] = np.asarray(ir[-1], dtype=np.int)

        countlast = {}
        countTrain = {}
        for i in target:
            if str(i) in countlast:
                countlast[str(i)] += 1
            else:
                countlast[str(i)] = 0

        for i in target:
            countTrain[str(i)] = int(countlast[str(i)] * 0.75)

        print countlast
