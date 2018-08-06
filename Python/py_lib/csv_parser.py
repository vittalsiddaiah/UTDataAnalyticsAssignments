# Copyright (c) 2018, Vittal Siddaiah
# All rights reserved.

__author__ = "Vittal Siddaiah"
__author_email__ = "vittal.siddaiah@gmail.com"

import math
import re


class csv_parser:
    """
    This is a CSV file parser and a the data set holder
    """

    __fileName__ = ''
    __is_first_header__ = False
    __columns__ = []
    __data__ = []

    def __init__(self, data_from, is_first_row_header=False):
        if isinstance(data_from, str):
            self.__fileName__ = data_from
            self.__data__ = self.read_csv(data_from)
            self.__is_first_header__ = is_first_row_header
            if self.__is_first_header__:
                self.__columns__ = self.__data__[0]
            tempCol = []
            for col in self.__columns__:
                tempCol.append(col.strip())
            self.__columns__ = tempCol
            self.__data__.pop(0)
        elif isinstance(data_from, list):
            self.__data__ = data_from
            counter = 0
            for cols in self.__data__[0]:
                self.__columns__.append("col_" + str(counter))
                counter += 1
        return

    def __del__(self):
        return

    def __iter__(self):
        """
        Returns itself as an iterator
        """
        return self

    def __len__(self):
        return len(self.__data__)


    def __repr__(self):
        return "csv_parser()"



    def __str__(self):
        st = ''
        for header in self.__columns__:
            st += " " + header
        st += "\n"
        for row in self.__data__:
            for col in row:
                st += " " + str(col)
            st += "\n"
        return st

    def __get_col_offset__(self, column_name):
        return self.__columns__.index(column_name)
    #####################################################################

    def fileName(self):
        return self.__fileName__

    #####################################################################

    def columns(self, cols=[]):
        if cols==[]:
            return self.__columns__
        else:
            self.__columns__ = cols

    #####################################################################
    def read_csv(self, csv_file):
        data = []
        with open(csv_file) as fd:
            for count, line in enumerate(fd):
                data.append(list(map(str.strip, re.split(r'\s*\,\s*', line))))
        return data

    #####################################################################
    def unique(self, column_name):
        unique_list = []
        offset = self.__get_col_offset__(column_name)
        for value in self.__data__:
            if value[offset] not in unique_list:
                unique_list.append(value[offset])
        return unique_list

    #####################################################################
    def count_unique(self, column_name):
        finalData = []
        for uCd in self.unique(column_name):
            count = 0
            for data in self.__data__:
                if uCd in data: count += 1
            finalData.append([uCd, count])
        return finalData

    #####################################################################
    def sum(self, column_name='', column_offset=math.nan, is_abs=False):
        sum = 0
        if math.isnan(column_offset): column_offset = self.__get_col_offset__(column_name)
        for row in self.__data__:
            if is_abs:
                sum += abs(row[column_offset])
            else:
                sum += row[column_offset]
        return sum

    #####################################################################
    def insert_pctg(self, column_name='', column_offset=math.nan):
        if math.isnan(column_offset): column_offset = self.__get_col_offset__(column_name)
        sum = self.sum(self.__data__, column_offset=column_offset)
        for data in self.__data__:
            data.append(data[column_offset] / sum)
        column_name = self.__columns__[column_offset]
        self.__columns__.append(column_name + "_Pctg")
        return [self.__data__, column_name + "_Pctg"]

    #####################################################################
    def max(self, column_name='', column_offset=math.nan):
        if math.isnan(column_offset): column_offset = self.__get_col_offset__(column_name)
        max = self.__data__[0][column_offset]
        max_offset = 0
        counter = 0
        for data in self.__data__:
            if data[column_offset] >= max:
                max = data[column_offset]
                max_offset = counter
            counter += 1
        return [max, max_offset]

    #####################################################################

    #####################################################################
    def min(self, column_name='', column_offset=math.nan):
        if math.isnan(column_offset): column_offset = self.__get_col_offset__(column_name)
        min = self.__data__[0][column_offset]
        min_offset = 0
        counter = 0
        for data in self.__data__:
            if data[column_offset] <= min:
                min = data[column_offset]
                min_offset = counter
            counter += 1
        return [min, min_offset]

    #####################################################################
    def diff(self, column_name='', column_offset=math.nan, is_sum_abs=False):
        if math.isnan(column_offset): column_offset = self.__get_col_offset__(column_name)
        diff_array = []
        min = 0
        max = 0
        min_offset = 0
        max_offset = 0
        sum = 0
        for counter in range(len(self.__data__)):
            if counter == 0: continue
            delta = self.__data__[counter][column_offset] - self.__data__[counter - 1][column_offset]
            if counter == 1:
                min = delta
                max = delta
            diff_array.append(delta)
            if delta < min:
                min = delta
                min_offset = counter
            if delta > max:
                max = delta
                max_offset = counter
            counter += 1
            if is_sum_abs:
                sum += abs(delta)
            else:
                sum += delta
        return [diff_array, min, min_offset, max, max_offset, sum]

    #####################################################################
    def row(self, row_id):
        return self.__data__[row_id]

    #####################################################################
    def cell(self, row_id, column_name='', column_offset=math.nan):
        if math.isnan(column_offset): column_offset = self.__get_col_offset__(column_name)
        return self.__data__[row_id][column_offset]

    #####################################################################
    def apply(self, function, column_name='', column_offset=math.nan):
        if (math.isnan(column_offset)): column_offset = self.__get_col_offset__(column_name)
        for data in self.__data__:
            data[column_offset] = function(data[column_offset])
        return

    #####################################################################
