from flask import Flask, jsonify, render_template, request
import import_ipynb
import Index

app = Flask(__name__)

@app.route('/')
def fetch_data():
    return render_template("movie_details.html")

@app.route('/movie_details', methods=['POST', 'GET'])
def send_data():
    genre = request.form['genre']
    cast = request.form['cast']
    plot = request.form['plot']
    director = request.form['director']

    if request.method == 'POST':
        # Predict movie success
        predicted_rating, predicted_audience = Index.predict_movie_success(genre, cast, director, plot)   
        # Determine movie status based on rating
        if predicted_rating >= 9:
            movie_status = "SUPER HIT"
        elif 7 <= predicted_rating < 9:
            movie_status = "HIT"
        elif 5 <= predicted_rating < 7:
            movie_status = "AVERAGE"
        else:
            movie_status = "FLOP"

        # Predict target audience using average Popularity_Score and rating
        return render_template(
            "result.html", 
            movie_status=movie_status,
            predicted_rating=predicted_rating,
            predicted_audience=predicted_audience
        )

# Start Flask app
if __name__== "__main__":
    app.run(port=5500, debug=True)