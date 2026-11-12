---
layout: post
title: "Test de fuite de courant automobile (Édition Chute de tension) : localiser les fuites de batterie avec un multimètre et le tableau de chute de tension des fusibles"
lang: fr
date: 2026-11-03 10:00:00
categories: Auto
tags: [Électricité automobile, Réparation auto, Guide DIY, Fuite de courant, Chute de tension, Test fusible, Décharge batterie]
related_posts:
  - 2026-11-01-parasitic-drain-tester-guide.md
  - 2026-11-02-dc-clamp-meter-parasitic-drain-guide.md
  - 2025-09-17-memory-saving-battery.md
description: "Vous retirez encore les fusibles un par un pour trouver les fuites de batterie ? Sur les véhicules modernes multiplexés en réseau CAN-bus, retirer un fusible réveille les calculateurs et fausse les mesures. Découvrez la méthode professionnelle de chute de tension des fusibles au multimètre en mV pour localiser une fuite en 2 minutes sans retirer aucun fusible."
keywords: "chute de tension fusible, tableau chute de tension fusible, courant parasite, fuite de courant, decharge batterie voiture, multimetre mV, diagnostic electrique automobile, courant de repos"
image: /images/FuseVoltageMethod.webp
faq:
  - question: "En quoi consiste la méthode de chute de tension sur les fusibles ?"
    answer: "Chaque fusible automobile à lame possède une résistance interne fixe minime (en milliohms, mΩ). Selon la loi d'Ohm (U = R × I), tout courant parasite qui le traverse génère une micro-chute de tension en millivolts (mV) entre ses points de test. En mesurant cette chute au multimètre et en se référant à un tableau de conversion, on déduit instantanément l'intensité exacte sans ouvrir le circuit."
  - question: "Pourquoi la mesure de chute de tension est-elle bien supérieure au retrait des fusibles ?"
    answer: "Les véhicules actuels utilisent des réseaux de calculateurs interconnectés (CAN-bus / LIN-bus). Retirer un fusible coupe l'alimentation d'un boîtier, ce qui alerte la passerelle réseau et réveille en chaîne des dizaines de calculateurs endormis. Il faut alors attendre de nouveau 15 à 45 minutes pour retrouver le sommeil profond. La méthode en mV est 100 % non invasive, ne réveille rien et préserve le serrage des connecteurs."
  - question: "Que signifie une lecture négative sur le multimètre (ex. -0,5 mV) ?"
    answer: "C'est absolument normal. Le signe négatif indique simplement la polarité des pointes de touche par rapport au sens d'écoulement du courant. Les fusibles n'ont aucun sens de polarité ; ignorez le signe moins et utilisez la valeur absolue (0,5 mV) pour consulter le tableau."
---

![Mesure de la micro-chute de tension sur fusible automobile pour diagnostiquer une fuite](/images/FuseVoltageMethod.webp)

Face à une batterie de voiture qui se vide mystérieusement pendant la nuit, la méthode classique consistant à retirer les fusibles un à un vire souvent au cauchemar. Sur les véhicules modernes équipés de réseaux informatiques embarqués (bus CAN), retirer un fusible **réveille instantanément les calculateurs**, créant des pics d'intensité qui rendent le diagnostic impossible.

La **méthode de chute de tension sur fusibles (avec tableau de conversion en mV)** est la technique de référence des meilleurs électriciens automobiles : **100 % sans retrait de fusible, sans coupure d'alimentation et sans réveil électronique**. Avec un simple multimètre numérique, vous inspectez une boîte à fusibles complète en moins de deux minutes et ciblez la ligne en fuite avec une précision chirurgicale.

