# AutoCircuit

AutoCircuit is a tool I built to convert english descriptions of digital logic circuits into circuit specifications. It outputs logic expressions, truth tables, and ASCII diagrams. You tell it what the circuit should do, and it gives you a clean breakdown.

It uses Streamlit for the frontend and pulls responses from Google’s Gemini API.  
The backend is managed with SQL.

---

## What It Does

- Classifies the circuit as combinational or sequential  
- Gives a short explanation  
- Outputs a logic expression or HDL-style pseudocode  
- Shows a simple truth table  
- Draws a basic ASCII circuit diagram  

It’s designed to help students, hardware people, or anyone wanting to sketch out digital designs quickly and effectively.

---

## Backend

Every interaction is logged in a local SQLite database. It tracks:
- number of inputs  
- behavior description  
- sync/async flag  
- generated response  
- user feedback on whether the response was accurate  

It also calculates and displays a live model accuracy score on the frontend.

All test cases are stored in the database (`response_log.db`) instead of a separate file.

---

## How to Run It

1. Clone the repo:
   ```bash
   git clone https://github.com/kush1434/autocircuit.git
   cd autocircuit
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your API key:
   ```env
   GEMINI_API_KEY=api-key
   ```

4. Start the app:
   ```bash
   streamlit run main.py
   ```

---

## Credits

- Frontend and AI responses are powered by [Streamlit](https://streamlit.io/) and [Google Gemini API](https://deepmind.google/technologies/gemini).
- Prompting, backend logic, and debugging assistance supported by [ChatGPT](https://openai.com/chatgpt).
