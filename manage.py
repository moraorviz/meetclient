import os
from webapp import mongo, create_app
from webapp.group.models import Group

env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('config.%sConfig' % env.capitalize())

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, mongo=mongo, Group=Group)

