from flask import Flask, jsonify, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and anime titles once when app starts
model = joblib.load("models/svd_model.pkl")
anime = pd.read_csv("data/anime.csv")
anime_titles = dict(zip(anime['anime_id'], anime['name']))

@app.route("/recommend")
def recommend():
    user_id = int(request.args.get("user_id", 1))
    predictions = [model.predict(user_id, i) for i in range(1, 100)]
    top_preds = sorted(predictions, key=lambda x: x.est, reverse=True)[:5]
    
    results = []
    for pred in top_preds:
        results.append({
            "anime_id": pred.iid,
            "title": anime_titles.get(int(pred.iid), "Unknown"),
            "predicted_rating": round(pred.est, 2)
        })
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
