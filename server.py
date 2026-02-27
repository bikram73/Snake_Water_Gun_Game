from flask import Flask, render_template, request, jsonify
import random

# Initialize Flask to serve HTML and static files (css/js) from the current folder
app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    user_choice = data.get('choice')
    
    options = ["Snake", "Water", "Gun"]
    comp_choice = random.choice(options)
    
    result = ""
    winner = "" # 'user', 'computer', or 'tie'
    
    if user_choice == comp_choice:
        result = "It's a Tie! 😐"
        winner = "tie"
    elif (user_choice == "Snake" and comp_choice == "Water") or \
         (user_choice == "Water" and comp_choice == "Gun") or \
         (user_choice == "Gun" and comp_choice == "Snake"):
        result = "You Win! 🎉"
        winner = "user"
    else:
        result = "Computer Wins! 🤖"
        winner = "computer"
        
    return jsonify({
        "user_choice": user_choice,
        "comp_choice": comp_choice,
        "result": result,
        "winner": winner
    })

if __name__ == '__main__':
    app.run(debug=True)