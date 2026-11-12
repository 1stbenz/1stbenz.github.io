---
layout: post
title: "Kfz-Ruhestromprüfung (Spannungsabfall-Edition): Ruhestrom finden ohne Sicherungsziehen per Fuse Voltage Drop Chart"
lang: de
date: 2026-11-03 10:00:00
categories: Auto
tags: [Autoelektrik, Autoreparatur, DIY Anleitung, Ruhestrom, Spannungsabfall, Sicherung prüfen, Autobatterie Entladung]
related_posts:
  - 2026-11-01-parasitic-drain-tester-guide.md
  - 2026-11-02-dc-clamp-meter-parasitic-drain-guide.md
  - 2025-09-17-memory-saving-battery.md
description: "Ruhestrom suchen durch Ziehen von Sicherungen? Bei modernen CAN-Bus-Fahrzeugen weckt das Ziehen Steuergeräte auf und verfälscht die Messung. Diese Anleitung zeigt, wie Sie per Millivolt-Spannungsabfall an Sicherungen (Fuse Voltage Drop) Kriechströme in 2 Minuten aufspüren."
keywords: "Sicherungsspannungsabfall, Fuse Voltage Drop Chart, Ruhestrom messen, Kfz Kriechstrom, Sicherungen nicht ziehen, Multimeter Millivolt, Power Probe Sicherungstabelle, Autobatterie entlädt sich"
image: /images/FuseVoltageMethod.webp
faq:
  - question: "Was ist die Methode des Spannungsabfalls an Sicherungen (Fuse Voltage Drop)?"
    answer: "Jede Kfz-Flachsicherung besitzt einen winzigen, konstanten Innenwiderstand (im Milliohm-Bereich, mΩ). Nach dem Ohmschen Gesetz (V = I × R) erzeugt jeder durch die Sicherung fließende Ruhestrom einen minimalen Spannungsabfall in Millivolt (mV) an den Prüfpunkten. Durch Messung dieses mV-Werts und Abgleich mit einer Tabelle lässt sich der Strom exakt berechnen, ohne die Sicherung herauszuziehen."
  - question: "Warum ist diese Methode dem Ziehen von Sicherungen überlegen?"
    answer: "Moderne Fahrzeuge nutzen vernetzte Steuergeräte (CAN-Bus / LIN-Bus). Das Ziehen einer Sicherung unterbricht die Stromversorgung, was die Netzwerk-Gateways alarmiert und das gesamte Fahrzeug wieder aufweckt (Wake-up). Nach dem Wiedereinstecken muss man erneut 15 bis 45 Minuten auf die Busruhe warten. Die Spannungsabfallmethode ist völlig unterbrechungsfrei und weckt keine Steuergeräte auf."
  - question: "Ist ein negativer Messwert (z. B. -0,5 mV) normal?"
    answer: "Vollkommen normal. Das Minuszeichen zeigt lediglich die Polung der Messspitzen zur Stromflussrichtung an. Sicherungen haben keine Polarität; ignorieren Sie das Vorzeichen und nutzen Sie den Absolutwert (0,5 mV) für die Tabelle."
---

![Kfz-Sicherungsspannungsabfall messen](/images/FuseVoltageMethod.webp)

Entlädt sich die Autobatterie nach wenigen Tagen Standzeit, wird bei der Fehlersuche oft reflexartig Sicherung für Sicherung gezogen. Bei modernen Fahrzeugen mit CAN-Bus-Vernetzung ist das **oft fatal**: Das Ziehen einer Sicherung weckt die schlafenden Steuergeräte auf, der Ruhestrom schießt in die Höhe und die Messung wird unbrauchbar.

Die **Spannungsabfall-Methode an Sicherungen (Fuse Voltage Drop Chart)** ist der Goldstandard professioneller Kfz-Diagnostiker: **Kein Sicherungsziehen, keine Stromunterbrechung, kein Aufwecken der Steuergeräte**. Mit einem herkömmlichen Multimeter im Millivolt-Bereich scannen Sie den gesamten Sicherungskasten in unter zwei Minuten.

> **Serien-Navigation:**
> - Gesamten Ruhestrom messen: [Reihenschaltungs-Guide (Bypass-Schalter)](/de/2026/parasitic-drain-tester-guide.html) | [DC-Stromzangen-Guide](/de/2026/dc-clamp-meter-parasitic-drain-guide.html)

---

