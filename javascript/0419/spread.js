let parts = ['어깨', '무릎']
let lyrics = ['머리', ...parts, '발']
console.log(lyrics)
// ['머리', '어깨', '무릎', '발']

const restPrs = function (arg1, arg2, ...restArgs){
	return [arg1, arg2, restArgs]
}

restPrs(1,2,3,4,5) // [1, 2, [3, 4, 5]]
restPrs(1,2) // [1, 2, []]