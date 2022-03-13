acronyms = ['LOL', 'IDK', 'TBH']
translations = ['laugh out loud', "I don't know", 'to be honest']

del acronyms[0]
del translations[0]

print(acronyms)
print (translations)


acronyms = {'LOL': 'laugh out loud',
            'IDK': "I don't know",
            'TBH': 'to be honest'}

print(acronyms['LOL'])

acronyms['LOL']= 'laugh out loud'
acronyms['IDK'] = "I don't know"
print(acronyms)
