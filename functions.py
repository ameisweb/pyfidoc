# @Kapitel: Die functions.py Datei
# @Author: A_#_M -> Datei: functions.py

# @Unterkapitel: Funktionsdefinitionen des Programms
# @Comment: Alle Codezeilen in dieser Datei haben "noch" Spaghetti-Aufbau. Später, ab Ver. 2.x, wird es
# @Comment: einen übersichtlicheren Klassenaufbau geben. Z.B. die "vielen" harten Copy&Paste Stellen mit
# @Comment: "with open.." wird es dann so nicht mehr geben.

# @Thema: Importe
# @Comment: Folgende Importe werden benötigt:
import fnmatch
import os, shutil
import re
from os.path import exists as file_exists


# @Thema: Python Files einlesen
# @Comment: Hier werden alle ".py"-Files eingelesen, die in "path_source" zu finde sind. In der main.py
# @Comment: wird über "list_files" in einer IF/Else-Bedingungen definiert, ob alle .py-File oder nur die
# @Comment: Files in "source_liste" betrachtet werden:
def files_read(path):
    list_files = []
    for file in os.listdir(path):
        if fnmatch.fnmatch(file, '*.py'):
            list_files.append(file)
    return list_files

# @Thema: Linke Navigationsbereich in HTML schreiben
# @Comment: Hier wird der Teil unterhalb von Python-Dateien bis inkl. zum Bereich "Dokument-Index" in den
# @Comment: linken Navigationsbereich in der HTML-Seite geschrieben:
def files_write_navi(file_list, path_source):
    for file in file_list:
        # Schreibt die Filenamen als HTML-Link unter "::Python-Dateien::" in die
        # in die nav_fragment.txt":
        no_extension = file.split(".")
        with open("./workfile/nav_fragment.txt", "a", encoding="utf-8") as nav_file:
            nav_file.write('<li><a href="' + 'py_texte/' + no_extension[0] + '.html' + '"' + " " +
                           'target="_blank"' + '>' + file + '</a></li>' + "\n")

    # Schreibt pro Filename die passende iFrame-HTML-Seite:
    write_iframe(file_list, path_source)

    # Schreibt den Trenner "::Dokument_Index::" in die nav_fragment.txt":
    with open("./workfile/nav_fragment.txt", "a", encoding="utf-8") as nav_file:
        nav_file.write('<li><a class="active" href="#home">::Dokument_Index::</a></li>' + "\n")

# @Thema: IFrame-HTML pro Filename schreiben
# @Comment: Hier wird die jeweilige iFrame-HTML-Seite pro Filenamen geschrieben. Klickt man auf der HTML
# @Comment: auf einen Filenamen unterhalb von "::Python-Dateien::", dann wird man auf die hier erstellten
# @Comment: iFrame-Seiten gelinkt. Den iFrame-Aufbau pro Python-Datei habe ich gewählt, weil man so
# @Comment: mit einfachen Mitteln txt.Dateien quasi im Original in den Browser lesen kann. Die Python
# @Comment: Files mit .py am Ende werden in der Funktion "copy_in_txt" in "py_texte" als .txt-Dateien kopiert.
# @Comment: Dadurch kann man die Python-files auch im Browser aufrufen. Würde man die .py-Dateien aufrufen,
# @Comment: bekommt man leider keinen Inhalt der Datei angezeigt im Browserfenster:
def write_iframe(file_list, path_source):
    for file in file_list:
        no_anhang = file.split(".")
        # Zieldateiname schreiben der iFrame-HTML-Datei:
        link = path_source + "pyfidocs/html/py_texte/" + no_anhang[0] + ".html"

        # Schreibt Link Inhalt in text_iframe.txt Datei:
        with open("./workfile/text_iframe.txt", "a", encoding="utf-8") as iframe_file:
            iframe_file.write(' src = "' + file + '.txt' + '" >' + '</div> </body> </html>')

        # Öffnet readlines in "text_iframe.txt" Datei:
        with open("./workfile/text_iframe.txt", "r", encoding="utf-8") as frame_write:
            for line in frame_write.readlines():
                # Schreibt in die link-Datei die Zeilen:
                with open(link, "a", encoding="utf-8") as index_write:
                    index_write.write(line)

        # Löscht die Datei ./workfile/text_iframe.txt nach jedem Filename:
        if os.path.exists("./workfile/text_iframe.txt"):
            os.remove("./workfile/text_iframe.txt")
        else:
            print("File ./workfile/text_iframe.txt does not exist")

        # Kopiert dann wieder das Original-File text_iframe.txt in workfile-Verzeichnis für den
        # nächsten Filename:
        y_orig = "./workfile/originals/text_iframe.txt"
        y_copy = "./workfile/text_iframe.txt"
        shutil.copy(y_orig, y_copy)


