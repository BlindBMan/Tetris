var playState = {
	create: function() {
		console.log('play');
		this.add.image(0, 0, 'background');

		block = this.add.sprite(295, 120, 'letter_i');
	    block.height = 104;
	    block.width = 104;
	    // block.setCollideWorldBounds(true);
	},

	update: function() {
		
	}
};