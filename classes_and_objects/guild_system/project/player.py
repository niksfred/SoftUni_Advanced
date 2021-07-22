class Player:
    def __init__(self, name, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        else:
            return "Skill already added"

    def player_info(self):
        res = ""
        res += f"Name: {self.name}\n"
        res += f"Guild: {self.guild}\n"
        res += f"HP: {self.hp}\n"
        res += f"MP: {self.mp}\n"
        for skill, mana_cost in self.skills.items():
            res += f"==={skill} - {mana_cost}\n"
        return res
