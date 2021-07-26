
class Zoo:
    def __init__(self, name:str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity:
            if price <= self.__budget:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"  

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"  
        return "Not enough space for worker" 

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker_name == worker.name:
                self.workers.remove(worker)
                return f"{worker.name} fired successfully"  
        return f"There is no {worker_name} in the zoo"
    
    def pay_workers(self):
        total_salary = [worker.salary for worker in self.workers]
        if sum(total_salary) > self.__budget:
            return f"You have no budget to pay your workers. They are unhappy"
        self.__budget -= sum(total_salary)
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_animals_care = [animal.money_for_care for animal in self.animals]
        if sum(total_animals_care) > self.__budget:
            return f"You have no budget to tend the animals. They are unhappy."
        self.__budget -= sum(total_animals_care)
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        res = ""
        res += f"You have {len(self.animals)} animals\n"
        lions = [repr(lion) for lion in self.animals if lion.__class__.__name__ == "Lion"]
        tigers = [repr(tiger) for tiger in self.animals if tiger.__class__.__name__ == "Tiger"]
        cheetahs = [repr(cheetah) for cheetah in self.animals if cheetah.__class__.__name__ == "Cheetah"]
        res += f"----- {len(lions)} Lions:\n"
        res += "\n".join(lions)
        res += "\n"
        res += f"----- {len(tigers)} Tigers:\n"
        res += "\n".join(tigers)
        res += "\n"
        res += f"----- {len(cheetahs)} Cheetahs:\n"
        res += "\n".join(cheetahs)
        return res

    def workers_status(self):
        res = ""
        res += f"You have {len(self.workers)} workers\n"
        keepers = [repr(keeper) for keeper in self.workers if keeper.__class__.__name__ == "Keeper"]
        caretakers = [repr(worker) for worker in self.workers if worker.__class__.__name__ == "Caretaker"]
        vets = [repr(worker) for worker in self.workers if worker.__class__.__name__ == "Vet"]
        res += f"----- {len(keepers)} Keepers:\n"
        res += "\n".join(keepers)
        res += "\n"
        res += f"----- {len(caretakers)} Caretakers:\n"
        res += "\n".join(caretakers)
        res += "\n"
        res += f"----- {len(vets)} Vets:\n"
        res += "\n".join(vets)
        return res
