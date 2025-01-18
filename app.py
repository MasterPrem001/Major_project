import pickle
import pandas as pd
import requests
from flask import Flask,render_template,request,jsonify,redirect,session
from feature import feature

app = Flask(__name__)
app.secret_key= 'Cyber_buddy'
with open('Cyber_model.pkl','rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form.get('url')  # Get URL from user input
    try:
        if not url:
            return jsonify({'error': 'URL is Required'}), 400
        
        # putting that url into functions in feature.py and excuding label
        features = feature(url, label=0)[:-1] 

        # feature names used in the model during training
        feature_names = ['Having_IP', 'Having_At', 'URL_Length', 'URL_Depth', 'Redirect', 'Https_Domain', 'TinyURL', 'Prefix/Suffix']
        
        # making the features into a DataFrame to use that to predict the model 
        features_df = pd.DataFrame([features], columns=feature_names)
        #storing the output of prediction 
        prediction = model.predict(features_df)  
        #if prediction is phishing making a text output to show 
        if prediction[0] == 1:
            output= "Caution: The entered URL appears to be a phishing site"
            return jsonify({'prediction_bad': output})
        else:
            output= "The entered URL appears to be safe and legitimate"
            return jsonify({'prediction_good':output})
    #if some exception happend
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/info')
#rendering what is phishing page
def phishing():
    return render_template('info.html')


#rendering the chatbot made with ollama and hosted locally
AI_API = 'http://127.0.0.1:11434/api/generate'

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    # Initialize session variable for conversation history
    if 'conversation' not in session:
        session['conversation'] = []

    reply = ""  

    if request.method == 'POST':
        user_input = request.form.get('query')  # Get the user's query
        try:
            # Prepare data for the AI model (Gemma2:2b)
            prompt = f"{user_input} Answer in brief."
            template = {
                "model": "gemma2:2b",  
                "prompt": prompt,  
                "stream": False       
            }

            # Send request to Ollama model 
            response = requests.post(AI_API, json=template)

            if response.status_code != 200:
                reply = f"Error from AI model API: {response.text}"
            else:
                llm_response = response.json()
                reply = llm_response.get('response', 'No response from model')

            # Update conversation history in session
            session['conversation'].append({'user': user_input, 'bot': reply})

        except Exception as e:
            reply = f"Something went wrong: {str(e)}"
            session['conversation'].append({'user': user_input, 'bot': reply})

    # Render the chatbot template with conversation history
    return render_template('chatbot.html', conversation=session['conversation'], bot_reply=reply)


if __name__ == "__main__":
    app.run(debug=True)
