import csv

team_stat_list = ['Year', 'Team', 'Team Abbreviation', 'Wins', 'Losses', 'Winning Percentage', 'Division', 'League', 'Season Outcome', 'Payroll']
tslAbb = ['Yr', 'Tm', 'Abb', 'W', 'L', 'W%', 'Dv', 'Lg', 'SO', 'P']

fielding_stat_list = ['Year', 'Name', 'Age', 'Team', 'Games played', 'Games Started', 'Complete Games', 'Innings played', 
                      'Defensive Chances', 'Putouts', 'Assists', 'Errors', 'Fielding Percentage', 'Total Fielding Runs Above Average', 
                      'Defensive Runs Saved Above Average', 'Range Factor per 9 Innings', 'Range Factor per game', 'Position(s)']
fslAbb = ['Yr', 'Name', 'Age', 'Tm', 'GP', 'GS', 'CG', 'IP', 'DC', 'PO', 'A', 'E', 'FP', 'FRtot', 'DRStot', 'RF/9', 'RF/G', 'Pos']

print("\n Team Season Statistics")
print(tslAbb[:])
with open('mlb_data/Teams_2018-2023.csv', "r") as csvfile:
    reader = csv.reader(csvfile)
    for r in reader:
        if r[1] == 'Atlanta Braves':
            print(r)

print("\n Player Fielding Statistics")
print(fslAbb[:])
with open('mlb_data/Fielding_2018-2023.csv', "r") as csvfile:
    reader = csv.reader(csvfile)
    for r in reader:
        if r[1] == 'Ronald Acuna Jr.':
            print(r)