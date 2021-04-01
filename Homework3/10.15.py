
# Mohammad Qureshi
# PSID: 1789301
# 10.15



class Team:
    def init(self):
        self.teamname = 'none'
        self.teamwins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        win_percent = self.team_wins / (self.team_wins + self.team_losses)
        return win_percent

getInfo = Team()
teamName = input()
getInfo.team_wins = int(input())
getInfo.team_losses = int(input())
if(getInfo.get_win_percentage() >= 0.5):
    print('Congratulations, Team', teamName, 'has a winning average!')
else:
    print('Team', teamName, 'has a losing average.')


