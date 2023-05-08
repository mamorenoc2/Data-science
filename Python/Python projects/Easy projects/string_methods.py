highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
highlighted_poems_list = highlighted_poems.split(',')
highlighted_poems_stripped = []
# highlighted_poems_stripped = [highlighted_poems_stripped.append(i.strip()) for i in highlighted_poems_list]

for i in highlighted_poems_list:
    highlighted_poems_stripped.append(i.strip())

highlighted_poems_details = [i.split(':') for i in highlighted_poems_stripped]

titles = []
poets = []
dates = []

for i in highlighted_poems_details:
    titles.append(i[-3])
    poets.append(i[-2])
    dates.append(i[-1])

for i in range(0, len(highlighted_poems_details)):
    continue
    #print('The poem {title} was published by {poet} in {date}.'.format(title=titles[i], poet=poets[i], date=dates[i]))
