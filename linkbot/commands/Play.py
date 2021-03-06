from linkbot.utils.cmd_utils import *


@command(
    ["{c}"],
    "Plays something in voice chat with you!",
    [
        ("play", "Bot joins the voice channel with you.")
    ]
)
@restrict(DISABLE | SERVER_ONLY, "Not currently implemented")
async def play(cmd: Command):
    voice = cmd.author.voice
    if voice.voice_channel is None:
        raise CommandSyntaxError( "You need to be in a voice channel.")

    inSameServer = False
    vc = None
    inSameChannel = False

    # find out if we're in the same server/channel as our inviter.
    for voiceClient in client.voice_clients:
        if voiceClient.server == voice.voice_channel.server:
            inSameServer = True
            vc = voiceClient
        if voiceClient.channel == voice.voice_channel:
            inSameChannel = True

    # join the voice channel, either by moving from the current one, or by creating a new voice client.
    if not inSameChannel:
        if inSameServer:
            vc.move_to(voice.voice_channel)
        else:
            client.join_voice_channel(voice.voice_channel)
