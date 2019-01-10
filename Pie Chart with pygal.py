import pygal

#Shortened notation
pie = pygal.Pie()

#Creating a title
pie.title = "Solar System Mass (in kgs)"

#Adding Data
pie.add("Sun", 1.9885*(10**30))
pie.add("Mercury",3.3011*(10**23))
pie.add("Venus", 4.8675*(10**24))
pie.add("Earth", 5.97237*(10**24))
pie.add("Mars", 6.4171*(10**23))
pie.add("Jupiter", 1.8982*(10**27))
pie.add("Saturn", 5.6834*(10**26))
pie.add("Uranus", 8.6810*(10**25))
pie.add("Neptune", 	1.02413*(10**26))

#Calling render to 'print' the chart
pie.render()

#Shortened notation
bar = pygal.Bar()

#Creating title
bar.title = "Solar System Mass (in kgs)"

#Adding Data
bar.add("Mercury",3.3011*(10**23))
bar.add("Venus", 4.8675*(10**24))
bar.add("Earth", 5.97237*(10**24))
bar.add("Mars", 6.4171*(10**23))
bar.add("Jupiter", 1.8982*(10**27))
bar.add("Saturn", 5.6834*(10**26))
bar.add("Uranus", 8.6810*(10**25))
bar.add("Neptune", 	1.02413*(10**26))

#Rendering
bar.render()