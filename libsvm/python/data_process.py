#!/usr/bin/env python

from __future__ import print_function
from array import array
import sys

try:
	import scipy
	from scipy import sparse
except:
	scipy = None
	sparse = None


__all__ = ['svm_data_process']


def svm_data_process(data_file_name, return_scipy=False):
    """
    svm_read_problem(data_file_name, return_scipy=False) -> [y, x], y: list, x: list of dictionary
    svm_read_problem(data_file_name, return_scipy=True)  -> [y, x], y: ndarray, x: csr_matrix

    Read LIBSVM-format data from data_file_name and return labels y
    and data instances x.
    """
    if scipy != None and return_scipy:
        prob_y = array('d')
        prob_x = array('d')
        row_ptr = array('l', [0])
        col_idx = array('l')
    else:
        prob_y = []
        prob_x = []
        row_ptr = [0]
        col_idx = []
    indx_start = 1
    k = 0
    for i, line in enumerate(open(data_file_name)):
        # In case an instance with all zero features
        line = line.split(",")
        if len(line) == 1: line += ['']
        label = line[len(line) - 1]
        features = line[:len(line) - 1]
        if features[0] == "M":
            features[0] = -1
        elif features[0] == "F":
            features[0] = 0
        elif features[0] == "I":
            features[0] = 1
        prob_y.append(float(label))
        if scipy != None and return_scipy:
            nz = 0
            for e in features.split():
                ind, val = e.split(":")
                if ind == '0':
                    indx_start = 0
                val = float(val)
                if val != 0:
                    col_idx.append(int(ind)-indx_start)
                    prob_x.append(val)
                    nz += 1
            row_ptr.append(row_ptr[-1]+nz)
        else:
            xi = {}
            ind = 1
            if int(label) > 9:
                z = "+1"
            else:
                z = "-1"
            for e in features:
                val = e
                xi[int(ind)] = float(val)
                z = z + " " + str(ind) + ":" + str(float(val))
                ind = ind + 1
            if k >= 3133:
                print(z) 
            prob_x += [xi]
        k = k + 1
    if scipy != None and return_scipy:
        prob_y = scipy.frombuffer(prob_y, dtype='d')
        prob_x = scipy.frombuffer(prob_x, dtype='d')
        col_idx = scipy.frombuffer(col_idx, dtype='l')
        row_ptr = scipy.frombuffer(row_ptr, dtype='l')
        prob_x = sparse.csr_matrix((prob_x, col_idx, row_ptr))
    return (prob_y, prob_x)
