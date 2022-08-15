# @Kapitel: Doku-Drucker aus Python-Sccripten -  Ver. 1.0
# @Author: A/M
# @Copyright: Zur freien nichtkommerziellen Verfügung

# @Unterkapitel: Das Programm
# @Thema: Import ins Script:
from functions import source_read, writing_docu, files_read, files_write_navi, vorlagen_restaurieren, copy_in_txt
from functions import delete_make_dir

# @Thema: Konfiguration Pfade, Dateinamen
# @Comment: Eingabe des Doku-Dateinamens, des Pfades des Verzeichnisses etc.:
path_source = "C:/Users/work/Documents/test_files/"
source_liste = []
name_doku_file = path_source + "pyfidocs/" + "test_doku.txt"
name_html_file = path_source + "pyfidocs/html/" + "index.html"



# @Thema: Das main()-Programm
def main():
    delete_make_dir(path_source)
    vorlagen_restaurieren()
    if len(source_liste) == 0:
        list_files = files_read(path_source)
        files_write_navi(list_files, path_source)
    else:
        list_files = source_liste
        files_write_navi(list_files, path_source)
    dicttionary = source_read(path_source, list_files)
    writing_docu(dicttionary, name_doku_file, name_html_file)
    copy_in_txt(path_source)



if __name__ == "__main__":
    main()
