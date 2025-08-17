# Boomer-AI_Assistant
A conversational AI assistant built using Natural Language Processing (NLP) and Machine Learning techniques. It is trained on a custom intents.json dataset, which maps user queries to predefined tags and responses. The assistant is capable of understanding user input, predicting the correct intent, and providing contextually relevant answers
** 1. main.py**
Purpose: This is the entry point for your chatbot application.
**What it does:**
Loads your trained model (chat_model.h5) and tokenizer/pickle files.
Opens intents.json to understand the predefined intents and responses.
Accepts user input (via text or voice).
Passes input through the trained model → predicts intent → selects the right response.
Returns the chatbot’s answer back to the UI (HTML/Streamlit).
Think of it as: The brain + communication layer that connects the ML model with your front end.
 **2. train_model.py**
Purpose: Used for training your chatbot model.
**What it does:**
Reads intents.json.
Tokenizes and pads training sentences.
Creates a Neural Network model (Embedding → GlobalAveragePooling → Dense layers).
Compiles and trains the model on the dataset.
Saves the trained model (chat_model.h5) and tokenizer (tokenizer.pkl) for later use.
Think of it as: The trainer that teaches your chatbot how to understand and respond.
 **3. test_model.py**
Purpose: Used for testing your trained model before deploying.
**What it does:**
Loads the model, tokenizer, and intents.json.
Lets you type test inputs directly in terminal.
Predicts intent & shows chatbot’s response.
Think of it as: The examiner where you test if your chatbot gives the right answers.
 **4. intents.json**
Purpose: This is the knowledge base of your chatbot.
**What it contains:**
A collection of intents (categories of user requests).
Each intent has:
"tag" → the intent name (example: "greeting", "goodbye", "machine_learning").
"patterns" → sample user inputs (example: "hi", "hello", "how are you?").
"responses" → chatbot replies (example: "Hello! How can I help you today?").
Think of it as: The dictionary that tells the model what to say when a user asks something.
**Putting It All Together**
You train the model using train_model.py.
Generates chat_model.h5 + tokenizer.pkl.
You test the model with test_model.py.
Ensures it works properly.
You run the chatbot with main.py.
Connects with either a HTML UI (Flask) or Streamlit app.
You customize responses by editing intents.json.
Add/remove topics anytime.
