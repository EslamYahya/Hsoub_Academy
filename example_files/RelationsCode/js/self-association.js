function Person(worksIn) {
    this.worksIn = worksIn;
    this.managedWorkers = [];
    console.log("person works in the department");
    console.log("person manages other persons");
    this.add_managedWorker = function(worker) {
        this.managedWorkers.push(worker);
        console.log("person added to managed workers");
    }   
}

function Department() {
    this.workers = [];
    console.log("department employs persons");
    this.add_worker = function(worker) {
        this.workers.push(worker);
        console.log("person added to managed workers");
    }
}

let department = new Department();
let person1 = new Person(department);
let person2 = new Person(department);
let person3 = new Person(department);
person1.add_managedWorker(person2);
person1.add_managedWorker(person3);
department.add_worker(person1);
department.add_worker(person2);