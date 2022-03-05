import turtle as t 
import random
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
sab = t.Turtle()
directions = [0, 90, 180, 360]
sab.pensize(10)
for _ in range(100):
    sab.color(random.choice(colours))
    sab.forward(40)
    sab.setheading(random.choice(directions))
