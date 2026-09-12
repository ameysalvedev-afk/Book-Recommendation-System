import os
from flask import Flask, render_template, request
import pickle
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

popular_df = pickle.load(open(os.path.join(BASE_DIR, 'popular.pkl'), 'rb'))
pt = pickle.load(open(os.path.join(BASE_DIR, 'pt.pkl'), 'rb'))
books = pickle.load(open(os.path.join(BASE_DIR, 'books.pkl'), 'rb'))
similarity_scores = pickle.load(open(os.path.join(BASE_DIR, 'similarity_scores.pkl'), 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                            book_name=popular_df['Book-Title'].values.tolist(),
                            author=popular_df['Book-Author'].values.tolist(),
                            image=popular_df['Image-URL-M'].values.tolist(),
                            votes=popular_df['num_rating'].values.tolist(),
                            rating=popular_df['avg_rating'].values.tolist(),
                            )


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')

    if user_input not in pt.index:
        return render_template('recommend.html', error=f"'{user_input}' not found in our catalog.")

    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

    data = []
    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')
        item = {
            'title': temp_df['Book-Title'].values[0],
            'author': temp_df['Book-Author'].values[0],
            'image': temp_df['Image-URL-M'].values[0],
        }
        data.append(item)

    return render_template('recommend.html', data=data)


if __name__ == '__main__':
    app.run()