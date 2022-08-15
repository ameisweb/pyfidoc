# @Kapitel: Arbeiten mit Dateien
# @Author: A.M. aus Dings
# @Copyright: MIT

# @Comment: Online gibt es weiterführende Informationen zu dem Thema:
# @Doku-HTML: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

# @Comment: In diesem Dokument wird das Arbeiten mit Dateien beschrieben. Es werden diverse Übungsscipte
# @Comment: als Beispiele aufgelistet. In den jeweiligen Beispielscripten gibt es dann weitere hilfreiche Kommentare.

# @Unterkapitel: Daten aus einer Datei lesen
# @Thema: Datei öffnen
# @Comment: Mit open("path", "modus") wird eine Datei geöffnet und einer Variable zugeordnet. Es müssen immer zwei
# @Comment: Argument übergeben werden, erste Argument "path zur Datei", zweite Argument "modus = r, w, a, r*":
file = open("path", "modus")

# @Comment: Die Datei lesend öffnen:
file = open("path", "r")
file.read()

# @Comment: Die Datei schreibend öffnen:
file = open("path", "w")
file.write("Alles wird gegen das hier gelöscht")

# @Comment: Die Datei am Ende beschreiben. Dateiinhalt wird nicht gelöscht. Der Anhang findet aber nicht nächster
# @Comment: Zeile statt, sondern wird direkt am letzten Zeichen angehängt. Beim Datei beschreiben sollte man also immer
# @Comment: vorher bereits eine neue Zeile begonnen haben:
file = open("path", "a")
file.write("wir am Ende angehängt")

# @Comment: Datei mit Modus "x" beschreiben. Dieser Modus x sollte genommen werden, wenn man sichergehen will, dass
# @Comment: man keine bestehenden Dateien mit "w" überschreibt. Existiert die Datei bereits (in path angegeben),
# @Comment: dann wird ein # @Comment: FileExistsError geworfen. Diesen könnte man dann also z.B. via Try/Except
# @Comment: abfangen. Existiert Datei noch nicht, dann wird sie ganz normale erzeugt und im Schreibmodus geöffnet:
file = open("path", "x")
file.write("Funktioniert nur dann, wenn Datei noch nicht vorhanden ist")

# @Comment: Alle oben genannten Moduseinstellungen kann man auch mit einem Pluszeichen versehen, z.B. "r+", "w+",
# @Comment: "a+", "x+". Mit dem Modus "+" wird jede Datei sowohl im zugehörigen Modus (r, w, a, x) geöffnet, man kann
# @Comment: sie aber jeweils auch lesen und schreiben. Das "+" dient als für beides (lesen und schreiben). Aber öffnet
# @Comment: man z.B. in "w+" dann wird trotzdem der Inhalt einer bestehenden Datei komplett gelöscht. Der Modi "r+"
# @Comment: wäre also als "sinnvollste" alternative zu nennen:
file = open("dateipfad", "r+")
file = open("dateipfad", "w+")
file = open("dateipfad", "a+")
file = open("dateipfad", "x+")
file.read()
file.write()

# @Comment: Dateien im Binärmodus öffnen mit z.B. "rb" oder "r+b" etc., mit dem Binärmodus kann man z.B. dann
# @Comment: Bildateien öffnen etc:
file = open("dateipfad", "rb")
file = open("dateipfad", "r+b")
file = open("dateipfad", "wb")
file = open("dateipfad", "w+b")
file = open("dateipfad", "ab")
file = open("dateipfad", "a+b")
file = open("dateipfad", "xb")
file = open("dateipfad", "x+b")
file.read()
file.write()

# @Thema: Datei lesen
# @Comment: Der read()-Befehl ohne Angaben in der Klammer, schreibt kompletten Inhalt der Datei. Mit der Angabe einer
# @Comment: Ganzzahl in den Klammern, wird die Anzahl Bytes (Zeichen) definiert, z.B. 5 für die ersten 5 Zeichen:
print(file.read(5))

# @Thema: Eine Zeile lesen
# @Comment: Mit readline()-Befehl liest man nur eine Zeile einer Datei. Mehrfaches Aufrufen des Befehls liest
# @Comment: jeweils die nächste Zeile. Der Befehl behält sich quasi die jeweilige Leseposition (die ausgelesene Zeile):
print(file.readline())
print(file.readline())

# @Thema: Alle Zeilen auslesen in Listenrückgabe
# @Comment: Mit readlines()-Befehl werden alle Zeilen einer Datei in einer Liste zurückgegeben. Beispiel:
# @Comment: ['Text Zeile 1\n', 'Text Zeile 2\n', etc..]. Der Zeilenumbruch "\n" hängt auch immer an. Diese Zeichen
# @Comment: sollte man dann frühzeitig mit z.B. .replace("\n", "") loswerden:
print(file.readlines())

# @Thema: Readlines in Dictonary überführen
# @Comment: Man kann mit readlines()-Befehl z.B. die jeweiligen Einzelzeilen trennen lassen und in ein
# @Comment: Dictonary überführen in einer for-Schleife. Zuerst leeres Dioctonary erzeugen, dann for-Schleife.
# @Comment: Die Ausgabe ist dann z.B. für dict_liste = {'Wert vor Trennzeichen Zeile 1': 'Wert nach Trennzeichen
# @Comment: Zeile 1'..etc}. Hier gilt auch das mit dem Zeilenumbruchzeichen "\n":
dict_liste = {}
file = open("path", "r")
for line in file.readlines():
    # Weiteres Blablabla
    line_splitted = line.split(" ")
    dict_liste[line_splitted[0]] = line_splitted[1]
