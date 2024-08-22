const incrementScore = (player) => {
  let score;
  if (player === 1) {
    score = document.getElementById("score-one");
  } else {
    score = document.getElementById("score-two");
  }

  let currScore = parseInt(score.innerHTML) + 1;
  score.innerHTML = currScore.toString();
};

const resetScore = () => {
  const scoreOne = document.getElementById("score-one");
  const scoreTwo = document.getElementById("score-two");

  scoreOne.innerHTML = "0";
  scoreTwo.innerHTML = "0";
};