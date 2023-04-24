function Member(name, age, sId) {
	this.name = name
    this.age = age
    this.sId = sId
}

const member1 = new Member('John', 30, 1123412341)

const obj = {
    name: '김민구',
    age: 27,
    birth: '1997-11-07',
    gender: 'male',
    marriged: false,
    country: 'Korea',
    major: 'Mechanical Engineering',
    phone: '010-9241-5759',
}

function Introduce(name,age,birth,gender,marriged,country,major,phone){
    this.name = name
    this.age = age
    this.birth = birth
    this.gender = gender
    this.marriged = marriged
    this.country = country
    this.major = major
    this.phone = phone
}

const obj1 = new Introduce('김남우', 'null', 'null', 'male', false, 'Korea', 'Chemical', 'null')
console.log(obj1)