print(dict_liste)
file.close()

# @Comment: Mit Erweiterung Dictanary könnte man jetzt z.B. Werte zu den Dictanary-einträgen ausgeben lassen. Die
# @Comment: Ausgabe im Beispiel wäre dann: Wert nach Trennzeichen Zeile 1:
print(dict_liste["Wert vor Trennzeichen Zeile 1"])

# @Thema: Datei schliessen
# @Comment: Den close()-Befehl sollte man nach jedem öffnen anhängen, das OS-System nur bestimmte Anzahl Dateien
# @Comment: geöffnet halten kann:
file.close()

# @Unterkapitel: Dateipfade angeben (relativ und absolut)
# @Thema: Dateipfad absolut angeben
# @Comment: Die Pfadangabe wäre z.B. "C:/Verzeichnisname/Unterverzeichnisname/Dateiname.txt", die Pfadangabe sollte
# @Comment: sowohl für Windows und Mac jeweils mit dem Zeichen erfolgen "/". Mac Beispiel:
# @Comment: /Users/Username/Desktop/Dateiname.txt". Liest man mit Windows z.b. Pfade aus, sollte man also ein
# @Comment: .replace("\", "/") bei Pfadangaben machen:
file = open("C:/Verzeichnisname/Unterverzeichnisname/Dateiname.txt", "r")

# @Thema: Dateipfad relativ angeben
# @Comment: Hier gibt es quasi Unix-Schreibweise. Die Datei ist im aktuellen Verzeichnis "./dateiname.txt",
# @Comment: die Datei ist im Unterverzeichnis "./verzeichnisname/dateiname.txt", die Datei ist eine Ebene oberhalb
# @Comment: vom aktuellen Verzeichnis, dann macht man zwei Punkte "../", pro Ebene nach Oben also "../", z.B. zwei
# @Comment: Ebenen nach Oben wäre dann"../../dateiname.txt" etc:
file = open("./dateiname.txt", "r")
file = open("../dateiname.txt", "r")
file = open("../../dateiname.txt", "r")

# @Unterkapitel: Daten in Dateien schreiben
# @Thema: Datei schreibend öffnen mit "w" und .write()
# @Comment: Mit dem Modus "w" kann eine Datei schreibend geöffnet werden, hier aber dran denken, das Öffnen im
# @Comment: Schreibmodus löscht sämtliche Inhalte in der Datei. Wird als Dateipfad der Name einer nicht
# @Comment: vorhandenen Datei angegeben, dann wird diese Datei im Dateipfad erzeugt:
file = open("path", "w")
file.write("Das ist ein Testeintrag in die Datei")

# @Thema: Datei mit .writelines beschreiben
# @Comment: Mit .writelines()-Befehl kann man den Inhalt einer Liste in die Datei schreiben. Die Inhalte in der Liste
# @Comment: dürfen nur Strings sein. Integer etc. z.B. führen zu einem Fehler bei der Ausführung. Es wird kein
# @Comment: Leerzeichen nach jedem Einzelinhalt der Liste gesetzt, diese müssten also in der Liste im jeweiligen
# @Comment: String enthalten sein. Man könnte in der Liste ebenfalls Escape-Sequenzen übergeben, also z.B. "\n" oder
# @Comment: für Tab "\t" etc:
words = ["Das ist", "ein", "Test"]
file = open("Dateipfad", "w")
file.writelines(words)
file.close()

# @Unterkapitel: Schreib- und Leseposition verändern
# @Thema: Die Funktion .tell()
# @Comment: Mit der Funktion .tell() kann man sich den aktuellen Positionszeiger anzeigen lassen. Gezählt wird von
# @Comment: 0 bis zum Ende z.b. einer Zeile. Steht in erster Zeile z.B. "Dies ist ein Text", dann sind das 17 Zeichen
# @Comment: von D bis Mit .readline() würde man also z.b. erste Zeile auslesen und mit .tell() würde man vorher 0
# @Comment: bekommen und nach .readline() dann z.B. 18. Mit .readline() bekommt man in diesem Beispiel dann z.B.
# @Comment: "Dies ist ein Text":
file = open("dateipfad", "r")
file.tell()
file.readline()
file.tell()

# @Thema: Die Funktion .seek()
# @Comment: Mit der Funktion .seek() kann man direkt angeben, ab welcher Position innerhalb des Files man starten
# @Comment: möchte. Im Beispiel oben war ja nach erstem .readline() die Position via .tell() abgefragt dann bei 18. Man
# @Comment: könnte jetzt also z.B. bei 18 auch direkt starten und würde dann alles folgendes der nächsten Zeile
# @Comment: einlesen. Im Modus "a" kann .seek() die Position nicht verschieben:
file = open("dateipfad", "r")
file.seek(18)
file.readline()

# @Unterkapitel: Inhalte von Dateien löschen
# @Thema: Die Funktion .truncate()
# @Comment: Diese Funktion kann nur im Modus "r+" verwendet werden. Mit der Funktion .truncate() und einer Angabe
# @Comment: in den Klammern, wird dann alles ab der Position bis zum Ende der Datei gelöscht:
file = open("dateipfad", "r+")
file.truncate(18)

# @End:

