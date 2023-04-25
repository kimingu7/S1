const p1 = ['rock', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'paper', 'paper', 'rock', 'scissors']
const p2 = ['paper', 'paper', 'rock', 'scissors', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'rock']
  
const playGame = (p1_choices, p2_choices) => {
	p1_choices.forEach((p1_choice, i) => {
	  const p2_choice = p2_choices[i]
	  if (p1_choice === p2_choice) {
		console.log(0)
	  } else if (
		(p1_choice === 'rock' && p2_choice === 'scissors') || 
		(p1_choice === 'paper' && p2_choice === 'rock') ||
		(p1_choice === 'scissors' && p2_choice === 'paper')
	  ) {
		console.log(1)
	  } else {
		console.log(2)
	  }
	})
  }
  
  playGame(p1, p2)
  
  

// 2
// 0
// 2
// 0
// 2
// 1
// 2
// 1
// 0
// 2