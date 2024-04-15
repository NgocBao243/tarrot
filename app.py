from flask import Flask, render_template
import random

app = Flask(__name__)

# Define danh sách các lá bài Tarot
tarot_cards = [
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
    "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
    "The Devil", "The Tower", "The Star", "The Moon", "The Sun",
    "Judgement", "The World"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tarot')
def tarot():
    # Lựa chọn ngẫu nhiên một lá bài Tarot từ danh sách
    card = random.choice(tarot_cards)
    return render_template('tarot.html', card=card)

if __name__ == '__main__':
    app.run()