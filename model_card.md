# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

EnergyTunes 

---

## 2. Intended Use  

This is a classroom exploration for recommending music based on a user's preference based heavily on their targeted energy.

---

## 3. How the Model Works  

Scoring is based on a weighted sum of features: genre, mood, energy and acousticness. Due to doubling the weight of energy, the other features are minimized, thus skewing the results to be less mood favored.

Profiles created are "high-energy pop" which favors more upbeat happy pop songs, "chill lofi" for more chill lofi types and "deep intense rock" for intense rock music.

---

## 4. Data  

Here's an example of a dataset I used and tested after doing a weight shift to double the importance of energy with half importance of genre. The remaining features were minimized to make the score close to 1. Results are now rebalanced for energy to be the dividing factor between close songs.

======================================================================
 Profile: "high-energy pop"
======================================================================
OLD weights (0.35/0.30/0.20/0.15)     NEW weights (0.175/0.60/0.1286/0.0964)
1. Sunrise City (0.964)               1. Sunrise City (0.965)
2. Gym Hero (0.768)                   2. Gym Hero (0.819)
3. Rooftop Lights (0.571)             3. Rooftop Lights (0.737)
4. Concrete Bloom (0.423)             4. Concrete Bloom (0.659)
5. Storm Runner (0.417)               5. Storm Runner (0.651)

Same top-5 set: True | Same order: True

======================================================================
 Profile: "chill lofi"
======================================================================
OLD weights (0.35/0.30/0.20/0.15)     NEW weights (0.175/0.60/0.1286/0.0964)
1. Library Rain (0.964)               1. Midnight Coding (0.960)  <-- changed
2. Midnight Coding (0.950)            2. Library Rain (0.957)  <-- changed
3. Focus Flow (0.767)                 3. Focus Flow (0.850)
4. Spacewalk Thoughts (0.602)         4. Spacewalk Thoughts (0.745)
5. Coffee Shop Stories (0.424)        5. Coffee Shop Stories (0.668)

Same top-5 set: True | Same order: False

======================================================================
 Profile: "deep intense rock"
======================================================================
OLD weights (0.35/0.30/0.20/0.15)     NEW weights (0.175/0.60/0.1286/0.0964)
1. Storm Runner (0.982)               1. Storm Runner (0.984)
2. Gym Hero (0.633)                   2. Gym Hero (0.802)
3. Iron Reckoning (0.424)             3. Iron Reckoning (0.652)
4. Concrete Bloom (0.408)             4. Sunrise City (0.631)  <-- changed
5. Sunrise City (0.399)               5. Concrete Bloom (0.629)  <-- changed

Same top-5 set: True | Same order: False

======================================================================
 Profile: "ADV: nonexistent genre & mood"
======================================================================
OLD weights (0.35/0.30/0.20/0.15)     NEW weights (0.175/0.60/0.1286/0.0964)
1. Island Sway (0.360)                1. Island Sway (0.598)
2. Concrete Bloom (0.348)             2. Golden Hour Static (0.586)  <-- changed
3. Night Drive Loop (0.342)           3. Midnight Coding (0.580)  <-- changed
4. Sunrise City (0.327)               4. Focus Flow (0.561)  <-- changed
5. Rooftop Lights (0.320)             5. Coffee Shop Stories (0.533)  <-- changed

Same top-5 set: False | Same order: False

======================================================================
 Profile: "ADV: metal genre but wants zero energy"
======================================================================
OLD weights (0.35/0.30/0.20/0.15)     NEW weights (0.175/0.60/0.1286/0.0964)
1. Spacewalk Thoughts (0.569)         1. Spacewalk Thoughts (0.679)
2. Library Rain (0.539)               2. Library Rain (0.632)
3. Midnight Coding (0.495)            3. Midnight Coding (0.575)
4. Iron Reckoning (0.379)             4. Sonata for Rainy Days (0.542)  <-- changed
5. Sonata for Rainy Days (0.367)      5. Coffee Shop Stories (0.494)  <-- changed

Same top-5 set: False | Same order: False

======================================================================
 Profile: "ADV: extreme out-of-range target_energy"
======================================================================
OLD weights (0.35/0.30/0.20/0.15)     NEW weights (0.175/0.60/0.1286/0.0964)
1. Sunrise City (-1.781)              1. Sunrise City (-4.525)
2. Gym Hero (-1.928)                  2. Gym Hero (-4.575)
3. Rooftop Lights (-2.174)            3. Iron Reckoning (-4.724)  <-- changed
4. Iron Reckoning (-2.263)            4. Rooftop Lights (-4.753)  <-- changed
5. Storm Runner (-2.292)              5. Storm Runner (-4.767)

Same top-5 set: True | Same order: False

======================================================================
 Profile: "ADV: empty-string preferences"
======================================================================
OLD weights (0.35/0.30/0.20/0.15)     NEW weights (0.175/0.60/0.1286/0.0964)
1. Island Sway (0.360)                1. Island Sway (0.598)
2. Concrete Bloom (0.348)             2. Golden Hour Static (0.586)  <-- changed
3. Night Drive Loop (0.342)           3. Midnight Coding (0.580)  <-- changed
4. Sunrise City (0.327)               4. Focus Flow (0.561)  <-- changed
5. Rooftop Lights (0.320)             5. Coffee Shop Stories (0.533)  <-- changed

Same top-5 set: False | Same order: False

---

## 5. Strengths  

