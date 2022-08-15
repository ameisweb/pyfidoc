# @Kapitel: Funktions-Script
# @Unterkapitel: Importe

import fnmatch
import os, shutil
import re
from os.path import exists as file_exists
# import json
# import pprint

# @Thema: Funktion Verzeichnisfiles einlesen in Liste
def files_read(path):
    list_files = []
    for file in os.listdir(path):
        if fnmatch.fnmatch(file, '*.py'):
            list_files.append(file)
    return list_files

def files_write_navi(file_list):
    for file in file_list:
        with open("./workfile/nav_fragment.txt", "a", encoding="utf-8") as nav_file:
            nav_file.write('<li><a href="' + file + '.txt' + '"' + " " + 'target="_blank"' + '>'
                           + file + '.txt' + '</a></li>' + "\n")
    with open("./workfile/nav_fragment.txt", "a", encoding="utf-8") as nav_file:
        nav_file.write('<li><a class="active" href="#home">::Dokument_Index::</a></li>' + "\n")


# @Thema: Die Sourcefiles einlesen und in Dictionary schreiben
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

    # For-Schleife und lesen aller Inhalte der Dateien in der Liste:
    for onefile in list_files:
        # Pro Datei komplettes auslesen und schreiben der Zeilen ins Dictionary:
        with open(path + onefile, "r", encoding="utf-8") as file:
            for line in file.readlines():
                # Kapitel-Bereich:
                if line.startswith("# @Kapitel"):
                    count_kapitel += 1
                    if count_kapitel > 1:
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
                    var_com = "comment" + str(count_comment)
                    line = line.replace("\n", "")
                    if var_com not in dict_print.keys():
                        dict_print[str(var_com)] = [line + " " + "\n"]
                    else:
                        get_value = str(dict_print.get(var_com)).replace("[", "").replace("]",
                                                                    "").replace("'", "").replace("\\n", "")
                        value_plus = str(get_value) + (str(line + " " + "\n").replace("# @Comment: ", ""))
                        dict_print.pop(var_com)
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



# @Thema: Alle Comments im Dictionary mit Zeilenumbruch am Ende versehen
def dict_comments(dict_print):
    key_liste = list(dict_print.keys())
    for k in key_liste:
        if k.startswith("comment"):
            dict_print[k].append("\n")
    return dict_print


