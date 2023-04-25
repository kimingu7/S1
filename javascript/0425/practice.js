const obj = new Promise((resolve, reject) => {
    resolve(3)
})

obj.then(result => {
    console.log(result+3 + '시입니다')
}).catch(error => {
    console.log(error)
}).finally(() => {
    console.log('퇴근합시다')
})