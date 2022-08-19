# PyFiDoc Version 1.0
#
1.1 Wofür ist das Programm
-
1.1.1 Ausgangslage
-
Jetzt gerade erlerne ich die Python-Programmierung. Noch kenne ich längst nicht alle Themen. Meine Arbeitsweise ist 
wie folgt: Wenn ich Themen erarbeite, dann übe ich diese Themen auch gleich in Python-Dateien. Wenn man dann so 
im Übungsmodus ist, dann lernt man "Dies oder Das" zu Themenbereichen. Dieses Wissen möchte ich mir selbst auf Dauer 
zur Verfügung stellen. Mehrere Suchen ergaben aber leider, dass es zwar bereits Code to Dokumentation Projekte gibt, 
diese Projekte aber insgesamt so komplex sind, dass man da durchaus mehrere Wochen benötigt, nur um sich 
einzuarbeiten. Diese Zeit habe ich gerade nicht, da lerne ich lieber weiter die Python Programmierung, die ich 
noch nicht kenne.

1.1.2 Idee für eigenes Programm
-
Da ich bisher schon ein paar Dinge gelernt habe in der Python-Programmierung, habe ich mich direkt entschieden, 
mir ein eigenes kleines Programm zu schreiben, um meine Notizen in den Lerncode-Dateien gleich auf sinnvolle Weise 
in eine Dokumentation zu überführen. HTML bietet sich hier direkt an. Also habe ich mir eine möglichst einfache 
"Doctag"-Syntax überlegt, die dann von PyFiDoc erkannt und in entsprechende Form gebracht werden kann. Die 
Grundlagen die ich jetzt gerade erlerne und zu eigenen Zwecken kommentiere in den Code-Dateien, soll mir in 
Zukunft als "Cheat-Sheet" dienen.

1.1.3 Grundlagen Syntax
-

Die wichtigste Basis-Syntax: Jede "Nicht-Code-Zeile" sollte mit einem # beginnen. Danach dann ein Leerzeichen und:
"@Name: " (Leerzeichen nach : ist erforderlich). Folgende Möglichkeiten gibt es: "@Kapitel: ", "@Unterkapitel: ",
"@Thema: ", "@Author: ", "@Copyright: ", "@Doku-HTML: ", "End:" und natürlich "@Comment: ". Die eigentlichen 
Codezeilen haben keine Kennung am Anfang einer Zeile, d.h. jede Zeile im Code ohne die obigen Kennungen werden 
als Code-Zeile interpretiert. Die Namen stehen für genau das: Kapitel für Kapitel, Unterkapitel für Unterkapitel 
etc. Alle "@Doku-HTML: " erwarten http(s)-Links und werden entsprechend gelinkt im Dokument. ....

..more here:

http://pyfidoc.de