from apuesta import Apuesta
from perinola import Perinola
from jugador import Jugador
from ronda import Ronda


jugadores = Ronda ()
nombres = ("j1", "j2", "j3", "j4")
for n in nombres:
    j = Jugador (n)
jugadores.agregarjugador(j)
apuesta = Apuesta()
perinola = Perinola()
 








p = Perinola()
print(p)
print(p.cara_visible)
resultado = p.tirar ()
print(resultado)
print(p)
print(p.cara_visible)


