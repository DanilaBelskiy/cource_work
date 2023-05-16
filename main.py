import codecs
import os
import math as m

from data import Data
from hash_table import HashTable

from quick_sort import quick_sort
from binary_tree_search import binary_tree_search
from binary_search import binary_search


#  Reading information from a file
fileObj = codecs.open("table.csv", "r", "utf_8")
text = fileObj.read()
fileObj.close()

text = text.split("\r\n")
for i in range(len(text)):
    text[i] = text[i].split(";")

# Hashtable with ids and names
name_table = HashTable(10)

# Arrays with amounts and costs
amount_arr = []
cost_arr = []

# Arrays with amounts + ids and costs + ids
amount_data_arr = []
cost_data_arr = []

# Array with ids
numbers_arr = []

for i in range(1, len(text)):

    number = int(text[i][0])

    name = text[i][2]
    amount = int(text[i][4])
    price = int(text[i][5])
    cost = int(text[i][6])

    # Protection against non-unique ids
    # If id has been changed program will print it
    if binary_search(numbers_arr, number) > -1:
        print(f"Id {number} for {name} changed to ", end='')
        while binary_search(numbers_arr, number) > -1:
            number = number + 10
        print(number)

    # Protection against incorrectly calculated cost
    if price * amount != cost:
        cost = price * amount

    name_table.add(Data(number, name))

    numbers_arr.append(number)

    amount_arr.append(amount)
    cost_arr.append(cost)

    amount_data_arr.append(Data(number, amount))
    cost_data_arr.append(Data(number, cost))

# Sorting arrays to find max amount and cost
quick_sort(amount_arr, 0, len(amount_arr)-1)
quick_sort(cost_arr, 0, len(cost_arr)-1)

# Max amount and cost
max_amount = amount_arr[0]
max_cost = cost_arr[0]

# Ids of max amount and cost
max_amount_id = binary_tree_search(amount_data_arr, max_amount).key
max_cost_id = binary_tree_search(cost_data_arr, max_cost).key

# Calculating total revenue
total_revenue = 0
for i in cost_arr:
    total_revenue += i

# Making report
if os.path.exists("report.txt"):
  os.remove("report.txt")

report_file = open("report.txt", "a")

report_file.write(f"Total store revenue = {total_revenue}\n")
report_file.write(f"Product sold most times : {name_table.get_value(max_amount_id).value}\n")
report_file.write(f"Product with the highest revenue : {name_table.get_value(max_cost_id).value}\n\n")

report_file.write("ID -- Sales -- Revenue(%) -- Name\n\n")
for i in range(len(amount_data_arr)):
    report_file.write(f"{amount_data_arr[i].key} -- {amount_data_arr[i].value} -- "
                      f"{round(cost_data_arr[i].value * 100 / total_revenue, 2)}% -- "
                      f"{name_table.get_value(amount_data_arr[i].key).value}\n")

report_file.close()
