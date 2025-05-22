---
layout: post
title: "Kfz-Ruhestromprüfung (Reihenschaltung): Ruhestrom sicher messen mit dem Bypass-Prüfschalter"
lang: de
date: 2026-11-01 10:00:00
categories: Auto
tags: [Autoelektrik, Autoreparatur, DIY Anleitung, Ruhestrom, Autobatterie Entladung]
related_posts:
  - 2026-11-02-dc-clamp-meter-parasitic-drain-guide.md
  - 2026-11-03-fuse-voltage-drop-parasitic-drain-guide.md
  - 2025-09-17-memory-saving-battery.md
description: "Ist Ihre Autobatterie nach wenigen Tagen Standzeit leer? Diese Anleitung erklärt Schritt für Schritt, wie Sie mit einem Ruhestrom-Bypass-Schalter und Multimeter den Ruhestrom messen, ohne Sicherungen zu zerstören oder Steuergeräte zu resetten."
keywords: "Ruhestrom messen, Autobatterie entlädt sich, Ruhestromprüfer, Bypass Schalter, Parasitic Drain Tester, Multimeter Sicherung defekt, Steuergeräte Ruhezustand, Sicherung ziehen, Auto Kriechstrom"
image: /images/howtoconnect.webp
faq:
  - question: "Was versteht man unter dem Kfz-Ruhestrom und welcher Wert ist normal?"
    answer: "Der Ruhestrom ist die geringe Stromaufnahme, die Steuergeräte (Alarmanlage, Funkschlüssel-Empfänger, Uhr) nach dem Abstellen, Verriegeln und vollständigen Einschlafen aller Fahrzeugsysteme dauerhaft aus der Batterie ziehen. Bei modernen Fahrzeugen liegt der normale Ruhestrom üblicherweise zwischen 20 mA und 60 mA (0,02 A - 0,06 A). Werte dauerhaft über 60 mA - 80 mA deuten auf einen unzulässigen Kriechstrom hin."
  - question: "Warum darf man ein Multimeter nicht einfach direkt in Reihe an den Minuspol hängen?"
    answer: "Beim Abklemmen wird das Fahrzeug stromlos. Schließt man das Multimeter direkt an, weckt der Einschaltstromstoß die Bordnetzsteuergeräte auf. Dieser kurzzeitige Einschaltstrom kann dutzende Ampere erreichen und brennt die interne 10A-Sicherung des Multimeters sofort durch. Zudem gehen Speicherwerte und Kalibrierungen verloren. Ein Bypass-Schalter leitet diesen Einschaltstrom über massives Metall um und schaltet erst nach dem Einschlafen auf das Multimeter um."
  - question: "Warum müssen die Fenster geöffnet und das Motorhaubenschloss manuell verriegelt werden?"
    answer: "Vollständig geöffnete Fenster verhindern ein versehentliches Aussperren durch die automatische Zentralverriegelung und sichern den Zugang zum Innenraumsicherungskasten. Das manuelle Einrasten der Haubenfalle mit einem Schraubendreher täuscht der Bordelektronik eine geschlossene Motorhaube vor, sodass die Alarmanlage und Karosseriesteuergeräte (BCM) in den Tiefschlaf gehen können."
  - question: "Warum muss man 15 bis 45 Minuten warten und Funkschlüssel 5 Meter fernhalten?"
    answer: "Moderne Fahrzeuge besitzen zahlreiche Steuergeräte (CAN-Bus, Gateway, BCM), die nach dem Abschließen Diagnosezyklen durchlaufen und erst nach 15 bis 45 Minuten schrittweise in den Tiefschlaf wechseln. Befindet sich ein Keyless-Go-Schlüssel in Funkreichweite, kommuniziert das Fahrzeug ununterbrochen damit und verhindert den Ruhezustand."
  - question: "Wie lokalisiert man den heimlichen Stromfresser, wenn der Ruhestrom über 60 mA liegt?"
    answer: "Lassen Sie das Multimeter aktiv angeschlossen. Öffnen Sie die Sicherungskästen im Motorraum oder Innenraum und ziehen Sie mit einer Sicherungszange eine Sicherung nach der anderen heraus, während Sie das Messgerät beobachten. Fällt der Ruhestrom beim Ziehen einer bestimmten Sicherung schlagartig unter 50 mA, ist der betroffene Stromkreis die Ursache (häufige Verursacher: Dashcam-Dauerstromwandler, Nachrüst-Radios oder defekte Türschlösser)."
  - question: "Wie lautet die korrekte Reihenfolge beim Rückbau nach der Messung?"
    answer: "Die Reihenfolge ist entscheidend: Schalten Sie den Prüfschalter IMMER zuerst auf ON (Geschlossen / Bypass) zurück. Ziehen Sie erst dann die Bananenstecker des Multimeters ab. Entfernen Sie das Trennmaterial, setzen Sie die originale Polklemme fest auf den Batteriepol und ziehen Sie die M10-Mutter fest. Nehmen Sie erst danach die Prüfklemmen ab und entriegeln Sie die Haubenfalle über den Hebel im Innenraum."
