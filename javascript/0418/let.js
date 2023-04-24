/* let
1. 생략 불가능
	console.log(a) // 에러 발생
	let a = 1
2. 변수 호이스팅이 동작하지 않는 것처럼
3. 재선언 불가능
	let a = 1
	let a = 2 // X 
	a = 2 // O
	console.log(a)
4. 블록레벨스코프
	let a = 1
	if (a === 1){
		let a = 2
		console.log(a) // 2
	}
	console.log(a) // 1

	function test(){
		let a = 3
		console.log(a)
	}
	test() // 3
	console.log(a) // 1
*/