# Jarandon Adams - 1812590
# Zylabs 10.15

class Team:

    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def def_team_name(self, team_names):
        self.team_name = team_names

    def num_team_wins(self, team_wins_amt):
        self.team_wins = team_wins_amt

    def num_team_losses(self, team_losses_amt):
        self.team_losses = team_losses_amt

    # Calculate Win Percentage Here
    def get_win_percentage(self):
        percent = self.team_wins / (self.team_wins + self.team_losses)
        return percent


if __name__ == "__main__":

    team = Team()

    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team.def_team_name(team_name)
    team.num_team_wins(team_wins)
    team.num_team_losses(team_losses)

    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.team_name, 'has a winning average!')

    else:
        print('Team', team.team_name, 'has a losing average.')
