from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

word_list = [
    ("pizza", "It's a fast food made in slices."),
    ("beach", "Best place to see the sun and moon."),
    ("light", "Fastest thing in the solar system."),
    ("wifi", "Very important for IT people."),
    ("tata", "Famous Indian company.")
]

@app.route('/')
def index():
    word, hint = random.choice(word_list)
    return render_template("index.html", hint=hint, word_length=len(word), word=word)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
