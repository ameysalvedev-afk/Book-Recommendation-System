# 📚 Book Recommendation System

A simple machine learning project that helps users discover books they might enjoy based on the book they choose.

I built this project using Python, Flask, and machine learning techniques to find books that are similar to a user's selected book. The application also shows popular books along with their ratings, authors, and cover images.

🔗 **Live Demo:*[*https://book-recommendation-system-drab.vercel.app/recommend_books(https://book-recommendation-system-drab.vercel.app/recommend_books)](https://book-recommendation-system-drab.vercel.app/recommend_books)

---

## 🚀 What You Can Do

- 📖 Browse popular books
- 🔍 Search for a book
- 🤖 Get recommendations based on a selected book
- ⭐ View ratings and number of ratings
- 👤 See the author of each book
- 🖼️ View book cover images
- 🌐 Use the application online through Vercel

---

## 🧠 How the Recommendation Works

The recommendation system uses a pre-trained similarity model to find books that are similar to the one selected by the user.

The basic flow is:

1. The user enters a book name.
2. The system checks if the book is available in the dataset.
3. It looks up the selected book in the pre-trained model.
4. Similarity scores are used to find books that are closest to it.
5. The top 5 similar books are shown as recommendations.

The similarity scores were calculated beforehand, so the model doesn't need to be trained every time someone uses the website.

---

## 🛠️ Technologies Used

**Backend**
- Python
- Flask

**Machine Learning**
- NumPy
- Pandas
- Scikit-learn
- Collaborative Filtering
- Cosine Similarity

**Frontend**
- HTML
- CSS

**Deployment**
- GitHub
- Vercel

---

## 📂 Project Structure

```text
Book-Recommendation-System/
│
├── app.py
├── books.pkl
├── popular.pkl
├── pt.pkl
├── similarity_scores.pkl
├── Procfile
├── requirements.txt
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── recommend.html
│
└── README.md
