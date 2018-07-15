from app import app, db
from entries.blueprint import entries

import models
import views

app.register_blueprint(entries, url_prefix='/entries')

if __name__ == '__main__':
    app.run()
