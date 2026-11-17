---
layout: post
title: "Wie liest man einen einfachen Batterie-Innenwiderstandstester? Mythen zu CCA und Referenzwert entlarvt"
lang: de
date: 2025-02-10 09:40:00
categories: Auto
tags: [Autobatterie, Fahrzeugwissen]
description: "Wie genau sind CCA- und SOH-Werte eines handlichen Batterie-Innenwiderstandstesters? Erfahren Sie, wie die Messung bei Blei-Säure-Batterien funktioniert, was der Referenzwert bewirkt, wie Spannung das Ergebnis beeinflusst und wie Sie richtig messen."
keywords: "Batterie Innenwiderstandstester, Leitfähigkeitstester, CCA, SOH, Batteriezustand, Innenwiderstand, Referenzwert, Autowartung, DIY Wartung"
image: /images/batterytool01.webp
math: true
faq:
  - question: "Ist der vom einfachen Innenwiderstandstester angezeigte CCA-Wert der echte Kaltstartstrom?"
    answer: "Nein. Solche Tester führen keine Hochstromentladung durch, sondern messen die Ruhespannung sowie über ein schwaches Signal (AC-Leitfähigkeit oder kleiner Puls) den Innenwiderstand. CCA und SOH sind Schätzwerte aus Erfahrungsformeln für Blei-Säure-Batterien."
  - question: "Beeinflusst der eingestellte CCA-Referenzwert (z. B. 415 oder 500) das Messergebnis?"
    answer: "Bei gleicher Prüfnorm und gleichem Batterietyp bleiben gemessener Innenwiderstand und geschätzter CCA unverändert; es ändern sich nur die SOH-Prozentangabe (je nach Gerät linear oder quadratisch) und die Gut-/Ersetzen-Bewertung. Ein Wechsel von Norm oder Batterietyp kann bei manchen Geräten das Ergebnis verändern."
  - question: "Warum schwanken die Innenwiderstands- oder CCA-Werte derselben Batterie je nach Zeitpunkt?"
    answer: "Temperatur, Ladezustand und Ruhespannung (gerade geladen, abgestellt oder teilentladen) sowie die Klemmposition beeinflussen den gemessenen Innenwiderstand und den berechneten CCA."
  - question: "Wie nutzen Autofahrer einen einfachen Innenwiderstandstester am sinnvollsten?"
    answer: "Voll geladen nach einer Ruhephase direkt an den Batteriepolen messen und mit demselben Gerät langfristig den Anstieg des Innenwiderstands (mΩ) verfolgen – das ist aussagekräftiger als ein einzelner SOH-Wert."
  - question: "Kann man den Innenwiderstand verschiedener Marken oder Modelle direkt vergleichen?"
    answer: "Das ist nicht sinnvoll. Marke, Plattenaufbau und Lagerzustand bestimmen den Ausgangswiderstand. Am besten vergleicht man mit dem Referenzwert derselben Batterie im Neuzustand (voll geladen und beruhigt), hilfsweise mit dem Richtbereich eines Neuteils gleicher Marke und desselben Modells."
  - question: "Welcher Innenwiderstand ist bei einer Autobatterie normal? Gibt es einen festen Grenzwert?"
    answer: "Es gibt keinen einheitlichen Standardwert. Größere Kapazität bedeutet meist niedrigeren Innenwiderstand. Maßgeblich ist der Neuzustands-Referenzwert derselben Batterie oder der Richtbereich eines neuen Modells derselben Marke."
  - question: "Ist eine Messung direkt nach dem Abstellen des Motors oder nach dem Laden genau?"
    answer: "Die Messwerte werden leicht verfälscht. Nach der Fahrt sorgen Oberflächenladung und Wärme oft für zu optimistische Werte und niedrigeren Widerstand; direkt nach dem Laden können Polarisation und Gasbläschen zu Schwankungen führen. Vorher ruhen lassen."
  - question: "Misst ein Innenwiderstandstester bei niedriger Batteriespannung (unter 12,5 V) noch genau?"
    answer: "Die Abweichung nimmt deutlich zu und fällt zu pessimistisch aus. Unter ca. 12,4 V–12,5 V (bei AGM höher) ist die Batterie nicht voll geladen; geringere Säuredichte und reversibles Bleisulfat erhöhen den Widerstand vorübergehend. Vor dem Test voll laden und ruhen lassen."
  - question: "Kann man einen einfachen Batterie-Innenwiderstandstester für LiFePO4-Batterien verwenden?"
    answer: "Für die CCA- und SOH-Auswertung ist er nicht geeignet. Handelsübliche Kfz-Tester nutzen Blei-Säure-Logik und werden zudem vom integrierten BMS einer LiFePO4-Starterbatterie beeinflusst (für den mΩ-Abgleich einzelner Zellen braucht man ein spezielles AC-Innenwiderstandsmessgerät)."
---

Viele beurteilen eine Autobatterie anhand des CCA- und SOH-Werts auf dem Display eines einfachen Innenwiderstandstesters – doch diese Zahlen sind meist nur „Schätzwerte“. Wer die für klassische Blei-Säure-Batterien entwickelte Logik und ihre Grenzen kennt, interpretiert die Daten richtig (warum CCA bei Lithiumbatterien nicht gilt, erklärt **[Warum die Messung der CCA-Werte von Lithium-Ionen-Akkus sinnlos ist](/de/2025/about-cca.html)**).

## 1. Was misst ein einfacher Innenwiderstandstester wirklich?
Solche elektronischen Tester führen keine Lastentladung mit hunderten Ampere durch. Sie messen lediglich die **Ruhespannung (V)** und über ein schwaches Signal (AC-Leitfähigkeit oder kleiner Impuls) den **Innenwiderstand (mΩ)**.