System seems to follow the scoring metric. It's good at shuffling songs, however, weights are what determines what the acutal recommendations will be based upon.

---

## 6. Limitations and Bias  

Silent/ambient music with a target_energy of 0 will be capped at 0.72 as there are no songs in the dataset lower than 0.28 energy.
The readjusted energy weight creates a bubble where 4/5 recommendations are almost identical regardless of favored genre or mood. Filtering by energy eradicates genre preference. The old weights allowed less homogenization in recommendations.
Lofi catalog has three songs while the rest of the genres have single songs, thus minimizing their genre tastes.

---

## 7. Evaluation  

python3 /private/tmp/claude-501/-Users-sajidahw-CP-AI-Engineering/1a11ec79-2213-4c9a-bb16-43705dda361d/scratchpad/adversarial_profiles.py

============================================================
 Profile: "nonexistent genre & mood"
 prefs = {'favorite_genre': 'k-pop', 'favorite_mood': 'ecstatic', 'target_energy': 0.5, 'likes_acoustic': False}
 comment: It's interesting that the recommendations aren't choosing what the user likes. Top songs seems to have a lower energy.
============================================================
1. Island Sway (by Solstice Roots) - genre=reggae, mood=playful, energy=0.6
   Score: 0.3600
     - genre (reggae) doesn't match your favorite (k-pop)
     - energy 0.60 vs. your target 0.50
     - mood (playful) doesn't match your favorite (ecstatic)
     - acousticness 0.40 fits your preference for non-acoustic songs
2. Concrete Bloom (by MC Lyrical) - genre=hip hop, mood=euphoric, energy=0.8
   Score: 0.3480
     - genre (hip hop) doesn't match your favorite (k-pop)
     - energy 0.80 vs. your target 0.50
     - mood (euphoric) doesn't match your favorite (ecstatic)
     - acousticness 0.08 fits your preference for non-acoustic songs
3. Night Drive Loop (by Neon Echo) - genre=synthwave, mood=moody, energy=0.75
   Score: 0.3420
     - genre (synthwave) doesn't match your favorite (k-pop)
     - energy 0.75 vs. your target 0.50
     - mood (moody) doesn't match your favorite (ecstatic)
     - acousticness 0.22 fits your preference for non-acoustic songs
4. Sunrise City (by Neon Echo) - genre=pop, mood=happy, energy=0.82
   Score: 0.3270
     - genre (pop) doesn't match your favorite (k-pop)
     - energy 0.82 vs. your target 0.50
     - mood (happy) doesn't match your favorite (ecstatic)
     - acousticness 0.18 fits your preference for non-acoustic songs
5. Rooftop Lights (by Indigo Parade) - genre=indie pop, mood=happy, energy=0.76
   Score: 0.3195
     - genre (indie pop) doesn't match your favorite (k-pop)
     - energy 0.76 vs. your target 0.50
     - mood (happy) doesn't match your favorite (ecstatic)
     - acousticness 0.35 fits your preference for non-acoustic songs


============================================================
 Profile: "contradictory: loves metal but wants zero energy"
 prefs = {'favorite_genre': 'metal', 'favorite_mood': 'chill', 'target_energy': 0.05, 'likes_acoustic': True}
 Comment: Again, the genres are different from the users preference, and still higher in energy than the targeted energy.
============================================================
1. Spacewalk Thoughts (by Orbit Bloom) - genre=ambient, mood=chill, energy=0.28
   Score: 0.5690
     - genre (ambient) doesn't match your favorite (metal)
     - energy 0.28 vs. your target 0.05
     - matches your favorite mood (chill)
     - acousticness 0.92 fits your preference for acoustic songs
2. Library Rain (by Paper Lanterns) - genre=lofi, mood=chill, energy=0.35
   Score: 0.5390
     - genre (lofi) doesn't match your favorite (metal)
     - energy 0.35 vs. your target 0.05
     - matches your favorite mood (chill)
     - acousticness 0.86 fits your preference for acoustic songs
3. Midnight Coding (by LoRoom) - genre=lofi, mood=chill, energy=0.42
   Score: 0.4955
     - genre (lofi) doesn't match your favorite (metal)
     - energy 0.42 vs. your target 0.05
     - matches your favorite mood (chill)
     - acousticness 0.71 fits your preference for acoustic songs
4. Iron Reckoning (by Grave Circuit) - genre=metal, mood=aggressive, energy=0.97
   Score: 0.3785
     - matches your favorite genre (metal)
     - energy 0.97 vs. your target 0.05
     - mood (aggressive) doesn't match your favorite (chill)
     - acousticness 0.03 fits your preference for acoustic songs
5. Sonata for Rainy Days (by Elena Voss) - genre=classical, mood=melancholic, energy=0.3
   Score: 0.3675
     - genre (classical) doesn't match your favorite (metal)
     - energy 0.30 vs. your target 0.05
     - mood (melancholic) doesn't match your favorite (chill)
     - acousticness 0.95 fits your preference for acoustic songs




---

## 8. Future Work  

Changing the weight of the scoring system so genre and mood are weighed more. Also adding more than three songs in each genre category to make diverse recommendations.

---

## 9. Personal Reflection  

I feel like I have a better understanding on how recommendations work for music and how important it is to decide how to portion out weights. I think I'm beginning to see it's less magical.
I feel like this project has enabled me to see how AI/ML works behind the scenes and how tweaking and testing several times helps to get better results.