## Grundprinzip: Ohmsches Gesetz $$V = I \times R$$

Kfz-Flachsicherungen sind keine widerstandslosen Supraleiter. Der Schmelzdraht besitzt einen minimalen, stabilen und bekannten Innenwiderstand (meist zwischen 2mΩ und 30mΩ).

Nach dem **Ohmschen Gesetz**:

$$V = I \times R \quad \Longrightarrow \quad I = \frac{V}{R}$$

- $$R$$ (Innenwiderstand der Sicherung): Fest und bekannt anhand von Typ und Nennstrom.
- $$V$$ (Spannungsabfall): Die winzige Spannungsdifferenz an den Prüfpunkten in Millivolt ($$mV$$).
- $$I$$ (Ruhestrom): Der tatsächlich fließende Strom in Milliampere ($$mA$$).

Auf der Oberseite von Flachsicherungen befinden sich **zwei freiliegende Metall-Testpunkte**. Wenn Strom durch die Sicherung fließt, entsteht zwischen diesen Punkten ein messbarer Millivolt-Spannungsabfall ($$mV$$):
- **`0.0 mV`** → Kein Stromfluss, Stromkreis schläft ordnungsgemäß.
- **Messwert vorhanden (z. B. `0.6 mV`)** → Stromkreis zieht Strom; anhand der Tabelle kann der genaue mA-Wert abgelesen werden.

---

## Benötigte Werkzeuge

![Feine Prüfspitzen für Multimeter](/images/sharppoint.webp)

1. **Digitalmultimeter**: Eingestellt auf den Bereich **DC mV (Gleichspannung Millivolt)** (Auflösung 0,1 mV oder 0,01 mV).
2. **Nadel-Messspitzen (unerlässlich)**: Standard-Prüfspitzen sind zu dick für die kleinen Testöffnungen der Sicherungen. Verwenden Sie feine 0,7mm–1,0mm Prüfspitzen, um Oxidschichten sicher zu durchdringen.
3. **Vergleichstabelle**: Die nachfolgenden Tabellen.

---

## Schritt-für-Schritt Messanleitung

### Schritt 1: Fahrzeug verriegeln und Busruhe abwarten
1. Zündung ausschalten, alle Verbraucher abschalten, **alle Fenster vollständig öffnen** (Schutz vor Aussperren).
2. Sicherungskästen freilegen und die **Schlösser von Türen/Motorhaube/Heckklappe manuell mit einem Schraubendreher verriegeln**, um geschlossene Türen zu simulieren.
3. Fahrzeug per Funkfernbedienung abschließen und **Keyless-Schlüssel mindestens 5 Meter entfernen**.
4. **15 bis 45 Minuten warten**, bis alle Steuergeräte (BCM, ECU, Gateway) vollständig in den Tiefschlaf übergegangen sind.

---

### Schritt 2: Multimeter ansetzen und messen
1. Rote Messleitung in **V/Ω/mV**, schwarze Messleitung in **COM**.
2. Wahlschalter auf **DC mV** stellen.
3. Beide Messspitzen fest auf die **beiden Testpunkte der Sicherung** drücken, um die Oxidschicht zu durchstoßen.
4. Messwert ablesen:
   - **`0.0 mV`**: Stromlos. Direkt zur nächsten Sicherung übergehen.
   - **Messwert erscheint (z. B. `0.6 mV`)**: Hier fließt Strom! Sicherungstyp (Mini oder Standard/ATO), Nennstrom (z. B. 10A rot) und mV-Wert notieren.

> **Negativer Wert angezeigt (z. B. -0,5 mV)?**  
> Das Vorzeichen zeigt nur die Richtung der Prüfspitzen an. Sicherungen haben keine Polarität; **einfach den Absolutwert (`0,5 mV`)** für die Tabelle verwenden.

---

## Referenztabellen für den Sicherungsspannungsabfall

Mit dem gemessenen mV-Wert schlagen Sie in der passenden Tabelle den Stromverbrauch in Milliampere (mA) nach:

### 1. Mini-Flachsicherungen (ATM) Spannungsabfall-Tabelle (Einheit: mA)

