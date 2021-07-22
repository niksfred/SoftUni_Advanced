from project.task import Task

class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            print(task.name) 
            if task_name == task.name:
                task.completed = True
                return f"Completed task {task.name}"
        return f"Could not find task with the name {task_name}"
                

    def clean_section(self):
        cleared_amount = 0
        for task in self.tasks:
            if task.completed == True:
                self.tasks.remove(task)
                cleared_amount += 1
        return f"Cleared {cleared_amount} tasks."
    
    def view_section(self):
        res = ""
        res += f"Section {self.name}:\n"
        for task in self.tasks:
            res += f"{task.details()}\n"
        return res
