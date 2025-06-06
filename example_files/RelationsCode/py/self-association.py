class Person:
    def __init__(self, works_in):
        self.works_in = works_in
        self.managed_worker = []
    print("person works in the department")
    print("person manages other persons")

    def add_managedWorker(self, worker):
        self.managed_worker.append(worker)
        print("person added to managed workers")

class Department:
    def __init__(self):
        self.workers = []
    print("department employs persons")

    def add_worker(self, worker):
        self.workers.append(worker)
        print("person added to workers list")

department = Department()
person1 = Person(department)
person2 = Person(department)
person3 = Person(department)
person1.add_managedWorker(person2)
person1.add_managedWorker(person3)
department.add_worker(person1)
department.add_worker(person2)
