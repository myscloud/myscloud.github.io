from flask import Flask, render_template
from convert_num import convert_num_to_word
app = Flask(__name__)


@app.route("/")
def run_app():
    word = convert_num_to_word(3)
    return word

@app.route("/pink-page")
def pink_page():
    return render_template('convert-num-to-word.html')


if __name__ == "__main__":
    app.run()