Bei klassischen Blei-Säure-Batterien wird der **SOC (%)** überwiegend aus der Ruhespannung abgeleitet, während **geschätzter CCA** und **SOH (%)** über Erfahrungsformeln aus dem Innenwiderstand berechnet werden (ähnlich einer Körperfettwaage). Das eignet sich gut zur **Schnellprüfung und Trendbeobachtung**, ersetzt aber keinen echten Belastungstest. Außerhalb der Blei-Säure-Chemie verliert diese CCA-Berechnung ihre Gültigkeit.

## 2. Macht der eingestellte Referenzwert einen Unterschied?
Bei **gleicher Prüfnorm (z. B. CCA) und gleichem Batterietyp** verändert das Nachjustieren des Referenzwerts **weder den gemessenen Innenwiderstand (mΩ) noch den geschätzten CCA** – es verschiebt nur den **SOH-Prozentwert** und die Gut-/Ersetzen-Anzeige:

$$\text{SOH (\%)} \approx \frac{\text{Geschätzter CCA}}{\text{Eingegebener Referenzwert}} \times 100\%$$

Die genaue Kurve unterscheidet sich je nach Hersteller (teils linear, teils quadratisch wie $$(400/500)^2 = 64\%$$, meist bei `100%` gedeckelt; ein Wechsel der Norm oder zwischen Nass- und AGM-Batterie kann bei manchen Geräten auch die Umrechnung verändern). Wichtig ist nicht ob 400 oder 500 eingestellt wird, sondern **mit festen Einstellungen Veränderungen zu verfolgen**.

## 3. Warum liefert dieselbe Batterie unterschiedliche Werte?
Neben Gerätetoleranzen verschieben vier Bedingungen die Messwerte spürbar:
* **Direkt nach Fahrt oder Ladung:** Oberflächenladung und Motorwärme lassen den Ladezustand oft zu optimistisch und den Widerstand niedriger erscheinen; direkt nach dem Laden können Polarisation und Gasbläschen zu Messdrift führen.
* **Niedriger Ladezustand (unter ca. 12,4 V–12,5 V):** Bei zu geringer Ladung (bei AGM liegt die Schwelle höher) steigt der Innenwiderstand vorübergehend an – eine leere Batterie wird leicht als defekt fehldiagnostiziert.
* **Unterschiedliche Temperaturen:** Elektrochemische Reaktionen sind stark temperaturabhängig; Sommer- und Winterwerte weichen deutlich voneinander ab.
* **Übergangswiderstand:** Verschmutzte Klemmen oder schlechter Sitz am Bleipol verfälschen den `mΩ`-Wert direkt.

## 4. Bedeutet ein hoher Innenwiderstand automatisch eine schlechte Batterie?
Nicht unbedingt (**Hinweis: gilt nur für Blei-Säure-Batterien; die CCA-Logik ist für Nicht-Blei-Batterien [völlig ungeeignet](/de/2025/about-cca.html)**). Unterschiede zwischen Marken derselben Baugröße spiegeln meist konstruktive Kompromisse wider:
* **Plattenaufbau & Säuredichte:** Viele dünne Platten oder höhere Säuredichte steigern die Nennleistung, gehen aber zulasten der Hitzebeständigkeit bzw. fördern die Gitterkorrosion. Dickere Platten starten mit etwas höherem Widerstand, halten oft aber stabiler.
* **Lageralter:** Frisch produzierte Batterien und monatelang gelagerte Ware haben von vornherein unterschiedliche Ausgangswerte.

Ein **direkter Markenvergleich über den Innenwiderstand ist daher sinnlos**; prüfen Sie zusätzlich Gewicht und Spannungsverhalten.

## 5. So messen Sie mit maximaler Aussagekraft
1. **Voll geladen und beruhigt testen:** Prüfen Sie, ob die Batterie voll geladen und in Ruhe ist (klassische Nassbatterie ca. `12,6 V+`, AGM ca. `12,8 V+`; mindestens über `12,5 V` messen).
2. **Direkt an die Batteriepole klemmen:** Befestigungsschrauben und Kabelschuhe meiden. **4-Leiter-Kelvin-Klemmen** eliminieren zwar Leitungs- und Klemmenkontaktwiderstände, aber nicht den Übergangswiderstand durch Oxidation zwischen Bleipol und Polklemme.
3. **Mit dem „eigenen Neuwert“ vergleichen:** Vergleichen Sie vorrangig mit dem Wert derselben Batterie im Neuzustand (voll geladen und beruhigt); fehlt dieser, dient der Richtbereich eines Neuteils gleicher Marke und desselben Modells als Anhaltspunkt.
4. **Immer dasselbe Messgerät nutzen:** Da jede Marke eigene Algorithmen verwendet, liefert nur ein festes Gerät eine verlässliche Verlaufskurve.

## Fazit
Der größte Nutzen eines einfachen Innenwiderstandstesters liegt nicht in einer einzelnen CCA- oder SOH-Zahl, sondern in der **langfristigen Verfolgung des Innenwiderstands derselben Batterie** im voll geladenen Ruhezustand. Bei Blei-Säure-Batterien sagt der Trend des Innenwiderstands weit mehr aus als einzelne Prozentwerte (warum CCA bei Lithiumbatterien versagt, lesen Sie in **[Warum die Messung der CCA-Werte von Lithium-Ionen-Akkus sinnlos ist](/de/2025/about-cca.html)**).
