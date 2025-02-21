import random
import time
import sqlite3
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download required NLTK data
try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

class MentalHealthAI:
    def __init__(self):
        self.stress_relief = [
            "Deep Breathing: Inhale for 4s, hold for 4s, exhale for 4s. Repeat 5 times.",
            "Progressive Muscle Relaxation: Tense and relax each muscle group from toes to head.",
            "5-4-3-2-1 Grounding: Name 5 things you see, 4 touch, 3 hear, 2 smell, 1 taste.",
            "Visualization: Imagine a peaceful place for 2 minutes - beach, forest, or mountains.",
            "Stretching: Do gentle neck and shoulder stretches for 1 minute."
        ]
        
        self.mindfulness = [
            "Body Scan: Focus on each body part for 30s, noting sensations.",
            "Mindful Listening: Listen to ambient sounds for 1 minute without judgment.",
            "Gratitude Moment: List 3 things you're grateful for and why.",
            "Mindful Eating: Take 1 minute to eat something slowly, noticing all senses.",
            "Breath Counting: Count your breaths up to 10, then restart for 2 minutes."
        ]
        
        self.resources = {
            "USA": "National Suicide Prevention: 1-800-273-8255",
            "UK": "Samaritans: 116 123",
            "Crisis Text": "Text HOME to 741741",
            "Online Therapy": "BetterHelp: www.betterhelp.com",
            "Emergency": "Call your local emergency number"
        }

        self.sia = SentimentIntensityAnalyzer()
        
        self.conn = sqlite3.connect('user_prefs.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS preferences 
                            (user_id TEXT PRIMARY KEY, 
                            favorite_stress_technique TEXT,
                            favorite_mindfulness TEXT,
                            last_mood TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS mood_history 
                            (user_id TEXT, mood TEXT, timestamp TEXT)''')
        self.conn.commit()
        
        self.user_id = "user1"
        self.encouragements = [
            "Great job taking care of yourself!",
            "You’re doing amazing—keep it up!",
            "Every step counts, and you’re making progress!",
            "Well done for prioritizing your well-being!"
        ]

    def greet_user(self):
        return "Hello! I'm here to support your mental well-being. What would you like to do?\n" \
               "1. Try a stress relief technique\n" \
               "2. Do a mindfulness exercise\n" \
               "3. See helpful resources\n" \
               "4. Talk about how you're feeling\n" \
               "5. View your saved preferences\n" \
               "6. See your mood history\n" \
               "Or just tell me how you're feeling!"

    def analyze_sentiment(self, text):
        scores = self.sia.polarity_scores(text)
        if scores['compound'] <= -0.05:
            return "negative"
        elif scores['compound'] >= 0.05:
            return "positive"
        return "neutral"

    def save_preference(self, category, value):
        self.cursor.execute("INSERT OR REPLACE INTO preferences (user_id, " + category + ") VALUES (?, ?)",
                          (self.user_id, value))
        self.conn.commit()

    def get_preferences(self):
        self.cursor.execute("SELECT * FROM preferences WHERE user_id = ?", (self.user_id,))
        result = self.cursor.fetchone()
        if result:
            return f"Your preferences:\n" \
                   f"- Favorite Stress Technique: {result[1] or 'None'}\n" \
                   f"- Favorite Mindfulness: {result[2] or 'None'}\n" \
                   f"- Last Mood: {result[3] or 'Not recorded'}"
        return "No preferences saved yet."

    def save_mood_history(self, mood):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO mood_history (user_id, mood, timestamp) VALUES (?, ?, ?)",
                          (self.user_id, mood, timestamp))
        self.conn.commit()

    def show_mood_history(self):
        self.cursor.execute("SELECT mood, timestamp FROM mood_history WHERE user_id = ? ORDER BY timestamp DESC LIMIT 5",
                          (self.user_id,))
        results = self.cursor.fetchall()
        if results:
            return "Your recent moods:\n" + "\n".join([f"{mood} ({time})" for mood, time in results])
        return "No mood history yet."

    def guided_timer(self, exercise):
        if "Deep Breathing" in exercise:
            print("Let’s do Deep Breathing together...")
            for _ in range(3):
                print("Inhale...", end=" ")
                for i in range(4, 0, -1):
                    print(f"{i}", end=" ")
                    time.sleep(1)
                print("\nHold...", end=" ")
                for i in range(4, 0, -1):
                    print(f"{i}", end=" ")
                    time.sleep(1)
                print("\nExhale...", end=" ")
                for i in range(4, 0, -1):
                    print(f"{i}", end=" ")
                    time.sleep(1)
                print("")
            return True
        elif "Visualization" in exercise:
            print("Imagine a peaceful place... I’ll count down 30 seconds for you.")
            for i in range(30, 0, -1):
                if i % 10 == 0:
                    print(f"{i}...", end=" ")
                time.sleep(1)
            print("Done!")
            return True
        return False

    def get_personalized_recommendation(self, category):
        # Use the exact column name based on category
        column = "favorite_stress_technique" if category == "stress" else "favorite_mindfulness"
        self.cursor.execute(f"SELECT {column} FROM preferences WHERE user_id = ?", (self.user_id,))
        favorite = self.cursor.fetchone()
        if favorite and favorite[0]:
            return favorite[0], True
        # Match category to the correct list
        options = self.stress_relief if category == "stress" else self.mindfulness
        return random.choice(options), False

    def handle_stress_relief(self):
        technique, is_favorite = self.get_personalized_recommendation("stress")  # Changed to "stress"
        prefix = "Since you liked it before, here’s" if is_favorite else "Try this"
        print(f"{prefix}: {technique}")
        
        guided = self.guided_timer(technique)
        if not guided and input("Want to give it a go? (yes/no): ").lower() == "yes":
            print("Take a moment to try it...")
            time.sleep(1)
        
        if input("Did it help? (yes/no): ").lower() == "yes":
            self.save_preference("favorite_stress_technique", technique)
            print("Saved as your favorite!")
        return random.choice(self.encouragements) + " How are you feeling now?"

    def handle_mindfulness(self):
        exercise, is_favorite = self.get_personalized_recommendation("mindfulness")
        prefix = "Since you enjoyed it last time, here’s" if is_favorite else "Here’s an exercise"
        print(f"{prefix}: {exercise}")
        
        guided = self.guided_timer(exercise)
        if not guided:
            time.sleep(1)
            if input("Did you enjoy it? (yes/no): ").lower() == "yes":
                self.save_preference("favorite_mindfulness", exercise)
                print("Saved as your favorite!")
        return random.choice(self.encouragements) + " How do you feel after that?"

    def show_resources(self):
        return "\n".join([f"{k}: {v}" for k, v in self.resources.items()])

    def chat(self, user_input):
        sentiment = self.analyze_sentiment(user_input)
        self.save_preference("last_mood", sentiment)
        self.save_mood_history(sentiment)
        
        print("Thanks for sharing. I’m here to listen—tell me more if you’d like.")
        more = input(">").strip()
        if more:
            print(f"I hear you: {more}")
        
        responses = {
            "negative": "It sounds tough. ",
            "positive": "I’m glad to hear that! ",
            "neutral": ""
        }
        
        if "sad" in user_input.lower() or "sad" in more.lower():
            response = "I’m sorry you’re feeling sad. "
        elif "anxious" in user_input.lower() or "anxious" in more.lower():
            response = "Anxiety can be rough. "
        elif "tired" in user_input.lower() or "tired" in more.lower():
            response = "Being tired can weigh on you. "
        else:
            response = responses[sentiment]
        
        return response + "What would you like to do next?\n" \
               "- Stress relief (s)\n" \
               "- Mindfulness (m)\n" \
               "- Resources (r)\n" \
               "- Keep talking (t)"

    def run(self):
        print(self.greet_user())
        
        while True:
            choice = input("> ").strip().lower()
            
            if choice == "1" or choice == "s":
                print(self.handle_stress_relief())
            
            elif choice == "2" or choice == "m":
                print(self.handle_mindfulness())
            
            elif choice == "3" or choice == "r":
                print(self.show_resources())
            
            elif choice == "4" or choice == "t":
                feeling = input("How are you feeling? ")
                print(self.chat(feeling))
            
            elif choice == "5":
                print(self.get_preferences())
            
            elif choice == "6":
                print(self.show_mood_history())
            
            else:
                print(self.chat(choice))
            
            if input("Want to keep going? (yes/no): ").lower() != "yes":
                print("Take care! I’m always here if you need me.")
                self.conn.close()
                break

if __name__ == "__main__":
    ai = MentalHealthAI()
    ai.run()

