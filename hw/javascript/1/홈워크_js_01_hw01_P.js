// 1번
const nums = [1,2,3,4,5,6,7,8]

console.log('1번 출력 결과')
for (let i = 0; i < nums.length; i++) {
  console.log('nums[' + i + ']: ' + nums[i])
}
console.log()
// for (const i = 0; i < nums.length; i++) {
//                                     ^

// TypeError: Assignment to constant variable.

// const로 선언된 변수는 값을 변경할 수 없음
// 따라서 let i = 0으로 변경해야함


// 2번
console.log('2번 출력 결과')
nums.forEach((num) => {
  console.log(num, typeof num)
})

// for in 루프를 사용하게 되면 변수에 property의 이름이 할당되어 string 타입이 됨
// forEach나 for of 루프를 사용해야함