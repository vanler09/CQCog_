from redbot.core import commands 
import sys
import asyncio

sys.path.append('/home/vanler/Red-DiscordBot/cogs/CQCog')

liste_questions= [
("1  Le patriarcat existe : ", "g"),
("2  Le travail domestique doit   tre reconnu et compens   : ","g" ),
("3  L'h  t  rosexualit   est une norme sociale inchangeable : ", "d"),
("4  Il faut apprendre le consentement d  s l'  cole : ", "g"),
("5  Les femmes subissent une tr  s forte pression sociale pour enfanter : ","g"),
("6  Il faut renforcer les dispositifs de protection et d'accompagnement des personnes trans :","g"),
("7  L ^`^yid  ologie LGBTQIA+ existe : ", "d"),
("8  Les athl  tes trans doivent pouvoir participer de mani  re inconditionnelle aux comp  titions sportives : ","g"),
("9  Les   tablissements scolaires devraient supprimer les toilettes genr  es : ","g"),
("10  L'  cole doit   tre inclusive politiquement et techniquement : elle doit accueillir tous les enfants, ind  pendamment de toute forme de handicap : ","g"),
("11  Faire des fautes d'orthographe, de grammaire et de syntaxe nuit    l'argumentation : ","d"),
("12  Il faut r  gulariser tous les   trangers et leur accorder le droit de vote : ","g"),
("13  Il est l  gitime d'  tre nationaliste kanak ou nationaliste berb  re : ","g"),
("14  Il faut conserver et d  velopper le nucl  aire civil : ","g"),
("15  Mon pays doit payer pour r  parer les d  g  ts caus  s par les crimes qu'il a commis    l'  tranger : ","g"),
("16  L'  criture inclusive est une menace pour la langue fran  aise : ","d"),
("17  Toute tradition doit pouvoir   tre remise en question : ","g"),
("18  Il est raciste et sexiste d'interdire le port du voile en France : ","g"),
("19  La peine de mort n'est jamais justifiable : ","g"),
("20  Le principe *mon corps, mon choix* doit d  terminer toute r  glementation sur l'avortement : ","g"),
("21  La tr  s grande majorit   des d  tenu  es n'a pas besoin d'  tre incarc  r  e dans des   tablissements p  nitentiaires ferm  s : ","g"),
("22  Les personnes sortant de prison doivent b  n  ficier d'un accompagnement rigoureux : ",'g'),
("23  La police doit   tre arm  e : ","d"),
("24  Les peines lourdes sont efficaces car elles sont dissuasives : ","d"),
("25  La Russie est pleinement responsable du conflit actuel avec l'Ukraine : ","g"),
("26  Une campagne de vaccination est pr  f  rable au risque d'  pid  mie: ","g")]

ch_message_intro="Test d'entr  e au SD. Pour r  pondre, il suffit de r  agir aux messages avec les emojis propos  e,  ^|^e  pour absolument d'accord,  ^=^q^m  pour relativement d'accord, ^=^q^n pour rela>

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
        global liste_questions
        resultat=len(liste_questions)*2
        flag=False
        for question,position in liste_questions:
            await asyncio.sleep(1)                                                                                    question.py                                                                                              
            message = await ctx.send(question)
            for emoji in liste_emoji:
                await message.add_reaction(emoji)
            def check(reaction,reacting_user):
                return reacting_user==user and reaction.message.id==message.id
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=180.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send("l'utilisateur n'a pas réagit au message en temps impartit (3 minutes)")
                flag=False
                break
            else:
                if str(reaction.emoji)==' ^|^e':
                    res.append(f"{question} **Absolument d'accord**")
                    if position=='g':
                        resultat+=2
                    else:
                        resultat-=2
                elif str(reaction.emoji)==' ^=^q^m':
                    res.append(f"{question}**Relativement d'accord**")
                    if position=='g':
                        resultat+=1
                    else:
                        resultat-=1
                elif str(reaction.emoji)==' ^=^q^n':
                    res.append(f"{question}**Relativement pas d'accord**")
                    if position=='d':
                        resultat+=1
                    else:
                        resultat-=1
                else:
                    res.append(f"{question}**Absolument pas d'accord**")
                    if position=='d':
                        resultat+=2
                    else:
                        resultat-=2

                await message.delete()
        await message_intro.delete()
        for reponse in res:
            if flag:
                break
            await ctx.send(reponse)
            await asyncio.sleep(1)
        pourcentage=resultat*100//(len(liste_questions)*4)
        await ctx.send(f"# Résultats: {str(pourcentage)}% de gauchisme, certifié Serveur De Gauche®  ")
        
    
