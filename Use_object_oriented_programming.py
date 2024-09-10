class Player:
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team

    def introduce(self):
        print(f"Hello I'm {self.name} and I play for {self.team}")

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)

    def remove_player(self, name):
        for player in self.players:
            if player.name == name:
                self.players.remove(player)

    def show_player(self):
        for player in self.players:
            player.introduce()

    def show_team_xp(self):
        team_xp = 0
        for player in self.players:
            team_xp += player.xp
        print(f"The total xp of {player.team} is {team_xp}")

team_x = Team("Team X")
blue_team = Team("Blue Team")

team_x.add_player("tomas")
blue_team.add_player("Bradley")


team_x.show_team_xp()
blue_team.show_team_xp()