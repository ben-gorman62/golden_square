class TodoList():
    def __init__(self):
        self.list = []
    
    def add_task(self, task):
        self.list.append(str(task))
    
    def see_tasks(self):
        return self.list
    
    def check_complete(self, task):
        if task not in self.list:
            raise ValueError("Task not in Todo list.")
        task_done = task
        self.list.remove(task)
        return f"Task complete! Task removed from Todo List."