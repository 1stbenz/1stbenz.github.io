---
layout: post
title: "Analyse des ISG-Elektrobooster-Systems bei Motorrädern: Funktionsweise, Leistungssteigerung durch LiFePO4-Batterien und physikalische Grenzen"
lang: de
date: 2026-07-14 20:00:00
categories: Moto
tags: [Fahrzeugwissen, Autoelektrik, Fahrzeugtuning]
description: "Eine detaillierte Analyse der Funktionsweise und der physikalischen Grenzen des integrierten Startergenerators (ISG) bei Motorrädern (flüsterleiser Start und Elektro-Boost). Wir untersuchen, warum der Austausch der herkömmlichen Blei-Säure-Batterie durch eine Lithium-Eisenphosphat-Batterie (LiFePO4) das Ansprechverhalten des Boosters spürbar verbessert und warum dieses Tuning die systembedingten Engpässe des Fahrzeugs dennoch nicht überwinden kann."
keywords: "ISG Motorrad, Elektrobooster, integrierter Startergenerator, LiFePO4 Batterie Tuning, Blei-Säure-Batterie Vergleich, Mild-Hybrid Motorrad, flüsterleiser Start, sofortige Beschleunigungshilfe, Spannungsabfall, ohmscher Spannungsabfall"
image: /images/isg-motorcycle-system.webp
faq:
  - question: "Was ist das ISG-Elektrobooster-System eines Motorrads und was ist seine Hauptfunktion?"
    answer: "Das ISG (Integrated Starter Generator, integrierter Startergenerator) kombiniert den herkömmlichen Anlasser und die Lichtmaschine in einer einzigen Einheit, die direkt an der Kurbelwelle montiert ist. Es ermöglicht einen geräuschlosen und vibrationsfreien Start ('Silent Start') sowie eine Start-Stopp-Automatik. Beim Anfahren oder bei plötzlichem Beschleunigen liefert das System ein zusätzliches Drehmoment (Elektro-Boost) mithilfe von Batteriestrom, um den Kraftstoffverbrauch zu senken und die Beschleunigung zu verbessern."
  - question: "Warum verbessert der Wechsel von einer Blei-Säure-Batterie zu einer LiFePO4-Batterie die Leistung des ISG-Boosters so deutlich?"
    answer: "Lithium-Eisenphosphat-Batterien (LiFePO4) haben einen extrem niedrigen Innenwiderstand und eine sehr hohe Entladerate (C-Rate). Wenn der ISG plötzlich hohe Ströme für den Elektro-Boost anfordert, bricht die Spannung bei einer LiFePO4-Batterie im Gegensatz zu einer Blei-Säure-Batterie nicht ein (ohmscher Spannungsabfall). Sie liefert sofort stabilen und ausreichenden Strom, sodass der ISG-Motor sein maximales Solldrehmoment entfalten kann. Gleichzeitig nimmt sie den Ladestrom des Generators weitaus schneller auf."
  - question: "Kann man nach dem Upgrade auf eine LiFePO4-Batterie die Beschleunigung des ISG unendlich steigern oder das Motorrad wie ein reines E-Bike fahren?"
    answer: "Nein. Obwohl die LiFePO4-Batterie den Engpass auf der Stromseite beseitigt, wird die maximale Leistung des ISG-Systems letztendlich durch das Design der Motorwicklungen, die Strombegrenzung und Wärmeabfuhr des Motorsteuergeräts (ECU/MCU) sowie die physikalischen Grenzen des 12V-Niederspannungssystems (zu hohe Ströme führen zu starker Erwärmung der Leitungen) begrenzt. Das Batterie-Upgrade schöpft nur die werkseitigen Leistungsreserven des ISG aus, kann aber die Hardware-Sicherheitsgrenzen von Motor und Steuergerät nicht überschreiten."
---

In den letzten Jahren haben viele etablierte Motorradmarken (wie SYM, Kymco oder Yamaha) die **ISG-Technologie (Integrated Starter Generator)** in ihren Modellen eingeführt. Neben dem vibrationsfreien, flüsterleisen Start und der Start-Stopp-Automatik gilt vor allem der elektrische Zusatzantrieb („Motor Assist / Mild Hybrid“) als wichtiges Verkaufsargument für mehr Fahrkomfort.

