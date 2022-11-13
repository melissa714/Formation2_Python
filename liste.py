liste=[x for x in range(5)]
nouvelle_liste=[2* x for x in liste]
print(liste)
print(nouvelle_liste)

listes = ["hello", "the", "world"]
nvle=[len(x) for x in listes]
print(nvle)


for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    print(item)
    print(type(item))