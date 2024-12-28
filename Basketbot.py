from discord.ext import commands
import discord
import http.client
import json

BOT_TOKEN = ''
CHANNEL_ID = 

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Hello! Basketbot is ready!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello! Basketbot is ready")


@bot.command()
async def standings(ctx):
    conn = http.client.HTTPSConnection("api.sportradar.us")
    payload = ''
    headers = {}
    conn.request("GET", "/nba/trial/v8/en/seasons/2023/REG/rankings.json?api_key=yyakuvd7tkkt3jh3ccnx3dhz", payload, headers)
    res = conn.getresponse()
    data = res.read()

    # Parse JSON
    parsed_data = json.loads(data)

    # Function to get top 8 teams from a conference
    def get_top_teams(conference):
        teams = []
        for division in conference['divisions']:
            for team in division['teams']:
                teams.append((team['name'], team['rank']['conference']))
        teams.sort(key=lambda x: x[1])  # Sort teams by conference rank
        return [team[0] for team in teams[:10]]  # Get top 8 teams

    # Get top 8 teams from each conference
    eastern_conference = parsed_data['conferences'][0]
    western_conference = parsed_data['conferences'][1]

    top_eight_eastern = get_top_teams(eastern_conference)
    top_eight_western = get_top_teams(western_conference)

    # Output
    await ctx.send("Top 10 teams in the Eastern Conference:")
    for i, team in enumerate(top_eight_eastern, 1):
        await ctx.send(f"{i}. {team}")

    await ctx.send("\nTop 10 teams in the Western Conference:")
    for i, team in enumerate(top_eight_western, 1):
        await ctx.send(f"{i}. {team}")


@bot.command()
async def TeamLeaders(ctx, TeamAbb):
    conn = http.client.HTTPSConnection("api.sportradar.us")
    payload = ''
    headers = {}
    conn.request("GET", "/nba/trial/v8/en/seasons/2023/REG/rankings.json?api_key=yyakuvd7tkkt3jh3ccnx3dhz", payload, headers)
    res = conn.getresponse()
    data = res.read().decode('utf-8')  # Decode the bytes to a string

    # Parse JSON data
    parsed_data = json.loads(data)

    # Function to find team ID by name
    def find_team_id_by_name(data, TeamAbb):
        for team in parsed_data['conferences']:
            for division in team['divisions']:
                for t in division['teams']:
                    if t['name'] == TeamAbb:
                        return t['id']
        return None

    team_id = find_team_id_by_name(parsed_data, TeamAbb)

    conn.request("GET", f"/nba/trial/v8/en/seasons/2023/REG/teams/{team_id}/statistics.json?api_key=yyakuvd7tkkt3jh3ccnx3dhz", payload, headers)
    res = conn.getresponse()
    data1 = res.read().decode('utf-8')  # Decode the bytes to a string

    # Parse JSON data
    parsed_data1 = json.loads(data1)

    # Sort players based on points scored
    sorted_players = sorted(parsed_data1['players'], key=lambda x: x['total']['points'], reverse=True)

    # Extract top 5 players
    top_5_scorers = sorted_players[:5]

    # Print information for top 5 scorers
    standings_info = "Top 5 Scorers:\n"
    for player in top_5_scorers:
        name = player['full_name']
        points = player['total']['points']
        assists = player['total']['assists']
        rebounds = player['total']['rebounds']
        games_played = player['total']['games_played']
        points_per_game = player['average']['points']
        assists_per_game = player['average']['assists']
        rebounds_per_game = player['average']['rebounds']
        standings_info += f"{name}: Points - {points} ({points_per_game} per game), Assists - {assists} ({assists_per_game} per game), Rebounds - {rebounds} ({rebounds_per_game} per game), Games Played - {games_played}\n"
    
    await ctx.send(standings_info)

bot.run(BOT_TOKEN)
