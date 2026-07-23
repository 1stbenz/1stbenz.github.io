---
layout: post
title: "Wissenschaft der Batterielagerung – Spannung, Innenwiderstand und Leistungsdrosselung"
date: 2026-03-30 22:30:00 +0800
categories: Auto
lang: de
image: /images/battery_aging.webp
tags: [Autobatterie, Fahrzeugwissen]
description: "Erforschen Sie die physikalischen Wahrheiten der BatterielAlterung. Durch äquivalente Schaltkreismodelle und das Ohmsche Gesetz analysieren wir, wie ein Anstieg des Innenwiderstands zu ungewöhnlicher Erwärmung beim Laden, einer scheinbar hohen Endspannung sowie einem Spannungsabfall während des Entladens führt. Dieser Artikel bietet einfache Formelbeispiele, die Ihnen helfen, die wissenschaftlichen Prinzipien und Sicherheitsbewertungen hinter dem Phänomen «Lithium- oder Blei-Säurebatterien laden nicht voll auf / entladen sich schnell» zu verstehen."
keywords: "Batterialterungsursachen, Zunahme des Innenwiderstands, Äquivalentkreis, Lithium-Ionen-Batterie-Lebensdauer, Blei-Säure-Akku-Wartung, Spannungsabfallberechnung, Formel für Leistungsverschwendung, Batterieerwärmungsprinzip, Interner Widerstand, Batteriezustandsüberprüfung"
math: true
faq:
  - question: "Warum altert der Akku besonders schnell bei kaltem Wetter?"
    answer: "Bei niedrigen Temperaturen erhöht sich die Viskosität des Elektrolyten, was zu einer vorübergehenden Steigerung des Innenwiderstands R führt. Gemäß $$V_{measured} = V_{ocv} - (I \times R)$$ bewirkt der erhöhte Spannungsabfall, dass das Gerät den Schaltschwellenwert für die Spannung früher unterschreitet."
  - question: "Führt schnelles Laden zur Beschleunigung des Anstiegs des Innenwiderstands der Batterie?"
    answer: "Ja. Der hohe Strom bei schnellem Laden erzeugt ein Vielfaches an Abwärme ($$P = I^2 R$$). Die hohen Temperaturen beschleunigen interne chemische Nebenreaktionen, die zu nicht leitfähigen Substanzen führen, welche die Platten überziehen und einen dauerhaften Anstieg des Innenwiderstands verursachen."
  - question: "Nachdem der Batteriestand auf 100 % angezeigt wurde, sofort abziehen. Warum entlädt sich die Batterie dann schnell?"
    answer: "Wenn R groß ist, wird das Ladepotential künstlich nach unten gezogen. Sobald der Strom I stoppt, verschwindet der Spannungsabfall $$(I \times R)$$ und das Endpotential fällt sofort auf den echten $$V_{ocv}$$ ab, was zu einem plötzlichen Abtauchen des Prozentsatzes führt."
  - question: "Sind Batteriereparaturgeräte auf dem Markt wirksam?"
    answer: "Sie haben einen schwachen Entkristallisationseffekt bei Blei-Säure-Batterien, sind aber für strukturelle Alterungsprozesse von Lithium-Ionen-Batterien wirkungslos. Zudem weisen alternde Batterien ein hohes Innenwiderstand auf; eine erzwungene Reparatur kann aufgrund unzureichender Wärmeabfuhr zu Sicherheitsrisiken führen."
---

Egal, ob es sich um Lithium-Ionen- oder Blei-Säure-Akkus handelt: Das auffälligste Merkmal nach Alterung ist das **„Laden gleich voll, Entladen sofort leer"**, begleitet von schwerem Überhitzungsphänomen. Um diese Phänomene zu verstehen, muss man bei der **inneren Impedanz (R)** ansetzen.


## I. Ladevorgänge nach Alterung: Warum wird das Fahrzeug beim Laden immer heißer?


