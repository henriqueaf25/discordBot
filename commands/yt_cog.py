# import discord
# from discord.ext import commands
# import youtube_dl
#
#
# class music_play(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
#         self.is_playing = False
#         self.music_queue = []
#         self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
#         self.FFMPEG_OPTIONS = {
#             'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5 -probesize 7M', 'options': '-vn'}
#         self.vc = ""
#
#     def search_yt(self, item):
#         with YoutubeDL(self.YDL_OPTIONS) as ydl:
#             try:
#                 info = ydl.extract_info("ytsearch:%s" %
#                                         item, download=False)['entries'][0]
#             except Exception:
#                 return False
#         return {'source': info['formats'][0]['url'], 'title': info['title']}
#
#     def play_next(self):
#         if len(self.music_queue) > 0:
#             self.is_playing = True
#             m_url = self.music_queue[0][0]['source']
#             self.music_queue.pop(0)
#             self.vc.play(discord.FFmpegPCMAudio(
#                 m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_nexy())
#         else:
#             self.is_playing = False
#
#     async def play_music(self, ctx):
#         if len(self.music_queue) > 0:
#             self.is_playing = True
#             m_url = self.music_queue[0][0]['source']
#
#             if self.vc == "" or not self.vc.is_connected():
#                 self.vc = await self.music_queue[0][1].connect()
#             else:
#                 try:
#                     self.vc = await self.bot.move_to(self.music_queue[0][1])
#                 except:
#                     print("")
#             await ctx.send(f"Tocando {self.music_queue[0][0]['title']}")
#             self.music_queue.pop(0)
#             self.vc.play(discord.FFmpegPCMAudio(
#                 m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
#         else:
#             self.is_playing = False
#
#     @commands.command(name='p', aliases=['play', 'buta'], help='Toca uma musica')
#     async def p(self, ctx, *args):
#         query = " ".join(args)
#
#         voice_channel = ctx.author.voice
#
#         if voice_channel is None:
#             await ctx.send("Entre numa sala primeiro pra querer ouvir música, parêa!")
#
#         else:
#             voice_channel = ctx.author.voice.channel
#             song = self.search_yt(query)
#             if type(song) == type(True):
#                 await ctx.send("Achei a música não. Sou especial")
#             else:
#                 if self.is_playing == True:
#                     await ctx.send("Música adicionada na fila!")
#                 self.music_queue.append([song, voice_channel])
#                 if self.is_playing == False:
#                     await self.play_music(ctx)
#
#     @commands.command(name='q', aliases=['queue'], help='Mostra as músicas na fila')
#     async def q(self, ctx):
#         retval = ""
#         for i in range(0, len(self.music_queue)):
#             retval += self.music_queue[i][0]['title'] + "\n"
#
#         print(retval)
#         if retval != "":
#             await ctx.send(retval)
#         else:
#             await ctx.send("Nenhuma música na fila!")
#
#     @commands.command(name='s', aliases=['skip', 'pula'], help='Pula uma música')
#     async def s(self, ctx):
#         if len(self.music_queue) == 0 and self.is_playing == False:
#             await ctx.send("Tem nada pra pular não, fedor de rabo")
#         elif len(self.music_queue) == 0 and self.is_playing == True:
#             if self.vc != "":
#                 await ctx.send("Parando de tocar")
#                 self.vc.stop()
#         else:
#             if self.vc != "":
#                 self.vc.stop()
#                 await self.play_music(ctx)
#
#
# def setup(bot):
#     bot.add_cog(music_play(bot))
