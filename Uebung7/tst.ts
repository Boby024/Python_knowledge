

var laptops=[{"name":"Firefox",
             	"age":30,
                 "id": "ab"},
             {"name":"Google",
             	"age":35,
                 "id": "cd",
             	"date":"00.02.1990"},
             {"name":"Microsoft",
                 "id": "ef",
             	"age":40}];

function getLaptopByAsin(id: string) {
    return  this.laptops.find(
        laptopObject =>
           laptopObject.id === id

      );
}

//id:string;

var enter="cd";

//nan= this.getLaptopByAsin(enter).name;
var age;
age= this.getLaptopByAsin(enter).age;
var date= this.getLaptopByAsin(enter).date;
console.log(name);
console.log(age);
console.log(date);

/*
 getLaptopByAsin(id: string){
  var laptop= this.laptops.find(
        (laptopObject) => {
          return laptopObject.name === id;
        }
      );
       return laptop;
    }
 */
