# Basketbot Discord Bot

## Overview
Basketbot is a Discord bot designed to provide NBA standings and team statistics in real-time. It leverages the Sportradar API to fetch and display data, giving users a seamless way to interact with NBA stats directly within a Discord server.

---

## Features

### 1. Bot Initialization
- **Greeting:** Upon startup, Basketbot sends a message to a specified channel indicating it is ready for use.

### 2. Standings Command (`!standings`)
- **Functionality:** Displays the top 10 teams from both the Eastern and Western Conferences.
- **Details:**
  - Fetches NBA rankings for the 2023 regular season from the Sportradar API.
  - Parses and organizes teams by conference rank.
  - Outputs the top 10 teams from each conference in a ranked list format.

### 3. Team Leaders Command (`!TeamLeaders <TeamAbb>`)
- **Functionality:** Provides a detailed breakdown of the top 5 players for a specified NBA team based on scoring.
- **Details:**
  - Accepts a team's abbreviation (e.g., `LAL` for Los Angeles Lakers) as input.
  - Fetches the team ID and associated player statistics from the Sportradar API.
  - Outputs key statistics for the top 5 scorers, including:
    - **Points:** Total and per game.
    - **Assists:** Total and per game.
    - **Rebounds:** Total and per game.
    - **Games Played.**

---

## Dependencies
- **Libraries:**
  - `discord` and `discord.ext.commands` for Discord bot functionality.
  - `http.client` for API communication.
  - `json` for parsing and processing API responses.

---

## Usage
1. **Start the bot:** Run the script with a valid Discord bot token and a specified channel ID.
2. **Commands:**
   - `!standings`: Retrieves and displays the top 10 teams in the Eastern and Western Conferences.
   - `!TeamLeaders <TeamAbb>`: Retrieves and displays statistics for the top 5 scorers of the specified team.

---

## Example Output

### Command: `!standings`

