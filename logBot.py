import hikari

# Initialize an instance of GatewayBot
bot = hikari.GatewayBot(token='MY_TOKEN')

# Create a listener for a VoiceStateUpdate
@bot.listen(hikari.VoiceStateUpdateEvent)

# Event response
async def voice_update(event):
    # Get the username from this event
    username = await bot.rest.fetch_user(event.state.user_id)

    # If old_state == None, then user joined server
    if event.old_state == None:
        # Send user joined message
        await bot.rest.create_message(MY_CHANNEL_ID, f"{username} Joined the Server.")

    # If the new channel_id == None, then the user left the server
    elif event.state.channel_id == None:
        # Send user left message
        await bot.rest.create_message(MY_CHANNEL_ID, f"{username} Left the Server.")

# Start the bot
bot.run()
