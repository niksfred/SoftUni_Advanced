from project.dvd import DVD
from project.customer import Customer


class MovieWorld:
    def __init__(self, name: str) -> None:
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15
    
    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)
    
    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        for object in self.dvds:
            if object.id == dvd_id:
                dvd = object
                break
        for customer_obj in self.customers:
            if customer_obj.id == customer_id:
                customer = customer_obj
                break
        
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        elif dvd.is_rented:
            return "DVD is already rented"
        elif customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        for movie in self.dvds:
            if movie.id == dvd_id:
                dvd = movie
                break
        for customer in self.customers:
            if customer.id == customer_id:
                customer = customer
                break
        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        else:
            return f"{customer.name} does not have that DVD"

    def __repr__(self) -> str:
        res = []
        for customer in self.customers:
            res.append(repr(customer))
        for dvd in self.dvds:
            res.append(repr(dvd))
        return "\n".join(res) 
        

