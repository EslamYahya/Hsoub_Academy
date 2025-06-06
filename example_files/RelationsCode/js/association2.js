function Car(driver) {
  this.drivenBy = driver;
  console.log("car is driven by the driver");
}

function Driver() {
    console.log("driver is ready");
}

let driver = new Driver();
let car = new Car(driver);
