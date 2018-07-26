import random
import asyncio
import aiohttp
import json
import discord
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands



class ImperialGuard:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ig',
                description='About Imperial Guard',
                brief='About Imperial Guard',
                aliases=['imperial','IG','alliance','tig','TIG','Ig'])
    async def ig(self):
        embed=discord.Embed(title='The Imperial Guard', description='Imperial Guard is an red team alliance of orbis', color=0xff0000)
        embed.add_field(name="Founded", value="8 July 2018", inline=False)
        embed.add_field(name="Color", value="Red", inline=False)
        await self.bot.say(embed=embed)


    @commands.command(name='questions',
                description='Questions of Applicant',
                brief='Questions of Applicant',
                aliases=['Questions','question','Question'])
    async def questions(self):
        embed=discord.Embed(title='Questions of Applicant', color=0xff0000)
        embed.add_field(name=" Nation Name", value="Ans:", inline=False)
        embed.add_field(name="Why do you want to join us?", value="Ans:", inline=False)
        embed.add_field(name="Where did you hear from us?", value="Ans:", inline=False)
        embed.add_field(name=" How active are you (especially in Discord)?", value="Ans:", inline=False)
        embed.add_field(name="Are you willing to follow the instructions of the mods?", value="Ans:", inline=False)
        embed.add_field(name="Did you read the rules in #welcome", value="Ans:", inline=False)
        embed.add_field(name="Did you recently leave your old alliance? If yes, why?", value="Ans:", inline=False)
        await self.bot.say(embed=embed)

    @commands.command(name='rules',
                description='Rules of IG',
                brief='Rules of IG',
                aliases=['rule','Rule', 'Rules'],
                pass_context=True)
    async def rules(self,context):

        await self.bot.say('For rules of IG, please go to #welcome, '+ context.message.author.mention)

        

    @commands.command(name='applicant',
                description='Application form and quiry',
                brief='Application form and quiry',
                aliases=['Applicant','application', 'Application','join','Join'],
                pass_context=True)
    async def applicant(self,context):

        await self.bot.say('Awesome! Please apply for membership by answering the questions in #member-application, '+ context.message.author.mention)

    @commands.command(name='req',
                description='Requirments of applicant',
                brief='Requirments of applicant',
                aliases=['requirments','requirment','Requirment','requir','Requir'],
                pass_context=True)
    async def req(self,context):

        await self.bot.say('At least 5 cities and 15 days old of gametime, '+ context.message.author.mention)


    @commands.command(name='fa',
                description='FA inquiry',
                brief='FA inquiry',
                aliases=['FA','Fa','fA'],
                pass_context=True)
    async def fainq(self,context):

        await self.bot.say('The Imperial Guard is protected by NPO and GoTG. For more talk to @denia#8628  '+ context.message.author.mention)

    @commands.command(name='mask',
                description='To mask/ assign role',
                brief='To mask/ assign role',
                aliases=['Mask','role','Role','MASK','ROLE'],
                pass_context=True)
    async def maskme(self,context):

        await self.bot.say('State your alliance so that @Primarch will mask you soon, '+ context.message.author.mention)


    @commands.command(name='govt',
                description='How is the Imperial Guard governed?',
                brief='How is the Imperial Guard governed?',
                aliases=['Govt'],
                pass_context=True)
    async def govt(self,context):

        await self.bot.say('The Imperial Guard is governed by an Emperor, a High Lord and 4 Primarchs each governing over their respective departments, '+ context.message.author.mention)



    @commands.command(name='tax',
                description='Tax rate of IG',
                brief='Tax rate of IG',
                aliases=['Tax'],
                pass_context=True)
    async def tax(self,context):

        await self.bot.say('@Denia#8628 is tax freak. Please ask him, '+ context.message.author.mention)



    @commands.command(name='loan',
                description='Loan programs of IG',
                brief='Loan programs of IG',
                aliases=['Loan','loans','Loans'],
                pass_context=True)
    async def loan(self,context):

        await self.bot.say('IG gives loan upto 150 mil, depends on income, '+ context.message.author.mention)


    @commands.command(name='grant',
                description='City grants of IG',
                brief='City grants of IG',
                aliases=['Grant','grants','Grants'],
                pass_context=True)
    async def grant(self,context):

        await self.bot.say('IG gives funding up to 12 city, '+ context.message.author.mention)


    @commands.command(name='raid',
                description='Raid policy of IG',
                brief='Raid policy of IG',
                aliases=['Raid','raids','Raids'],
                pass_context=True)
    async def raid(self,context):

        await self.bot.say('Do not raid who is in a top 30 alliance, allied to a top 30 alliance or protected by a top 30 alliance, '+ context.message.author.mention)


    @commands.command(name='link',
                description='In-game link of IG',
                brief='In-game link of IG',
                aliases=['links','Link','Links'],
                pass_context=True)
    async def link(self,context):

        await self.bot.say('https://politicsandwar.com/alliance/id=4932')

def setup(bot):
    bot.add_cog(ImperialGuard(bot))