Wenn wir einen Akku mit einem Ladegerät aufladen, wird die vom Ladegerät ausgegebene Gesamtleistung ($$P_{\text{Gesamtleistung}}$$) in zwei Teile aufgeteilt:

$$P_{\text{gesamte Leistung}} = P_{\text{Wärmeentwicklung}} + P_{\text{tatsächliche Ladung}}$$


### Vertikaler Absturz der Energieeffizienz
Angenommen, wir verwenden einen Ladevorgang mit einem 5-Volt/2-Ampère-Ladegerät (Gesamtleistung 10 Watt) und vergleichen die Energieumwandlung zwischen den alten und neuen Batterien:

| Batteriezustand | Innenwiderstand (R) | Abwärmeleistung ($$I^2 R$$) | Tatsächliche Ladeleistung | Wirkungsgrad |
| :--- | :--- | :--- | :--- | :--- |
| **Neue Batterie** | 0,1 Ω | **0,4 W** | **9,6 W** | **96 %** (sehr hoch) |
| **Alte Batterie** | 1,5 Ω | **6,0 W** | **4,0 W** | **40 %** (sehr niedrig) |

**Stopp und nachdenken:** In alten Batterien wird mehr als die Hälfte der Leistung in dem inneren Widerstand $$R$$ zu nutzlosem Wärme verbrannt. Das ist genau der Grund, warum alte Batterien beim Aufladen wie ein „Wärmepack" anfühlen und das Aufladungsgeschwindigkeit sich langsamer anfühlt – denn nur weniger als die Hälfte der Leistung wird tatsächlich in chemische Energie umgewandelt.

---


### 2. Spannungstrick: Der entscheidende Fehler bei der Füllstandserkennung


`[Batteriesymbol](/images/battery-symbol.webp)`

* **Leerlaufspannung ($$V_{ocv}$$)**: Die Spannung, die an den Enden eines Akkus gemessen wird, wenn keine Last vorhanden ist und kein Strom fließt.
* **Innenwiderstand ($$R$$)**: Der physikalische Widerstand, der entsteht, wenn ein Strom durch die Elektroden, das Elektrolyt und die Trennmembran fließt.

Der Ladegerät erkennt das **Endspannung**:

$$V_{\text{Detektionsspannung}} = V_{\text{oCV}} + (I \times R)$$

* **Der Schein alter Batterien**: Wenn Strom ($$I$$) in eine Batterie fließt, kann es bei einer alternierten Zelle mit vergrößerter Innenwiderstandswert ($$R$$) zu einem starken Widerstand kommen. Dieser enorme Hindernis erzeugt direkt einen scheinbar hohen Spannungswert $$(I \times R)$$, der sich zur tatsächlichen Spannung addiert.

* **Ergebnis**: Wenn man das Aufladen wie das Befüllen eines Wasserreservoirs vorstellt, ist ein hoher Innenwiderstand vergleichbar mit einem "schwer verstopften Einfüllstutzen". Sobald Wasser hineingepumpt wird, steigt der Druck am Rohröffnung (die Messspannung) sofort an. Der Ladevorgang mischt dies und denkt fälschlicherweise: „Das Reservoir ist bis zum Rand gefüllt", stoppt das Aufladen sofort und leuchtet grün auf. Tatsächlich kann sich jedoch die tatsächliche Speicherkapazität im Inneren, $$V_{ocv}$$, noch in einem niedrigen Ladezustand befinden.

Das ist der Grund, warum alternde Batterien immer so aussehen, als würden sie sich sofort voll laden: Es handelt sich um eine Täuschung, bei der die Spannung durch den Innenwiderstand mit einer scheinbaren „Über-Spannung" addiert wird.

---


## II. Spannungsabfall beim Entladen: Der Ursprung des Stromausfalls


Wenn das Gerät einen Strom entzieht, wird die Formel umgekehrt:

$$V_{\text{Detektionsspannung}} = V_{\text{oCV}} - (I \times R)$$