# @Thema: Sourcefiles in Dictionary schreiben
# @Comment: Hier werden die jeweiligen .py-Dateien linear Zeile für Zeile eingelesen und in das Dictionary
# @Comment: "dict_print = {}" geschrieben. Dieses Dictionary ist die Grundlage für die spätere "writing_docu"
# @Comment: Funktion (siehe unten).
def source_read(path, list_files):
    dict_print = {}
    count_zeile = 0
    count_comment = 0
    count_kapitel = 0
    count_unterkapitel = 0
    count_thema = 0
    count_old_unterkapitel = 0
    count_old_unt_kapitel = 0
    count_old_the_kapitel = 0
    zeilenumbruch = ""

    # For-Schleife und lesen aller Zeilen der Dateien in der Liste:
    for onefile in list_files:
        # Pro Datei komplettes auslesen und schreiben der Zeilen ins Dictionary:
        with open(path + onefile, "r", encoding="utf-8") as file:
            for line in file.readlines():

                # Kapitel-Bereich:
                if line.startswith("# @Kapitel"):
                    count_kapitel += 1
                    if count_kapitel > 1:
                        # im Moment ohne wirkliche Funktion. Wird später verändert werden:
                        zeilenumbruch = "\n"
                    dict_print["#@Kapitel" + "_" + str(count_zeile)] = [str(count_kapitel) +
                                                                  "." + " " + line]
                    count_zeile += 1
                    count_comment += 1

                # Doku-HTML Bereich
                elif line.startswith("# @Doku-HTML"):
                    dict_print["#@Doku-HTML" + "_" + str(count_zeile)] = [line]
                    count_zeile += 1
                    count_comment += 1

                # Unterkapitel Bereich
                elif line.startswith("# @Unterkapitel"):
                    if count_old_unt_kapitel != count_kapitel:
                        count_unterkapitel = 0
                    count_unterkapitel += 1
                    dict_print["#@Unterkapitel" + "_" + str(count_zeile)] = [str(count_kapitel) + "."
                                                            + str(count_unterkapitel) + " " + line]
                    count_old_unt_kapitel = count_kapitel
                    count_zeile += 1
                    count_comment += 1

                # Thema Bereich:
                elif line.startswith("# @Thema"):
                    if count_old_the_kapitel != count_kapitel:
                        count_thema = 0
                    if count_old_unterkapitel != count_unterkapitel:
                        count_thema = 0
                    count_thema += 1
                    dict_print["#@Thema" + "_" + str(count_zeile)] = [
                        str(count_kapitel) + "." + str(count_unterkapitel) + "."
                        + str(count_thema) + " " + line]
                    count_old_unterkapitel = count_unterkapitel
                    count_old_the_kapitel = count_kapitel
                    count_zeile += 1
                    count_comment += 1

                # Comment Bereich:
                elif line.startswith("# @Comment"):
                    # Jeder comment_key bekommt einmaligen Namen durch "+ count_comment". Der count_comment
                    # Zähler wird nicht in diesem elif-Knoten aufgezählt, sondern nur in allen anderen
                    # Knoten. Ziel hier ist: Zusammenhängende Commentzeilen im py-Code als einen Textblock
                    # im Dictionary zu betrachten:
                    var_com = "comment" + str(count_comment)
                    line = line.replace("\n", "")
                    # Gibt es den comment-Key nicht, dann in Dictionary schreiben:
                    if var_com not in dict_print.keys():
                        dict_print[str(var_com)] = [line + " " + "\n"]
                    # Den comment-Key gibt es bereits, dann wird der Value der Variabel get_value
                    # übergeben und in "value_plus" zzgl. "line" erweitert:
                    else:
                        get_value = str(dict_print.get(var_com)).replace("[", "").replace("]",
                                                            "").replace("'", "").replace("\\n", "")
                        value_plus = str(get_value) + (str(line + " " + "\n").replace("# @Comment: ", ""))
                        # Der Key wird im Dictionary gelöscht:
                        dict_print.pop(var_com)
                        # Der Key wird mit erweiterter line wieder in Dictionary geschrieben:
                        dict_print[str(var_com)] = [value_plus]
                    count_zeile += 1

                # Author Bereich:
                elif line.startswith("# @Author"):
                    dict_print["#@Author" + "_" + str(count_zeile)] = [line]
                    count_zeile += 1
                    count_comment += 1

                # Copyright Bereich:
                elif line.startswith("# @Copyright"):
                    dict_print["#@Copyright" + "_" + str(count_zeile)] = [line]
                    count_zeile += 1
                    count_comment += 1

                # Leerzeilen Bereich:
                elif line.startswith("\n"):
                    dict_print[str(count_zeile)] = [line]
                    count_zeile += 1
                    count_comment += 1

                # End Bereich:
                elif line.startswith("# @End"):
                    dict_print["#@End" + "_" + str(count_zeile)] = [line]
                    count_zeile += 1
                    count_comment += 1

                # Code Bereich (alles ohne # vorab):
                else:
                    dict_print[str(count_zeile)] = ["\t" + line]
                    count_zeile += 1
                    count_comment += 1
    return dict_print

