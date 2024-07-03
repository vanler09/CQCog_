from redbot.core import commands 
import sys
import asyncio

sys.path.append('/home/vanler/Red-DiscordBot/cogs/CQCog')

liste_questions= [
"1  Le patriarcat existe : ",
"2  Le travail domestique doit   tre reconnu et compens   : ",
"3  L'h  t  rosexualit   est une norme sociale inchangeable : ",
"4  Il faut apprendre le consentement d  s l'  cole : ",
"5  Les femmes subissent une tr  s forte pression sociale pour enfanter : ",
"6  Il faut renforcer les dispositifs de protection et d'accompagnement des personnes trans :",
"7  L ^`^yid  ologie LGBTQIA+ existe : ",
"8  Les athl  tes trans doivent pouvoir participer de mani  re inconditionnelle aux comp  titions sportives : ",
"9  Les   tablissements scolaires devraient supprimer les toilettes genr  es : ",
"10  L'  cole doit   tre inclusive politiquement et techniquement : elle doit accueillir tous les enfants, ind  pendamment de toute forme de handicap : ",
"11  Faire des fautes d'orthographe, de grammaire et de syntaxe nuit    l'argumentation : ",
"12  Il faut r  gulariser tous les   trangers et leur accorder le droit de vote : ",
"13  Il est l  gitime d'  tre nationaliste kanak ou nationaliste berb  re : ",
"14  Il faut conserver et d  velopper le nucl  aire civil : ",
"15  Mon pays doit payer pour r  parer les d  g  ts caus  s par les crimes qu'il a commis    l'  tranger : ",
"16  L'  criture inclusive est une menace pour la langue fran  aise : ",
"17  Toute tradition doit pouvoir   tre remise en question : ",
"18  Il est raciste et sexiste d'interdire le port du voile en France : ",
"19  La peine de mort n'est jamais justifiable : ",
"20  Le principe *mon corps, mon choix* doit d  terminer toute r  glementation sur l'avortement : ",
"21  La tr  s grande majorit   des d  tenu  es n'a pas besoin d'  tre incarc  r  e dans des   tablissements p  nitentiaires ferm  s : ",
"22  Les personnes sortant de prison doivent b  n  ficier d'un accompagnement rigoureux : ",
"23  La police doit   tre arm  e : ",
"24  Les peines lourdes sont efficaces car elles sont dissuasives : ",
"25  La Russie est pleinement responsable du conflit actuel avec l'Ukraine : ",
"26  Une campagne de vaccination est pr  f  rable au risque d'  pid  mie : " ]

ch_message_intro="Test d'entr  e au SD. Pour r  pondre, il suffit de r  agir aux messages avec les emojis propos  e,  ^|^e  pour absoluement d'accord,  ^=^q^>

class QuestionCog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def Questions(self, ctx):
        res=[]
        global message_intro
        message_intro=await ctx.send(ch_message_intro)
        user=ctx.author
        liste_emoji=[' ^|^e',' ^=^q^m', ' ^=^q^n',' ^}^l']
        nb_
        global liste_questions
        flag=False
        for question in liste_questions:
            await asyncio.sleep(1)
            message = await ctx.send(question)
            for emoji in liste_emoji:
                await message.add_reaction(emoji)
            def check(reaction,reacting_user):
                return reacting_user==user and reaction.message.id==message.id
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=180.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send("l'utilisateur n'a pas r  agit au message en temps impartit (3 minutes)")
                flag=False
                break
            else:
                if str(reaction.emoji)==' ^|^e':
                    res.append(f'{question} **Absolument**')
                elif str(reaction.emoji)==' ^=^q^m':
                    res.append(f'{question}**Oui**')
                elif str(reaction.emoji)==' ^=^q^n':
                    res.append(f'{question}**Non**')
                else:
                    res.append(f'{question}**Absolument pas**')
                await message.delete()
        await message_intro.delete()
        for reponse in res:
            if flag:
                break
            await ctx.send(reponse)
            await asyncio.sleep(2)
