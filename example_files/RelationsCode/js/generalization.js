function Animal(name, description) {
    this.name = name;
    this.description = description;
  
    this.eating = function () {
        console.log(this.name + " is eating");
    }
}
function Ostrich(name, description) {
    Animal.call(this, name, description);
    this.head_bury = function () {
        console.log('The Ostrich bury its head in sand');
    }
}
function Crocodile(name, description) {
    Animal.call(this, name, description);
    this.go_out_water = function () {
        console.log('The Crocodile is go out water');
    }
}
function Duck(name, description) {
    Animal.call(this, name, description);
    this.float = function () {
        console.log('The Duck is floating');
    }
} 
let crocodile = new Crocodile("CoCo", "green color animal");
crocodile.go_out_water();
crocodile.eating();