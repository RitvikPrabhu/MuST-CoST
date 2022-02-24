# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold(x, y, n):
    sum = 0
    for i in range(n):
        for j in range(i + 1, n):
            sum += (abs(x[i] - x[j]) + abs(y[i] - y[j]))
    return sum


# TOFILL

if __name__ == '__main__':
    param = [
        ([2, 4, 6, 6, 8, 11, 12, 13, 14, 19, 20, 22, 24, 28, 29, 30, 32, 35, 37, 44, 48, 49, 51, 51, 56, 59, 59, 62, 65, 68, 68, 68, 72, 75, 77, 78, 89, 89, 91, 93, 95, 99], [
         6, 19, 19, 22, 25, 27, 31, 33, 34, 35, 37, 38, 38, 44, 46, 50, 51, 55, 58, 58, 64, 64, 64, 64, 65, 66, 66, 66, 67, 70, 75, 78, 79, 81, 81, 81, 82, 84, 84, 86, 94, 96], 37,),
        ([16, 76, 2, 42, -24, -82, 68, -2, 98, -42, -72, 28, -22, -52, 28, -38, 36, 66, 84, 64, -28, 86, 52, 84, -98, -30],
         [-34, 92, -24, -62, 28, 72, -10, 10, 8, 90, -72, -24, 50, -46, 52, 58, 68, -62, -64, -78, -12, 24, 62, -30, 62, -60], 24,),
        ([0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1], 5,),
        ([61, 37, 57, 99, 22, 72, 38, 85, 23, 85, 15, 4, 49, 9, 15, 25, 7, 63, 79, 6, 85, 30, 12, 34, 38, 6, 59, 62, 59, 34, 72, 97, 70, 44, 95, 58, 99], [
         72, 41, 77, 62, 78, 36, 75, 28, 91, 39, 32, 56, 60, 64, 21, 15, 80, 85, 28, 22, 53, 58, 69, 62, 60, 48, 66, 91, 38, 66, 54, 5, 24, 1, 49, 71, 49], 26,),
        ([-96, -86, -82, -72, -72, -64, -62, -60, -56, -56, -56, -54, -52, -40, -36, -30, -10, 10, 18, 26, 28, 56, 56, 56, 64, 90, 92, 94],
         [-98, -98, -96, -96, -82, -80, -80, -68, -62, -60, -46, -38, -26, -26, -20, -18, 16, 22, 24, 26, 34, 46, 52, 52, 74, 76, 90, 92], 26,),
        ([1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 0, 1, 1], 3,),
        ([6, 10, 24, 25, 31, 41, 43, 45, 47, 65, 67, 90], [
         4, 7, 11, 19, 21, 39, 57, 80, 84, 93, 94, 97], 10,),
        ([-74, 92, 34, 56, -54, -98, -76, -34, 16, 32, -4, -16, 22, 90, -52, -90, -60, 70, -40, 78, 96, -68, 78, -56, -94],
         [14, 20, 24, -92, 58, 12, 78, 78, -90, 96, -44, 36, 30, -46, -30, -80, 26, -2, 26, 28, -16, -50, -2, -36, -8], 21,),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 23,),
        ([20, 32], [23, 50], 1,)
    ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success += 1
    print("#Results: %i, %i" % (n_success, len(param)))
