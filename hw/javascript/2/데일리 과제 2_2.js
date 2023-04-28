function printStars(num) {
    for (let i = 1; i <= num; i++) {
      let str = '';
  
      for (let j = 1; j <= num - i; j++) {
        str += ' ';
      }
  
      for (let k = 1; k <= 2 * i - 1; k++) {
        str += '*';
      }
  
      console.log(str);
    }
  }
  printStars(5)