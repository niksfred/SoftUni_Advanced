
class Bunker:
    def __init__(self) -> None:
        self.survivors = []
        self.supplies = []
        self.medicine = []
    
    @property
    def food(self):
        res = [obj for obj in self.supplies if obj.__class__.__name__ == "FoodSupply"]
        if not res:
            raise IndexError("There are no food supplies left!")
        return res

    @property
    def water(self):
        res =  [obj for obj in self.supplies if obj.__class__.__name__ == "WaterSupply"]
        if not res:
            raise IndexError("There are no water supplies left!")
        return res

    @property
    def painkillers(self):
        res = [obj for obj in self.medicine if obj.__class__.__name__ == "Painkiller"]
        if not res:
            raise IndexError("There are no painkillers left!")
        return res

    @property
    def salves(self):
        res =  [obj for obj in self.medicine if obj.__class__.__name__ == "Salve"]
        if not res:
            raise IndexError("There are no salves left!")
        return res

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):  
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type: str):
        to_remove_medicine = [medicine for medicine in self.medicine if medicine.__class__.__name__ == medicine_type][-1]
        if survivor.needs_healing:
            self.medicine.remove(to_remove_medicine)
            to_remove_medicine.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type: str):
        to_remove_supply = [supply for supply in self.supplies if supply.__class__.__name__ == sustenance_type][-1]
        if survivor.needs_sustenance:
            self.supplies.remove(to_remove_supply)
            to_remove_supply.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"
    
    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2

        for survivor in self.survivors:
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")
