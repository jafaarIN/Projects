# 💡 CLI-Based Word Autosuggestor with Feedback-Driven learning

This is a simple word autosuggestion system written in Python. It takes a block of natural language text, splits it into word pairs then suggest the next word based on user input and pair frequency.

How it works:
1. It reads 'dataset.txt', which contains a block of natural language text
2. It cleans the data and splits it into individual words
3. Returns the suggestion (or lack of suggestion), asks for user input
4. Learns from user feedback, improving over time by boosting priorities of correct answers

Usage:
1. Ensure that the 'main.py' file is in the same directory as 'dataset.txt' file
2. python main.py
   or python3 main.py
   
