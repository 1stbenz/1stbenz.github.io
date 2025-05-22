---
layout: post
title: "Analyse der Fahrzeugstartspannung (2.3 NA × Lithium-Eisenphosphat-Batterie)"
lang: de
date:   2026-03-22 16:00:00
categories: Auto
tags: [Autobatterie, Fahrzeugwissen]
description: "Brich das Missverständnis, dass es nur eine einzige Startspannung gibt! Durch hochfrequente Messdaten über einen Zeitraum von 0,05 Sekunden analysieren wir die physikalische Leistungsfähigkeit einer Reihe aus vier Lithium-Eisenphosphat-Batterien im Moment des Motorstarts und erklären mit der Formel V = V₀ - (I × R), wie der Innenwiderstand der Batterie den Spannungsabfall und die Effizienz beim Aufladen durch den Generator beeinflusst."
keywords: "Eisen-Lithium-Startbatterie, Autobatterie, Spannungsabfall, Innenwiderstand, CCA, Startstrom, Generator, LiFePO4, Spannungsfallsformel"
image: /images/voltage_record_image.svg
faq:
  - question: "Warum fällt die Batteriespannung plötzlich ab, wenn der Motor gestartet wird?"
    answer: "Dies liegt daran, dass das Startmotor eine sehr hohe momentane Stromstärke (I) benötigt, um den statischen Reibungswiderstand des Motors zu überwinden. Gemäß dem Endspannungsformel $$V = V_0 - (I \times R)$$ führt der durch die innere Widerstandsresistenz (R) des Batteries verlaufende Strom zu unvermeidbaren Spannungsverlusten."
  - question: "Warum zeigt die Spannung beim Start eines Vierzylindermotors ein regelmäßiges sägezahnartiges Muster auf?"
    answer: "Weil bei den zwei nach oben bewegten Kolben nur einer sich im Kompressionsgang befindet, in dem sowohl der Einlass- als auch der Auslassventil vollständig geschlossen sind und einen enormen Widerstandswall erzeugen. Der Kurbelwellendrehpunkt trifft alle 180 Grad auf eine extrem hohe Kompressionsspannung, was dazu führt, dass vom Starter entnommene Stromstärke schwankt und somit ein regelmäßiges Spannungsmuster entsteht."
  - question: "Die Batterie hat 52.000 km zurückgelegt, wie kann man anhand des Spannungsverhaltens feststellen, ob sie altert?"
    answer: "Man sollte hauptsächlich die \"Leerlaufspannung\" und das \"Startfallpotential\" beobachten. Wenn sich nach einer Woche Leerstandsspannung noch auf einem Wert von über 13,2 V (charakteristisch für LiFePO4) hält und der Spannungsabfall beim Start unter 1,2 V liegt (indiziert niedrigen Innenwiderstand), bedeutet dies, dass die SOH des Akkus (Gesundheit) weiterhin ausgezeichnet ist."
---

In der Forschung zum Automobil-Elektrosystem ist das Startmoment die Phase mit den stärksten Laständerungen. Durch hochfrequente Spannungsabtastraten von 100 Hz im Millisekundenbereich können wir die physikalische Wechselwirkung zwischen Akku und Generator in extrem kurzer Zeit beobachten. Diese Analyse bezieht sich auf ein Fahrzeug, das einen Vierzylinder-2.3-Liter-Motor sowie eine 50 Ah Lithium-Eisenphosphat-Batterie (GreenRun2) verbaut hat, und untersucht die Prinzipien hinter dem Spannungsverlauf beim Startvorgang.

---


## I. Analyse der Einschalttransientenspannung


[![Spannungsrekord-Diagram](/images/voltage_record_image.svg)](/images/voltage_record_image.svg)

Der Startvorgang lässt sich in vier wesentliche physikalische Wendepunkte unterteilen, die den Wechsel zwischen mechanischer Belastung und elektrischem Versorgungsnetz widerspiegeln.


