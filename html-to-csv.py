import pandas as pd

# 1. Read all HTML tables from a given URL
tables = pd.read_html('https://www.baseball-reference.com/leagues/majors/2023-standard-batting.shtml')

# 2. Write first table, for example, to the CSV file
tables[0].to_csv('my_file.csv')