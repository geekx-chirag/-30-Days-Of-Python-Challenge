from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Set up the app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

# Define a Book model (table in the database)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()


# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()  # Get all books from the database
    book_list = []
    for book in books:
        book_list.append({'id': book.id, 'title': book.title, 'author': book.author})
    return jsonify(book_list)

# Route to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()  # Get the data sent in the request
    new_book = Book(title=data['title'], author=data['author'])
    db.session.add(new_book)  # Add the new book to the database
    db.session.commit()  # Save changes
    return jsonify({'message': 'Book added!'}), 201

# Route to delete a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)  # Find the book by its ID
    if book is None:
        return jsonify({'message': 'Book not found!'}), 404
    db.session.delete(book)  # Delete the book from the database
    db.session.commit()  # Save changes
    return jsonify({'message': 'Book deleted!'})

if __name__ == '__main__':
    app.run(debug=True)
