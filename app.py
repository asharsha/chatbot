from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def load_dataset(file_path):
    dataset = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            user_input, chatbot_response = line.strip().split('\t')  # Change '\t' to your actual delimiter
            dataset[user_input.lower()] = chatbot_response
    return dataset

# Load the dataset into memory
dataset_path = 'responses.txt'  # Update with your dataset file path
responses_dataset = load_dataset(dataset_path)

def get_chatbot_response(user_input):
    return responses_dataset.get(user_input.lower(), 'I did not understand that.')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']

    # Get chatbot response
    gpt_response = get_chatbot_response(user_input)

    return jsonify({'gpt_response': gpt_response})

if __name__ == '__main__':
    app.run(debug=True)