---

![Ruhestrom-Bypass-Schalter (Parasitic Drain Tester)](/images/tool.webp)

Bleibt Ihr Auto nach wenigen Tagen Standzeit mit leerer Batterie liegen? Höchstwahrscheinlich leidet Ihr Fahrzeug unter einem unzulässigen **Ruhestrom (Kriechstrom / Parasitic Drain)**.

Bei der klassischen Reihenmessung mit einem Multimeter muss die Batterie abgeklemmt werden. Dies führt jedoch zum Verlust von Einstellungen und Radio-Codes. Noch schlimmer: Der plötzliche Einschaltstromstoß beim Wiederanklemmen zerstört im Bruchteil einer Sekunde die **10A-Sicherung Ihres Multimeters**.

Der **Ruhestrom-Bypass-Schalter (Parasitic Drain Tester)** löst dieses Dilemma: Er schaltet das Multimeter **unterbrechungsfrei** in den Batteriekreis, schützt das Messgerät vor Zerstörung und verhindert, dass Steuergeräte aufwachen oder Daten verlieren.

> 💡 **Serien-Hinweis:**  
> Wenn Sie eine DC-Mikrostromzange besitzen und den Ruhestrom komplett ohne Werkzeug und ohne Abklemmen der Batterie prüfen möchten, lesen Sie unseren Begleitartikel:  
> 👉 [Kfz-Ruhestromprüfung (Zangen-Edition): Ruhestrommessung mit einer DC-Stromzange](/de/2026/dc-clamp-meter-parasitic-drain-guide.html)

---

## Aufbau des Bypass-Prüfschalters

Dieses Prüfwerkzeug zeichnet sich durch folgende Merkmale aus:

- **Zweiwege-Kippschalter (Bypass)**:
  - **ON (I / Geschlossen)**: Der Schalter leitet 100 % des Stroms über den Werkzeugkörper um. Das Multimeter zeigt 0 A an und ist vor Einschaltspitzen geschützt.
  - **OFF (O / Geöffnet)**: Der Bypass öffnet sich und zwingt den gesamten Ruhestrom durch das Multimeter für eine hochpräzise Milliampere-Messung (mA).
- **Spezielle Klemmen**: Eine **U-förmige Federklammer** (greift den Minuspol direkt unterhalb der Klemme) und eine **vollisolierte Batterieklemme** (für das Fahrzeugmassekabel).
- **Zwei steckbare 10A-Flachsicherungen**: Schützen das Messgerät zuverlässig vor Überlastung.
- **4-mm-Kupfer-Bananenstecker**: Kompatibel mit allen handelsüblichen Multimetern.

---

> [!CAUTION]
> ### ⚠️ Kurzschluss- und Zerstörungsgefahr
> **Vor der Messung Motor abstellen und Zündschlüssel abziehen. Niemals während der Messung die Zündung einschalten (ACC/ON) oder den Motor starten!**  
> **Keine Hochstromverbraucher einschalten (Scheinwerfer, Sitzheizung, Gebläse).** Es fließen sonst blitzartig Dutzende Ampere, die Sicherung und Messleitungen verbrennen.

---

## Standard-Ablauf (SOP) in 7 Schritten

![Bypass-Schalter Anschlussdiagramm](/images/howtoconnect.webp)

### Schritt 1: Fahrzeug vorbereiten & Motorhaubenschloss verriegeln
1. Zündung ausschalten, Innenbeleuchtung deaktivieren, Zündschlüssel abziehen.
2. **Alle vier Fenster vollständig öffnen** (verhindert Aussperren bei automatischer Verriegelung).
3. Motorhaube öffnen und die Schussfalle mit einem Schraubendreher nach unten in die **„Verriegelt“-Position** drücken. So erkennt das Bordnetzsteuergerät die Haube als geschlossen.

---

### Schritt 2: Prüfschalter auf ON (I / Geschlossen) stellen
Vor jedem Anschluss am Fahrzeug sicherstellen, dass der Prüfschalter auf **ON (I / Geschlossen)** steht. Der Werkzeugstrompfad ist nun überbrückt.

---

### Schritt 3: Prüfklemmen am Minuspol anbringen
1. Die **U-förmige Federklammer** fest an den Fuß des **Batterie-Minuspols** klemmen.
2. Die **isolierte Batterieklemme** sicher an der **originalen Minus-Polklemme** festklemmen.

---

### Schritt 4: Multimeter verbinden
1. Schwarzen 4-mm-Bananenstecker in die **COM-Buchse** des Multimeters stecken.
2. Roten 4-mm-Bananenstecker in die **10A / 20A Hochstrom-Buchse** stecken (niemals im mA-Eingang beginnen).
3. Drehschalter auf **Gleichstrom (DC A)** stellen.

