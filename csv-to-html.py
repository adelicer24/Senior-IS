from prettytable import PrettyTable

# open csv file
a = open("mlb_data/Fielding_Advanced_2018-2023.csv", 'r')
 
# read the csv file
a = a.readlines()
 
# Separating the Headers
l1 = a[0]
l1 = l1.split(',')
 
# headers for table
t = PrettyTable([l1[0],l1[1],l1[2],l1[3],l1[4],l1[5],l1[6],l1[7],l1[8],l1[9],l1[10]])
 
# Adding the data
for i in range(1, len(a)) :
    t.add_row(a[i].split(','))
 
code = t.get_html_string()
html_file = open('fielding2.html', 'w')
html_file = html_file.write(code)