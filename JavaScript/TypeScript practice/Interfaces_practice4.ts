interface User {
    firstName:string,
    lastName:string,
    sayHi(name:string):string,
    fullName():string
}
interface Human {
    health: number
}
class Player implements User, Human {
    constructor(
        public firstName:string,
        public lastName:string,
        public health:number
    ) {}
    fullName(){
        return `${this.firstName} ${this.lastName}`
    }
    sayHi(name:string){
        return `Hello ${name}. My name is ${this.fullName()}`
    }
}


function makeUser(user: User){
    return "hi"
}

makeUser({
    firstName: "nico",
    lastName: "las",
    fullName: () => "xx",
    sayHi: (name) => "string"
})

// abstract class User {
//     constructor(
//         protected firstName:string,
//         protected lastName:string
//     ) {}
//     abstract sayHi(name:string):string
//     abstract fullName():string
// }
//
// class Player extends User {
//     fullName(){
//         return `${this.firstName} ${this.lastName}`
//     }
//     sayHi(name:string){
//         return `Hello ${name}. My name is ${this.fullName()}`
//     }
// }