# @Thema: Comment-Erweitern in Dictionary
# @Comment: Da alle aufeinander folgende Comment-Zeilen in den Files als ein einziger Textblock im Dictionary
# @Comment: eingetragen werden sollen, wird hier ganz am Ende eines jeden comment-Values ein "\n"
# @Comment: Zeilenumbruch angefügt.
def dict_comments(dict_print):
    key_liste = list(dict_print.keys())
    for k in key_liste:
        if k.startswith("comment"):
            dict_print[k].append("\n")
    return dict_print


# @Thema: Das schreiben der txt/html-Dokumentation
# @Comment: Hier findet das temporäre schreiben der txt-Blueprint-Dateien statt, mit den Informationen
# @Comment: aus dem Dictionary "dict_print". Temporär ist so gemeint: Diese Funktion schreibt alle Einträge
# @Comment: aus dem Dictionary in die Dateien "workfile/body_fragment.txt" und workfile/nav_fragment.txt.
# @Comment: Diese Dateien liegen als Blueprint in dem Verzeichnis "workfile/originals" (siehe dazu weiter
# @Comment: unten). Die Einträge in "nav_fragment.txt" werden nur für folgende
# @Comment: Schlüssel im Python File geschrieben: Kapitel, Unterkapitel und Thema. Diese Einträge sind
# @Comment: in der HTML Seite im linken Navigationsbereich unterhalb von "::Dokument-Index::" zu finden.
# @Comment: Diese Einträge sind Sprungmarken zu den Ankerpunkten: Kapitel, Unterkapitel und Thema in der
# @Comment: Dokumentation. Das schreiben der eigentlichen HTML-Dokumentation findet ganz am Ende durch den
# @Comment: Aufruf der Funktion "write_html(html_write)" statt.
def writing_docu(dict_print, ziel1, html_write, txt_docu=True,
                 html_docu=True, docx_docu=False, pdf_docu=False):
    if file_exists(ziel1):
        os.remove(ziel1)

    # Das eigentliche Schreiben der Doku-Datei(en):
    for key, values in dict_print.items():
        if (isinstance(values, list)):
            for value in values:

                # Kapitel_Bereich:
                if key.startswith("#@Kapitel"):
                    k = re.search("(.*)# @Kapitel.*: (.*)", value)
                    if html_docu:
                        with open("./workfile/body_fragment.txt", "a", encoding="utf-8") as writer:
                            writer.write('<div class="div_kapitel"' + " " + 'id="' + k.group(1) + '#"' + '>' +
                                         '<H1>' + k.group(1) + k.group(2) + '</H1>' + '</div>' + "\n")

                        with open("./workfile/nav_fragment.txt", "a", encoding="utf-8") as nav_file:
                            nav_file.write('<li><a style="background-color:#D3D3D3" href=' + '"#'  + k.group(1)
                                           + '#' + '">' + k.group(1) + k.group(2) + '</a></li>'+ "\n")
                    if docx_docu:
                        pass
                    if pdf_docu:
                        pass

                # Link Doku Bereich:
                elif key.startswith("#@Doku-HTML"):
                    k = re.search(".*# @Doku-HTML.*: (.*)", value)
                    if html_docu:
                        with open("./workfile/body_fragment.txt", "a", encoding="utf-8") as writer:
                            writer.write('<div class="div_doku">' + '<a href=' + k.group(1) + " " + 'target="_blank">'
                                         + k.group(1) + '</a>' + '</div>' + "\n")
                    if docx_docu:
                        pass
                    if pdf_docu:
                        pass

                # Unterkapitel Bereich:
                elif key.startswith("#@Unterkapitel"):
                    k = re.search("(.*)# @Unterkapitel.*: (.*)", value)
                    if html_docu:
                        with open("./workfile/body_fragment.txt", "a", encoding="utf-8") as writer:
                            writer.write('<div class="div_unterkapitel"' + " " + 'id="' + k.group(1) + '#"' + '>'
                                         + '<H2>' + k.group(1) + " " + k.group(2) +
                                         '</H2>' + '</div>' + "\n")
                        with open("./workfile/nav_fragment.txt", "a", encoding="utf-8") as nav_file:
                            nav_file.write('<li><a href=' + '"#' + k.group(1) + '#' + '">' +
                                           k.group(1) + k.group(2) + '</a></li>'+ "\n")
                    if docx_docu:
                        pass
                    if pdf_docu:
                        pass

                # Thema Bereich:
                elif key.startswith("#@Thema"):
                    k = re.search("(.*)# @Thema.*: (.*)", value)
                    if html_docu:
                        with open("./workfile/body_fragment.txt", "a", encoding="utf-8") as writer:
                            writer.write('<div class="div_thema"' + " " + 'id="' + k.group(1) + '#"' + '>'
                                         + '<H3>' + k.group(1) + k.group(2) + '</H3>' + '</div>' + "\n")

                        with open("./workfile/nav_fragment.txt", "a", encoding="utf-8") as nav_file:
                            nav_file.write('<li><a href=' + '"#' + k.group(1) + '#' + '">' +
                                           k.group(1) + k.group(2) + '</a></li>'+ "\n")
                    if docx_docu:
                        pass
                    if pdf_docu:
                        pass

                # Comment-Bereich
                elif key.startswith("comment"):
                    k = value.replace("# @Comment: ", "")
                    if html_docu:
                        with open("./workfile/body_fragment.txt", "a", encoding="utf-8") as writer:
                            writer.write('<div class="div_comment">' + '<p>' + k + '</p>' + '</div>' + "\n")
                    if docx_docu:
                        pass
                    if pdf_docu:
                        pass

                # Author-Bereich:
                elif key.startswith("#@Author"):
                    k = value.replace("# @Author: ", "Author: ")
                    if html_docu:
                        with open("./workfile/body_fragment.txt", "a", encoding="utf-8") as writer:
                            writer.write('<div class="div_author">' + k + '</div>' + "\n")
                    if docx_docu:
                        pass
                    if pdf_docu:
                        pass

                # Copyright-Bereich:
                elif key.startswith("#@Copyright"):
                    k = value.replace("# @Copyright: ", "")
                    if html_docu:
                        with open("./workfile/body_fragment.txt", "a", encoding="utf-8") as writer:
                            writer.write('<div class="div_copyright">' + '©' + " " + k + '</div>' + "\n")
                    if docx_docu:
                        pass
                    if pdf_docu:
                        pass

                # Leerzeilen:
                elif value.startswith("\n"):
                    value.replace("\n", "")

                # End Bereich:
                elif key.startswith("#@End"):
                    k = value.replace("# @End:", "### End-Datei ###")
                    if html_docu:
                        with open("./workfile/body_fragment.txt", "a", encoding="utf-8") as writer:
                            writer.write(k + '<p>&nbsp;</p>' + '<p>&nbsp;</p>' + "\n")
                    if docx_docu:
                        pass
                    if pdf_docu:
                        pass

                # Codezeilen:
                else:
                    if html_docu:
                        k = value.replace(" ", "&nbsp;").replace("<", "&lt;").replace(
                            ">", "&gt;")
                        with open("./workfile/body_fragment.txt", "a", encoding="utf-8") as writer:
                            writer.write('<div class="div_code"><code>'+ k  + '</code></div>')
                    if docx_docu:
                        pass
                    if pdf_docu:
                        pass

                # Schreibt die TXT-Dokumentation:
                if txt_docu:
                    with open(ziel1, "a", encoding="utf-8") as writer:
                        value = replacer(value)
                        writer.write(value)
    # Hier wird die eigentliche HTML-Datei geschrieben, wenn "html_docu=True" auch auf True steht (siehe
    # weiter oben in main.py-Teil:
    if html_docu:
        write_html(html_write)

