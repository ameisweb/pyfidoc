import shutil, os

file_list = ["1_testdatei.py"]
path_source = "C:/Users/work/Documents/test_files/"
for file in file_list:
    print(file)
    no_anhang = file.split(".")

    # Schreibt die iFrame-Dateien:
    link = path_source + "pyfidocs/html/py_texte/" + no_anhang[0] + ".html"
    # Schreibt Link Inhalt in text_iframe.txt Datei:
    with open("./workfile/text_iframe.txt", "a", encoding="utf-8") as iframe_file:
        iframe_file.write(' src = "' + file + '.txt' + '" >' + '</div> </body> </html>')
################### bis hier alles ok #############################################

    # Schreibt readlines in Ziel-iFrame-HTML-Datei:
    with open("./workfile/text_iframe.txt", "r", encoding="utf-8") as frame_write:
        for line in frame_write.readlines():
            with open(link, "a", encoding="utf-8") as index_write:
                index_write.write(line)


    # löscht Datei ./workfile/text_iframe.txt
    if os.path.exists("./workfile/text_iframe.txt"):
        os.remove("./workfile/text_iframe.txt")
    else:
        print("File ./workfile/text_iframe.txt does not exist")
    # Kopiert dann wieder das Original-File text_iframe.txt in workfile-Verzeichnis:
    y_orig = "./workfile/originals/text_iframe.txt"
    y_copy = "./workfile/text_iframe.txt"
    shutil.copy(y_orig, y_copy)