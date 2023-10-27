from prettytable import PrettyTable

# open csv file
a = open("mlb_data/Awards_2018-2023.csv", 'r')
 
# read the csv file
a = a.readlines()
 
# Separating the Headers
l1 = a[0]
l1 = l1.split(',')
 
# headers for table
t = PrettyTable([l1[0],l1[1],l1[2],l1[3],l1[4],l1[5],l1[6],l1[7],l1[8],l1[9],l1[10],l1[11],l1[12],l1[13],l1[14],l1[15],l1[16],l1[17],l1[18],l1[19]])
 
# Adding the data
for i in range(1, len(a)) :
    t.add_row(a[i].split(','))
 
code = t.get_html_string()
html_file = open('awards.html', 'w')
html_file = html_file.write(code)