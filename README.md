# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Song facts from songs.csv pull in:
- Song identity such as title, artist, and song id as part of a display
- Category tags which are labels like genre, mood for comparisons
- Numerical features to represent energy, valence, danceability, tempo_bpm, acousticness

Depending on what is listed in a UserProfile, the Recommender will compute a score for each song based on how well it matches the user's preferences. The system then ranks the songs by score and recommends the top matches to the user.

A UserProfiler will store four type of preferences: favorite_genre for a category, favorite_mood, target_energy and likes_acoustic.

Each song is compared against the profile on those four preferences and scored on a 0.0 to 1.0 scale based on user's preference.

Weights will place genre and energy as top consideration, mood as sometimes and acoustic as lower. Each recommendation will provide an explanation of why it was recommended based on the earlier dimensions noted.

Scoring is done one song at a time while ranking is for a list of the scored songs. Songs will be sorted by highest final_score as the top 'k' with explanations provided for each recommendation.

songs.csv ──► load_songs() ──► List[Song]
                                    │
UserProfile (4 preferences) ───────┤
                                    ▼
                    score_song(user, song) for each song
                    → (score 0-1, [reasons])
                                    │
                                    ▼
                    sort all (song, score, reasons) by score, desc
                                    │
                                    ▼
                          take top k  →  recommendations


Finalized "Algorithm Recipe" uses the following weight distribution for scoring:
Component	Weight	Match type
Genre	0.35	categorical (partial credit, see below)
Energy	0.30	continuous (similarity)
Mood	0.20	categorical (exact match)
Acoustic	0.15	continuous (derived similarity)
Total = 1.0, final score is a weighted sum


Genre outranks mood.

### Genre similarity table

Genre started as a strict exact-match, but with only 15 songs across 12 genres, most genres have exactly one song — an exact-match-only rule meant a user's non-favorite genre never got any credit, no matter how close it was in feel. To soften that, genre now gives partial credit to a short list of related genre pairs instead of scoring every non-match as zero:

| Genre A | Genre B | Similarity |
|---|---|---|
| lofi | ambient | 0.5 |
| lofi | jazz | 0.5 |
| jazz | classical | 0.5 |
| ambient | classical | 0.5 |
| pop | indie pop | 0.5 |
| pop | synthwave | 0.5 |
| rock | metal | 0.5 |
| hip hop | reggae | 0.5 |
| indie pop | folk | 0.5 |

Rule: exact genre match = 1.0, a listed related pair = 0.5, anything else = 0.0. Pairs were grouped by feel (chill/instrumental: lofi-ambient-jazz-classical; upbeat/produced: pop-indie pop-synthwave; heavy: rock-metal; groove-based: hip hop-reggae; singer-songwriter: indie pop-folk), not by genre taxonomy, so the grouping is a judgment call rather than a strict musicological one.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

```
==================================================
 Top 5 Recommendations
==================================================

1. Library Rain (by Paper Lanterns)
   Score: 0.96
   Reasons:
     - matches your favorite genre (lofi)
     - energy 0.35 vs. your target 0.40
     - matches your favorite mood (chill)
     - acousticness 0.86 fits your preference for acoustic songs

2. Midnight Coding (by LoRoom)
   Score: 0.95
   Reasons:
     - matches your favorite genre (lofi)
     - energy 0.42 vs. your target 0.40
     - matches your favorite mood (chill)
     - acousticness 0.71 fits your preference for acoustic songs

3. Focus Flow (by LoRoom)
   Score: 0.77
   Reasons:
     - matches your favorite genre (lofi)
     - energy 0.40 vs. your target 0.40
     - mood (focused) doesn't match your favorite (chill)
     - acousticness 0.78 fits your preference for acoustic songs

4. Spacewalk Thoughts (by Orbit Bloom)
   Score: 0.60
   Reasons:
     - genre (ambient) doesn't match your favorite (lofi)
     - energy 0.28 vs. your target 0.40
     - matches your favorite mood (chill)
     - acousticness 0.92 fits your preference for acoustic songs

5. Coffee Shop Stories (by Slow Stereo)
   Score: 0.42
   Reasons:
     - genre (jazz) doesn't match your favorite (lofi)
     - energy 0.37 vs. your target 0.40
     - mood (relaxed) doesn't match your favorite (chill)
     - acousticness 0.89 fits your preference for acoustic songs
```

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this
