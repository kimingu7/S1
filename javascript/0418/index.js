// 호이스팅
// 실행 이전에 선언

/* var의 특징
1. 생략가능
2. 변수 호이스팅
	console.log(a) // undefined
	var a = 1
	console.log(a) // 1
3. 암묵적결합(중복선언가능)
	var a = 1
	var a = 2
	console.log(a) // 2
4. 함수레벨스코프(함수 안에서만 바뀜)
	a = 1
	function test(){
		var a = 2
		console.log(a)
	}
	test() // 2
	console.log(a) // 1
	if (a === 1){
		var a = 3
		console.log(a) // 3
	}
	console.log(a) // 3
*/