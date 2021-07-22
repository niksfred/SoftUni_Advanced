from project.player import Player
class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        elif player.guild == "Unaffiliated":
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"
        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        for player in self.players:
            if player_name == player.name:
                player.guild = "Unaffiliated"
                self.players.remove(player)
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        res = ""
        res += f"Guild: {self.name}\n"
        for player in self.players:
            res += f"{player.player_info()}\n"
        return res
        