import discord
from numpy import random as rd

client = discord.Client()
e = discord.Embed(type='rich')

@client.event
async def on_ready():
    print('I have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!G'): # !Gx (x : nb de dés)
    	S=str(message.content)[2:]
    	N=0
    	if ',' not in S : # 1 lancer de groupement x : !NGx
	    	while N==0 and len(S)>0 :
		    	try :
	    			N = int(S)
	    		except :
	    			S=S[:-1]

	    	if len(S)<=0 or N==0:
	    		pass
	    	else: # Groupement non nul
	    		succes = rd.binomial(N, 0.5) # Probabilité de tomber sur un pair : 0.5
	    		e.add_field(value='1 groupement de {} dés.'.format(N), name=str(succes)+' succès.', inline=True)
	    		await message.channel.send(embed=e)
	    		e.remove_field(-1)

	    else : # n lancers d'un groupement x : !NGx,n
	    	str_group = ''
	    	while S[0] != ',' :
	    		str_group+=S[0]
	    		S=S[1:]
	    	nb_group=0
	    	while nb_group==0 and len(str_group)>0 :
		    	try :
		    		nb_group = int(str_group)
	    		except :
	    			str_group=str_group[:-1]

	    	if len(str_group)<=0 or nb_group==0:
	    		pass
	    	else: # Groupement non nul
		    	S=S[1:] # Supprimer la virgule
		    	nb_lancers=0
		    	while nb_lancers==0 and len(S)>0 :
			    	try :
		    			nb_lancers = int(S)
		    		except :
		    			S=S[:-1]

		    	if len(S)<=0 or nb_lancers==0 or nb_lancers==1: # 1 seul lancer du groupement
		    		succes = rd.binomial(nb_group, 0.5) # Probabilité de tomber sur un pair : 0.5
		    		e.add_field(value='1 groupement de {} dés.'.format(nb_group), name=str(succes)+' succès.', inline=True)
		    		await message.channel.send(embed=e)
		    		e.remove_field(-1)
		    	else: # nb lancers non nul et non 1
		    		succes = rd.binomial(nb_group, 0.5, size=nb_lancers) # Probabilité de tomber sur un pair : 0.5
		    		som = sum(succes)
		    		out=str(succes[0])
		    		for k in succes[1:] :
		    			out+=', '+str(k)
		    		e.add_field(value='{} groupements de {} dés.\n Détail : '.format(nb_lancers, nb_group)+out, name=str(som)+' succès.', inline=True)
		    		await message.channel.send(embed=e)
		    		e.remove_field(-1)


client.run('NzY1MzIyMjUwMjYxNjI2OTMw.X4TH4w.37cCduOUtFtGUG2Rar8-LFPI1DY')