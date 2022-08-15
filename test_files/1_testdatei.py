# @Kapitel: PyFiDoc Ver. 1.0 - Python Files to Dokumentation ssssss
# @Author: A_#_M
# @Copyright: CC BY-NC-SA
# @Comment: Online gibt es weiterführende Informationen zu dem Thema Lizenz:
# @Doku-HTML: https://de.creativecommons.net/was-ist-cc/

# @Unterkapitel: Mögliche Syntax in Code-Dateien
# @Thema: Grundlagen Syntax
# @Comment: Die wichtigste Basis-Syntax: Jede nicht-Code-Zeile muss mit einem # beginnen. Danach dann ein
# @Comment: Leerzeichen und: "@[Name]: " (Leerzeichen nach : ist erforderlich). Folgende Möglichkeiten
# @Comment: gibt es: "@Kapitel: ", "@Unterkapitel: ", "@Thema: ", "@Author: ", "@Copyright: ",
# @Comment: "@Doku-HTML: ", und natürlich "@Comment: ". Die eigentlichen Codezeilen haben keine Kennung am
# @Comment: Anfang einer Zeile, d.h. jede Zeile im Code ohne die obigen Kennungen werden als Code-Zeile
# @Comment: interpretiert. Die Namen stehen für genau das: Kapitel für Kapitel, Unterkapitel für Unterkapitel etc.
# @Comment: Alle "@Doku-HTML: " erwarten http(s)-Links und werden entsprechend gelinkt im Dokument.

# @Thema: Einstellmöglichkeiten
# @Comment: Mit den folgenden Variablen kann die Dokumentationserstellung gesteuert werden:
path_source = "../test_files/"
source_liste = []
name_doku_file = path_source + "test_doku.txt"
name_html_file = path_source + "index.html"

# @Comment: "path_source": Hier den Pfad zu der/den Sourcedatei(en) eingeben. Das Programm kann alle Python
# @Comment: Dateien (mit Endung .py) im Pfad erkennen und erstellt dafür direkt eine Text-Dokumentation und auch
# @Comment: eine HTML-Dokumentation. Beide Dateien werden im identischen Verzeichnis erstellt. Möchte man aber
# @Comment: nur für bestimmte Dateien Dokumentationen erstellen, dann sollte man in "souce_liste" die Dateinamen
# @Comment: eintragen. Beispiel:
source_liste = ["1_testdatei.py", "3_testdatei.py"]

# @Comment: Mit den beiden Variablen "name_doku_file" und "name_html_file" können die Dokumentationsdateien
# @Comment: benannt werden. Die HTML-Datei sollte man nur dann ändern, wenn man z.B. größere Webdokumenationen
# @Comment: vor hat, ansonsten ist "index.html" eine gute Wahl. Beispiel:
name_doku_file = path_source + "Dokumenations_1.txt"
name_html_file = path_source + "index.html"

# @Comment: Das war es eigentlich schon..:-)

# @Thema: Die main.py Datei
# @Comment: In der Datei "main.py" können im unteren Bereich in der Funktion "def main():" weitere Dinge eingestellt
# @Comment: werden:
def main():
    vorlagen_restaurieren()
    if len(source_liste) == 0:
        list_files = files_read(path_source)
        files_write_navi(list_files)
    else:
        list_files = source_liste
        files_write_navi(list_files)
    dicttionary = source_read(path_source, list_files)
    writing_docu(dicttionary, name_doku_file, name_html_file)

# @Comment: In der Funktion "writing_docu()" können folgende Argumente eingestellt werden, die möglichen Werte sind
# @Comment: jeweils "True" oder "False":
txt_docu=True    # Das ist auch der Standardwert
html_docu=True   # Das ist auch der Standardwert
docx_docu=False  # Noch nicht umgesetzt!
pdf_docu=False   # Noch nicht umgesetzt!

# @Comment: Eine Einstellung wäre z.B., wenn man zwar HTML aber keine TXT-Dokumentation haben möchte:
writing_docu(dicttionary, name_doku_file, name_html_file, txt_docu=False)

# @Comment: Wenn man keine HTML-Dokumentation haben möchte. aber eine TXT-Dokumentation:
writing_docu(dicttionary, name_doku_file, name_html_file, html_docu=False)

# @Thema: Imports
# @Comment: Es gibt folgende Imports in der "functions.py"-Datei:
import fnmatch
import os, shutil
import re
from os.path import exists as file_exists

# @Thema: Reihenfolge der Dateien
# @Comment: Die Reihenfolge der Dateien spielt natürlich eine Rolle für Dokumentationen. Man möchte bei vielen
# @Comment: einzelnen Python-Dateien in einem Verzeichnis die wichtigste Datei sicherlich am Anfang stehen haben
# @Comment: etc. Hierfür gibt es keine "Patentlösung", da die Dateinamen im Normalfall ja nicht aufsteigend nach
# @Comment: A-Z benannt werden. Es gibt zwei Möglichkeiten, um die Reihenfolge zu steuern. Die erste einfache
# @Comment: Variante ist: Die Dateinamen vornummerieren, z.B. wie auch die Testdaten hier im Verzeichnis
# @Comment: "testdateien" --> "1_testdatei.py, 2_testdatei.py, 3_testdatei.py". Man könnte z.B. alle Dateien
# @Comment: in ein eigenes Verzeichnis legen und durchnummerieren. Die zweite Variante ist die Steuerung über die
# @Comment: Variable "source_liste". Dazu wurde am Anfang schon mehr geschrieben.

