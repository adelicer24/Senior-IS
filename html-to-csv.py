# Import pandas library to use its read_html funcntion
import pandas as pd

# Read all HTML tables from given URL
tables = pd.read_html('https://www.baseball-reference.com/leagues/majors/2023-standard-batting.shtml')

# Write HTML table to a CSV file
tables[0].to_csv('my_file.csv')