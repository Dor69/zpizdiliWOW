
# Wowhead News Telegram Bot

This is a Telegram bot that parses news from the [Wowhead Retail News](https://www.wowhead.com/wow/retail) section and sends updates to users who subscribe to the bot. The bot allows users to:
- View the 3 latest news articles.
- View the latest news article.
- Subscribe to news updates.
- Unsubscribe from news updates.

## Project Structure

```
wowhead-news-bot/
├── bot.py                   # Main file to run the Telegram bot
├── parser.py                # Contains functions for parsing news from Wowhead
├── .gitignore               # Ignores unnecessary files for version control
├── README.md                # Project documentation
```

## Prerequisites

- Python 3.7 or higher.
- Telegram Bot API token. You can get it from [@BotFather](https://t.me/BotFather) on Telegram.
- A Telegram account to interact with the bot.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/dor69/zpizdiliWOW.git
   cd zpizdiliWOW
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` doesn't exist, you can manually install the required packages:

   ```bash
   pip install pyTelegramBotAPI beautifulsoup4 requests
   ```

4. Create a `.env` file to store your Telegram API token:

   ```env
   API_TOKEN=YOUR_TELEGRAM_API_TOKEN
   ```

   Replace `YOUR_TELEGRAM_API_TOKEN` with the token you received from [@BotFather](https://t.me/BotFather).

## Usage

1. Run the bot:

   ```bash
   python bot.py
   ```

2. Open Telegram and search for your bot. Start the conversation by typing `/start`. You'll see options to:
   - View the 3 latest news.
   - View the latest news.
   - Subscribe to news updates.
   - Unsubscribe from news updates.

   If subscribed, you will receive new news notifications automatically every 10 minutes.

## How It Works

- **Parsing**: The bot uses BeautifulSoup to scrape the Wowhead Retail news page. It skips the first 3 pinned articles and starts parsing from the 4th news item.
- **Subscribing**: Users can subscribe to receive the latest news updates every 10 minutes.
- **Bot Commands**:
  - `/start`: Displays the main menu.
  - `Вывести 3 последних новости`: Displays the last 3 news articles.
  - `Вывести последнюю новость`: Displays the most recent news article.
  - `Подписаться на рассылку`: Subscribes the user to regular updates.
  - `Отписаться от рассылки`: Unsubscribes the user from updates.
