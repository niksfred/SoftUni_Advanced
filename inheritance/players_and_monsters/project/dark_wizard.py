from project.wizard import Wizard

class DarkWizard(Wizard):
    def __init__(self, username, level) -> None:
        super().__init__(username, level)