### Erster Spannungsabfall durch Einschaltstrom
Wenn der Motor-Elektromagnet-Kontakt geschlossen wird und sich der Motor aus dem Ruhezustand in Rotation setzt, entsteht ein extrem hoher **Anlaufstrom**.  
*   **Leistungsdaten**: Die Spannung fällt von einem Stillstandswert von **13,24 V** auf **12,07 V**.  
*   **Technische Erklärung**: Dieser Spannungsabfall hängt vom Innenwiderstand $$R$$ der Batterie und dem Startimpedanz des Motors ab. Gemäß der Formel:  
    $$V_{terminal} = V_{ocv} - (I_{start} \times R_{internal})$$  
*   **Analyse**: Aufgrund ihrer chemischen Eigenschaften weist das Lithium-Eisenphosphat-Batteriesystem einen sehr niedrigen Innenwiderstand auf; daher ist der Spannungsabfall bei gleichem Anlaufstrom $$I$$ deutlich geringer als bei herkömmlichen Blei-Säure-Akkus. Dieser Test zeigt, dass der Spannungsabfall nur etwa **1,17 V** beträgt und eine hervorragende Entladestromdichte demonstriert.


### Spannungsfluktuationen im Kompressionshub
Während des Betriebs des Startmotors zeigt sich das Spannungsniveau zwischen **12,07 V und 12,5 V**.  
* **Technische Erklärung**: Dies ist die direkte Reaktion des Motors auf den **Zylinderhub** beim Kompressionsstadium.  
    * **Talfeld**: Der Kolben bewegt sich in Richtung des Kompressionshubs; der Widerstand gegen den Druck steigt an, was zu einem starken Anstieg des Strombedarfs und einer tieferen Spannungsabnahme führt.  
    * **Gipfel**: Sobald der Kolben die Oberste Totpunktlage überschritten hat und im Auslass- oder Ladehub ist, nimmt der Widerstand ab, der Energieverbrauch sinkt und das Spannungsniveau steigt wieder an.  
* **Physikalische Bedeutung**: Die Frequenz und Dauer der Schwankungen geben Aufschluss über die Drehzahlleistung des Startmotors. In diesem Fall wurde innerhalb von etwa **0,55 Sekunden** eine Zündung erreicht, was auf ein sehr hohes Leistungsniveau des Startsystems hinweist.


### 3. Lastabwurf und Induktionsspannungsimpuls
Wenn der Motor erfolgreich gezündet hat und die Drehzahl über den vom Hersteller angegebenen Wert steigt, wird das Einwegkupplung des Motors getrennt und der Stromkreis unterbrochen.  
* **Datenanzeige**: Die Spannung springt von **12,64 V** schnell auf **13,31 V**, um dann rasch wieder bei ca. **13,30 V** zu stabilisieren.  
* **Prinzip**: Dies ist ein Phänomen des Lastabwurfs. Da der Motor als großes Induktivitätselement wirkt, setzt er beim Unterbrechen des Stromkreises die verbleibende Energie frei; gleichzeitig verliert die Batterie im Moment ihrer hundertampere schweren Belastung und ihre Endspannung stellt sich sofort wieder nahe ihrem statischen Niveau ein.


### 4. Erregungsaufbau und Übergabe an den Generator
Nach dem Sprung stieg der Spannungswert nicht sofort an, sondern hielt sich zunächst kurz im Bereich von **13,28 V bis 13,41 V**, bevor er signifikant ansteigte (auf **13,69 V**).

* **Aufbauzeit der Erregung**: Nach dem Start dreht sich die Generatorwelle mit dem Motor, doch das interne Spannungsregelungsgerät benötigt Zeit, um das Rotormagnetfeld aufzubauen. Da die Ausgangsspannung noch nicht über die Spannung des Akkus hinausgeht, versorgt das System in dieser Phase hauptsächlich den Akku.

