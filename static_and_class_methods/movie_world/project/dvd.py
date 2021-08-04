class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int) -> None:
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        day, month, year = list(map(int, date.split(".")))
        months = {1:"January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7:"July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
        month_str = months[month]
        return cls(name, id, year, month_str, age_restriction)
    
    def __repr__(self) -> str:
        if self.is_rented:
            status = "rented"
        else:
            status =  "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}"