| Nennstrom | Widerstand ca. | 0.2 mV | 0.4 mV | 0.6 mV | 0.8 mV | 1.0 mV | 1.5 mV | 2.0 mV |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **5A (Hellbraun)** | ~15.2 mΩ | 13 mA | 26 mA | 39 mA | 53 mA | **66 mA** | 99 mA | 132 mA |
| **7.5A (Braun)** | ~10.1 mΩ | 20 mA | 40 mA | 59 mA | 79 mA | **99 mA** | 149 mA | 198 mA |
| **10A (Rot)** | ~7.1 mΩ | 28 mA | 56 mA | 85 mA | 113 mA | **141 mA** | 211 mA | 282 mA |
| **15A (Blau)** | ~4.6 mΩ | 43 mA | 87 mA | 130 mA | 174 mA | **217 mA** | 326 mA | 435 mA |
| **20A (Gelb)** | ~3.3 mΩ | 61 mA | 121 mA | 182 mA | 242 mA | **303 mA** | 455 mA | 606 mA |
| **25A (Transparent)**| ~2.5 mΩ | 80 mA | 160 mA | 240 mA | 320 mA | **400 mA** | 600 mA | 800 mA |
| **30A (Grün)** | ~2.0 mΩ | 100 mA | 200 mA | 300 mA | 400 mA | **500 mA** | 750 mA | 1000 mA|

---

### 2. Standard-Flachsicherungen (ATO / ATC) Spannungsabfall-Tabelle (Einheit: mA)

| Nennstrom | Widerstand ca. | 0.2 mV | 0.4 mV | 0.6 mV | 0.8 mV | 1.0 mV | 1.5 mV | 2.0 mV |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **5A (Hellbraun)** | ~17.8 mΩ | 11 mA | 22 mA | 34 mA | 45 mA | **56 mA** | 84 mA | 112 mA |
| **7.5A (Braun)** | ~10.9 mΩ | 18 mA | 37 mA | 55 mA | 73 mA | **92 mA** | 138 mA | 183 mA |
| **10A (Rot)** | ~7.4 mΩ | 27 mA | 54 mA | 81 mA | 108 mA | **135 mA** | 203 mA | 270 mA |
| **15A (Blau)** | ~4.8 mΩ | 42 mA | 83 mA | 125 mA | 167 mA | **208 mA** | 313 mA | 417 mA |
| **20A (Gelb)** | ~3.4 mΩ | 59 mA | 118 mA | 176 mA | 235 mA | **294 mA** | 441 mA | 588 mA |
| **25A (Transparent)**| ~2.6 mΩ | 77 mA | 154 mA | 231 mA | 308 mA | **385 mA** | 577 mA | 769 mA |
| **30A (Grün)** | ~2.1 mΩ | 95 mA | 190 mA | 286 mA | 381 mA | **476 mA** | 714 mA | 952 mA |

> **Schnelle Faustformel (für Mini 10A Sicherungen):**  
> **Alle 0,1 mV Spannungsabfall entsprechen ca. 14 mA Ruhestrom.** Eine Messung von `0,5 mV` bedeutet etwa $$0.5 \times 14 = 70\text{ mA}$$.

---

## Verursacher lokalisieren und bestätigen

Haben Sie eine Sicherung mit messbarem Spannungsabfall gefunden, **ziehen Sie diese Sicherung weiterhin nicht heraus**:

1. **Belegungsplan prüfen**: Im Bordbuch oder Sicherungsdeckel nachschlagen, welche Verbraucher an diesem Stromkreis hängen (z. B. Radio, Dashcam, Türsteuergerät, Innenbeleuchtung).
2. **Verbraucher abstecken**: Das verdächtige Bauteil direkt am Stecker trennen (nicht am Sicherungskasten).
3. **Erneut messen**: Fällt die Messung an der Sicherung sofort von z. B. `1,2 mV` auf **`0,0 mV`**, ist der Verursacher zweifelsfrei identifiziert!

---

## Zusammenfassung des Diagnoseablaufs

* **Schritt 1 (Gesamtwert prüfen)**: Mit der DC-Stromzange am Massekabel prüfen, ob überhaupt ein erhöhter Ruhestrom vorliegt (< 50mA ist normal).
* **Schritt 2 (Lichtmaschine prüfen)**: Stromzange an das B+ Kabel der Lichtmaschine halten, um defekte Gleichrichterdioden auszuschließen.
* **Schritt 3 (Stromkreis aufspüren)**: Mit dem Multimeter im **DC mV**-Bereich Sicherungen abscannen und per Tabelle den Stromkreis ohne Aufwecken in 2 Minuten identifizieren!
