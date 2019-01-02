# Pogromca obcych
# Demonstruje współdziałanie obiektów

class Gracz(object):
    """Gracz w strzelance"""
    def strzel(self, przeciwnik):
        print("Gracz razi wroga \n")
        przeciwnik.smierc()


class Kosmita(object):
    """Obcy w strzelance"""
    def smierc(self):
        print("Obcy z trudem łapie oddech, 'To już koniec. Ale wielki koniec... \n" \
              "Tak, już robi się ciemno. Powiedz moim dwóm milionom larw, że je kochałem... \n" \
        "Żegnaj, okrutny Wszechświecie.'")


# main
print("\t\t Śmierć Obcego")

bohater = Gracz()
najezdzca = Kosmita()
bohater.strzel(najezdzca)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")