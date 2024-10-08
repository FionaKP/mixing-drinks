from app import create_app, db
from config import Config
# from app.Model.models import 

app = create_app(Config)

@app.before_request
def initDB(*args, **kwargs):
    if app._got_first_request:
        db.create_all()
        # if Tag.query.count() == 0:
        #     tags = ['funny','inspiring', 'true-story', 'heartwarming', 'friendship']
        #     for t in tags:
        #         db.session.add(Tag(name=t))
        #     db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)