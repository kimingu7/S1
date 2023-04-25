const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]

participantNums.forEach(nums => {
    const counts = {}
    nums.forEach(num => {
      if (counts[num]) {
        counts[num]++
      } else {
        counts[num] = 1
      }
    });

    console.log(counts)
  
    Object.entries(counts).forEach(([num, count]) => {
      if (count === 1) {
        console.log(num)
      }
    })
  })

// 3
// 100
// 62

// participantNums는 2차원 배열이기 때문에 2번의 forEach 문을 사용함
// nums는 이차원 배열 안의 배열을, num은 나눠진 배열 nums들의 원소들을 의미함
// 이 때 counts로 만들어진 딕셔너리를 Object.entries()로 이차원 배열 형태로 반환함
// 이 때 value값인 count가 1인 원소의 key 값을 출력해주면 됨