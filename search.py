import csv

team_stat_list = ['Year', 'Team Name', 'Team Abbreviation', 'Wins', 'Losses', 'Winning Percentage', 'Division', 'League', 'Division Rank', 'Season Outcome', 'Payroll']
tslAbb = ['Yr', 'Tm', 'Abb', 'W', 'L', 'W%', 'Dv', 'Lg', 'DvR', 'SO', 'P']

fielding_stat_list = ['Year', 'Name', 'Age', 'Team', 'Games played', 'Games Started', 'Complete Games', 'Innings played', 
                      'Defensive Chances', 'Putouts', 'Assists', 'Errors', 'Fielding Percentage', 'Total Fielding Runs Above Average', 
                      'Defensive Runs Saved Above Average', 'Range Factor per 9 Innings', 'Range Factor per game', 'Position(s)']
fslAbb = ['Yr', 'Nm', 'Age', 'Tm', 'GP', 'GS', 'CG', 'IP', 'DC', 'PO', 'A', 'E', 'FP', 'FRtot', 'DRStot', 'RF/9', 'RF/G', 'Pos']

pitching_stat_list = ['Year', 'Name', 'Age', 'Team', 'Wins', 'Losses', 'Winning Percentage', 'Earned Runs Average', 'Games played', 
                      'Games Started', 'Games Finished', 'Complete Games', 'Shutouts', 'Saves', 'Innings played', 'Hits allowed', 'Runs allowed', 
                      'Earned Runs', 'Home Runs Allowed', 'Bases on Balls/Walks', 'Strikeouts', 'Wild Pitches', 'Batters Faced', 
                      'Earned Runs Average Plus', 'Fielding Independent Pitching', 'Walks and Hits Per Inning Pitched', 'Hits per 9 innings', 
                      'Home Runs per 9 Innings', 'Base on Balls per 9 Innings', 'Strikeouts per 9 Innings', 'Strikeout to Walk Ratio', 
                      'Wins Above Replacement', 'Runs Above Replacement', 'Batted Average Against', 'On-Base Percentage Against', 
                      'Slugging Percentage Against', 'On-base Percentage Plus Slugging Percentage Against', 'Batted Average on Balls in Play Against', 
                      'Plays Included in Win Probability Added', 'Win Probability Added by Pitcher', 'Win Probability Added', 
                      'Win Porbability Subtracted', 'Average Leverage Index', 'Situational Wins', 'Home Run Percentage', 'Strikeout Percentage', 
                      'Base on Balls Percentage', 'Extra Base Hit Percentage']
pslAbb = ['Yr', 'Nm', 'Age', 'Tm', 'W', 'L', 'W%', 'ERA', 'GP', 'GS', 'GF', 'CG', 'SHO', 'SV', 'IP', 'HA', 'RA', 'ER', 'HRA', 'BB/W', 'SO', 
          'WP', 'BF', 'ERA+', 'FIP', 'WHIP', 'H9', 'HR9', 'BB9', 'SO9', 'SO/W', 'WAR', 'RAR', 'BAA', 'OBPA', 'SLGA', 'OPSA', 'BAbipA', 
          'P', 'WPA', 'WPA+', 'WPA-', 'aLI', 'WPA/LI', 'HR%', 'SO%', 'BB%', 'XBH%']

batting_stat_list = ['Year', 'Name', 'Age', 'Team', 'Games played', 'Plate Appearances', 'At Bats', 'Runs', 'Hits', 'Doubles', 'Triples', 
                     'Home Runs', 'Runs Batted In', 'Stolen Bases', 'Caught Stealing', 'Base on Balls/Walks', 'Strikeouts', 'Batting Average', 
                     'On-Base Percentage', 'Slugging Percentage', 'On-base Percentage Plus Slugging Percentage', 
                     'On-base Percentage Plus Slugging Percentage Plus', 'Total Bases', 'Position(s)', 'Outs', 'Runs Created', 
                     'Runs Created per game', 'Runs Above Average', 'Runs Above Replacement', 'Wins Above Replacement', 'Offensive Wins Above Replacement', 
                     'Defensive Wins Aabove Replacement', 'Offensive Runs Above Replacement', 'Plays', 'Win Probability Added by Offensive Player', 
                     'Win Probability Added', 'Win Probability Subtracted', 'Average Leverage Index', 'Situational Wins', 'Player offensive contributions (rOBA)', 
                     'Batting Average on Balls In Play', 'Isolated Power', 'Home Run Percentage', 'Strike Out Percentage', 'Base On Balls Percentage', 
                     'Run Scoring Percentage', 'Stolen Base Percentage', 'Extra Base Hit Percentage', 'Strikeouts per Walk', 'At Bats per Strikeout', 
                     'At Bats per Home Run', 'At Bat Run Batted In', 'Balls In Play Percentage', 'Line Drive Percentage']
bslAbb = ['Yr', 'Nm', 'Age', 'Tm', 'GP', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'SO', 'BA', 'OBP', 'SLG', 'OPS', 'OPS+', 
          'TB', 'Pos', 'O', 'RC', 'RC/G', 'RAA', 'RAR', 'WAR', 'oWAR', 'dWAR', 'oRAR', 'P', 'WPA', 'WPA+', 'WPA-', 'aLI', 'WPA/LI', 'rOBA', 'BAbip', 
          'ISO', 'HR%', 'SO%', 'BB%', 'RS%', 'SB%', 'XBH%', 'SO/W', 'AB/SO', 'AB/HR', 'AB/RBI', 'IP%', 'LD%']

player_award_list =['Year', 'ALCS MVP', 'NLCS MVP', 'World Series MVP', 'AL MVP Award', 'NL MVP Award', 'AL Cy Young Award', 'NL Cy Young Award', 
                    'AL Hank Aaron Award', 'NL Hank Aaron Award', 'Babe Ruth Award', 'Edgar Martinez Award', 'AL Batting Champion', 'NL Batting Champion', 
                    'AL Pitching ERA Chamption', 'NL Pitching ERA Champion', 'AL Rookie of the Year', 'NL Rookie of the Year', 'AL Comeback Player of the Year', 
                    'NL Comeback Player of the Year']
palAbb = ['Year', 'ALCS MVP', 'NLCS MVP', 'World Series MVP', 'AL MVP Award', 'NL MVP Award', 'AL Cy Young Award', 'NL Cy Young Award', 
                    'AL Hank Aaron Award', 'NL Hank Aaron Award', 'Babe Ruth Award', 'Edgar Martinez Award', 'AL Batting Champion', 'NL Batting Champion', 
                    'AL Pitching ERA Chamption', 'NL Pitching ERA Champion', 'AL Rookie of the Year', 'NL Rookie of the Year', 'AL Comeback Player of the Year', 
                    'NL Comeback Player of the Year']


print("\n Player Awards")
print(palAbb[:])
with open('mlb_data/Awards_2018-2023.csv', "r") as csvfile:
    reader = csv.reader(csvfile)
    for r in reader:
        if r[0] == '2022':
            print(r)

print("\n Team Season Statistics")
print(tslAbb[:])
with open('mlb_data/Teams_2018-2023.csv', "r") as csvfile:
    reader = csv.reader(csvfile)
    for r in reader:
        if r[9] == 'World Series Champion':
            print(r)