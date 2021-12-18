from math import *
def theor():
  a = float(input("La longueur a: "))
  b = float(input("La longueur b: "))
  c = a**2+b**2
  print("L'hypoténuse est de" ,round(sqrt(c), 1))
def autre():
    a = float(input("La longueur que tu connais: "))
    hyp = float(input("L'hypoténuse: "))
    c = hyp**2-a**2
    c = sqrt(c)
    print("La troisème longueur est de:", round(c, 1))
def reciproque():
  a = float(input("La longueur a: ")) 
  b = float(input("La longueur b: "))
  c = float(input("Hypoténuse: "))
  round(c)
  calc = round(sqrt(a**2+b**2), 1)
  if c == calc:
    print("C'est un triangle rectangle")
  else:
    print("ce n'est pas un triangle rectangle")
choix = input("""
Théorème de pythagore:
t = théorème de pythagore
r = réciproque de pythagore
a = je connais l'hypotenuse 
et 1 mesure mais 
pas l'autre mesure
Alors t/r/a: 
""")
if choix == "t":
    theor()
if choix == "r":
    reciproque()
if choix == "a":
    autre()
