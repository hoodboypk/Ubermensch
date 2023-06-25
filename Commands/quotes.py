import random

def generate_quotes():
  quotes = ("There is nothing outside of yourself that can ever enable you to get better, stronger, richer, quicker, or smarter. Everything is within. Everything exists. Seek nothing outside of yourself.\n ~ Miyamoto Musashi", 
            "Think lightly of yourself and deeply of the world.\n ~ Miyamoto Musashi", 
            "Philosophy is a battle against the bewitchment of our intelligence by means of language.\n ~ Ludwig Wittgenstein", 
            "Well, I must endure the presence of a few caterpillars if I wish to become acquainted with the butterflies.\n ~ Antoine de Saint-Exupéry", 
            "The highest activity a human being can attain is learning for understanding, because to understand is to be free.\n ~ Baruch Spinoza", 
            "Both in fighting and in everyday life you should be determined though calm. Meet the situation without tenseness yet not recklessly, your spirit settled yet unbiased. Even when your spirit is calm do not let your body relax, and when your body is relaxed do not let your spirit slacken. Do not let your spirit be influenced by your body, or your body be influenced by your spirit.\n ~ Miyamoto Musashi", 
            "The unexamined life is not worth living. \n ~ Socrates", 
            "Polish your wisdom: learn public justice, distinguish between good and evil, study the ways of different arts one by one. \n ~ Miyamoto Musashi")
  return random.choice(quotes)