// 기본 인자
const greeting = function (name = 'Anonymous') {
	return `Hello ${name}`
}
greeting() // Hello Anonymous

/* 
javascript에선 인자가 없어도 에러가 발생하지 않음
따라서 기본 인자를 전달해 인자를 빼놓고 함수를 호출하더라도 기본 인자를 출력
*/

// 매개변수보다 인자의 개수가 많을 경우(매개 변수와 인자의 불일치 허용)
const noArgs = function () {
	return 0
}
noArgs(1, 2, 3) // 0

const twoArgs = function (arg1, arg2) {
	return [arg1, arg2]
}
twoArgs(1, 2, 3) // [1, 2]

// 매개변수보다 인자의 개수가 적을 경우(매개 변수와 인자의 불일치 허용)
const threeArgs = function (arg1, arg2, arg3) {
	return [arg1, arg2, arg3]
}
threeArgs() // [undifiend, undifined, undifined]
threeArgs(1) // [1, undefined, undefined]
threeArgs(2, 3) // [2, 3, undefined]