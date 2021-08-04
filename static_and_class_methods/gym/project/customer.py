class Customer:
    id = 1

    def __init__(self, name: str, address: str, email: str) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.id = __class__.id
        __class__.id += 1
    
    def get_next_id():
        return __class__.id

    def __repr__(self) -> str:
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
