from scriber.extensions import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.isbn'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    review_text = db.Column(db.String(300), nullable=False)
    created = db.Column(db.DateTime)