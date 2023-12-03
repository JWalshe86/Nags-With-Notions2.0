/**
 * @jest-environment jsdom
 */

const testing = {
    test1: 'cat',
}


//make jquery functions available after the document has loaded
// $(document).ready(function () {
//     $('#pills-pizzas .menu-item img').after('<p class="float-right t-1"><strong>€14</strong></p>'); //prices under all pizza items
//     $('#pills-dips .menu-item img').after('<p class="float-right t-1"><strong>€2</strong></p>'); //prices under all dips
//     $('#pills-drinks .menu-item img').after('<p class="float-right t-1"><strong>€2</strong></p>'); //prices under all dips
//     $("p:nth-child(2)").css("background-color", "pink").css('padding', '5px'); //background color of prices pink & padding 5px; 
// });

let game = {
    currentGame: [],
    playerMoves: [],
    score: 0,
    turnNumber: 0,
    choices: ["button1", "button2", "button3", "button4"]
};

function newGame() {
    game.currentGame = [];
    game.playerMoves = [];
    game.score = 0;

    for (let circle of document.getElementsByClassName("circle")) {
        if (circle.getAttribute("data-listener") !== "true") {
            circle.addEventListener("click", (e) => {
                let move = e.target.getAttribute("id");
                game.playerMoves.push(move);
                lightsOn(move);
                playerTurn();
            });
            circle.setAttribute("data-listener", "true");
        }
    }
    showScore();
    addTurn();
}

function addTurn() {
    game.playerMoves = [];
    game.currentGame.push(game.choices[(Math.floor(Math.random() * 4))]);
    showTurns();
}

function showTurns() {
    game.turnNumber = 0;
    let turns = setInterval(function () {
        lightsOn(game.currentGame[game.turnNumber]);
        game.turnNumber++;
        if (game.turnNumber >= game.currentGame.length) {
            clearInterval(turns);
        }
    }, 800);
}

function lightsOn(circ) {
    document.getElementById(circ).classList.add("light");
    setTimeout(function () {
        document.getElementById(circ).classList.remove("light");
    }, 400);
}

function playerTurn() {
    let i = game.playerMoves.length - 1;
    if (game.currentGame[i] === game.playerMoves[i]) {
        if (game.currentGame.length === game.playerMoves.length) {
            game.score++;
            showScore();
            addTurn();
        }
    } else {
        alert("Wrong move!");
        newGame();
    }
}

function showScore() {
    document.getElementById("score").innerText = game.score;
}

module.exports = { game, newGame, showScore, addTurn, lightsOn, showTurns, playerTurn };