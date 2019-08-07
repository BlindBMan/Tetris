/**
* Created by gusti on 8/2/2019.
*/

const LEFTBOUNDY = 90,
      LEFTBOUNDX = 12,
      RIGHTBOUNDX = 426,
      RIGHTBOUNDY = 650;

var config = {
    type: Phaser.AUTO,
    width: 590,
    height: 650
};

var game = new Phaser.Game(590, 650, Phaser.AUTO, 'gameDiv');

var cursors;

game.state.add('load', loadState);
game.state.add('menu', menuState);
game.state.add('play', playState);
game.state.add('singleplayerPrep', singleplayerState);
game.state.add('gameover', gameoverState);

game.state.start('load');


// var game = new Phaser.Game(config);
// var block;



// function create () {
    



    

// }

// function update() {
    


// }
