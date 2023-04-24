const numbers = [1, 2, 3, 4, 5]

console.log(numbers[0]) // 1
console.log(numbers[-1]) // undefined
console.log(numbers.length) // 5
console.log(numbers[numbers.length - 1]) // 5
console.log(numbers[numbers.length - 2]) // 4
console.log(numbers[numbers.length - 3]) // 3
console.log(numbers[numbers.length - 4]) // 2
console.log(numbers[numbers.length - 5]) // 1

// reverse (배열 뒤집음)
numbers.reverse()
console.log(numbers) // [5, 4, 3, 2, 1]

const numbers1 = [1, 2, 3, 4, 5]

// push (배열의 끝에 원소 추가), pop (배열의 끝 원소 추출)
numbers1.push(6)
console.log(numbers1) // [1, 2, 3, 4, 5, 6]

console.log(numbers1.pop()) // 6
console.log(numbers1) // [1, 2, 3, 4, 5]

// unshift (배열의 처음에 원소 추가), shift(배열의 처음 원소 추출)
numbers1.unshift(0)
console.log(numbers1) // [0, 1, 2, 3, 4, 5]
console.log(numbers1.shift()) // 0
console.log(numbers1) // [1, 2, 3, 4, 5]

// 배열에 원소가 존재한다면 true, 아니면 false
console.log(numbers1.includes(1)) // true)
console.log(numbers1.includes(6)) // false))

// 해당 인덱스에 원소가 존재한다면 index, 아니면 -1
console.log(numbers1.indexOf(1)) // 0)
console.log(numbers1.indexOf(6)) // -1)