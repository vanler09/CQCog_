from question import QuestionCog

async def setup(bot):
    await bot.add_cog(QuestionCog(bot))
