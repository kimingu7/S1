// 1. 속성명 축약 (key와 value 명이 같다면 축약 가능)
const books = ['book1', 'book2']
const magazines = ['magazine1','magazine2']

const bookShop = {
	books,
    magazines,
}
console.log(bookShop)

// 2. method명 축약 (funciton 키워드 생략 가능)
const obj = {
	greeting() {
		console.log('안녕하세요')
	}
}
obj.greeting()

// 3. 계산된 속성
const key = 'country'
const value = ['한국', '미국', '일본', '중국']

const myObj = {
    [key]: value,
}
console.log(myObj)
console.log(myObj.country)

// 4. 구조 분해 할당
const userInformation = {
	name: 'ssafy kim',
	userId: 'ssafyStudent1234',
	email: 'ssafy@ssafy.com',
}
const {name} = userInformation
const {userId, email} = userInformation

// 5. Spread syntax(...) 배열과 같음