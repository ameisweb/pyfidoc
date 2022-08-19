# @Kapitel: PyFiDoc - Python Files to Dokumentation
# @Author: A_#_M -> Datei: main.py
# @Copyright: CC BY-NC-SA
# @Comment: Das Programm ist auch bei Github:
# @Doku-HTML: https://github.com/ameisweb/pyfidoc
# @Comment: Hier können die Lizenzbedingungen eingesehen werden:
# @Doku-HTML: http://pyfidoc.de/py_texte/license.html

# @Unterkapitel: Wofür ist das Programm
# @Thema: Ausgangslage
# @Comment: Jetzt gerade erlerne ich die Python-Programmierung. Noch kenne ich längst nicht alle Themen.
# @Comment: Meine Arbeitsweise ist wie folgt: Wenn ich Themen erarbeite, dann übe ich diese Themen auch
# @Comment: gleich in Python-Dateien. Wenn man dann so im Übungsmodus ist, dann lernt man "Dies oder Das"
# @Comment: zu Themenbereichen. Dieses Wissen möchte ich mir selbst auf Dauer zur Verfügung stellen.
# @Comment: Mehrere Suchen ergaben aber leider, dass es zwar bereits Code to Dokumentation Projekte gibt,
# @Comment: diese Projekte aber insgesamt so komplex sind, dass man da durchaus mehrere Wochen benötigt,
# @Comment: nur um sich einzuarbeiten. Diese Zeit habe ich gerade nicht, da lerne ich lieber weiter die Python
# @Comment: Programmierung, die ich noch nicht kenne.

# @Thema: Idee für eigenes Programm
# @Comment: Da ich bisher schon ein paar Dinge gelernt habe in der Python-Programmierung, habe ich mich
# @Comment: direkt entschieden, mir ein eigenes kleines Programm zu schreiben, um meine Notizen in den
# @Comment: Lerncode-Dateien gleich auf sinnvolle Weise in eine Dokumentation zu überführen. HTML bietet sich
# @Comment: hier direkt an. Also habe ich mir eine möglichst einfache "Doctag"-Syntax überlegt, die dann
# @Comment: von PyFiDoc erkannt und in entsprechende Form gebracht werden kann. Die Grundlagen die ich jetzt
# @Comment: gerade erlerne und zu eigenen Zwecken kommentiere in den Code-Dateien, soll mir in Zukunft als
# @Comment: "Cheat-Sheet" dienen.

# @Thema: Grundlagen Syntax
# @Comment: Die wichtigste Basis-Syntax: Jede "Nicht-Code-Zeile" sollte mit einem # beginnen. Danach dann ein
# @Comment: Leerzeichen und: "@Name: " (Leerzeichen nach : ist erforderlich). Folgende Möglichkeiten
# @Comment: gibt es: "@Kapitel: ", "@Unterkapitel: ", "@Thema: ", "@Author: ", "@Copyright: ",
# @Comment: "@Doku-HTML: ", "End:" und natürlich "@Comment: ". Die eigentlichen Codezeilen haben keine Kennung am
# @Comment: Anfang einer Zeile, d.h. jede Zeile im Code ohne die obigen Kennungen werden als Code-Zeile
# @Comment: interpretiert. Die Namen stehen für genau das: Kapitel für Kapitel, Unterkapitel für Unterkapitel etc.
# @Comment: Alle "@Doku-HTML: " erwarten http(s)-Links und werden entsprechend gelinkt im Dokument.

