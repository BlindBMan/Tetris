var gameoverState = {
	create: function() {
		this.add.image(0, 0, 'menu_bkgr');

		var gameoverLabel = game.add.text(game.world.width / 3, 50, 'Gameover');
		var scoreLabel = game.add.text(game.world.width / 4, 250, 'Score');
		var score = game.add.text(game.world.width - 250, 250, 'SCOREHERE');

		var btnRePlay = game.add.button(game.world.width / 2, 370,
								  'play_btn', function() { game.state.start('singleplayerPrep'); },
								  this, 1, 2, 0);
		btnRePlay.anchor.setTo(0.5, 0.5);
		var lblRePlay = game.add.text(game.world.width / 2, 360, 'Rematch');
		lblRePlay.anchor.setTo(0.5, 0.5);

		var btnMenu = game.add.button(game.world.width / 2, 470,
								  'play_btn', function() { game.state.start('menu'); },
								  this, 1, 2, 0);
		btnMenu.anchor.setTo(0.5, 0.5);
		var lblMenu = game.add.text(game.world.width / 2, 460, 'Menu');
		lblMenu.anchor.setTo(0.5, 0.5);

	}
};