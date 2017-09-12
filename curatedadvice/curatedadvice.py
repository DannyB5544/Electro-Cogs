
import discord
import MySQLdb
from discord.ext import commands
from cogs.utils import checks

class dankmemes:
    """Dem Gosh Darn Dank Memes"""

    def __init__(self, bot):
        self.bot = bot
   

    @commands.command()
    async def dankmemes(self):
        """Grab The Newest Dank Meme!"""


        #Your code will go here
        db = MySQLdb.connect(host="theendlessweb.com",    # your host, usually localhost
                     user="electrom_dankmemesuser",         # your username
                     passwd="DankMemes",  # your password
                     db="electrom_dankmemes")
        cur = db.cursor()
        cur.execute("SELECT advice from advice ORDER BY id desc LIMIT 1")
        newmsg = cur.fetchall()
        printout = str(newmsg) [3:-5]
        await self.bot.say(printout) 
        db.close()
        
    @commands.command()
    async def submitmemes(self, link):
        """Submit memes. Or Dank ones."""
        
        
        
        db = MySQLdb.connect(host="theendlessweb.com",    # your host, usually localhost
                     user="electrom_dankmemesuser",         # your username
                     passwd="DankMemes",  # your password
                     db="electrom_dankmemes")
        cur = db.cursor()
        cur.execute("INSERT INTO submitadvice (link) VALUES (\"{}\")".format(link))
        db.commit()
        await self.bot.say("Your Meme has been Submitted!")
        db.close()
        
    @commands.command()
    @checks.admin()
    async def graballmemes(self):
        """An Admin Command to grab all memes and IDs to remove them"""
        
        
        
        db = MySQLdb.connect(host="theendlessweb.com",    # your host, usually localhost
                     user="electrom_dankmemesuser",         # your username
                     passwd="DankMemes",  # your password
                     db="electrom_dankmemes")
                     
        cur = db.cursor()
        cur.execute("SELECT advice, id from advice ORDER BY id desc")
        msg = cur.fetchall()
        await self.bot.say(msg)
        db.close()
        
    @commands.command()
    @checks.admin()
    async def deletememe(self, id):
        """Delete a meme based on ID"""
        
        db = MySQLdb.connect(host="theendlessweb.com",    # your host, usually localhost
                     user="electrom_dankmemesuser",         # your username
                     passwd="DankMemes",  # your password
                     db="electrom_dankmemes")
                     
        cur = db.cursor()
        cur.execute("DELETE FROM advice WHERE id=\"{}\";".format(id))
        db.commit()
        await self.bot.say("Meme Deleted")
        db.close()
        
    @commands.command()
    @checks.admin()
    async def editmemeid(self, oldid, newid):
        """Change the ID of a Meme to make it first"""
        
        
        db = MySQLdb.connect(host="theendlessweb.com",    # your host, usually localhost
                     user="electrom_dankmemesuser",         # your username
                     passwd="DankMemes",  # your password
                     db="electrom_dankmemes")
                     
        cur = db.cursor()
        cur.execute("UPDATE advice SET id = \"{}\" WHERE id = \"{}\"".format(newid, oldid))
        db.commit()
        await self.bot.say("Meme has been updated")
        db.close()
    
        

def setup(bot):
    bot.add_cog(dankmemes(bot))