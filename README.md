<h2 align="center">
  🎬 MovieMatch — Content-Based Movie Recommendation System with Sentiment Analysis
</h2>

<p align="center">
  <em>Select 3 movies you love → Get intelligent recommendations powered by multi-feature cosine similarity → Share your feedback analyzed by Google Gemini</em>
</p>

---

### Project Overview

**MovieMatch** is a content-based movie recommendation engine that suggests films based on deep feature similarity rather than simple genre matching. Given 3 user-selected movies, the system identifies the strongest pairwise similarity and generates 4 tailored recommendations by analyzing multiple content dimensions simultaneously.

The app also includes a **sentiment analysis layer** — after receiving recommendations, users can describe how they felt about the suggested movies, and a Google Gemini LLM analyzes the emotional tone of their feedback in real time.

---

### How It Works

#### 1. Feature Engineering Pipeline
The raw [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) (5,000 movies with full cast/crew metadata) is processed through a feature engineering pipeline that converts categorical movie attributes into binary vector representations:

| Feature | What It Captures | Encoding |
|---------|-----------------|----------|
| `genres_bin` | Genre tags (Action, Comedy, Drama, etc.) | Multi-hot binary vector |
| `cast_bin` | Top-billed cast members | Binary presence vector |
| `director_bin` | Film director | Binary indicator vector |
| `words_bin` | Plot keywords and overview terms | Binary bag-of-words vector |

#### 2. Multi-Dimensional Similarity Scoring
Instead of matching on a single attribute, the system computes a **composite distance score** between any two movies by summing cosine distances across all 4 feature vectors:

```
similarity(A, B) = cosine_dist(genres) + cosine_dist(cast) + cosine_dist(director) + cosine_dist(keywords)
```

This multi-dimensional approach captures nuanced relationships — two movies might share a director and genre but differ in cast, and the system accounts for all of these dimensions simultaneously.

#### 3. Recommendation Strategy
When a user selects 3 movies:
1. **Pairwise Comparison** — The system computes similarity between all 3 pairs (A↔B, B↔C, A↔C)
2. **Strongest Pair Selection** — Identifies the 2 movies with the smallest distance (most similar pair)
3. **K-Nearest Neighbor Search (K=2)** — For each movie in the strongest pair, finds the 2 nearest neighbors from the full dataset
4. **Result** — Returns 4 recommendations (2 per movie) that align with the user's strongest taste signal

#### 4. Sentiment Analysis
After receiving recommendations, users can type free-text feedback. This feedback is sent to **Google Gemini (gemini-1.5-flash)** which analyzes the sentiment and provides a natural language response about the user's emotional reaction.

---

### System Architecture

```
MovieMatch/
├── home.py                          # Landing page — project intro + navigation
├── pages/
│   ├── match.py                     # Core recommendation UI + sentiment feedback
│   └── report a bug.py             # Bug reporting form
├── algorithms/
│   ├── notebook544bc4c95c.ipynb     # Feature engineering + model training notebook
│   ├── moviesPredictor.py          # Similarity engine (cosine distance + KNN)
│   └── movie_model.pkl             # Pre-processed feature vectors (87 MB)
├── api/
│   ├── sentiment_gpt.py            # Gemini LLM integration for sentiment analysis
│   ├── gsheet_auth.py              # Google Sheets auth (disabled locally)
│   └── openai_auth.py              # Legacy OpenAI auth (deprecated)
├── datasets/
│   ├── tmdb_5000_movies.csv        # Raw movie metadata (5.7 MB)
│   └── tmdb_5000_credits.csv       # Raw cast/crew data (40 MB)
├── assets/files/
│   ├── moviesdos.csv               # Curated movie title list for UI dropdown
│   └── movies.csv                  # Alternate movie list format
├── requirements.txt
└── .streamlit/
    └── secrets.toml                # API keys (not committed to git)
```

---

### Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | Streamlit (multi-page app) |
| **ML Engine** | SciPy (cosine distance), Pandas, NumPy |
| **LLM Integration** | Google Gemini 1.5 Flash via `google-generativeai` |
| **Dataset** | TMDB 5000 (Kaggle) |
| **Model Serialization** | Python Pickle (`.pkl`) |

---

### Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/Laveshjadon/MovieMatch.git
cd MovieMatch
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv

# Windows
.\venv\Scripts\Activate

# macOS/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure your API key**

Create a `.streamlit/secrets.toml` file in the project root:
```toml
GEMINI_API_KEY = "your-google-gemini-api-key"
```

> You can get a free Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)

**5. Launch the application**
```bash
streamlit run home.py
```

The app will open at `http://localhost:8501`

---

### Usage

1. Click **"Start Matching"** on the landing page
2. Select **3 movies** from the dropdown (4,800+ titles available)
3. Click **"Get Recommendations"** — the engine will return 4 similar movies
4. Optionally, type how you felt about the recommendations in the feedback box
5. Click **"Submit"** to receive AI-powered sentiment analysis of your feedback

---

### Dataset

This project uses the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) which contains:
- **4,803 movies** with metadata (genres, keywords, budget, revenue, overview)
- **Full cast and crew listings** for each movie
- Data spanning multiple decades of cinema

---

### License

[MIT](https://choosealicense.com/licenses/mit/)
