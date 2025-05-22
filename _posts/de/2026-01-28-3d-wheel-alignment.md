---
layout: post
title: "Notizen zum Funktionsprinzip der 3D-Four-Rad-Alignment-Maschine"
lang: de
date:   2026-01-28 10:28:29
categories: Auto
tags: [Reifen, Vierradausrichtung, Fahrzeugwartung, Fahrwerk, Camber, Toe, Caster, ADAS]
description: "Eine tiefgehende Analyse der mathematischen Grundlagen, optischen Konstruktion und Fehlerkorrektur von 3D-Vierradausrichtgeräten – ein Muss vor dem Wechseln der Reifen oder einer Karosseriearbeit!"
keywords: "Vierradausrichtung, 3D Ausrichtmaschine, Fahrzeugwartung, Camber, Spurwinkel (Toe), Lenkneifung (Caster), ADAS-Kalibrierung, Drehachse der Räder, Laufabweichungskompensation, Fahrzeuginstandhaltung, Reifenpflege"
image: /images/3d-wheel.webp
faq:
  - question: "Was ist das Grundprinzip der 3D-Four-Rad-Alignment-Maschine?"
    answer: "Die 3D-Ausrichtmaschine nutzt Computer Vision, um die dynamischen Bahnen von Merkmalspunkten auf Reflektoren zu erfassen. Anschließend werden durch geometrische Berechnungen die physikalische Rotationsachse (Spindle Axis) des Rades rekonstruiert, anstatt sich nur mit der Messung der Radfelgen-Ebene zufriedenzugeben, um eine präzise Ausrichtung zu erreichen."
  - question: "Wie findet das 3D-Positionierungssystem die «physikalische Rotationsachse» der Räder?"
    answer: "Während des Durchlaufkompensationsverfahrens (Run-out Compensation) erfasst die Kamera kontinuierlich den Bewegungspfad charakteristischer Punkte am Reflektor. Diese Punkte beschreiben Bogenkurven. Das System berechnet über Algorithmen (wie das kleinste-Quadrate-Verfahren) den optimalen Mittelpunkt dieser Bögen sowie deren Kollinearität und Parallelismus, um eine Verbindungslinie oder einen Normalvektor zu bestimmen; dies entspricht der Rotationsachse. Dies korrigiert auch Fehler durch Verzug des Halterungsgeräts."
  - question: "Welche Eigenschaften hat das optische System des 3D-Positioniergeräts?"
    answer: "Hochwertige Positionierer verwenden in der Regel ein stereoskopisches visuelles System (Stereo Vision), um mit Hilfe von Parallaxe die Tiefe und räumliche Ausrichtung des Reflektors präzise zu berechnen. Der Reflektor besteht aus einem Rückstrahlermaterial, das zusammen mit einer Infrarot-Blitzlichtquelle neben der Linse und einem Filter ein Bild mit hohem Signal-Rausch-Verhältnis erzeugt und Störungen durch sichtbares Licht blockiert."
  - question: "Wie korrigiert die 3D-Positioniermaschine Montagefehler und Reifenfelgenabweichungen?"
    answer: "Das System berechnet den Schwingungsbetrag (Wobble) des Reflektors während der Rotation mit dem Reifen und zieht diesen aus den endgültigen Daten ab. Wenn jedoch das Rad selbst stark unrund ist (Verzerrung), müssen die Felge trotz mathematisch korrekter Positionierdaten repariert oder ersetzt werden, sonst bleibt die Fahrqualität beeinträchtigt."
  - question: "Wie reagiert der 3D-Positionierer auf Fehler, die durch Umwelteinflüsse verursacht werden?"
    answer: "Das System korrigiert den Abstand zwischen den beiden Kameras (Basislinie), der sich aufgrund des thermischen Ausdehnens und Zusammenziehens des Strahls ändert, mithilfe eines Temperatursensors. Hochwertige Systeme kompensieren zusätzlich die Temperatur in den CMOS/CCD-Chips der Kamera, um eine Verschiebung der Pixelkoordinaten durch Erwärmung zu verhindern. Darüber hinaus wird das System regelmäßig über ISO-zertifizierte Stativ kalibriert, um die Genauigkeit des Koordinatensystems sicherzustellen."
  - question: "3D 定位機在 ADAS 校正中扮演什麼角色？"
    answer: "這是現代定位機的關鍵功能。它能測算出車輛後輪形成的「推力線（Thrust Line）」，並以此為基準引導放置 ADAS 校正靶板，確保輔助駕駛系統（雷達、攝影機）的視線與車輛實際行進方向一致，進行精確校正。"
  - question: "Wie kann man beurteilen, ob die 3D-Four-Rad-Alignmentsanlage einer Werkstatt genau ist?"
    answer: "Man kann Folgendes prüfen: 1. Bestätigen Sie, dass regelmäßige Kalibrierungen vorliegen (in der Regel alle 6–12 Monate). 2. Prüfen Sie den Zustand des Geräts (Linsen, Querträger und Reflektoren müssen sauber und unbeschädigt sein). 3. Beobachten Sie die Messkonsistenz (sind wiederholte Tests hochgradig konsistent?). 4. Vergleichen Sie mit dem Fahrzeugzustand (kehrt das Lenkrad nach der Ausrichtung in den Nullpunkt zurück, fährt das Auto gerade?) 5. Fragen Sie nach einer offiziellen Zertifizierung durch einen Hersteller oder eine unabhängige Prüfstelle."
  - question: "Warum muss die Kalibrierung des Positioniergeräts überprüft werden?"
    answer: "Das Positioniergeät muss regelmäßig kalibriert werden, um seine Messgenauigkeit zu gewährleisten. Wenn eine Werkstatt einen aktuellen Kalibrierschein vorlegen kann, bedeutet dies, dass das Gerät gut gewartet ist und die Daten ein höheres Maß an Zuverlässigkeit aufweisen."
  - question: "Wenn das Fahrzeug nach der Ausrichtung weiterhin Probleme aufweist, was könnte die Ursache sein?"
    answer: "Falls sich das Lenkrad auch nach der Ausrichtung immer noch verzieht, wenn das Fahrzeug nicht gerade fährt oder die Reifen schnell asymmetrisch abnutzen, kann dies darauf hindeuten, dass das Ausrichtgerät selbst defekt ist, dass der Techniker einen Fehler bei der Arbeit gemacht hat oder dass physikalische Probleme wie ein unzureichender Echtheitsgrad des Felgenrings nicht gelöst wurden."
