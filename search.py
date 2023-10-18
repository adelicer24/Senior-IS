import csv

team_stat_list = ['Year', 'Team Name', 'Team Abbreviation', 'Wins', 'Losses', 'Winning Percentage', 'Division', 'League', 'Season Outcome', 'Payroll']
tslAbb = ['Yr', 'Tm', 'Abb', 'W', 'L', 'W%', 'Dv', 'Lg', 'SO', 'P']

fielding_stat_list = ['Year', 'Name', 'Age', 'Team', 'Games played', 'Games Started', 'Complete Games', 'Innings played', 
                      'Defensive Chances', 'Putouts', 'Assists', 'Errors', 'Fielding Percentage', 'Total Fielding Runs Above Average', 
                      'Defensive Runs Saved Above Average', 'Range Factor per 9 Innings', 'Range Factor per game', 'Position(s)']
fslAbb = ['Yr', 'Name', 'Age', 'Tm', 'GP', 'GS', 'CG', 'IP', 'DC', 'PO', 'A', 'E', 'FP', 'FRtot', 'DRStot', 'RF/9', 'RF/G', 'Pos']

pitching_stat_list = ['Year', 'Name', 'Age', 'Team', 'Wins', 'Losses', 'Winning Percentage', 'Earned Runs Average', 'Games played', 
                      'Games Started', 'Games Finished', 'Complete Games', 'SHO', 'Saves', 'Innings played', 'Hits allowed', 'Runs allowed', 
                      'Earned Runs', 'Home Runs Allowed', 'Bases on Balls/Walks', 'Strikeouts', 'Wild Pitches', 'Batters Faced', 
                      'Earned Runs Average Plus', 'Fielding Independent Pitching', 'Walks and Hits Per Inning Pitched', 'Hits per 9 innings', 
                      'Home Runs per 9 Innings', 'Base on Balls per 9 Innings', 'Strikeouts per 9 Innings', 'Strikeout to Walk Ratio', 
                      'Wins Aabove Replacement', 'Runs Above Replacement', 'Batted Average Against', 'On-Base Percentage Against', 
                      'Slugging Percentage', 'On-base Percentage Plus Slugging Percentage', 'Batting Average on Balls in Play', 
                      'Plays Included in Win Probability Added', 'Win Probability Added by Pitcher', 'Win Probability Added', 
                      'Win Porbability Subtracted', 'Average Leverage Index', 'Situational Wins', 'Home Run Percentage', 'Strikeout Percentage', 
                      'Base on Balls Percentage', 'Extra Base Hit Percentage']
pslAbb = ['Yr', 'Name', 'Age', 'Tm', 'W', 'L', 'W%', 'ERA', 'GP', 'GS', 'GF', 'CG', 'SHO', 'SV', 'IP', 'HA', 'RA', 'ER', 'HRA', 'BB/W', 'SO', 
          'WP', 'BF', 'ERA+', 'FIP', 'WHIP', 'H9', 'HR9', 'BB9', 'SO9', 'SO/W', 'WAR', 'RAR', 'BAA', 'OBPA', 'SLGA', 'OPSA', 'BAbipA', 
          'Plays', 'WPA', 'WPA+', 'WPA-', 'aLI', 'WPA/LI', 'HR%', 'SO%', 'BB%', 'XBH%']

batting_stat_list = []
bslAbb = []


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

print("\n Player Pitching Statistics")
print(pslAbb[:])
with open('mlb_data/Pitching_2018-2023.csv', "r") as csvfile:
    reader = csv.reader(csvfile)
    for r in reader:
        if r[1] == 'Max Fried':
            print(r)