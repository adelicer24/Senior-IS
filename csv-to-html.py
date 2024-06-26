# Import PrettyTable library to create an html table using a csv file
from prettytable import PrettyTable

# Open given csv file
a = open("my_file.csv", 'r')
 
# Read the given csv file
a = a.readlines()
 
# Separate the csv file headers
l1 = a[0]
l1 = l1.split(',')
 
# Choose the headers to include from table
t = PrettyTable([l1[0],l1[1],l1[2],l1[3],l1[4],l1[5]])
 
# Adding the table data
for i in range(1, len(a)) :
    t.add_row(a[i].split(','))

# Get string representation of table
code = t.get_html_string()

# Open a new HTML file to write into
html_file = open('my_table.html', 'w')

# Write the table into the html file
html_file = html_file.write(code)