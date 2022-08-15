# PyFiDoc Version 1.0
#
1.1 Mögliche Syntax in Code-Dateien

1.1.1 Grundlagen Syntax

Die wichtigste Basis-Syntax: Jede nicht-Code-Zeile muss mit einem # beginnen. Danach dann ein Leerzeichen und: "@Name: " (Leerzeichen nach : ist erforderlich). Folgende Möglichkeiten gibt es: "@Kapitel: ", "@Unterkapitel: ", "@Thema: ", "@Author: ", "@Copyright: ", "@Doku-HTML: ", und natürlich "@Comment: ". Die eigentlichen Codezeilen haben keine Kennung am Anfang einer Zeile, d.h. jede Zeile im Code ohne die obigen Kennungen werden als Code-Zeile interpretiert. Die Namen stehen für genau das: Kapitel für Kapitel, Unterkapitel für Unterkapitel etc. Alle "@Doku-HTML: " erwarten http(s)-Links und werden entsprechend gelinkt im Dokument.

..more here:

http://pyfidoc.de