# @Thema: Replacer für nicht benötigte Strings
# @Comment: Dieser Replacer wird nur für das Schreiben der .txt-Dokumentation benötigt:
def replacer(value):
    text = value.replace(
        "# @Kapitel: ", "").replace(
        "# @Doku-HTML: ", "").replace(
        "# @Unterkapitel: ", "").replace(
        "# @Thema: ", "").replace(
        "# @Comment: ", "").replace(
        "# @Author: ", "Author: ").replace(
        "# @Copyright: ", "Copyright: ").replace(
        "# @End:", "##### Ende_File #####")
    return text

# @Thema: HTML-Dokument erstellen
# @Comment: Hier werden die temporären Dateien in "/workfile/" zu einer kompletten HTML-Datei
# @Comment: zusammengesetzt. Diese Funktion wird in "writing_docu" automatisch aufgerufen, wenn eine
# @Comment: HTML-Dokumentation erstellt werden soll.
def write_html(path):
    if file_exists(path):
        os.remove(path)

    # Schreibt zuerst alles aus header_fragment.txt in index.html:
    with open("./workfile/header_fragment.txt", "r", encoding="utf-8") as header_write:
        for head in header_write.readlines():
            with open(path, "a", encoding="utf-8") as index_write:
                index_write.write(head)

    # Dann Inhalte aus nav_fragment.txt in index.html:
    with open("./workfile/nav_fragment.txt", "r", encoding="utf-8") as nav_write:
        for nav in nav_write.readlines():
            with open(path, "a", encoding="utf-8") as index_write:
                index_write.write(nav)

    # Dann alles aus body_fragment.txt in index.html:
    with open("./workfile/body_fragment.txt", "r", encoding="utf-8") as body_write:
        for body in body_write.readlines():
            with open(path, "a", encoding="utf-8") as index_write:
                index_write.write(body)

    # Schreibt dann zum Schluss alles aus end_fragment.txt in index.html:
    with open("./workfile/end_fragment.txt", "r", encoding="utf-8") as end_write:
        for end in end_write.readlines():
            with open(path, "a", encoding="utf-8") as index_write:
                index_write.write(end)

