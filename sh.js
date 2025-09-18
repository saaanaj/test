const savan = document.querySelector("#main");
savan.innerHTML = "savan love u";
savan.id = "sav";
savan.style.color = "red"

let kumar = document.querySelector("#kumar");
kumar.innerHTML = "ponk";
kumar.innerHTML = "kumari"
kumar.style.color = "pink"

var varuse = document.querySelector("#varuse")
varuse.innerHTML = "var use mktc"
varuse.style.color = "green"


// number use

let d = "6.2";
let m = 9;
let s = Number(d)
let total = s  + m;
const num = document.querySelector("#num1")
num.innerHTML  = total;
num.style.color = "#000"

//string use

let k = 10;
let f = `[{
  "name": "savan kumar",
  "age": "20",
  "pink": {
    "sneah": "kumari randi" 
    , "lodulalit": 
     {"bor" : "choda" , 
      "bhosda" :
    [{"torachut": "landdalem"}]}
  },
  "pelab sare" : 
  [{"love" : "savanlove"}] 
}]`;



let prs = JSON.parse(f)
let get = prs[0]["pelab sare"][0].love;


const stri = document.querySelector("#strv")
stri.style.color = "#000"
stri.innerHTML =  get;



//boolean use 

const bolnen = document.querySelector("#bolnen")

let  blnch = false;

bolnen.innerHTML = "login"

bolnen.addEventListener("click" , () => {
  if (!blnch) {
    bolnen.innerHTML = "please login"
  }
  else{
    bolnen.innerHTML = "welcome"
  }
  // blnch =  !blnch
})

const ary = document.querySelector("#ary")

ary.innerHTML = "yes"
let lisy  = ["savan" , "kumar" , "love"]

ary.addEventListener("click" , () => {
  let hiny =   lisy[1]
  ary.innerHTML = hiny
})



const opt  = document.querySelector("#opratrors")

let frst = opt.innerHTML = "click for oprators"
let op = 10 ;
let ud = 21;
 
let chngs = (ud + 5);

let plus = op + ud;

let minus = ud - op;

let multiply = ud * op;

let divide = ud / op ;

let perct = chngs % op ;

let andh = op && ud;

let andyr = op || ud ;

let notoper = op !== ud ;
let clickcount = 0;

opt.addEventListener("click", () => {
  clickcount++;

  switch (clickcount) {
    case 1:
      opt.innerHTML = `Plus: ${plus}`;
      break;
    case 2:
      opt.innerHTML = `Minus: ${minus}`;
      break;
    case 3:
      opt.innerHTML = `Multiply: ${multiply}`;
      break;
    case 4:
      opt.innerHTML = `Modulus: ${perct}`;
      break;
    case 5:
      opt.innerHTML = `AND (&&): ${andh}`;
      break;
    case 6:
      opt.innerHTML = `OR (||): ${andyr}`;
      break;
    case 7:
      opt.innerHTML = `NOT (!==): ${notoper}`;
      break;
    case 8:
      opt.innerHTML = `Divide: ${divide}`;
      break;
    case 9:
      opt.innerHTML = frst;
      clickcount = 0; // reset
      break;
  }
});


let flormath = document.querySelector("#mathflor");

flormath.innerHTML = "start the random number";

flormath.addEventListener("click", () => {
    flormath.innerHTML = ""; // purane results clear karo
    flormath.style.color = "pink";
    let index = 0;
    let interval = setInterval(() => {
        let mathss = Math.floor(Math.random() * 100);
        flormath.innerHTML += mathss + "<br>";

        index++;
        if (index >= 100) {
            clearInterval(interval); // 100 numbers ke baad stop
        }
    }, 100); 
});

let ndh = document.querySelector("#numooo")
 let ckfd = 1;

let  intbvrs = setInterval(() => {
        ndh.innerHTML += ckfd + "<br>";
        ckfd ++;
        if (ckfd > 1) {
          clearInterval(intbvrs)
        }
}, 100)

const namwa = document.querySelector("#name input");
const emailwa = document.querySelector("#email input");
const phonwa = document.querySelector("#phone input");
const submitwa = document.querySelector("#submit button");
const view = document.querySelector("#view");
const search = document.querySelector("#search input")
const earchbtn = document.querySelector("#seacrbtn button")
const deletes = document.querySelector("#deletes button")
const viewalldata = document.querySelector("#viewalldata")
let filecre = "contacts"; // localStorage key

// Load contacts from localStorage
function loadContacts() {
    const data = localStorage.getItem(filecre);
    if (data) {
        return JSON.parse(data);
    }
    return {};
}

// Save contacts into localStorage
function saveContacts(contact) {
    localStorage.setItem(filecre, JSON.stringify(contact, null, 4));
}

let contacts = loadContacts(); // load old contacts

function addContact() {
  let name = namwa.value.trim();
  let phone = phonwa.value.trim();
  let email = emailwa.value.trim();

  if (name === "" || phone === "" || email === "") {
    alert("Please fill all the fields!");
    return;
  }

  contacts[name] = { phone, email }; // save in object
  saveContacts(contacts); // save in localStorage

  // view.textContent = JSON.stringify(contacts, null, 4);

  // reset inputs
  namwa.value = "";
  phonwa.value = "";
  emailwa.value = "";
}

submitwa.addEventListener("click", addContact);

// show saved contacts on page load
// view.textContent = JSON.stringify(contacts, null, 4);


function searchbyname() {
  let name = search.value.trim();
  if (name === ""){
     view.innerHTML = "please enter your name"
    return;
  }
  let data = contacts[name];
  if (data){
    view.innerHTML =  (`Found:\nPhone: ${data.phone}\nEmail: ${data.email}`);
  } 
  else{
    view.innerHTML = "not found your data"
  }
   search.value = ""
} 

earchbtn.addEventListener("click" ,  searchbyname );


function deletebysearch() {
  let namedelte = search.value.trim();
  if (namedelte === "") {
    view.innerHTML = "please enter your name"
    return;
  }
  let data = contacts[namedelte];
  if (data) {
       delete contacts[namedelte];   
        localStorage.setItem("contacts", JSON.stringify(contacts, null, 4));
        view.innerHTML = `${namedelte} data is delete now`
  }
  else{
    view.innerHTML = "contacts not found in there bro"
  }
}

deletes.addEventListener("click" , () => {
  deletebysearch()
})

viewalldata.addEventListener("click" , () => {
  let alldata = localStorage.getItem("contacts");
  if (!alldata || alldata === "{}"){
    view.innerHTML = "not contacts found"
    return;
  }
  view.textContent = JSON.stringify(JSON.parse(alldata), null, 4);
})