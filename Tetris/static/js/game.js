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
    height: 650,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 200 }
        }
    },  
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

var game = new Phaser.Game(config);
game.scale.pageAlignHorizontally = true;

var block;

function preload () {

    this.load.image('background', './static/img/sprites/background.jpg');
    this.load.image('letter_i', './static/img/sprites/I.png');
    this.load.image('letter_L', './static/img/sprites/L.png');
    this.load.image('letter_R', './static/img/sprites/R.png');
    this.load.image('letter_S', './static/img/sprites/S.png');
    this.load.image('letter_T', './static/img/sprites/T.png');
    
}

function create () {
    

    this.add.image(295, 325, 'background');

    block = this.physics.add.sprite(295, 120, 'letter_i');
    block.displayHeight = 104;
    block.displayWidth = 104;
    block.setCollideWorldBounds(true);

    

}

function update() {
    
    let cursors = this.input.keyboard.createCursorKeys();

    if (Phaser.Input.Keyboard.JustDown(cursors.left)) {
        block.x -= 20;
    } else if (Phaser.Input.Keyboard.JustDown(cursors.right)) {
        block.x += 20;
    } else if (Phaser.Input.Keyboard.JustDown(cursors.up)) {
        block.angle += 90;
    } else if (Phaser.Input.Keyboard.JustDown(cursors.down)) {
        block.y += 20;
    }

}