---

![Vierradjustierung](/images/3d-wheel.webp)  
Die Präzision der 3D-Vierradjustierungsanlage liegt darin, dass sie nicht auf die perfekte physikalische Installation (Klemmen können verziehen sich, Felgen können deformieren) vertraut. Stattdessen nutzt sie Computer Vision zur Erfassung dynamischer Bahnen und rekonstruiert durch geometrische Mathematik das unsichtbare „physikalische Drehzentrum".


## 1. Grundlegende mathematische Prinzipien: Suche nach dem einzigen „Rotationsachse"-Prinzip
Das ultimative Ziel der dreidimensionalen Positioniermaschine besteht nicht darin, die „Raden-Ebene" zu messen, sondern den **„physikalischen Rotationsachse (Spindel-Achse)"** des Rades festzulegen.

*   **Trajektorienanpassung (Trajectory Fitting):**  
    Bei der Durchführung einer Laufauslauf-Kompensation (Run-out Compensation) erfasst die Kamera nicht einfach nur einen statischen Ebenen, sondern dokumentiert kontinuierlich den Bewegungspfad charakteristischer Punkte auf dem Reflektor im Raum.
    *   Diese Punkte beschreiben im Raum mehrere **Kreissegmente (oder Ellipsensegmente in der Projektion)**.
    *   Das System berechnet mittels Algorithmen (z. B. Methode der kleinsten Quadrate / Least Squares Fitting) den **optimal angepassten Mittelpunkt** dieser räumlichen Bögen sowie deren **Koplanarität**.
*   **Vektorbestimmung:**  
    Die Verbindungslinie zwischen den Mittelpunkten dieser angepassten Kreise (bzw. die Normalvektoren, die senkrecht auf der angepassten Ebene stehen), stellt den einzigen Rotationsachse dieses Rades dar.
    > **Wichtige Korrektur:** Selbst wenn der Reflektor schief montiert ist, liegen weiterhin die Mittelpunkte der Bahnen des sich bewegenden Punktes genau auf der Rotationsachse. Das System eliminiert daher durch das „Berechnen der geometrischen Achse der Trajektorie" Montagefehler und stützt sich nicht ausschließlich auf den Ebenenwinkel des Reflektors.


