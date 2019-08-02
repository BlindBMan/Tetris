from Tetris.views import app, db
from flask_script import Manager, prompt_bool
from Tetris.models import User, Game
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def insert_data():
    sam = User(username='Sam', email='sam@gmail.com', password='test')
    suzzy = User(username='Suzzy', email='suzzy@gmail.com', password='test')
    db.session.add(sam)
    db.session.add(Game(score=20, user=sam))
    db.session.add(Game(score=500, user=suzzy))
    db.session.commit()
    print('Initialized database')


@manager.command
def dropdb():
    if prompt_bool('Are you sure you want to delete all?'):
        db.drop_all()
        print('Dropped database')


if __name__ == '__main__':
    manager.run()