# @Thema: Copy der py-Files in txt-files
# @Comment: Hier werden alle .py-Files in das Verzeichnis "pyfidocs/html/py_texte/" als .txt-Dateien
# @Comment: kopiert. Die .py-Files lassen sich in der HTML-Seite nicht aufrufen. Deshalb werden die
# @Comment: Inhalte der .py-Files einfach in .txt-Giles kopiert und können dann in den iFrames angezeigt werden.
# @Comment: Das dient hier nur als Zusatzhilfe, wenn man später einfacher ganze Bereiche aus dokumentierten
# @Comment: Python-Files kopieren möchte, z.B. um dies in neuen Projekten direkt einzufügen etc.:
def copy_in_txt(path):
    list_copy_txt = []
    path_2 = path
    path_3 = path + "pyfidocs/html/py_texte/"
    for file in os.listdir(path_2):
        if fnmatch.fnmatch(file, '*.py'):
            list_copy_txt.append(file)
    for list in list_copy_txt:
        x_orig= list
        shutil.copy(path_2 + x_orig, path_3 + x_orig + ".txt")

# @Thema: Die temporären Dateien löschen
# @Comment: In der main.py wird mit jedem Programmstart diese Funktion hier gestartet. Dadurch werden dann
# @Comment: die temporären Dateien gegen die Originaldateien ausgetauscht. Man kann Pyfidoc also beliebig oft
# @Comment: direkt hintereinander verwenden und hat hinterher dann keine doppelt/dreifach..Einträge in der
# @Comment: HTML-Datei bzw. in der txt-Dokumentation:
def vorlagen_restaurieren():
    path_2 = "./workfile/"
    path_3 = "workfile/originals/"
    try:
        list_working = []
        for file in os.listdir(path_2):
            if fnmatch.fnmatch(file, '*.txt'):
                list_working.append(file)
        for file in list_working:
            os.remove(path_2 + file)
    except:
        print("Die Working-Dateien können nicht gelöscht werden. Funktion 'vorlagen_restaurieren'")
    try:
        list_originals = []
        for origs in os.listdir(path_3):
            if fnmatch.fnmatch(origs, '*.txt'):
                list_originals.append(origs)
        for originals in list_originals:
            y_orig = originals
            shutil.copy(path_3 + y_orig, path_2 + y_orig)
    except:
        print("Die Originals-Dateien können nicht gelöscht werden. Funktion 'vorlagen_restaurieren'")

# @Thema: Zielverzeichnisse erstellen
# @Comment: Hier werden die Verzeichnisse mit jedem PyFiDoc-Lauf vorher gelöscht und dann wieder erstellt.
# @Comment: So wird ein mehrfacher Lauf von Pyfidoc hintereinander gewährleistet, wenn man z.b. am Ende eines
# @Comment: Projekts die Dokumentation innerhalb der Py-Files erstellt und direkt auch schon immer die
# @Comment: Auswirkungen auf das fertige Produkt "Html-Dokumentation" prüfen will etc.:
def delete_make_dir(path_source):
    dir_path = path_source + "pyfidocs/"
    html_path = path_source + "pyfidocs/html"
    html_path_2 = path_source + "pyfidocs/html/py_texte/"
    try:
        shutil.rmtree(dir_path)
    except OSError as e:
        pass

    while True:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        if os.path.exists(dir_path):
            break
    while True:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        if os.path.exists(dir_path):
            break
    if not os.path.exists(html_path):
        os.mkdir(html_path)
    if not os.path.exists(html_path_2):
        os.mkdir(html_path_2)

# @Thema: name = main
# @Comment: So soll man das ja machen:
if __name__ == "__main__":
    main()

# @End:


