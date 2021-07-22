from project.hero import Hero

class Wizard(Hero):
    def __init__(self, username, level) -> None:
        super().__init__(username, level)