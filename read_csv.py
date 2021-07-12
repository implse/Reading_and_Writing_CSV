import sys
import csv
import pandas

# csv file provided as a command-line argument 
first_arg = sys.argv[1]


# Reading a CSV file with reader object
with open(first_arg, mode='r') as csv_file:
    # Delimiters (.), (\t), (:), (;)
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        print(row)



# Reading a CSV file into an ordered dictionnary with DictReader object
with open(first_arg, mode='r') as csv_file:

    csv_reader = csv.DictReader(csv_file)
 
    for row in csv_reader:
        print(row)


# Reading CSV file into a pandas DataFrame 
import pandas
df = pandas.read_csv(sys.argv[1])
print(df)

