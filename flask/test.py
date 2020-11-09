import os
import click
from flask_migrate import Migrate, upgrade
from app import create_app, db
from flask_script import Manager, Shell
from app.models import User
from flask_cors import CORS

app = create_app('default') #返回一个值到'app/__init__.py'
migrate = Migrate(app, db)
manager = Manager(app)
CORS(app, resources={r'/*': {'origins': '*'}})


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)
manager.add_command("shell",Shell(make_context=make_shell_context))


@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    app.run(port=9000, debug=True)
    #manager.run()