## 2. Optische Systeme und Zielkonzepte
Um hochpräzise räumliche Koordinaten zu erhalten, kombiniert das Hardware-Design Materialwissenschaft mit Stereovisionstechnologie.

*   **Stereo Vision (räumliche Tiefenwahrnehmung):**
    Hochwertige Positionierungssysteme verfügen typischerweise auf beiden Seiten des Querträgers jeweils um eine „Doppellinse"-Anordnung.
    *   Durch Anwendung des **Parallax-Effekts** – ähnlich wie beim menschlichen Auge –, können sie die Tiefe (Z-Achsen-Distanz) und räumliche Orientierung präziser als mit einer einzelnen Linse berechnen.
    *   Dies verbessert erheblich die Messgenauigkeit von „Radstand", "Radbasis" sowie dem „Schubwinkel (Thrust Angle)".
*   **PnP-Algorithmen und Musterkodierung:**
    Die Punkte oder Quadrate auf den Reflektoren weisen eine spezifische geometrische Anordnung auf. Das System nutzt den **Perspective-n-Point (PnP)** Algorithmus, um aus 2D-Bildern die 3D-Orientierung abzuleiten.
*   **Hohe Signal-zu-Rausch-Verhältnisse (High SNR):**
    *   **Retroreflektive Materialien:** Diese sorgen dafür, dass das Licht den Rückweg nimmt; in Kombination mit Infrarot-Stroboskopen neben der Linse sorgt dies für eine Musterhelligkeit, die weit über dem Umgebungslicht liegt.
    *   **Filter:** Sie blockieren sichtbare Störquellen (wie Sonnenlicht oder Werkhallebeleuchtung) und lassen nur Wellenlängen des Infrarots passieren.


## 3. Fehlerquellen und mehrstufige Korrektur
Das Systemdesign muss gegen physikalische Installationsfehler, Hardware-Verformungen und Umgebungsvariablen gewirkt werden können.

*   **Installation und Laufabweichungskompensation (Run-out Compensation):**
    *   **Mathematische Korrektur:** Wenn sich der Reflektor mit dem Reifen drehend „schwingt" (Wobble), berechnet das System die Schwingungsamplitude und zieht diese aus den endgültigen Daten ab.
    *   **Physikalische Grenzen:** Bei schwerer Unzulänglichkeit des wahren Kreisrundheitsgrads der Felge (Verzerrung) kann zwar mathematisch eine Rotationsachse berechnet werden, aber das Fahrzeug wird beim Fahren physische Vibrationen erfahren. In diesem Fall sind die Positionsdaten zwar „mathematisch korrekt", jedoch muss in der Praxis empfohlen werden, die Felge zu reparieren oder auszutauschen; sonst bleibt die Fahrqualität unzureichend.
*   **Thermischer Drift und Umgebungsentschädigung:**
    *   **Strukturelle thermische Ausdehnung/Verzerrung:** Die Metallquerträger dehnen sich aufgrund der Temperaturwirkung minimal aus, sodass das System über Temperatursensoren den Abstand zwischen den beiden Kameras (Baseline) korrigieren muss.
    *   **Sensorenderift:** Hochwertige Systeme kompensieren die internen CMOS-/CCD-Chips bezüglich der Temperatur, um Pixelkoordinatenverschiebungen durch Chipüberhitzung zu verhindern.
*   **Kamerakalibrierung (Calibration):**
    Durch regelmäßige Kalibrierung mit ISO-Standardgerüsten wird sichergestellt, dass die relative Positionierung der Koordinatensysteme beider Kameras absolut präzise ist.


## 4. Systemintegration und Anwendungsebene
Der Positionierer ist nicht nur ein Messinstrument, sondern auch das Integrationszentrum für Daten des Fahrzeugschädels.

*   **OEM-Datenbank-Abgleich:**  
    Das System verfügt über eingebaute Werkseinstellungen (Kamm, Caster, Lenkwinkel). Die Messergebnisse werden sofort mit den Toleranzbereichen abgeglichen und führen Techniker mithilfe einer grafischen Benutzeroberfläche zur Einstellung.
