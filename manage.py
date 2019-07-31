from Tetris.views import app, db
from flask_script import Manager, prompt_bool
from Tetris.models import User
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
