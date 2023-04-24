// for Each

const colors = ['red', 'green', 'blue']

const printFunc = function(color) {
	console.log(color)
}

const result = colors.forEach(function(color, index, array) {
	console.log(color, index, array)
})

colors.forEach((color) => {console.log(color)})

const arr1 = [1, 2, 3, 4, 5]

arr1.forEach((element) => {console.log(element)}) // 1 2 3 4 5

/// map

const numbers = [1, 2, 3]

const doubleFunc = function(number) {
	return number * 2
}

const doubleNumbers = numbers.map(doubleFunc)
console.log(doubleNumbers) // [2, 4, 6]

/* 
함수 정의를 인자로 넣으면
const doubleNumbers = numbers.map(function(number) {
	return number * 2
})
console.log(doubleNumbers)

화살표 함수를 적용했을 때
const doubleNumbers = numbers.map((number) => {
	return number * 2
})
console.log(doubleNumbers)
*/

// filter

const products = [
	{ name: 'cucumber', type: 'vegetable'},
	{ name: 'banana', type: 'fruit'},
	{ name: 'carrot', type: 'vegetable'},
	{ name: 'apple', type: 'fruit'},
]

const fruitFilter = function(product) {
	return product.type === 'fruit'
}

const fruits = products.filter(fruitFilter)
console.log(fruits) // [ { name: 'banana', type: 'fruit'}, { name: 'apple', type: 'fruit'} ]

/*
함수 정의를 인자로 넣으면
const fruits = products.filter(function(product) {
	return product.type === 'fruit'
})
console.log(fruits)

화살표 함수를 적용했을 때
const fruits = products.filter((product) => {
	return product.type === 'fruit'
})
console.log(fruits)
*/

// reduce

const tests = [90, 90, 80, 77]

const sum = tests.reduce(function(total, x) {
	return total + x 
}, 0)

/* 화살표 함수
const sum = tests.reduce((total, x) => total + x, 0)
console.log(sum)
*/
const avg = tests.reduce((total, x) => total + x, 0) / tests.length
console.log(avg)

// find

const avengers = [
	{ name: 'Tony Stark', age: 45 },
    { name: 'Steve Rogers', age: 32 },
    { name: 'Thor', age: 40 },
]

const avenger = avengers.find(function(avenger) {
	return avenger.name === 'Tony Stark'
})
console.log(avenger)

/* 화살표 함수
const avenger = avengers.find((avenger) => {
	return avenger.name === 'Tony Stark'
})
*/

// some

const arr = [1, 2, 3, 4, 5]

const result1 = arr.some((elem) => {
	return elem % 2 === 0
})

// every

const result2 = arr.every((elem) => {
	return elem % 2 === 0
})

// 예제
// for Each 활용

const arr3 = [4, 3, 5, 1, 6, 5]

let cnt = 0

arr3.forEach((num) => {
	if (num % 2 === 1) {
        cnt++
    } 
})
console.log(cnt)

const arr4 = [-5, 3, 4, 2, -7, 2, 7]

arr4.forEach((e) => {
    if (e > 0){
        pplus.push(e)
    }
    else
    {
        mminus.push(e)
    }
})
console.log(pplus)
console.log(mminus)

// map 활용

const arr5 = [1, 2, 3, 4, 5]

const arr6 = arr5.map((e) => e ** 2)

console.log(arr6)

const arr7 = ['a', 'bcd', 'ef', 'g']

const arr8 = arr7.map((e) => e.length)

console.log(arr8)

// filter 활용

const arr9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

const arr9_1 = arr9.filter((e) => e % 2 === 1)
const arr9_2 = arr9.filter((e) => {
	return e > 3 && e < 9
})

console.log(arr9_1)
console.log(arr9_2)

const bucketlist = [
	{
		id: 1,
		text: '치킨 먹기',
		done: true,
	},
	{
		id: 2,
        text: '치킨 삭제',
        done: false,
	},
]
const arr10 = bucketlist.filter((e) => !e.done)
console.log(arr10)
// console.log(bucketlist.filter((b) =>!b.done))

// reduce로 map 구현하기

const arr11 = [1, 2, 3, 4]

arr11.reduce((acc, cur) => {
	const data = cur ** 2
	acc.push(data)
	return acc
}, [])


const arr12 = ['피카츄', '라이츄', '파이리', '꼬부기', '피카츄', '파이리']

const results = arr12.reduce((acc, cur) => {
	if (acc[cur]){
		acc[cur]++
	}
	else{
		acc[cur] = 1
	}
	return acc
}, {})

results

const arrz = [1,2,3,4,5]
const a = []
arrz.forEach(num => {
    if (num%2 === 0){
        a.push(num**2)
    }
})
console.log(a)

console.log(arrz.filter((el) => el%2 === 0).map((el) => el ** 2))