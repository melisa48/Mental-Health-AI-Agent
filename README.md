# Mental Health AI Agent

A Python-based AI assistant designed to support mental well-being by offering stress relief techniques, mindfulness exercises, professional help resources, and a conversational interface. Built with interactivity and user preferences in mind, this tool aims to provide a compassionate and personalized experience.

## Features
- **Stress Relief Techniques**: Offers a variety of methods like deep breathing, visualization, and grounding exercises, with guided timers for select techniques.
- **Mindfulness Exercises**: Includes activities such as body scans, mindful listening, and gratitude moments to promote relaxation and awareness.
- **Professional Resources**: Provides contact information for crisis lines and online therapy services.
- **Conversational Support**: Allows users to express feelings, with sentiment analysis to tailor responses and follow-up options.
- **Mood Tracking**: Logs user moods with timestamps, viewable as a history of the last 5 entries.
- **Personalized Recommendations**: Suggests favorite techniques based on user feedback stored in a database.
- **Guided Timers**: Real-time countdowns for exercises like Deep Breathing and Visualization.
- **Positive Reinforcement**: Encourages users with uplifting messages after completing activities.
- **Persistent Storage**: Uses SQLite to save user preferences and mood history.

## Requirements
- Python 3.x
- NLTK library (`pip install nltk`)
- SQLite (included in Python standard library)

## Setup
1. **Clone or Download**: Get the code from this repository or copy it into a file named `mental_health_ai.py`.
2. **Install Dependencies**:
- pip install nltk
The script will automatically download the `vader_lexicon` for sentiment analysis on first run.
3. **Run the Program**:
- ​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​python mental_health_ai.py
- This will create a `user_prefs.db` SQLite database file in the same directory to store preferences and mood history.

## Usage
1. **Start the Program**: Run the script, and you'll see a welcome message with options:
​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​Hello! I'm here to support your mental well-being. What would you like to do?
​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​1. Try a stress relief technique
   2. Do a mindfulness exercise
   3. See helpful resources
   4. Talk about how you're feeling
   5. View your saved preferences
   6. See your mood history
   Or just tell me how you're feeling!

2. **Interact**:
- Enter a number (1-6) or type your feelings directly (e.g., "I’m sad").
- Follow prompts to try exercises, share feelings, or view data.
- Use shortcuts like `s` (stress relief), `m` (mindfulness), `r` (resources), or `t` (talk) during chat.
3. **Exit**: Type "no" when asked "Want to keep going?" to close the program.
### Example Interaction
​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​> 1
- Since you liked it before, here’s: Deep Breathing: Inhale for 4s, hold for 4s, exhale for 4s. Repeat 5 times.
- Let’s do Deep Breathing together...
- ​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​Inhale... 4 3 2 1 
- Hold... 4 3 2 1 
- Exhale... 4 3 2 1 
[...]
- Did it help? (yes/no): yes
- Saved as your favorite!
- Great job taking care of yourself! How are you feeling now?

## Project Structure
- `mental_health_ai.py`: The main script containing all functionality.
- `user_prefs.db`: SQLite database (auto-generated) storing preferences and mood history.

## Notes
- **User ID**: Currently hardcoded to "user1". For multi-user support, modify the `user_id` logic.
- **Database**: If you modify the schema, delete `user_prefs.db` and rerun to recreate it.
- **Guided Timers**: Limited to Deep Breathing and Visualization; expandable to other exercises.
- **Sentiment Analysis**: Uses NLTK’s VADER, suitable for short text but can be upgraded for more complex analysis.

## Future Enhancements
- Add multi-user support with a login system.
- Expand guided timers to more exercises.
- Integrate audio cues or a GUI for a richer experience.
- Export mood history to CSV or connect to external apps.

## Contributing
Feel free to fork this project, submit pull requests, or suggest improvements via issues!

## License
This project is open-source and available under the [MIT License](LICENSE).


   