# @Unterkapitel: Source(n) einlesen
# @Thema: HTML-Datei(en)
# @Comment: In der HTML-Datei wird die Nummerierung umgesetzt, wie das in der "functions.py" Datei umgesetzt wurde.
# @Comment: Beispiel für Unterkapitel. Hier werden die Zähler bei jedem Vorkommen um eins hochgezählt:
if count_old_unt_kapitel != count_kapitel:
    count_unterkapitel = 0
count_unterkapitel += 1

# @Comment: Die Nummersetzung erfolgt dann hier:
dict_print["xxx" + "_" + str(count_zeile)] = [str(count_kapitel) + "."
                                            + str(count_unterkapitel) + " " + line]

# @Comment: Der Zähler ist nur für die Kapitel, Unterkapitel und fürs Thema vorgesehen. Natürlich muss bei jedem
# @Comment: neuen Kapitel der Unterkapitelzähler wieder bei 1 beginnen, ebenso bei jedem neuen Unterkapitel muss der
# @Comment: Thema-Zähler auch wieder bei 1 starten. Die Source-Datei(en) werden in Funktion "source_read()"
# @Comment: eingelesen. Für jede gefundene Source-Datei wird einmal der komplette Inhalt in ein Dictionary
# @Comment: eingelesen.:
for onefile in list_files:
    # Pro Datei komplettes auslesen und schreiben der Zeilen ins Dictionary:
    with open(path + onefile, "r", encoding="utf-8") as file:
        for line in file.readlines():

# @Comment: Z.B. der Bereich für die Unterkapitel. Hier wird pro Source-Zeile erkannt, ob am Anfang der Bereich
# @Comment: für Unterkapitel zu finden ist, wenn ja, wird die Nummerierung angeworfen und dann in "dict_print" in
# @Comment: Dictionary geschrieben:
elif line.startswith("xxx"):
    if count_old_unt_kapitel != count_kapitel:
        count_unterkapitel = 0
    count_unterkapitel += 1
    dict_print["xxx" + "_" + str(count_zeile)] = [str(count_kapitel) + "."
                                     + str(count_unterkapitel) + " " + line]
    count_old_unt_kapitel = count_kapitel
    count_zeile += 1
    count_comment += 1

# @Unterkapitel: Dokumente erzeugen
# @Thema: Funktion writing_docu() - HTML
# @Comment: In der Funktion "writing_docu()" werden die eigentlich Dokumentationen geschrieben, nachdem alle
# @Comment: Source-Dateien eingelesen und in das Dictionary geschrieben wurden. Beispiel Unterkapitel:
elif re.search("^[0-9].*# @Unterkapitel.*", value):
k = re.search("(.*)# @Unterkapitel.*: (.*)", value)
if html_docu:
    with open("./tmp_dateien/body_fragment.txt", "a", encoding="utf-8") as writer:
        writer.write('<div class="div_unterkapitel"' + " " + 'id="' + k.group(1) + '#"' + '>'
                     + '<H2>' + k.group(1) + " " + k.group(2) +
                     '</H2>' + '</div>' + "\n")
    with open("./tmp_dateien/nav_fragment.txt", "a", encoding="utf-8") as nav_file:
        nav_file.write('<li><a href=' + '"#' + k.group(1) + '#' + '">' +
                       k.group(1) + k.group(2) + '</a></li>')

# @Comment: Das sieht zuerst "wüst" aus, ist es auch vermutlich ..:-), aber so kann ich schlicht den Code besser
# @Comment: lesen. Den "with open()" Bereich werde ich später vermutlich zu einer Funktion umbauen. Aber erst
# @Comment: irgendwann viel später. Das erste "with open()" beschreibt die tmp-Datei "body_fragment.txt" mit den
# @Comment: nötigen HTML-Codes. Die "body_fragment.txt"-Datei später für die eigentliche Erstellung der "index.html"
# @Comment: Datei benötigt. Das zweite "with open()" beschreibt den linken Navi-Bereich.

# @Thema: Funktion writing_docu() - TXT Datei
# @Comment: Die TXT-Datei wird komplett in diesem Bereich geschrieben:
if txt_docu:
    with open(ziel1, "a", encoding="utf-8") as writer:
        value = replacer(value)
        writer.write(value)

# @Thema: Mehrfache Ausführungen möglich
# @Comment: Die erstellten Dateien (index.html, test_doku.txt) werden bei jedem Start des Programms vorab immer
# @Comment: gelöscht. Man kann das Programm also beliebig oft ausführen.

# @Unterkapitel: Abschluss
# @Thema: Zusammenfassung
# @Comment: Weitere Hinweise zu den benötigten Versionen: Programmiert mit Python: 3.9.x

# @End:


