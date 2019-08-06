var loadState = {
	preload: function() {

    this.load.image('background', './static/img/sprites/background.jpg');
    this.load.image('letter_i', './static/img/sprites/I.png');
    this.load.image('letter_L', './static/img/sprites/L.png');
    this.load.image('letter_R', './static/img/sprites/R.png');
    this.load.image('letter_S', './static/img/sprites/S.png');
    this.load.image('letter_T', './static/img/sprites/T.png');
    
},

	update: function() {
		console.log('loadState finished');
		game.state.start('menu');
	}
};