> **Navigation dans la série :**
> - Pour mesurer le courant de repos global : [Guide de l'interrupteur en série](/fr/2026/parasitic-drain-tester-guide.html) | [Guide de la pince ampèremétrique DC](/fr/2026/dc-clamp-meter-parasitic-drain-guide.html)

---

## Le principe fondamental : la loi d'Ohm $$U = R \times I$$

Les fusibles à lame automobiles ne sont pas des supraconducteurs parfaits. Leur élément métallique interne possède une résistance électrique connue, stable et calibrée (généralement comprise entre 2 mΩ et 30 mΩ).

D'après la **loi d'Ohm** :

$$U = I \times R \quad \Longrightarrow \quad I = \frac{U}{R}$$

- $$R$$ (Résistance interne du fusible) : Fixe et calibrée selon le type et l'ampérage du fusible.
- $$U$$ (Chute de tension) : La micro-différence de potentiel mesurée aux bornes du fusible en millivolts ($$mV$$).
- $$I$$ (Courant parasite) : Le courant réel traversant le circuit en milliampères ($$mA$$).

Les fusibles à lame comportent **deux petits plots métalliques de test apparents** sur leur tranche supérieure. En posant les pointes du multimètre sur ces deux plots, on mesure directement la tension résiduelle ($$mV$$) sans ouvrir le circuit.

---

## Outils nécessaires

![Pointes de test fines pour multimètre](/images/sharppoint.webp)

1. **Multimètre numérique (DMM)** : Réglé sur le calibre **DC mV (millivolts)** (avec une résolution de 0,1 mV ou 0,01 mV).
2. **Pointes de touche effilées aiguilles (Indispensables)** : Les pointes standard sont trop épaisses pour atteindre les plots encastrés. Des pointes aiguilles de 0,7 mm à 1,0 mm percent l'oxydation de surface.
3. **Tableaux de référence** : Les tables ci-dessous.

---

## Mode opératoire pas à pas

### Étape 1 : Simuler la fermeture et attendre le sommeil profond
1. Coupez le contact, éteignez tous les accessoires et **baissez entièrement les vitres** (évite d'être enfermé dehors).
2. Ouvrez les trappes des boîtes à fusibles et **verrouillez manuellement les gâches de serrures (portes, capot, coffre)** à l'aide d'un tournevis pour simuler des portes fermées.
3. Verrouillez le véhicule à la télécommande et **éloignez les clés mains libres à plus de 5 mètres**.
4. **Attendez 15 à 45 minutes** pour que tous les boîtiers électroniques (BCM, ECU, passerelle) entrent en sommeil profond.

---

### Étape 2 : Réglage du multimètre et mesure
1. Branchez la pointe rouge sur **V/Ω/mV** et la noire sur **COM**.
2. Positionnez le sélecteur rotatif sur **DC mV**.
3. Appliquez fermement les deux pointes aiguilles sur les **deux plots métalliques de test** situés sur le dessus du fusible en appuyant légèrement pour traverser l'oxydation.
4. Lisez la valeur affichée :
   - **`0.0 mV`** : Aucun courant ne circule. Le circuit dort paisiblement ; passez immédiatement au fusible suivant.
   - **Valeur numérique (ex. `0.6 mV`)** : Du courant circule activement à travers ce fusible ! Notez le format (Mini ou Standard/ATO), le calibre en ampères et la tension mesurée en mV.

> **Une lecture négative (ex. -0,5 mV) ?**  
> Cela dépend simplement du côté où se trouve la pointe rouge par rapport au sens du courant. Les fusibles n'ont aucune polarité : **prenez la valeur absolue (`0,5 mV`)** pour consulter le tableau.

---

## Tableaux de conversion Chute de tension / Courant

Après avoir relevé la tension en millivolts, référez-vous aux tableaux suivants pour connaître l'intensité correspondante en milliampères (mA) :

### 1. Tableau pour fusibles Mini à lame (ATM) (Unité : mA)

| Calibre du fusible | Résistance approx. | 0,2 mV | 0,4 mV | 0,6 mV | 0,8 mV | 1,0 mV | 1,5 mV | 2,0 mV |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **5A (Beige)** | ~15,2 mΩ | 13 mA | 26 mA | 39 mA | 53 mA | **66 mA** | 99 mA | 132 mA |
| **7,5A (Marron)** | ~10,1 mΩ | 20 mA | 40 mA | 59 mA | 79 mA | **99 mA** | 149 mA | 198 mA |
| **10A (Rouge)** | ~7,1 mΩ | 28 mA | 56 mA | 85 mA | 113 mA | **141 mA** | 211 mA | 282 mA |
| **15A (Bleu)** | ~4,6 mΩ | 43 mA | 87 mA | 130 mA | 174 mA | **217 mA** | 326 mA | 435 mA |
| **20A (Jaune)** | ~3,3 mΩ | 61 mA | 121 mA | 182 mA | 242 mA | **303 mA** | 455 mA | 606 mA |
| **25A (Blanc/Clair)**| ~2,5 mΩ | 80 mA | 160 mA | 240 mA | 320 mA | **400 mA** | 600 mA | 800 mA |
| **30A (Vert)** | ~2,0 mΩ | 100 mA | 200 mA | 300 mA | 400 mA | **500 mA** | 750 mA | 1000 mA |

---

### 2. Tableau pour fusibles Standard à lame (ATO / ATC) (Unité : mA)

| Calibre du fusible | Résistance approx. | 0,2 mV | 0,4 mV | 0,6 mV | 0,8 mV | 1,0 mV | 1,5 mV | 2,0 mV |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **5A (Beige)** | ~17,8 mΩ | 11 mA | 22 mA | 34 mA | 45 mA | **56 mA** | 84 mA | 112 mA |
| **7,5A (Marron)** | ~10,9 mΩ | 18 mA | 37 mA | 55 mA | 73 mA | **92 mA** | 138 mA | 183 mA |
| **10A (Rouge)** | ~7,4 mΩ | 27 mA | 54 mA | 81 mA | 108 mA | **135 mA** | 203 mA | 270 mA |
| **15A (Bleu)** | ~4,8 mΩ | 42 mA | 83 mA | 125 mA | 167 mA | **208 mA** | 313 mA | 417 mA |
| **20A (Jaune)** | ~3,4 mΩ | 59 mA | 118 mA | 176 mA | 235 mA | **294 mA** | 441 mA | 588 mA |
| **25A (Blanc/Clair)**| ~2,6 mΩ | 77 mA | 154 mA | 231 mA | 308 mA | **385 mA** | 577 mA | 769 mA |
| **30A (Vert)** | ~2,1 mΩ | 95 mA | 190 mA | 286 mA | 381 mA | **476 mA** | 714 mA | 952 mA |

> **Règle de calcul mental rapide (Fusible Mini 10A très courant) :**  
> **Chaque tranche de 0,1 mV correspond à environ 14 mA de fuite.** Une lecture de `0,5 mV` équivaut donc à $$0,5 \times 14 = 70\text{ mA}$$.

---

## Localiser et isoler l'élément consommateur en défaut

Dès qu'un fusible présente une chute de tension anormale, **ne le retirez surtout pas** :

1. **Identifier l'affectation du fusible** : Consultez le carnet d'entretien ou le schéma de boîte à fusibles pour savoir ce qu'il alimente (ex. autoradio de seconde monte, dashcam, éclairage d'accueil, calculateur de porte).
2. **Débrancher le récepteur suspect** : Déconnectez la prise électrique directement sur l'appareil lui-même (et non à la boîte à fusibles).
3. **Re-tester la chute de tension** : Si la tension s'écroule instantanément de `1,2 mV` à **`0,0 mV`**, vous avez localisé avec certitude le composant responsable !

---

## Résumé de la stratégie de diagnostic en 3 étapes

* **Étape 1 (Mesure du courant global)** : Enserrez le câble négatif de batterie avec une pince ampèremétrique DC pendant 30 secondes pour vérifier si une fuite existe (< 50 mA est normal).
* **Étape 2 (Vérification de l'alternateur)** : Pincez le câble B+ de l'alternateur pour exclure tout court-circuit de diodes de redressement.
* **Étape 3 (Ciblage chirurgical du circuit)** : Scannez les fusibles au multimètre en **DC mV** avec le tableau de chute de tension pour localiser la fuite en 2 minutes sans jamais réveiller le véhicule !