# @Thema: Anfänger-Status
# @Comment: Die jetzige Umsetzung von PyFiDoc ist auf Anfängerniveau. So ist das vorerst. Im Moment kenne ich
# @Comment: zwar die generellen Grundlagen zu eigenen Klassen, Konstruktur (__init__ self) etc., bin da gerade
# @Comment: aber überhaupt noch nicht "Sattelfest". D.h. die jetzige Umsetzung von PyFiDoc ist durchaus noch
# @Comment: im "Spaghetticode"-Modus. Mir ist das auch klar. Mit Einführung von sinnvollen klassen
# @Comment: kann ich einige meiner bisherigen Umsetzungen durchaus sinnvoller lösen. Das plane ich bereits,
# @Comment: wird aber noch etwas dauern. Vermutlich wird es ab Ver. 2.x ein komplettes Refactoring des Codes
# @Comment: geben. Dann mache ich aus dem Spaghetticode ein mehrgängiges Komplettmenü.

# @Thema: Zukünftige Erweiterungen
# @Comment: Wenn ich in TKinter oder QT soweit bin, wird es PyFiDoc als richtiges GUI-Programm geben.
# @Comment: Weiterhin will ich dann direkt in eine Datenbank schreiben. Dazu brauche ich gerade aber noch
# @Comment: mehr Wissen in sqlite3, da fehlt mir gerade noch zu viel. Diese GUI-PyFiDoc-Version, inkl. einer
# @Comment: DB im Hintergrund, kann man dann deutlich sinnvoller gestalten. Z.B. kann man sämtliche Code-Dateien
# @Comment: dann Projektweise zuordnen, in der DB Zeilenweise pro Datei abspeichern und so eben auch
# @Comment: mehrfache Py-Projekte immer zu "einer" Gesamt-HTML-Dokumentation zusammenführen. Bald werde ich
# @Comment: ebenfalls mit Java und C# lernerei beginnen. D.h. dann natürlich auch, das ich dort ebenfalls
# @Comment: ähnliche Code to Documentation Anforderungen habe, wie jetzt auch für Python. D.h. dann auch
# @Comment: das z.B. das typische Python "#" Commentzeichen durch z.B. "//" etc. ersetzt werden muss bzw.
# @Comment: wird der dann umgesetzte Stand von PyFiDoc dies selbständig erkennen und entsprechend in den weiteren
# @Comment: Abarbeitungen berücksichtigen. Später setze ich evtl. auch noch Syntax Highlighting in der HTML
# @Comment: Seite um.

# @Unterkapitel: Das eigentliche PyFiDoc-Programm
# @Thema: Importe ins Script
# @Comment: Die "functions"-Datei wird weiter unten ausgiebig dokumentiert:
from functions import source_read, writing_docu, files_read, files_write_navi
from functions import vorlagen_restaurieren, copy_in_txt
from functions import delete_make_dir

# @Thema: Konfiguration Pfade, Dateinamen
# @Comment: Eingabe des Doku-Dateinamens, des Pfades des Verzeichnisses und die eigene Gestaltung
# @Comment: der Verzeichnisstrukturen. in der jetzigen Version sollte "pyfidocs/" und "pyfidocs/html/"
# @Comment: nicht verändert werden. Falls doch: Eine fehlerfreie Umsetzung ist nicht unbedingt möglich.
# @Comment: Die Einträge ""txt_doku.txt" und "index.html" können nach belieben gewählt werden.
path_source = "C:/Users/work/Documents/Programm_Pyfidoc/"
name_doku_file = path_source + "pyfidocs/" + "txt_doku.txt"
name_html_file = path_source + "pyfidocs/html/" + "index.html"

