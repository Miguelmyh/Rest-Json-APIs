from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db = SQLAlchemy()
engine = create_engine("postgresql+psycopg2://http://miguel704:159753waloL@localhost:5000/cupcakes")


def connect_db(app):
    db.app = app
    app.app_context().push()
    db.init_app(app)

class Cupcake(db.Model):
    """Model for cupcakes"""
    __tablename__ = 'cupcakes'
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    flavor = db.Column(db.Text,
                       nullable=False)
    size = db.Column(db.Text,
                     nullable=False)
    rating = db.Column(db.Float,
                       nullable=False)
    image = db.Column(db.Text,
                      nullable=False,
                      default= 'https://tinyurl.com/demo-cupcake')
    
    def serialize(self):
        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }
                       