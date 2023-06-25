import random

def generate_books():
  books = ("Meditations by Marcus Aurelius", 
           "The Alchemist by Paulo Coelho", 
           "Atomic Habits by James Clear", 
           "The Subtle Art of Not Giving a F*ck by Mark Manson", 
           "12 Rules For Life by Jordan Peterson",
           "Man’s Search for Meaning by Viktor Frankl",
           "Meditations by Marcus Aurelius",
           "The Book of Five Rings by Miyamoto Musashi",
           "Essentialism: The Disciplined Pursuit Of Less by Greg McKeown",
           "Thinking, Fast And Slow by Daniel Kahneman",
           "Getting More: How You Can Negotiate To Succeed In Work And Life by Stuart Diamond",
           "The Courage To Be Disliked by Ichiro Kishimi & Fumitake Koga",
           "The Power Of Positive Thinking by Norman Vincent Peale",
           "How To Win Friends And Influence People by Dale Carnegie",
           "Ikigai: The Japanese secret to a long and happy life by Francesc Miralles and Hector Garcia")
  return random.choice(books)