---

### Schritt 5: Originale Polklemme lösen und isolieren
1. Mit einem **M10-Schlüssel** die Mutter der Minus-Polklemme lockern.
2. Die Polklemme vorsichtig nach oben vom Batteriepol abheben (die Stromversorgung bleibt über das Prüfwerkzeug unterbrechungsfrei bestehen).
3. **Ein Stück dicke Pappe oder Kunststoff zwischen Polklemme und Pol schieben**, um jeden versehentlichen Metallkontakt zu verhindern.

---

### Schritt 6: Fahrzeug verriegeln und Ruhephase abwarten (15 - 45 Minuten)
1. Alle Türen schließen und Fahrzeug per Fernbedienung verriegeln.
2. **Keyless-Go-Schlüssel mindestens 5 Meter vom Auto entfernen.**
3. **15 bis 45 Minuten warten**, bis sämtliche Steuergeräte (BCM, ECU, CAN-Bus) schrittweise in den Tiefschlaf wechseln.

---

### Schritt 7: Schalter auf OFF kippen und Ruhestrom ablesen
1. Prüfen, ob das Multimeter noch eingeschaltet ist.
2. Den Schalter auf **OFF (O / Geöffnet)** kippen.
3. Der Bypass ist nun getrennt; der gesamte Strom fließt durch das Multimeter. Den stabilen Ruhestromwert ablesen.

> [!TIP]
> **Umschalten in den feinen mA-Messbereich:**  
> Wenn der Strom bereits sehr niedrig ist und Sie eine höhere Nachkommastellengenauigkeit wünschen, **schalten Sie den Prüfschalter IMMER zuerst auf ON (Geschlossen) zurück**, bevor Sie den Multimeter-Drehschalter umstellen oder die rote Messleitung in die mA-Buchse umstecken. Schalten Sie erst danach wieder auf **OFF**.

| Messwert (DC A) | Bewertung | Diagnose & Maßnahme |
| :--- | :--- | :--- |
| **20 mA - 60 mA (0,02 A - 0,06 A)** | ✅ **Normalbereich** | Sollerhaltung für Alarmanlage und Uhr; Batterie hält viele Wochen. |
| **60 mA - 80 mA (0,06 A - 0,08 A)** | ⚠️ **Leicht erhöht** | Zubehör prüfen (z. B. Dashcam-Parküberwachung im Standby). |
| **> 80 mA (oder Hunderte mA)** | ❌ **Starker Kriechstrom** | Schwere Entladung. Saugt die Batterie binnen Tagen leer; Sicherungen ziehen! |

---

## Fehlersuche durch Ziehen der Sicherungen

Liegt der gemessene Ruhestrom dauerhaft über **60 mA**, bleibt der Schalter auf OFF:

1. **Sicherungskästen lokalisieren**: Motorraum, Armaturenbrett oder Kofferraum.
2. **Einzeln ziehen**: Mit einer Sicherungszange **immer nur eine Sicherung herausziehen** und die Anzeige des Multimeters beobachten.
3. **Schaltkreis identifizieren**:
   - Ändert sich der Wert nicht, Sicherung **wieder einstecken** und die nächste prüfen.
   - Fällt der Strom beim Ziehen einer bestimmten Sicherung **schlagartig unter 50 mA**, haben Sie den fehlerhaften Stromkreis gefunden!
4. **Typische Übeltäter**:
   - Fest verdrahtete Dashcam-Spannungswandler mit defekter Unterspannungsabschaltung.
   - Nachgerüstete Android-Radios oder Subwoofer-Verstärker (Remote-Leitung dauerhaft aktiv).
   - Defekte Türkontaktschalter / Mikroschalter im Türschloss.
   - Handschuhfach- oder Kofferraumbeleuchtung schaltet nicht ab.

---

## Sicherer Rückbau nach der Messung (SOP)

Halten Sie die Reihenfolge strikt ein, um Abreißfunken und Datenverlust zu vermeiden:

1. **Schalter auf ON**: Den Prüfschalter zurück auf **ON (I / Geschlossen)** stellen.
2. **Multimeter abziehen**: Die 4-mm-Bananenstecker vom Multimeter trennen.
3. **Polklemme montieren**: Isolierpappe entfernen, originale Polklemme fest auf den Minuspol stecken und die M10-Mutter festziehen.
4. **Prüfwerkzeug abbauen**: Erst nach festem Sitz der Polklemme die U-Federklammer und die Prüfklemme abnehmen.
5. **Haubenfalle entriegeln**: **Motorhaube niemals mit verriegeltem Schloss zuschlagen!** Haubenentriegelungshebel im Innenraum ziehen, Schlossfeder aufspringen lassen, Haube normal schließen.
