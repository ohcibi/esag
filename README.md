# ESAG Materialien

Größtenteils sind das hier TeX-Dokumente, die für verschiedene
Planungsangelegenheiten der ESAG dienen.

# LaTeX-Quellen übersetzen

Es gibt ein `Rakefile`. Dieses kann auf 2 Weisen genutzt werden.

Übersetze alle .tex-Dateien im Ordner src/ in gleichnamige PDF-Dateien

    rake

Starte preview-Modus mit latexmk für eine bestimmte .tex-Datei

    rake dateinamemitpunktpdfstattpunkttex.pdf

Eine Übersicht über alle Tasks gibt es mit

    rake -T

Alle gebauten Dateien löschen geht mit

    rake clean

# Dokumente

Hier eine Übersicht aller Dokumente:

## ausgaben.tex

Übersicht über alle Ausgaben

## fuehrungen.tex

Stationen der Campus-Führungen

## gruppenzettel_rallye.tex

Die Gruppenzettel der Rallye

## laufzettel_rallye.tex

Die Laufzettel der Rallye

## pruefungsordnung.tex

Die „Prüfungsordnung” für die Ralye

## schnitzeljagd.tex

## spielregeln.tex

## spielregeln_schnitzeljagd.tex

## stationen_rallye.tex

Übersicht über die Rallye-Stationen.

# Arbeit am Repository

Die PDF-Dateien im `build/`-Ordner sollten mit versioniert werden. Dabei sollte
darauf geachtet werden, dass die generierte PDF immer mit der TeX-Datei im
commit übereinstimmt. Die Verwendung von latexmk bzw. das Rakefile hilft dabei.

Sollten andere Tools als das Rakefile zum bauen benutzt werden, so ist darauf
zu achten, die PDFs nicht im Hauptverzeichnis zu versionieren, damit das
Repository einigermaßen sauber bleibt.
