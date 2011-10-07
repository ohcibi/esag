#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Gruppe():
    def __init__(self, name):
        self._punkte = 0
        self._name = name

    def add_punkte(self, anzahl):
        self._punkte += anzahl

    def punkte(self):
        return self._punkte

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_val):
        self._name = new_val

    def __repr__(self):
        return self._name + ": " + str(self._punkte) + " Punkte"

class Frage():
    def __init__(self, name, text, loesung, gruppen, punktevergabe_methode):
        self._name = name
        self._text = text
        self._loesung = loesung
        self._gruppen = gruppen
        self._punktevergabe_methode = punktevergabe_methode

        # Frage stellen
        print "\n########################################################\n"
        print self

        # Antworten für jede Gruppe einlesen
        gewonnene_punkte = ''
        for gruppe in gruppen:
            antwort = self.lies_antwort_aus_console(gruppe, self._loesung)
            punkte = punktevergabe_methode(antwort, self._loesung)
            if punkte == 1:
                gewonnene_punkte = gewonnene_punkte + gruppe.name +  " bekommt " + str(punkte) + " Punkt.\n"
            else:
                gewonnene_punkte = gewonnene_punkte + gruppe.name +  " bekommt " + str(punkte) + " Punkte.\n"
            gruppe.add_punkte(punkte)

        print "\nKORREKTE LÖSUNG: " + str(self._loesung) + "\n"
        print gewonnene_punkte
        print gruppen

    def lies_antwort_aus_console(self, gruppe, loesung):
        korrekter_eingabetyp = False
        while not korrekter_eingabetyp:
            try:
                antwort = type(loesung)(raw_input(gruppe.name + ": "))
                korrekter_eingabetyp = True
            except ValueError:
                pass
        return antwort

    def __repr__(self):
        return "Frage " + self._name + ": " + self._text

