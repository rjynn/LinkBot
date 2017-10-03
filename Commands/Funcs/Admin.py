from Commands.CmdHelper import *
from Main.FileWriting import save_admins

# add/remove/list admins for the server in which the cmd was received
def cmd_admin(cmd):
    logging.info('Command: admin')

    # Check for args
    if len(cmd.args) == 0:
        cmd.OnSyntaxError('')
        return

    # Check for using cmd on server.
    if cmd.server is None:
        SendMessage(cmd.channel, 'You can only use this command in a server.')
        return

    if cmd.server.id not in link_bot.admins.keys():
        link_bot.admins[cmd.server.id] = list()

    # if "admin list"
    if cmd.args[0].lower() == "list":

        # Check for existing admins
        if len(link_bot.admins[cmd.server.id]) == 0:
            SendMessage(cmd.channel, 'There are no admins on this server.')
            return

        # get the admin names from their IDs, save them to a string, then send it to the channel.
        admins = 'Admins: '
        needs_comma = False
        for member in cmd.server.members:
            if member.id in link_bot.admins[cmd.server.id]:
                if needs_comma:
                    admins += ', '
                admins += member.name
                needs_comma = True
        SendMessage(cmd.channel, admins)
        logging.info("Listed admins.")

    # if "admin add"
    elif cmd.args[0].lower() == "add":

        # Check that the sender is an admin
        if not IsAdmin(cmd.author):
            SendMessage(cmd.channel, "You must be an admin to use this command.")
            return

        # the output cmd at the end.
        msg = ''

        # if there is a member mention, add them as an admin.
        for member in cmd.message.mentions:
            if member.id in link_bot.admins[cmd.server.id]:
                msg += member.display_name + " is already an admin.\n"
            else:
                link_bot.admins[cmd.server.id].append(member.id)
                msg += "Added " + member.display_name + " as an admin.\n"

        # if there is a role mention, add all members with that role as an admin.
        for role in cmd.message.role_mentions:
            for member in cmd.server.members:
                if role in member.roles:
                    if member.id in link_bot.admins[cmd.server.id]:
                        msg += member.display_name + " is already an admin.\n"
                    else:
                        link_bot.admins[cmd.server.id].append(member.id)
                        msg += "Added " + member.display_name + " as an admin.\n"
        # output
        save_admins()
        SendMessage(cmd.channel, msg)
        logging.info("Added admins.")

    # if "admin remove"
    elif cmd.args[0].lower() == "remove":

        # Check that the sender is an admin.
        if not IsAdmin(cmd.author):
            SendMessage(cmd.channel, "You must be an admin to use this command.")
            return

        # the output message at the end.
        msg = ''

        # if there is a member mention, add them as an admin.
        for member in cmd.message.mentions:
            if member.id not in link_bot.admins[cmd.server.id]:
                msg += member.display_name + " is not an admin.\n"
            else:
                link_bot.admins[cmd.server.id].remove(member.id)
                msg += "Removed " + member.display_name + " from the admin list.\n"

        # if there is a role mention, add all members with that role as an admin.
        for role in cmd.message.role_mentions:
            for member in cmd.server.members:
                if role in member.roles:
                    if member.id not in link_bot.admins[cmd.server.id]:
                        msg += member.display_name + " is not an admin.\n"
                    else:
                        link_bot.admins[cmd.server.id].remove(member.id)
                        msg += "Removed " + member.display_name + " from the admin list.\n"
        # output
        save_admins()
        SendMessage(cmd.channel, msg)
        logging.info("Removed admins.")

    # if "admin ..."
    else:
        SendMessage(cmd.channel, '{0} is not a valid argument.'.format(cmd.args[0]))