* **Formelle Übernahme durch den Generator**: Nach dem Aufbau des Magnetfelds beginnt die Ausgangsspannung, die Batteriespeisespannung zu übersteigen; das Lithium-Eisenphosphat-Batterie akzeptiert aufgrund seines niedrigen Innenwiderstands sofort einen hohen Strom und hält die Systemspannung vorübergehend auf etwa 13,3–13,4 V. Da der Startverbrauch von nur 0,55 s extrem gering ist und die Ladeleistung des Akkus hervorragend ist, wird das Defizit innerhalb weniger Sekunden ausgeglichen; der Ladestrom sinkt schnell ab, die Begrenzung wird aufgehoben, und die Spannung steigt auf den stabilen Bereich für Nachladung über 13,69 V an.

---


## II. Beobachtung des Spannungsausgleichs bei langfristiger Betriebsspannung


Im kontinuierlichen Monitoring nach Abschluss des Starts zeigt sich das Spannungsverhalten die Stabilität der Systemspannung:

| Überwachungsphase | Spannung (V) | Technische Statusbeschreibung |
| :--- | :--- | :--- |
| **Vor dem Start** | 13,24 | Die Batteriespannung OCV befindet sich auf einem hohen Potentialplateau; der Gesundheitszustand ist ausgezeichnet. |
| **Frühe Phase des Starts** | 13,69 | Der Generator beginnt mit der Stromabgabe und wird durch den großen Ladestrom vom Lithium-Eisen-Phosphat-Polymerelektrolyt-Lithium-Ionen-Akku (LFP) auf das Potential heruntergezogen. |
| **Steady-State-Betrieb** | 13,80–13,90 | Der Regler befindet sich im Bereich der konstanten Spannung; die Leitungsverluste sind extrem gering. |


### Technische Zusammenfassung
1. **Spannungsregelungslogik**: Das System stabilisiert sich schließlich im Bereich von **13,80 V bis 13,90 V**. Für Lithium-Eisenphosphat-Batterien vermeidet dieser Spannungsbereich den Ladebereich über **14,6 V**, bei dem der volle Ladestand erreicht ist; er ermöglicht sowohl die Nachladung als auch eine Verlängerung der Zelllebensdauer.
2. **Alterungsbestimmung**: Die Batterie dieses Fahrzeugs wurde nach 3 Jahren und 52.000 Kilometern verwendet. Bereits beim Startmoment hält sie ein Plattformniveau von über **12 V**, und nach einer Woche im Ruhezustand, bevor der nächste Start erfolgt, liegt das Niveau bei **13,24 V**. Dies beweist, dass ihr Innenwiderstand noch nicht signifikant angestiegen ist und sich der SOH-Zustand als gut erweist.

---


## III. Energiedichte und Entladestromstärke


Verstehen Sie, wie Lithium-Eisenphosphat-Batterien durch ihre physikalischen Eigenschaften die Startleistung verbessern:

1. **Hohe Energiedichte**  
   Die spezifische Energie von Lithium-Eisenphosphat liegt etwa 3- bis 5-mal höher als die von Blei-Säure-Akkus. Bei gleichem Volumen bietet es ein leichteres Gewicht und effizientere Elektrodenmaterialien; das statische Spannungsniveau bleibt stabil bei **13,2–13,3 V**, wobei beim Start eine höhere Anfangspotentialenergie zur Verfügung steht.

2. **Hohe Entladestromdichte**  
   Lithium-Eisenphosphat-Batterien weisen einen niedrigen Innenwiderstand auf und können extrem hohe C-Raten unterstützen. Durch ihre hohe Energiedichte und große Kapazität lassen sie bei einem plötzlichen Start enorme Ströme abgeben, wobei der Spannungsrückgang kaum spürbar ist – ein deutlicher Vorteil gegenüber Blei-Säure-Batterien, die auf einen langsamen chemischen Diffusionsprozess angewiesen sind.

----

Die Daten in diesem Bericht stammen von realen Fahrzeugen, die Messgenauigkeit beträgt 0,01 V und die Abtastrate liegt bei 100 Hz.