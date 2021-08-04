from project.subscription import Subscription
from project.exercise_plan import ExercisePlan
from project.equipment import Equipment
from project.trainer import Trainer
from project.customer import Customer


class Gym:
    def __init__(self) -> None:
        self.customers: Customer = []
        self.trainers: Trainer = []
        self.equipment: Equipment = []
        self.plans: ExercisePlan = []
        self.subscriptions: Subscription = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)
    
    
    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)
    
    
    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)


    def add_plan(self, plan:ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)


    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    
    def subscription_info(self, subscription_id: int):
        res = ""
        for subscription in self.subscriptions:
            if subscription_id == subscription.id:
                break
                
        for customer in self.customers:
            if subscription.customer_id == customer.id:
                break

        for trainer in self.trainers:
            if subscription.trainer_id == trainer.id:
                break

        for plan in self.plans:
            if subscription.exercise_id == plan.id:
                break        

        for equipment in self.equipment:
            if plan.equipment_id == equipment.id:
                break
        
        
        
        res += repr(subscription) + "\n"
        res += repr(customer) + "\n"
        res += repr(trainer) + "\n"
        res += repr(equipment) + "\n"
        res += repr(plan)
        

        return res
        
    @staticmethod
    def get_object(obj_id, cl_iterable):
        return list(filter(lambda _: _.id==obj_id, cl_iterable))
