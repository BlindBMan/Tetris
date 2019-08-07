var menuState = {
	create: function() {
		this.input.keyboard.addKeyCapture([Phaser.Keyboard.SPACEBAR]);
		cursors = this.input.keyboard.createCursorKeys();

		this.add.image(0, 0, 'menu_bkgr');
		this.add.image(game.world.width / 4, 50, 'logo');

		var btnPlay = game.add.button(game.world.width / 2, game.world.height / 2 + 50,
								  'play_btn', function() { game.state.start('gameover'); },
								  this, 1, 2, 0);
		btnPlay.anchor.setTo(0.5, 0.5);
		var lblPlay = game.add.text(game.world.width / 2, game.world.height / 2 + 40, 'Play');
		lblPlay.anchor.setTo(0.5, 0.5);

	},

	start: function() {
		game.state.start('singleplayerPrep');
	}
};