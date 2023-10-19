import csv

team_stat_list = ['Year', 'Team Name', 'Team Abbreviation', 'Wins', 'Losses', 'Winning Percentage', 'Division', 'League', 'Division Rank', 'Season Outcome', 'Payroll']
tslAbb = ['Yr', 'Tm', 'Abb', 'W', 'L', 'W%', 'Dv', 'Lg', 'DR', 'SO', 'PR']

print("\n Team Season Statistics")
print(tslAbb[:])
with open('mlb_data/Teams_2018-2023.csv', "r") as csvfile:
    reader = csv.reader(csvfile)
    for r in reader:
        if r[9] == 'World Series Champion':
            print(r)