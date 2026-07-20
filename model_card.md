# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias  

**Features it doesn't consider:**
- `valence`, `danceability`, and `tempo_bpm` sit unused — a fast, sad song and a slow, happy song with the same genre/mood/energy score identically
- No listening history, skip behavior, or secondary preferences — a user can express only *one* favorite genre and *one* favorite mood, never "I like lofi but I'm also okay with jazz"
- No lyrics or language understanding at all

**Underrepresented genres/moods:**
- 15 songs across 12 genres means most genres (classical, reggae, folk, hip hop, metal) have exactly one song each — if that one song is a bad recommendation, the user gets no alternative in that genre at all
- Partially mitigated for genre: a small genre-relatedness table (see README) now gives 0.5 similarity credit to related genre pairs (e.g. rock↔metal, lofi↔ambient, hip hop↔reggae) instead of scoring every non-exact genre as zero. This gives users of sparse genres a softer fallback, but it's a hand-picked list covering only 9 pairs — genres outside those pairs (e.g. classical vs. hip hop) still score zero, and the groupings reflect one person's judgment of "feel," not a real taxonomy
- Moods like "euphoric," "aggressive," "melancholic," "nostalgic," and "playful" each also appear on just one track — too sparse to say the system "understands" these moods versus just matching a label, and mood still has no equivalent relatedness table

**Overfitting to one preference:**
- Confirmed in testing: a lofi/chill profile scored *Library Rain* 0.964 but scored *Storm Runner* (rock), *Gym Hero* (pop), and *Iron Reckoning* (metal) all within 0.13–0.16 of each other — the system can't distinguish degrees of "not a match," it just lumps every non-preferred genre into the same low bucket

**Unintentional favoritism:**
- Genre/mood matching is exact-string, so a user who types "lo-fi" instead of "lofi" gets zero genre credit — small labeling inconsistencies silently tank a score
- Users whose favorite genre happens to be well-stocked in the catalog (lofi has 3 songs) get richer, more varied recommendations than users whose favorite genre has only one entry (classical, metal, reggae) — the system's quality is really a function of how the hand-picked dataset happened to be built, not of the scoring logic itself 

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