*   **Integration der ADAS-Kalibrierung (Advanced Driver Assistance Systems):**  
    Dies ist eine Schlüsselkomponente moderner Ausrichtgeräte.
    *   Die Radarsensoren des Fahrzeugs (ACC) und die Kameras (Lane Keeping Assist) müssen auf Basis der Fahrzeug-**„Schublinie" (Thrust Line)** kalibriert werden.
    *   Berechnet das 3D-Ausrichtgerät den Schubwinkel, der durch die Hinterräder gebildet wird, führt es zur Positionierung des ADAS-Kalibrierziels und stellt sicher, dass die Sichtfelder der Assistenzsysteme mit der tatsächlichen Fahrtrichtung des Fahrzeugs übereinstimmen.

---


## Methode zur Bestimmung der Genauigkeit von Positioniermaschinen



### 1. Korrekturprotokoll
- Fragen Sie den Techniker oder die Werkstatt nach einem **Nachweis der regelmäßigen Kalibrierung** (in der Regel alle 6–12 Monate).  
- Die Originalwerkstatt bietet spezielle Kalibriergestelle an; nach Abschluss des Vorgangs wird ein Bericht oder eine Beschriftung erstellt.  
- Wenn die Werkstatt einen aktuellen Nachweis über die Kalibrierung vorlegen kann, ist das Vertrauen in ihre Arbeit höher.


### 2. Gerätezustand
- **Objektiv und Querträger**: Prüfen Sie, ob das Objektiv der Positioniermaschine sauber ist und ob am Querträger keine Einschlagsspuren oder Verzug vorliegt.  
- **Reflektorplatte**: Überprüfen Sie die Oberfläche der Reflektorplatte auf Vollständigkeit ohne Kratzer oder Verschmutzungen.  
- **Softwareversion**: Hochwertige Positionierungssysteme erhalten regelmäßige Softwareupdates, um sicherzustellen, dass Algorithmen und Fahrzeugdatenbanken aktuell sind.


### 3. Messkonsistenz
- **Wiederholte Tests**: Es kann verlangt werden, dass der Techniker zwei Positionierungen an demselben Fahrzeug durchführt; die Daten sollten dabei hoch konsistent sein.  
- **Links-rechts-Symmetrie**: Bei normalen Fahrzeugen sollte es keine extremen Unterschiede im Camber oder Toe geben; deutet eine offensichtlich unvernünftige Datenerfassung auf ein Problem mit der Ausrüstung hin, so ist dies zu prüfen.


### 4. Fahrzeugstatus vergleichen
- **Richtungscheibe im Nullpunkt**: Nach der Ausrichtung sollte die Lenkradposition zentriert sein und nicht versetzt ausfallen.  
- **Fahrttest**: Das Fahrzeug sollte nach der Ausrichtung auf einer geraden Straße in gerader Linie fahren, ohne sich zu einem Seitenbereich hinanziehen.  
- **Reifenverschleiß**: Wenn auch nach der Ausrichtung ein schneller seitlicher Verschleiß auftritt, liegt möglicherweise ein Fehler am Gerät oder bei der Bedienung vor.


### 5. **Professionelle Zertifizierung**
- Einige Wartungsbetriebe verfügen über eine Zertifizierung durch ein **Fabrik oder Drittanbieter-Labor** (z. B. bieten Marken wie Hunter, John Bean etc. jährliche Prüfungsleistungen an).  
- Betriebe mit einer solchen Zertifizierung hängen in der Regel Zertifikate am Ort des Vorfalls aus.

---


## Zusammenfassung
Um zu überprüfen, ob die Kalibrierungsmaschine im Servicezentrum genau ist, können Sie Folgendes tun:  

1. **Korrekturprotokolle prüfen** (innerhalb der letzten sechs oder zwölf Monate korrigiert).  
2. **Gerätestatus kontrollieren** (Objektiv, Reflektor und Querträger in Ordnung?).  
3. **Messkonsistenz beobachten** (plausible Daten mit hoher Reproduzierbarkeit).  
4. **Echtzustand des Fahrzeugs vergleichen** (Lenkrad zentriert, gerader Lauf, keine Unebenheiten an den Reifen).  
5. **Zertifizierung und Markenqualität sicherstellen** (vorhandene Original- oder Drittanbieter-Zeugnisse für die Prüfung vorhanden).