# @Thema: Struktur HTML-Dokumentation
# @Comment: Wenn man so ein Programm erstellt, muss man sich insgesamt auch Gedanken machen, wie man die
# @Comment: Reihenfolge der einzelnen .py-Codedateien gestalten möchte in der HTML-Dokumentation und darüber
# @Comment: hinaus auch, wie man z.B. nur eine einzelne .py-Datei, statt alle .py-Dateien in einem Verzeichnis,
# @Comment: verwenden kann. Mein Vorgehen hier ist: Ich kopiere mir alle .py-Dateien einfach in ein
# @Comment: temporäres Verzeichnis, setze den Pfad dort hin ("path_source = ..."), dann nummeriere ich die
# @Comment: einzelnen Dateien mit führender Nummerierung im Dateinamen um, z.B. 1_testdatei.py, 2_testdatei.py
# @Comment: etc., PyfiDoc liest dann zuerst 1_testdatei.py ein, dann 2_testdatei.py usw. So kann ich definieren
# @Comment: wie die Struktur der HTML-Seite aussehen wird (gilt natürlich auch für die txt-Doku-Datei).
# @Comment: Die andere Möglichkeit ist hier gegeben mit "source_liste = []", hier kann man die Reihenfolge
# @Comment: der py-Dateien ebenfalls angeben, in dem man einfach die erste Datei, die zweite Datei etc. in die
# @Comment: Liste setzt. Beispiel: source_liste = ["1_testdatei.py", "2_testdatei.py"]. Hinweis:
# @Comment: Ist die "source_liste" nicht leer, dann wird nur für die Dateien die in dieser Liste
# @Comment: stehen die Dokumentation erstellt. Ist die Liste leer, dann werden alle .py-Dateien im
# @Comment: im angegeben Pfad "path_source" in die Dokumentation aufgenommen.
# @Comment: Für die Docu dieses Programms wähle ich diesen Weg hier:
source_liste = ["main.py", "functions.py"]



# @Thema: Das main()-Programm
# @Comment: Hier läuft das eigentliche PyFiDoc-Programm ab. Innerhalb der "Code-Zeilen" kann man immer
# @Comment: auch weitere # Kommentare setzen. Diese werden aber nicht weiter formatiert von PyFiDoc beim
# @Comment: schreiben der HTML-Doku. Vielleicht werde ich das später noch erweitern und diese sog.
# @Comment: "Code-Kommentare" in der HTML-Seite besonders umformatieren, z.B. Textfarbe, Stil etc.:
def main():
    """
    Beispiel für diesen Funktions-Doctag. PyFiDoc verwertet diese Doctags bisher nicht.
    Evtl. wird es hier später Erweiterungen in der Formatierung geben. Dies ist aber
    frühetens erst ab Ver. 2.x der Fall, wenn die GUI- und die DB-Anbindung umgesetzt wurde.
    Die unten aufgeführten Funktionen werden in der Functions genauer beschrieben.
    """
    delete_make_dir(path_source)
    vorlagen_restaurieren()
    if len(source_liste) == 0:
        list_files = files_read(path_source)
    else:
        list_files = source_liste
    files_write_navi(list_files, path_source)
    dicttionary = source_read(path_source, list_files)
    writing_docu(dicttionary, name_doku_file, name_html_file)
    copy_in_txt(path_source)

# @Comment: Im Funktionsaufruf "writing_docu()" können folgende Argumente eingestellt werden, die möglichen
# @Comment: Werte sind jeweils "True" oder "False":
# txt_docu=True    # Das ist auch der Standardwert
# html_docu=True   # Das ist auch der Standardwert
# docx_docu=False  # Noch nicht umgesetzt!
# pdf_docu=False   # Noch nicht umgesetzt!

# @Comment: Eine Einstellung wäre z.B., wenn man zwar HTML aber keine TXT-Dokumentation haben möchte:
# writing_docu(dicttionary, name_doku_file, name_html_file, txt_docu=False)

# @Comment: Wenn man keine HTML-Dokumentation haben möchte, aber eine TXT-Dokumentation:
# writing_docu(dicttionary, name_doku_file, name_html_file, html_docu=False)

# @Thema: name = main
# @Comment: So soll man das ja machen:
if __name__ == "__main__":
    main()

# @Thema: End-angabe
# @Comment: Am Ende jeder Datei setze ich noch ein "# @End:" ein. In der HTML-Seite sieht man dann
# @Comment: jeweils die Zeichenkette: "###End-Datei###". Das dient dazu, dass man mehrere .py-Dateien
# @Comment: die z.B. nicht jeweils mit Kapitel etc. beginnen, auf der HTML-Seite unterscheiden kann.
# @End:


