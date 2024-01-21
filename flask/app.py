from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vyl@localhost/movie_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

sql_db = SQLAlchemy(app)

class Movie(sql_db.Model):
    movie_id = sql_db.Column(sql_db.Integer, primary_key=True)
    movie_name = sql_db.Column(sql_db.String(50), nullable=False)

    def __repr__(self):
        return f'<Movie name {self.movie_name}>'

# Connect to MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")  # Update with your MongoDB connection string
mongo_db = mongo_client["movie"]
metadata_collection = mongo_db["metadata"]

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

        sql_db.session.add(new_movie)
        sql_db.session.commit()

        return jsonify({'message': 'Movie "{0}" added successfully'.format(data['movie_name'])})
    except Exception as e:
        if isinstance(e, ValueError):
            return jsonify({'bad request': str(e)}, 400)
        else:
            return jsonify({'internal server error': str(e)}, 500)

@app.route('/v1/movie', methods=['GET'])
def get_movie():
    movies = Movie.query.all()
    return ', '.join([str(m.movie_id) + ": " + m.movie_name for m in movies])

@app.route('/v1/movie/metadata', methods=['GET'])
def get_movie_metadata():
    cursor = metadata_collection.find()
    all_data = list(cursor)
    return jsonify({'metadata': all_data, 'count': metadata_collection.count_documents({})})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)






