import config

def basic_context(model_name):
    context = f"""

from main import app, db
from flask import jsonify
from dataclasses import dataclass
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

migrate = Migrate(app, db)


manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
"""

    return context


