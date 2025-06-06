function Collage(manager) {
    this.manager = manager;
}
  
function Manager(name) {
  this.name = name;
  console.log(name + " manages the collage");
}

let manager = new Manager("Dr. Ahmad");
let collage = new Collage(manager);