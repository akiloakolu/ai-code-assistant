from flask import Flask, render_template, request

app = Flask(__name__)

def generate_response(prompt):
    prompt = prompt.lower()

    if "reverse a string" in prompt:
        return """Example in Python:

def reverse_string(s):
    return s[::-1]

Explanation:
This uses slicing to reverse the string."""
    
    elif "list comprehension" in prompt:
        return """Example:

squares = [x*x for x in range(5)]

Explanation:
List comprehension allows you to create lists in a concise way."""
    
    else:
        return "This is a sample AI response. You can later integrate OpenAI API for real responses."

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""

    if request.method == "POST":
        user_input = request.form["prompt"]
        response = generate_response(user_input)

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