class PiMalDaumen():
    def print_intro(self):
        print "##################################"
        print "# ESAG Rallye 2011 - PiMalDaumen #"
        print "##################################"
        print ""

    def frage_1_punktevergabe(self, antwort, loesung):
        credit = 0
        #loesung 630
        if antwort >= 620 and antwort <= 640:
            credit = 5
        elif antwort >= 570 and antwort <= 690:
            credit = 3
        elif antwort >= 315 and antwort >= 945:
            credit = 1
        
        return credit

    def frage_2_punktevergabe(self, antwort, loesung):
        credit = 0
        if antwort == loesung:
            credit = 5
        return credit

    def frage_3_punktevergabe(self, antwort, loesung):
        credit = 0
        #Lösung: 1449
        if antwort >= 1425 and antwort <= 1465:
            credit = 5
        elif antwort >= 1280 and antwort <= 1600:
            credit = 3
        elif antwort >= 1140 and antwort <= 1740:
            credit = 1
        return credit

    def frage_4_punktevergabe(self, antwort, loesung):
        credit = 0
        #Lösung: x; Punkte: {1%, 10%, 50% Abweichung => 5, 3, 1}
        if antwort >= loesung-(loesung*.01) and antwort <= loesung+(loesung*.01):
            credit = 5
        elif antwort >= loesung-(loesung*.1) and antwort <= loesung+(loesung*.1):
            credit = 3
        elif antwort >= loesung-(loesung*.5) and antwort <= loesung+(loesung*.5):
            credit = 1

        #if antwort in range(loesung-(int(round(loesung*.01))), loesung+(int(round(loesung*.01)))+1):
        #    credit = 5
        #elif antwort in range(loesung-(int(round(loesung*.1))), loesung+(int(round(loesung*.1)))+1):
        #    credit = 3
        #elif antwort in range(loesung-(int(round(loesung*.5))), loesung+(int(round(loesung*.5)))+1):
        #    credit = 1
        return credit

    def frage_5_punktevergabe(self, antwort, loesung):
        credit = 0
        #Lösung: 4,5; Punkte {4,5 NK => 5, 4 od. 5 => 3, 3 od. 6 => 1}
        if antwort == 4.5:
            credit = 5
        elif antwort >= 4.0 and antwort <= 5.0:
            credit = 3
        elif antwort >= 3.0 and antwort <= 6.0:
            credit = 1
        return credit

    def frage_6_punktevergabe(self, antwort, loesung):
        credit = 0
        #Lösung: (2063) Punkte: {+-20 => 5; +-200 => 3; +-1000 => 1}
        if antwort >= 2043 and antwort <= 2083:
            credit = 5
        elif antwort >= 1863 and antwort <= 2263:
            credit = 3
        elif antwort >= 1063 and antwort <= 3063:
            credit = 1
        return credit

    def frage_7_punktevergabe(self, antwort, loesung):
        credit = 0
        #Lösung: (1966) Punkte: {1966 => 5; 1960-1970 => 3; 1900 - 2000 => 1}
        if antwort == 1966:
            credit = 5
        elif antwort >= 1960 and antwort <= 1970:
            credit = 3
        elif antwort >= 1900 and antwort <= 2000:
            credit = 1
        return credit

    def frage_8_punktevergabe(self, antwort, loesung):
        credit = 0
        #Lösung: (2002) Punkte: {2002 => 5; 1997-2007 => 3; 1992-2009 => 1}
        if antwort == 2002:
            credit = 5
        elif antwort >= 1997 and antwort <= 2007:
            credit = 3
        elif antwort >= 1992 and antwort <= 2009:
            credit = 1
        return credit

    def frage_9_punktevergabe(self, antwort, loesung):
        credit = 0
        #Lösung: Punkte: {+-1 => 5; +-3 => 3; +-6 => 1}
        if antwort >= 9 and antwort <= 11:
            credit = 5
        elif antwort >= 7 and antwort <= 13:
            credit = 3
        elif antwort >= 4 and antwort <= 16:
            credit = 1
        return credit

    def frage_10_punktevergabe(self, antwort, loesung):
        credit = 0
        #Lösung: (40%) Punkte: {40% => 5; 30-50 => 3; 20-60 => 1}
        if antwort == 40:
            credit = 5
        elif antwort >= 30 and antwort <= 50:
            credit = 3
        elif antwort >= 20 and antwort <= 60:
            credit = 1
        return credit

    def frage_11_punktevergabe(self, antwort, loesung):
        credit = 0
        #Lösung: (51,19 Grad Nord / 6,8 Grad Ost) Punkte: {Entfernung < 1km => 5; Entfernung <= 10km => 3; Entfernung <= 100 km => 1}
        antwort = float(antwort)
        if antwort <= 100.0:
            credit = 5
        elif antwort <= 300.0:
            credit = 3
        elif antwort <= 1000.0:
            credit = 1
        return credit

    def frage_12_punktevergabe(self, antwort, loesung):
        credit = 0
        #Lösung: (1045 Km/h) Punkte: {1030-1060 => 5; 950-1150 => 3; 500-1500 => 1}
        antwort = float(antwort)
        if antwort >= 1030 and antwort <= 1060:
            credit = 5
        elif antwort >= 950 and antwort <= 1150:
            credit = 3
        elif antwort >= 500 and antwort <= 1500:
            credit = 1
        return credit

    def frage_13_punktevergabe(self, antwort, loesung):
        credit = 0
        #Lösung: (etwa 900) Punkte: {890-910 => 5; 800-1000 => 3; 500-1300 => 1}
        antwort = float(antwort)
        if antwort >= 890 and antwort <= 910:
            credit = 5
        elif antwort >= 800 and antwort <= 1000:
            credit = 3
        elif antwort >= 500 and antwort <= 1300:
            credit = 1
        return credit

    def frage_14_punktevergabe(self, antwort, loesung):
        credit = 0
        #Lösung: (108.000.000 Km) Punkte {100 Mio - 110 Mio => 5; 80 - 150 Mio => 3; 50 - 200 Mio km => 1}
        antwort = float(antwort)
        if antwort >= 100000000 and antwort <= 110000000:
            credit = 5
        elif antwort >= 80000000 and antwort <= 150000000:
            credit = 3
        elif antwort >= 50000000 and antwort <= 200000000:
            credit = 1
        return credit

    def start(self):
        self.print_intro()

        a = Gruppe('Gruppe A')
        b = Gruppe('Gruppe B')
        gruppen = [a, b]
        print gruppen

        frage_1 = Frage('1', 'Wie viele Gummibärchen sind in diesem Glas?', 630, gruppen, self.frage_1_punktevergabe)
        frage_2 = Frage('2', 'Wie viele Rillen hat eine Schallplatte pro Seite?', 1, gruppen, self.frage_2_punktevergabe)
        frage_3 = Frage('3', 'Wie viele Rollen Klopapier benötigt man, um eine Marathon-Strecke abzulegen?', 1449, gruppen, self.frage_3_punktevergabe)
        frage_4 = Frage('4', 'Wieviel Gramm wiegt dieses Schwert?', 1096, gruppen, self.frage_4_punktevergabe)
        frage_5 = Frage('5', 'Wieviele Negerküsse ergeben 112 Gramm? (Rationale Lösungen erlaubt!)', 4.5, gruppen, self.frage_5_punktevergabe)
        frage_6 = Frage('6', 'Wie viele 3,5 Zoll Disketten benötigt man, um ein Windows 7 Image darauf unterzubringen?', 2063, gruppen, self.frage_6_punktevergabe)
        frage_7 = Frage('7', 'Seit wann gibt es die naturwissenschaftliche Fakultät an der Uni Düsseldorf?', 1966, gruppen, self.frage_7_punktevergabe)
        frage_8 = Frage('8', 'Seit wann kann man an der HHU Informatik studieren?', 2002, gruppen, self.frage_8_punktevergabe)
        frage_9 = Frage('9', 'Wie viele Pinguine sieht man in der Fachschaft Informatik?', 10, gruppen, self.frage_9_punktevergabe)
        frage_10 = Frage('10', 'Wie hoch war die Bestehensquote der Nebenfächler bei der Analysis-I-Klausur im Sommersemester 2011, die ihre Zulassung nicht in jenem Semester erworben haben? (in Prozent)', 40, gruppen, self.frage_10_punktevergabe)
        #frage_11 = Frage('11', 'Was sind die Geo-Koordinaten von Gebäude 25.12 der Uni Düsseldorf? (X Grad Nord, Y Grad Ost)', '51,19 Grad Nord / 6,8 Grad Ost', gruppen, self.frage_11_punktevergabe)
        frage_12 = Frage('11', 'Mit wieviel km/h dreht sich die Erde unter dir um sich selbst?', 1045, gruppen, self.frage_12_punktevergabe)
        frage_13 = Frage('12', 'Wieviele Schläge pro Minute kann das Ohr wahrnehmen, bis es ein einziger langer Ton wird?', 900, gruppen, self.frage_13_punktevergabe)
        frage_14 = Frage('13', 'Wieviele Kilometer ist die Venus von der Sonne entfernt?', 108000000, gruppen, self.frage_14_punktevergabe)

if __name__ == "__main__":
    p = PiMalDaumen()
    p.start()
