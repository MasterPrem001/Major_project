import pickle
file = "conversation_history.pkl"

def load_convo():
    try:
        with open(file, 'rb') as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        return []

def save_convo(history):
    with open(file, 'wb') as f:
        pickle.dump(history, f)

conversation = load_convo()
user_input="So, there's this girl I'm chatting with. Do you think she loves me?"
reply="🗣 Koi tumse kyu pyar karega? "
conversation.append({'user': user_input, 'bot': reply})
save_convo(conversation)