**Ein Beispiel aus dem Alltag:**  
Ihr Smartphone schaltet sich automatisch ab, wenn der Spannungswert unter 3,3 V fällt. Angenommen, die Batterie hat noch einen Restspannung von 3,7 V:

* **Neue Batterie (R=0,1 Ω)**: Bei einem hohen Strom von 2 A während des Spielens sinkt die Spannung auf 3,7 - (0,1 × 2) = **3,5 V** → **funktioniert weiterhin reibungslos**.
* **Alte Batterie (R=0,5 Ω)**: Unter gleichen Bedingungen mit einem hohen Strom von 2 A fällt die Spannung auf 3,7 - (0,5 × 2) = **2,7 V** → **unterhalb des Schwellenwerts; das Handy erlischt sofort**.

Das ist der Grund, warum alte Handys noch immer anzeigt, dass sie 20 % Akku haben, aber sobald man die Kamera öffnet oder ein Spiel spielt, wegen des zu starken Spannungseinbruchs sofort abstürzen und ausschalten.

---


## Fazit: Alterung ist ein irreversibles „Blockieren"


Wenn man den Akku mit einem **Wasserturm** vergleicht, ist der Innenwiderstand wie die **Rostbildung und Verstopfung des Auslaufrohres**:
*   Beim **Laden**: Das Rohr verstopft sich, der Wasserdruck (Spannung) steigt schnell auf das Maximum an – es scheint voll zu sein –, doch tatsächlich fließt kein Wasser rein.
*   Beim **Entladen**: Man möchte Wasser nutzen, aber die Verstopfung des Rohrs (Innenwiderstand) ist so groß, dass wenig Wasser herauskommt und man den dringend benötigten Strom nicht schnell genug erhält.

Dieser durch physikalische Materialien (Verklötzung der Platten, Zersetzung des Elektrolyten) verursachte Anstieg des Widerstands ist irreversibel; nur ein zeitnaher Batteriewechsel stellt sicher, dass das Gerät sicher und mit stabiler Stromversorgung arbeitet.

> **Fortgeschrittene Konzepte: Hat der Innenwiderstand wirklich einen Unterschied zwischen Wechselstrom (AC) und Gleichstrom (DC)?**
> 
> Wenn Sie die Spezifikationen eines Akkus nachschauen, finden Sie oft zwei verschiedene Angaben zum Innenwiderstand. Um die Physik nicht unnötig zu kompliziert darzustellen, können wir es so einfach verstehen:
> 
> * **Wechselstrom-Innenwiderstand (ACIR):** Das Messgerät speist in der Regel ein schwaches Wechselspannungssignal von 1 kHz ein. Es misst ausschließlich den physikalischen Widerstand durch die Struktur (wie Kontakte oder Leitfähigkeit des Elektrolyten). Da die Zeit extrem kurz ist, haben chemische Reaktionen noch keine Chance zu starten; daher sind die gemessenen Werte meist sehr niedrig und gut aussieht. Die meisten Handgeräte auf dem Markt messen diesen Wert.
> 
> * **Gleichstrom-Innenwiderstand (DCIR):** Hier wird tatsächlich ein Gerät angeschlossen und ein großer Strom entzogen, um den Widerstand zu messen. Neben dem ursprünglichen physikalischen Widerstand kommt nun noch der „Polarisationswiderstand" hinzu, der entsteht, weil die chemische Reaktion nicht mit der Lade- oder Entladegeschwindigkeit Schritt halten kann. Dieser Wert ist deutlich höher als beim ACIR, doch er repräsentiert den **echten Widerstand** Ihres Handys oder Autos.
> 
> *Hinweis: Um realen Nutzungsszenarien näherzukommen, basieren die in diesem Artikel diskutierten Formeln für Spannungsabfall und Wärmeentwicklung auf dem Gleichstrom-Innenwiderstand (DCIR).*