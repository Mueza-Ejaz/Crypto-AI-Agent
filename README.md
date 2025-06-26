# CryptoDataAgent 

A conversational AI agent powered by Google Gemini (via OpenAI-style API), designed to deliver **live cryptocurrency prices** using the **Coinlore API**. Built with **Chainlit**, it provides an interactive chatbot experience.

---

##  Features

* 🔍 Get real-time crypto price updates (top 5 coins)
* 🤖 Uses Gemini-2.0-flash model (via OpenAI-compatible endpoint)
* 🔗 Coinlore API integration for market data
* 💬 Conversational UI powered by Chainlit
* 🧠 Extensible function tool support (you can add more tools)

---

## ⚙️ Prerequisites

Make sure you have the following installed:

* Python 3.8+
* `pip`
* Chainlit
* Requests
* Python-dotenv

---

## 🧩 Installation

```bash
git clone https://github.com/yourusername/crypto-agent.git
cd crypto-agent
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Create `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## 🚀 How to Run

```bash
chainlit run crypto_agent.py -w
```

This will start the Chainlit app on `localhost:8000` in your browser.

---

## 🧠 How it Works

1. Gemini API key is loaded from `.env`
2. Agent is created with one tool: `get_crypto_prices()`
3. When a user chats, the tool fetches data from the Coinlore API
4. Top 5 cryptocurrencies are shown with:

   * Name and Symbol
   * Rank
   * Price in USD and BTC
   * Market Cap

---

## 🛠 Tech Stack

* **Chainlit** – UI + Chat events
* **Gemini** (via OpenAI-style wrapper) – for natural language processing
* **Coinlore API** – crypto market data
* **Python** – logic & environment

---

## 🔧 Future Improvements

* [ ] Add Telegram bot support
* [ ] Add more tools like historical data, charts
* [ ] Improve message formatting (markdown, emojis)
* [ ] Cache responses for efficiency

---

## 🤝 Contribution

Want to improve it?

1. Fork the repo
2. Create a new branch
3. Make your changes
4. Push and open a PR 

---

Happy Crypto Chatting! 💰



