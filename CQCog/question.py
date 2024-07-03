from redbot.core import commands 

liste_questions= [
"1  Le patriarcat existe : ",
"2  Le travail domestique doit être reconnu et compensé : ",
"3  L'hétérosexualité est une norme sociale inchangeable : ",
"4  Il faut apprendre le consentement dès l'école : ",
"5  Les femmes subissent une très forte pression sociale pour enfanter : ",
"6  Il faut renforcer les dispositifs de protection et d'accompagnement des personnes trans :",
"7  L’idéologie LGBTQIA+ existe : ",
"8  Les athlètes trans doivent pouvoir participer de manière inconditionnelle aux compétitions sportives : ",
"9  Les établissements scolaires devraient supprimer les toilettes genrées : ",
"10  L'école doit être inclusive politiquement et techniquement : elle doit accueillir tous les enfants, indépendamment de toute forme de handicap : ",
"11  Faire des fautes d'orthographe, de grammaire et de syntaxe nuit à l'argumentation : ",
"12  Il faut régulariser tous les étrangers et leur accorder le droit de vote : ",
"13  Il est légitime d'être nationaliste kanak ou nationaliste berbère : ",
"14  Il faut conserver et développer le nucléaire civil : ",
"15  Mon pays doit payer pour réparer les dégâts causés par les crimes qu'il a commis à l'étranger : ",
"16  L'écriture inclusive est une menace pour la langue française : ",
"17  Toute tradition doit pouvoir être remise en question : ",
"18  Il est raciste et sexiste d'interdire le port du voile en France : ",
"19  La peine de mort n'est jamais justifiable : ",
"20  Le principe *mon corps, mon choix* doit déterminer toute réglementation sur l'avortement : ",
"21  La très grande majorité des détenu·es n'a pas besoin d'être incarcérée dans des établissements pénitentiaires fermés : ",
"22  Les personnes sortant de prison doivent bénéficier d'un accompagnement rigoureux : ",
"23  La police doit être armée : ",
"24  Les peines lourdes sont efficaces car elles sont dissuasives : ",
"25  La Russie est pleinement responsable du conflit actuel avec l'Ukraine : ",
"26  Une campagne de vaccination est préférable au risque d'épidémie : " ]

class QuestionCog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def Questions(self, ctx):
        res=[]
        liste_emoji=[' ^|^e',' ^=^q^m', ' ^=^q^n',' ^}^l']
        global liste_questions
        for question in liste_questions:
            message = await ctx.send(question)
            for emoji in liste_emoji:
                await message.add_reaction(emoji)
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=180.0)
            except asyncio.TimeoutError:
                await ctx.send("l utilisateur n a pas r  agit au message en temps impartit(3 minutes)")
            else:
                if str(reaction.emoji)==' ^|^e':
                    res.append(f'{question} **Absolument**')
                elif str(reaction.emoji)==' ^=^q^m':
                    res.append(f'{question}**Oui**')
                elif str(reaction.emoji)==' ^=^q^n':
                    res.append(f'{question}**Non**')
                else:
                    res.append(f'{question}**Absolument pas')
        for reponse in res:
            await ctx.send(reponse)
