# pokemon grinder v2 

Major changes between v1 and v2 is reading using message.content bots changed to user account which made the energy consumption of the grinder to half with increase efficiency 

This Pokemon auto catcher can be used only if the the pokemon bot doesn't use slash commands for catching.. which may make this autocather bot unusable after April 2022.. where the discord bot privacy policy changes the verified bots to use onlyslash commandss for communication


to use this bot run the file <a href="https://github.com/vichubenzene/Self_account_discord_bot/blob/main/pokemon_grinder/user%20account.py">User accounnt.py</a>.. and <a href="https://github.com/vichubenzene/Self_account_discord_bot/tree/main/pokemon_grinder/pokemon">Bot account</a> in other environment 

To make the pokemon spawn.. user spam bots <a href="https://github.com/vichubenzene/Self_account_discord_bot/blob/main/pokemon_grinder/spam.py">Spam.py</a> create it more for faster spawn..


alogorithm :

user account does not have permission to read the message contents sent by others... but it can read the its content when its is already sent.. using the channel.history() 

So when the poikemon spawns the user account gets history of the channel and gets the image link and downloads using python request and stores it in <a herf="https://github.com/vichubenzene/Self_account_discord_bot/tree/main/pokemon_grinder%20v2/classifier"> classifier folder </a> then  and using cv2 lib it finds the pokemon name from the data set i created like <a herf=-"https://github.com/vichubenzene/Self_account_discord_bot/blob/main/pokemon_grinder%20v2/%235%20-%20Charmeleon.png"> here </a> and sends it in the channel

I used 2 user accunts duel aginst each other.. which grinds 10 crds per battle, which made a avrg of 30,000 credits per day.. i didn't add the code here cuz they replaced emoji to buttons.. where buttons are ment for human press..

 <hr>
Hmmm...<br>

<h3>I lost intrest in this feild now.. i stoped trying to make it for work for slash commands and buttons</h3>

If you need more details and help join my <a href="https://discord.gg/jF879hKJ4y"> discord server</a> 
