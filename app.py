from flask import Flask, render_template, request

app = Flask(__name__)


def count_vowels(text):
  vowels = "aeiouAEIOU"
  return sum(1 for char in text if char in vowels)


@app.route("/", methods=["GET", "POST"])
def index():
  vowel_count = None
  input_string = ""

  if request.method == "POST":
    input_string = request.form.get("text", "")
    vowel_count = count_vowels(input_string)

  return render_template(
      "index.html", vowel_count=vowel_count, input_string=input_string
  )


if __name__ == "__main__":
  app.run(debug=True)
