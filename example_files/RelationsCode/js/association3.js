function Driver(car) {
    this.hasDrive = car;
    console.log("driver drives a car");
}
  
function Car(driver) {
    this.drivenBy = driver;
    console.log("car is driven by driver");
}

let car = new Car();
let driver = new Driver(car);