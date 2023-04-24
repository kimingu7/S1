/* (호출할 수 있는) 함수의 종류
1. def 일반함수
2. method (객체 안에서 property의 값이 함수)
3. 생성자 함수
4. 간접호출
*/

// 전역 문맥에서의 this
console.log(this) // window

// 함수 문맥에서의 this
// 1. 단순 호출 (제일 흔하지만 제일 안씀)
const myFunc = function(){
	console.log(this)
}
myFunc() // window

// 2. Method (많이 쓰임, 60% 정도)
const myObj = {
	data: 1,
	myFunc() {
		console.log(this) // myObj
		console.log(this.data) // 1
	}
}
myObj.myFunc() // myObj

// 3. Nested

/* function 키워드 this의 바인딩이 잘못됨
const myObj2 = {
	numbers: [1],
	myFunc() {
        console.log(this) // myObj2
        this.numbers.forEach(function(num) {
			console.log(num) // 1
			console.log(this) // window
    	})
	}
}
myObj2.myFunc()
*/

// 화살표 함수 this의 바인딩이 올바름
const myObj2 = {
	numbers: [1],
	myFunc() {
        console.log(this) // myObj2
        this.numbers.forEach((num) => {
			console.log(num) // 1
			console.log(this) // myObj2
    	})
	}
}

myObj2.myFunc()
