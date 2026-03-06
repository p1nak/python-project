from flask import Flask, request, jsonify, render_template
import json
from ollama import chat

app = Flask(__name__)

NOTES_FILE = "notes.json"

# Load existing notes
def load_notes():
    try:
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    except:
        return []

# Save notes
def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save_note():
    data = request.get_json()
    notes = load_notes()
    notes.append(data)
    save_notes(notes)
    return jsonify({"message": "Note saved successfully!"})

@app.route("/notes", methods=["GET"])
def get_notes():
    notes = load_notes()
    return jsonify(notes)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    note = data.get('note', '')

    # Use Ollama/Mistral (or OpenAI) to summarize
    response = chat( 
    model="mistral",
    messages=[
        {"role": "system", "content": "Summarize the following note in 2-3 lines."},
        {"role": "user", "content": note}
    ]
    )

    summary = response['message']['content']
    return jsonify({'summary': summary})

if __name__ == "__main__":
    print("🟢 Flask server running at http://localhost:5000")
    app.run(debug=True)