Viele Fahrer stellen jedoch fest, dass sich der Elektro-Boost mit der werksseitigen Blei-Säure-Batterie recht unspektakulär anfühlt. Nach dem Wechsel auf eine „Lithium-Eisenphosphat-Batterie“ (LiFePO4) hingegen ist der Vorwärtsschub beim Anfahren und Beschleunigen deutlich kraftvoller. Welche Mechanismen stecken dahinter? Und warum gibt es selbst nach dem Batterie-Upgrade unüberwindbare physikalische Grenzen? In diesem Artikel erhalten Sie eine detaillierte Analyse.

---

![shindengen](/images/isg-motorcycle-system.webp)
*Bildquelle: [Shindengen](https://www.shindengen.com/products/electro/exhibition/private_exhibition/isg_ecu/)*

## Was ist ISG? Funktionsweise und Doppelrolle

In der Elektrik herkömmlicher Verbrennungsmotorräder sind Anlasser und Lichtmaschine (Generator) zwei getrennte Bauteile. Beim Starten muss der Anlasser die Kurbelwelle über ein Zahnradgetriebe andrehen, was oft von einem lauten, mechanischen Klackern und starken Vibrationen begleitet wird.

**Der ISG vereint diese beiden Funktionen in einem Bauteil**, indem der Stator und Rotor des bürstenlosen Motors direkt auf der Kurbelwelle des Motors montiert werden. Er arbeitet in drei verschiedenen Modi:

1. **Silent-Start-Modus (Motorbetrieb)**: Er bezieht Strom aus der Batterie und dreht die Kurbelwelle direkt, um den Motor zu starten. Dadurch entfällt das klassische Anlassergetriebe vollständig, was einen lautlosen, vibrationsfreien und extrem schnellen Start ermöglicht.
2. **Elektro-Boost-Modus (Motor Assist)**: Beim Anfahren oder plötzlichen Gasgeben steuert das Steuergerät den ISG-Motor so an, dass er ein zusätzliches Drehmoment direkt auf die Kurbelwelle überträgt. Dies unterstützt den Verbrennungsmotor und gleicht das Drehmomenttief bei niedrigen Drehzahlen aus.
3. **Generator- und Lademodus (Generatorbetrieb)**: Wenn der Motor normal läuft, arbeitet der ISG als Generator. Er wandelt einen Teil der mechanischen Energie des Motors in elektrische Energie um, um die Batterie wieder aufzuladen und den beim Start und Boost verbrauchten Strom auszugleichen.

## Die systembedingten Grenzen des ISG-Elektroboosters

Obwohl der ISG eine sofortige Leistungsspritze liefern kann, unterscheidet er sich grundlegend von einem 48V-Mild-Hybrid-System bei Pkws oder einem reinen Elektrofahrzeug (EV). Das System stößt vor allem an folgende Grenzen:

* **Leistungsgrenze des 12V-Bordnetzes**: Nach der Formel $$P = V \times I$$ (Leistung = Spannung × Stromstärke) sind im standardmäßigen 12V-System eines Motorrads für eine Boost-Leigung von 1 kW (ca. 1,35 PS) unter Berücksichtigung der Wirkungsgrade von Steuergerät (MCU) und Motor kurzzeitig Ströme von **mehr als 90 bis 100 Ampere** erforderlich. Würde man die Leistung weiter erhöhen, stiege der Strom drastisch an, was zu extremer Kabelerwärmung und Bauteilschäden führen würde.
* **Platzmangel und thermische Grenzen**: Der ISG-Motor sitzt direkt am Kurbelgehäuse in einer sehr heißen Umgebung mit minimalem Bauraum. Bei dauerhafter hoher Leistungsabgabe staut sich in den Motorwicklungen Hitze, was zum Durchbrennen der Drähte oder zur Entmagnetisierung der Permanentmagnete bei hohen Temperaturen führen kann.
* **Kurze Boost-Dauer**: Um die Batterie vor Tiefentladung und den Motor vor Überhitzung zu schützen, begrenzt die werkseitige ECU den Elektro-Boost meist auf die ersten 10 bis 20 Sekunden beim Anfahren oder Beschleunigen. Ein dauerhafter Schub bei höheren Geschwindigkeiten wie bei einem echten E-Bike ist nicht möglich.

## Blei-Säure-Batterie vs. LiFePO4-Batterie: Warum das Upgrade einen so großen Unterschied macht

Warum führt der bloße Austausch der alten Blei-Säure-Batterie gegen eine „Lithium-Eisenphosphat-Batterie (LiFePO4)“ zu einem so deutlich spürbaren Leistungszuwachs beim Elektro-Boost? Der Grund liegt in den **physikalischen Eigenschaften der Batterie, die das zuvor blockierte Potenzial des Motors freisetzen**.

```
【Spannungsverhalten bei hoher Entladung】
Blei-Säure-Batterie: 12,8V ──────► [Sofortige Entladung mit hohem Strom] ──────► Ohmscher Spannungsabfall auf 10,0V~10,5V (Leistungsverlust)
LiFePO4-Batterie:    13,2V ──────► [Sofortige Entladung mit hohem Strom] ──────► Klemmenspannung stabil bei 12,5V~12,8V (Volle Leistung)
```

### 1. Innenwiderstand und ohmscher Spannungsabfall (IR-Drop)
* **Blei-Säure-Batterie**: Sie weist einen relativ hohen Innenwiderstand auf. Wenn der ISG beim Anfahren schlagartig 60 bis 80 A Strom anfordert, führt dies nach dem ohmschen Gesetz ($$\Delta V = I \times R_\text{internal}$$) zu einem massiven **Spannungsabfall (IR-Drop)**. Die Batteriespannung kann sekundenbruchteilig von 12,8 V auf unter 10,5 V einbrechen. Da die Leistung des Motors ($$P = V \times I$$) mit sinkender Spannung abnimmt, wirkt der Elektro-Boost schwach und träge.
* **LiFePO4-Batterie**: Sie besitzt einen extrem niedrigen Innenwiderstand (weniger als ein Fünftel einer Blei-Säure-Batterie) und eine hohe Entladerate (C-Rate). Selbst bei einer plötzlichen Stromabgabe von über 100 A bleibt die Klemmenspannung stabil über 12,5 V. Dadurch erhält der ISG-Motor sofort die volle elektrische Leistung und kann sein maximales Drehmoment entfalten.

### 2. Spannungsniveau und ECU-„Boost-Schwellenwert“
Die werksseitige ECU nutzt meist eine Unterspannungsschwelle (z. B. mindestens 12,5 V, um den Boost freizugeben). Blei-Säure-Batterien haben ein niedrigeres Spannungsniveau, sodass der Spannungsabfall beim Anfahren oft eine vorzeitige Abschaltung auslöst. LiFePO4-Batterien halten ein höheres Niveau (voll geladen ca. 13,2–13,4 V), signalisieren der ECU ausreichend Kapazität und sorgen für ein aktiveres, konstanteres Boost-Eingreifen.

### 3. Ladeakzeptanz beim Nachladen durch den Generator
Nach dem Boost lädt der ISG die Batterie im Motorbetrieb wieder auf (Hinweis: Bei gängigen 12V-CVT-Rollern trennt beim Ausrollen die Kupplung, sodass keine echte Bremsrekuperation wie bei E-Fahrzeugen stattfindet). LiFePO4-Batterien nehmen den Ladestrom deutlich schneller auf als Blei-Säure-Batterien und verkürzen so die Ladezeit bis zum nächsten Boost.

| Eigenschaft / Kriterium | Herkömmliche Blei-Säure-Batterie (Lead-Acid) | Lithium-Eisenphosphat-Batterie (LiFePO4) |
| :--- | :--- | :--- |
| **Innenwiderstand** | Höher, führt bei hohem Entladestrom zu starkem Spannungsabfall | Extrem niedrig, Klemmenspannung bleibt unter Last hochstabil |
| **Entladerate (C-Rate)** | Mäßig (häufige hohe Entladeströme verkürzen die Lebensdauer) | Sehr hoch (kann kurzzeitig Entladeströme von 20C bis 40C bewältigen) |
| **Leistung des ISG-Boosters** | Eingeschränkt durch Spannungsabfall; Motor liefert nicht das volle Drehmoment | Spannung bleibt stabil; Motor liefert sein volles Solldrehmoment |
| **Ladeeffizienz (Generator)** | Langsame Ladungsaufnahme; Nachladen dauert länger | Sehr hohe Ladeakzeptanz; verbrauchter Boost-Strom wird schnell ersetzt |
| **Gewicht** | Schwer (ca. 3 bis 4 kg) | Extrem leicht (ca. 0,8 bis 1,2 kg) |

## Trotz LiFePO4-Upgrade: Die Leistungsgrenzen bleiben bestehen

Manche Fahrer glauben nach dem Wechsel der Batterie, sie hätten die „Motorleistung gesteigert“. Aus technischer Sicht **beseitigt der Einbau einer LiFePO4-Batterie jedoch lediglich den Engpass der einbrechenden Klemmenspannung. Dadurch wird dem ISG ermöglicht, seine werkseitig vorgesehene Leistung voll abzurufen – es handelt sich nicht um ein Tuning des Motors selbst**. Die Leistungssteigerung stößt weiterhin an folgende mechanische und elektrische Grenzen:

### 1. Strombegrenzung durch das Steuergerät (MCU/ECU)
Der maximale Ausgangsstrom des ISG wird durch die Firmware und die MOSFETs im Motorsteuergerät (MCU) geregelt. Selbst wenn die LiFePO4-Batterie theoretisch 200 A abgeben könnte, leitet das Steuergerät bei einer werkseitigen Begrenzung auf z. B. 60 A auch nur maximal 60 A an den Motor weiter. Die Batterie kann die Schutzschwellen des Steuergeräts nicht umgehen.

### 2. Sättigungsgrenze von Motorwicklung und Magnetfeld
Der ISG-Motor ist durch die Dicke seiner Siliziumstahlbleche, die Anzahl der Spulenwicklungen und die Stärke der Permanentmagnete physikalisch begrenzt. Sobald der Strom die magnetische Sättigungsgrenze erreicht, führt eine weitere Erhöhung des Stroms nicht zu mehr Drehmoment, sondern wird lediglich in Wärme umgewandelt, was den Motor überhitzen lässt.

### 3. Physik bei hohen Drehzahlen: Gegenspannung (Back-EMF) und CVT-Übersetzung
* **Gegenspannung (Back-EMF)**: Mit steigender Motordrehzahl wächst die induzierte Gegenspannung und wirkt direkt gegen die 12V-Batteriespannung ($$V_\text{netto} = V_\text{Batterie} - E_\text{EMF}$$). Bei hohen Drehzahlen reicht 12 V nicht mehr aus, um Strom in die Spulen zu „drücken“ (ein Hauptgrund, warum Pkw-Mild-Hybride 48 V nutzen).
* **CVT-Übersetzung**: Beim Anfahren verstärkt die kurze CVT-Übersetzung das geringe ISG-Drehmoment; bei mittleren bis hohen Geschwindigkeiten dominiert der Verbrenner, sodass der ISG-Anteil kaum noch ins Gewicht fällt.

## Fazit

Das ISG-Elektrobooster-System bei Motorrädern ist ein cleveres Konzept zur Verbrauchsoptimierung und Komfortverbesserung. Es gleicht durch den lautlosen Start und die Anfahrhilfe die konzeptbedingten Schwächen von Einzylinder-Verbrennungsmotoren im unteren Drehzahlbereich aus.

Der Wechsel von einer herkömmlichen Blei-Säure-Batterie zu einer Lithium-Eisenphosphat-Batterie eliminiert den Spannungsabfall bei hohen Entladeströmen und ermöglicht es dem ISG-Motor, **seine werkseitig konzipierte Höchstleistung voll auszuschöpfen**. Aufgrund des 12V-Systems, der Strombegrenzung, der Wärmeabfuhr des Motors und der CVT-Charakteristik bleibt der ISG jedoch stets ein reines Hilfssystem. Wer die Vorteile dieses Upgrades realistisch einschätzt, gewinnt mehr Fahrspaß, ohne die Haltbarkeit und Sicherheit des Bordnetzes zu gefährden.

## Referenzen

* Venkateshwaran B, Pushparajesh V, Kamalakannan D, [*Design and Optimization of mild hybrid BLDC based starter generator for two wheeler*](https://ijetcse.com/v24i6/), IJETCSE, Vol. 24, Issue 6, 2017.
* batteryuniversity.com: *How does Internal Resistance Affect Battery Performance?*
