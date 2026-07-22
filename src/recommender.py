import csv
import heapq
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


@dataclass
class Song:
    """Represents a song and its audio/metadata attributes."""
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """Represents a user's taste preferences for scoring songs."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """OOP wrapper that scores and ranks songs against a user profile."""
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns the top k songs for a user, sorted by match score."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Returns a human-readable reason for a song's recommendation."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"


def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file into a list of dicts with numeric fields converted."""
    numeric_fields = ("energy", "tempo_bpm", "valence", "danceability", "acousticness")
    songs = []
    with open(csv_path, newline="") as f:
        for row in csv.DictReader(f):
            row["id"] = int(row["id"])
            for field in numeric_fields:
                row[field] = float(row[field])
            songs.append(row)
    return songs


GENRE_WEIGHT = 0.175
ENERGY_WEIGHT = 0.60
MOOD_WEIGHT = 0.1286
ACOUSTIC_WEIGHT = 0.0964


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a single song against user preferences, returning (score, reasons)."""
    reasons = []

    genre_match = song["genre"] == user_prefs["favorite_genre"]
    genre_score = 1.0 if genre_match else 0.0
    if genre_match:
        reasons.append(f"matches your favorite genre ({song['genre']})")
    else:
        reasons.append(f"genre ({song['genre']}) doesn't match your favorite ({user_prefs['favorite_genre']})")

    energy_score = 1.0 - abs(song["energy"] - user_prefs["target_energy"])
    reasons.append(f"energy {song['energy']:.2f} vs. your target {user_prefs['target_energy']:.2f}")

    mood_match = song["mood"] == user_prefs["favorite_mood"]
    mood_score = 1.0 if mood_match else 0.0
    if mood_match:
        reasons.append(f"matches your favorite mood ({song['mood']})")
    else:
        reasons.append(f"mood ({song['mood']}) doesn't match your favorite ({user_prefs['favorite_mood']})")

    if user_prefs["likes_acoustic"]:
        acoustic_score = song["acousticness"]
        reasons.append(f"acousticness {song['acousticness']:.2f} fits your preference for acoustic songs")
    else:
        acoustic_score = 1.0 - song["acousticness"]
        reasons.append(f"acousticness {song['acousticness']:.2f} fits your preference for non-acoustic songs")

    score = (
        GENRE_WEIGHT * genre_score
        + ENERGY_WEIGHT * energy_score
        + MOOD_WEIGHT * mood_score
        + ACOUSTIC_WEIGHT * acoustic_score
    )

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores every song against user preferences and returns the top k, highest first."""
    scored = [(song, *score_song(user_prefs, song)) for song in songs]
    top_k = heapq.nlargest(k, scored, key=lambda entry: entry[1])
    return [(song, score, "; ".join(reasons)) for song, score, reasons in top_k]
