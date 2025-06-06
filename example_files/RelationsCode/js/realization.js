function OperatinSystem() {
    this.printOs = function () {}
}
  
function Windows() {
    OperatinSystem.call(this);
    this.printOs = function () {
        console.log("OS is windows");
    }
}
  
function IOS() {
    OperatinSystem.call(this);
    this.printOs = function () {
        console.log("OS is IOS ");
    }
}
  
function Android() {
    OperatinSystem.call(this);
    this.printOs = function () {
        console.log("OS is android ");
    }
}

let os = new Android();
os.printOs(); 