# @Thema: Informationen aus Dictionary in Dokumentationen schreiben
def writing_docu(dict_print, ziel1, html_write, txt_docu=True,
                 html_docu=True, docx_docu=False, pdf_docu=False):
    if file_exists(ziel1):
        os.remove(ziel1)
    # Das eigentliche Schreiben der Doku-Datei(en):
    for key, values in dict_print.items():
        if (isinstance(values, list)):
            for value in values:
                # print(value, end="")
                # Kapitel_Bereich:
                if re.search("^[0-9].*# @Kapitel.*", value):
                    k = re.search("(.*)# @Kapitel.*: (.*)", value)
                    if html_docu:
                        with open("./workfile/body_fragment.txt", "a", encoding="utf-8") as writer:
                            writer.write('<div class="div_kapitel"' + " " + 'id="' + k.group(1) + '#"' + '>' +
                                         '<H1>' + k.group(1) + k.group(2) + '</H1>' + '</div>' + "\n")

                        with open("./workfile/nav_fragment.txt", "a", encoding="utf-8") as nav_file:
                            nav_file.write('<li><a style="background-color:#D3D3D3" href=' + '"#'  + k.group(1)
                                           + '#' + '">' + k.group(1) + k.group(2) + '</a></li>')
                    if docx_docu:
                        pass
                    if pdf_docu:
                        pass

                # Link HTTP Bereich:
                elif value.startswith("# @Doku-HTML"):
                #elif re.search("^.*# @Doku-HTML.*", value):
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
                elif re.search("^[0-9].*# @Unterkapitel.*", value):
                    k = re.search("(.*)# @Unterkapitel.*: (.*)", value)
                    if html_docu:
                        with open("./workfile/body_fragment.txt", "a", encoding="utf-8") as writer:
                            writer.write('<div class="div_unterkapitel"' + " " + 'id="' + k.group(1) + '#"' + '>'
                                         + '<H2>' + k.group(1) + " " + k.group(2) +
                                         '</H2>' + '</div>' + "\n")
                        with open("./workfile/nav_fragment.txt", "a", encoding="utf-8") as nav_file:
                            nav_file.write('<li><a href=' + '"#' + k.group(1) + '#' + '">' +
                                           k.group(1) + k.group(2) + '</a></li>')
                    if docx_docu:
                        pass
                    if pdf_docu:
                        pass

                # Thema Bereich:
                elif re.search("^[0-9].*# @Thema.*", value):
                    k = re.search("(.*)# @Thema.*: (.*)", value)
                    if html_docu:
                        with open("./workfile/body_fragment.txt", "a", encoding="utf-8") as writer:
                            writer.write('<div class="div_thema"' + " " + 'id="' + k.group(1) + '#"' + '>'
                                         + '<H3>' + k.group(1) + k.group(2) + '</H3>' + '</div>' + "\n")

                        with open("./workfile/nav_fragment.txt", "a", encoding="utf-8") as nav_file:
                            nav_file.write('<li><a href=' + '"#' + k.group(1) + '#' + '">' +
                                           k.group(1) + k.group(2) + '</a></li>')
                    if docx_docu:
                        pass
                    if pdf_docu:
                        pass

                # Comment-Bereich
                elif re.search(".*# @Comment.*", value):
                    k = value.replace("# @Comment: ", "")
                    if html_docu:
                        with open("./workfile/body_fragment.txt", "a", encoding="utf-8") as writer:
                            writer.write('<div class="div_comment">' + '<p>' + k + '</p>' + '</div>' + "\n")
                    if docx_docu:
                        pass
                    if pdf_docu:
                        pass

                # Author-Bereich:
                elif re.search(".*# @Author.*", value):
                    k = value.replace("# @Author: ", "Author: ")
                    if html_docu:
                        with open("./workfile/body_fragment.txt", "a", encoding="utf-8") as writer:
                            writer.write('<div class="div_author">' + k + '</div>' + "\n")
                    if docx_docu:
                        pass
                    if pdf_docu:
                        pass

                # Copyright-Bereich:
                elif re.search(".*# @Copyright.*", value):
                    k = value.replace("# @Copyright: ", "")
                    if html_docu:
                        with open("./workfile/body_fragment.txt", "a", encoding="utf-8") as writer:
                            writer.write('<div class="div_copyright">' + '©' + " " + k + '</div>' + "\n")
                    if docx_docu:
                        pass
                    if pdf_docu:
                        pass

                # Leerzeilen:
                elif re.search("^\n", value):
                    value.replace("\n", "")

                # End Bereich:
                elif re.search(".*# @End.*", value):
                    k = value.replace("# @End: ", "")
                    if html_docu:
                        with open("./workfile/body_fragment.txt", "a", encoding="utf-8") as writer:
                            writer.write('<p></p>' + '<p></p>' + '<p></p>' + "\n")
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
                            writer.write('<div class="div_code">'+ k  + '</div>')
                    if docx_docu:
                        pass
                    if pdf_docu:
                        pass

                # Schreibt die TXT-Datei:
                if txt_docu:
                    with open(ziel1, "a", encoding="utf-8") as writer:
                        value = replacer(value)
                        writer.write(value)
    if html_docu:
        write_html(html_write)
    vorlagen_restaurieren()

# @Thema: Replacer für nicht benötigte Strings
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

# def html_header_writer(path):
#         with open("./tmp_dateien/header_fragment.txt", "r", encoding="utf-8") as header_write:
#             for line in header_write.readlines():
#                 with open(path, "a", encoding="utf-8") as index_write:
#                     index_write.write(line)


def write_html(path):
    if file_exists(path):
        os.remove(path)
    with open("./workfile/header_fragment.txt", "r", encoding="utf-8") as header_write:
        for head in header_write.readlines():
            with open(path, "a", encoding="utf-8") as index_write:
                index_write.write(head)
    with open("./workfile/nav_fragment.txt", "r", encoding="utf-8") as nav_write:
        for nav in nav_write.readlines():
            with open(path, "a", encoding="utf-8") as index_write:
                index_write.write(nav)
    with open("./workfile/body_fragment.txt", "r", encoding="utf-8") as body_write:
        for body in body_write.readlines():
            with open(path, "a", encoding="utf-8") as index_write:
                index_write.write(body)
    with open("./workfile/end_fragment.txt", "r", encoding="utf-8") as end_write:
        for end in end_write.readlines():
            with open(path, "a", encoding="utf-8") as index_write:
                index_write.write(end)

def copy_in_txt(path):
    list_copy_txt = []
    path_2 = path
    for file in os.listdir(path_2):
        if fnmatch.fnmatch(file, '*.py'):
            list_copy_txt.append(file)
    for list in list_copy_txt:
        x_orig= list
        shutil.copy(path_2 + x_orig, path_2 + x_orig + ".txt")


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


def delete_make_dir(path_source):
    dir_path = path_source + "documentations/"
    try:
        shutil.rmtree(dir_path)
    except OSError as e:
        pass

    while True:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        if os.path.exists(dir_path):
            break








# @Thema: Nur zur Sicherheit
if __name__ == "__main__":
    main()

