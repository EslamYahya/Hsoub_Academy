function Car() {
  console.log("car is ready");
}

function Driver(car) {
  this.hasDrive = car;
  console.log("driver drives the car");
}

let car = new Car();
let driver = new Driver(car);