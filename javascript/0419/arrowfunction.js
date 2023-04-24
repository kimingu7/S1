// 화살표 함수 예시
const arrow1 = function(name) {
	return 'hello, ${name}'
}
// 1. function 키워드 생략가능
const arrow2 = (name) => { return 'hello, ${name}'}
// 2. 매개변수가 하나라면 매개변수의 ()도 생략 가능
const arrow3 = name => { return 'hello, ${name}'}
// 3. 함수의 내용이 한줄이라면 {}와 return도 생략가능
const arrow4 = name => 'hello, ${name}'

// 화살표 함수 응용
// 1. 인자가 없다면 ()나 _ 로 표시 가능
let noArgs = () => 'No args'
noArgs = _ => 'No args'

// 2-1. object를 return 한다면
let returnObject = () => { return { key : 'value' } }

// 2-2. return을 적지 않으려면 괄호를 붙여야 함
returnObject = () => ({ key : 'value' })