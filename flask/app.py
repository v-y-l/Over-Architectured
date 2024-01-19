from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vyl@localhost/movie_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Movie name {self.movie_name}>'

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Love this paper about restful APIs: http://www.standardsforapis.org/pdfs/domo-api-design.pdf
# curl -X POST -H "Content-Type: application/json" -d '{"movie_name": "test_movie"}' http://localhost:5000/v1/movie
@app.route('/v1/movie', methods=['POST'])
def post_user():
    try:
        data = request.get_json()

        # I know, I know, this should be two conditions.
        if 'movie_name' not in data or len(data['movie_name']) > 50:
            raise ValueError("Make sure the movie_name has a character length from 0 - 50")

        new_movie = Movie(movie_name=data['movie_name'])

        db.session.add(new_movie)
        db.session.commit()

        return jsonify({'message': 'Movie "{0}" added successfully'.format(data['movie_name'])})
    except Exception as e:
        if isinstance(e, ValueError):
            return jsonify({'bad request': str(e)}, 400)
        else:
            return jsonify({'internal server error': str(e)}, 500)

@app.route('/v1/movie', methods=['GET'])
def get_movie():
    movies = Movie.query.all()
    return ', '.join([m.movie_name for m in movies])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
