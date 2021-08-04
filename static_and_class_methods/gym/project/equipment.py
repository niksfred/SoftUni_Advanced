class Equipment:
    id = 1

    def __init__(self, name: str) -> None:
        self.name = name
        self.id = __class__.id
        __class__.id += 1
    
    def get_next_id():  
        return __class__.id
    
    def __repr__(self) -> str:
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return __class__.id
    