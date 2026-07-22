# 🎵 Music Recommender Simulation

## Project Summary

This is a classroom example of a music recommender system. It consits of a small dataset of 15 songs with 12 genres and 5 moods. Each song has a set of numerical features to represent energy, valence, danceability, tempo_bpm, and acousticness. A user profile is created with four preferences: favorite_genre, favorite_mood, target_energy, and likes_acoustic. The recommender system scores each song based on how well it matches the user's preferences and ranks them to provide recommendations. However, due to completing the project, the final results are skewed as the weights favor energy over genre, and the dataset is small and not diverse enough to provide a wide range of recommendations.

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
take top k → recommendations

Finalized "Algorithm Recipe" uses the following weight distribution for scoring:
Component Weight Match type
Genre 0.35 categorical (partial credit, see below)
Energy 0.30 continuous (similarity)
Mood 0.20 categorical (exact match)
Acoustic 0.15 continuous (derived similarity)
Total = 1.0, final score is a weighted sum

Genre outranks mood.

### Genre similarity table

Genre started as a strict exact-match, but with only 15 songs across 12 genres, most genres have exactly one song — an exact-match-only rule meant a user's non-favorite genre never got any credit, no matter how close it was in feel. To soften that, genre now gives partial credit to a short list of related genre pairs instead of scoring every non-match as zero:

| Genre A   | Genre B   | Similarity |
| --------- | --------- | ---------- |
| lofi      | ambient   | 0.5        |
| lofi      | jazz      | 0.5        |
| jazz      | classical | 0.5        |
| ambient   | classical | 0.5        |
| pop       | indie pop | 0.5        |
| pop       | synthwave | 0.5        |
| rock      | metal     | 0.5        |
| hip hop   | reggae    | 0.5        |
| indie pop | folk      | 0.5        |

Rule: exact genre match = 1.0, a listed related pair = 0.5, anything else = 0.0. Pairs were grouped by feel (chill/instrumental: lofi-ambient-jazz-classical; upbeat/produced: pop-indie pop-synthwave; heavy: rock-metal; groove-based: hip hop-reggae; singer-songwriter: indie pop-folk), not by genre taxonomy, so the grouping is a judgment call rather than a strict musicological one.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

   ```

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

** New recommendations based on targeted energy **


==================================================
 Top 5 Recommendations for "high-energy pop"
==================================================

1. Sunrise City (by Neon Echo)
   Score: 0.96
   Reasons:
     - matches your favorite genre (pop)
     - energy 0.82 vs. your target 0.85
     - matches your favorite mood (happy)
     - acousticness 0.18 fits your preference for non-acoustic songs

2. Gym Hero (by Max Pulse)
   Score: 0.82
   Reasons:
     - matches your favorite genre (pop)
     - energy 0.93 vs. your target 0.85
     - mood (intense) doesn't match your favorite (happy)
     - acousticness 0.05 fits your preference for non-acoustic songs

3. Rooftop Lights (by Indigo Parade)
   Score: 0.74
   Reasons:
     - genre (indie pop) doesn't match your favorite (pop)
     - energy 0.76 vs. your target 0.85
     - matches your favorite mood (happy)
     - acousticness 0.35 fits your preference for non-acoustic songs

4. Concrete Bloom (by MC Lyrical)
   Score: 0.66
   Reasons:
     - genre (hip hop) doesn't match your favorite (pop)
     - energy 0.80 vs. your target 0.85
     - mood (euphoric) doesn't match your favorite (happy)
     - acousticness 0.08 fits your preference for non-acoustic songs

5. Storm Runner (by Voltline)
   Score: 0.65
   Reasons:
     - genre (rock) doesn't match your favorite (pop)
     - energy 0.91 vs. your target 0.85
     - mood (intense) doesn't match your favorite (happy)
     - acousticness 0.10 fits your preference for non-acoustic songs


==================================================
 Top 5 Recommendations for "chill lofi"
==================================================

1. Midnight Coding (by LoRoom)
   Score: 0.96
   Reasons:
     - matches your favorite genre (lofi)
     - energy 0.42 vs. your target 0.40
     - matches your favorite mood (chill)
     - acousticness 0.71 fits your preference for acoustic songs

2. Library Rain (by Paper Lanterns)
   Score: 0.96
   Reasons:
     - matches your favorite genre (lofi)
     - energy 0.35 vs. your target 0.40
     - matches your favorite mood (chill)
     - acousticness 0.86 fits your preference for acoustic songs

3. Focus Flow (by LoRoom)
   Score: 0.85
   Reasons:
     - matches your favorite genre (lofi)
     - energy 0.40 vs. your target 0.40
     - mood (focused) doesn't match your favorite (chill)
     - acousticness 0.78 fits your preference for acoustic songs

4. Spacewalk Thoughts (by Orbit Bloom)
   Score: 0.75
   Reasons:
     - genre (ambient) doesn't match your favorite (lofi)
     - energy 0.28 vs. your target 0.40
     - matches your favorite mood (chill)
     - acousticness 0.92 fits your preference for acoustic songs

5. Coffee Shop Stories (by Slow Stereo)
   Score: 0.67
   Reasons:
     - genre (jazz) doesn't match your favorite (lofi)
     - energy 0.37 vs. your target 0.40
     - mood (relaxed) doesn't match your favorite (chill)
     - acousticness 0.89 fits your preference for acoustic songs


==================================================
 Top 5 Recommendations for "deep intense rock"
==================================================

1. Storm Runner (by Voltline)
   Score: 0.98
   Reasons:
     - matches your favorite genre (rock)
     - energy 0.91 vs. your target 0.90
     - matches your favorite mood (intense)
     - acousticness 0.10 fits your preference for non-acoustic songs

2. Gym Hero (by Max Pulse)
   Score: 0.80
   Reasons:
     - genre (pop) doesn't match your favorite (rock)
     - energy 0.93 vs. your target 0.90
     - matches your favorite mood (intense)
     - acousticness 0.05 fits your preference for non-acoustic songs

3. Iron Reckoning (by Grave Circuit)
   Score: 0.65
   Reasons:
     - genre (metal) doesn't match your favorite (rock)
     - energy 0.97 vs. your target 0.90
     - mood (aggressive) doesn't match your favorite (intense)
     - acousticness 0.03 fits your preference for non-acoustic songs

4. Sunrise City (by Neon Echo)
   Score: 0.63
   Reasons:
     - genre (pop) doesn't match your favorite (rock)
     - energy 0.82 vs. your target 0.90
     - mood (happy) doesn't match your favorite (intense)
     - acousticness 0.18 fits your preference for non-acoustic songs

5. Concrete Bloom (by MC Lyrical)
   Score: 0.63
   Reasons:
     - genre (hip hop) doesn't match your favorite (rock)
     - energy 0.80 vs. your target 0.90
     - mood (euphoric) doesn't match your favorite (intense)
     - acousticness 0.08 fits your preference for non-acoustic songs
```

---

## Experiments You Tried

I doubled the weight to prefer energy and half of genre. This led to songs being more energetic and not the mood a user favored. I also didn't have enough variance of songs per genre.

---

## Limitations and Risks

The dataset is small and thus, not diverse enough. Not enough songs exist for each genre leading to similar recommendations. Also, the weights are skewed to favorit energy instead of a user's genre preference.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

I realized how a recommendation system needs to be adjusted to account for a user's preference as well as to ensure weights and scores are represented of the user. If not adjusted, or if the dataset isn't diverse, there will be homogenization or repression of preferences. It also helped me to peel back the "magic" layer and realize that the logic/algorithms are important.
