#!/usr/bin/env python3
import sys
import csv
import pandas


# Reading a CSV file with reader object, return a list generator (exclude header)
def read_csv_to_list(file):
    with open(file, mode='r', encoding='UTF-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = next(csv_reader)
        for row in csv_reader:
            yield(row)


# Reading a CSV file with DictReader object, return a dictionary generator
def read_csv_to_dictionary(file):
    with open(file, mode='r', encoding='UTF-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            yield(row)


# Reading a CSV file with Pandas, return a dataframe
def read_csv_to_dataframe(file):
    return pandas.read_csv(file)


if __name__ == "__main__":

    if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
        for l in read_csv_to_dictionary(sys.argv[1]):
            print(l)
    else:
        print("Add .csv file as command line argument")




