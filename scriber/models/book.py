from scriber.extensions import db

class Book(db.Model):
    isbn = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300))
    cover = db.Column(db.String(50))
    reviews = db.relationship('Review', backref='book', lazy=True)

    def __repr__(self):
        return f'<Book "{self.title}">'