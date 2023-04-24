// console.log(document.querySelector('input'))

// document.querySelector('input').addEventListener('input', function(e) {
// 	console.log(e.target.value)
// })
// function(e) {},true)를 실행하면 부모 노드부터
// e.stopPropagation()을 입력하면 버블링을 멈추고 그 이벤트만 동작

document.querySelector('button').addEventListener('click', function(e) {
	console.log(this)
})

document.querySelector('button').addEventListener('click', () => {
	console.log(this)
})