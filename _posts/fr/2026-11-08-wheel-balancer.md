---
layout: post
title: "Notes techniques : principes des équilibreuses de roues et uniformité des pneumatiques"
lang: fr
date: 2026-11-08 10:20:00
categories: Auto
tags: [Équilibrage de roues, Connaissances auto, Vibrations de châssis, Entretien des pneus]
description: "Découvrez le fonctionnement des équilibreuses de roues, la signification des points rouges et jaunes sur les pneus, et comment éliminer les vibrations à haute vitesse et le tirage persistant causés par les variations de force radiale (RFV) et latérale (LFV)."
keywords: "Equilibreuse de roues, Equilibrage dynamique, Equilibrage statique, Point rouge pneu, RFV, LFV, CONG, Ply Steer, Equilibrage Road Force, ForceMatch, Uniformite pneu, Vibration haute vitesse"
image: /images/wheel-balancer.webp
faq:
  - question: "Quel est le principe fondamental de fonctionnement d'une équilibreuse de roues ?"
    answer: "L'équilibreuse utilise des capteurs piézoélectriques fixés sur son arbre pour mesurer les forces centrifuges dynamiques et les couples de renversement. Associée à un encodeur optique angulaire, elle calcule précisément la masse et la position angulaire des masselottes de correction à poser sur les plans intérieur et extérieur de la jante."
  - question: "Que signifient les points rouge et jaune marqués sur un pneu neuf ?"
    answer: "Le point rouge indique le point de raideur radiale maximale (pic RFV 1H ou point haut géométrique). Le point jaune repère le point le plus léger en masse du pneu. Il faut toujours prioriser l'alignement du point rouge avec le point bas (creux) de la jante ; si absent, aligner le point jaune avec la valve. Le point rouge a toujours priorité sur le point jaune."
  - question: "Pourquoi un véhicule tire-t-il d'un côté même lorsque la géométrie du train avant est parfaite ?"
    answer: "Le tirage provient souvent des forces latérales générées par le pneu lui-même. La poussée latérale totale est la somme de la conicité (CONG, qui s'inverse en retournant le pneu) et de la rigidité de carcasse (Ply Steer, qui ne s'inverse pas). Le couple d'alignement résiduel (RAT) peut aussi décentrer le volant ou fausser le rappel en ligne droite."
  - question: "Pourquoi une voiture vibre-t-elle sur autoroute alors que les roues sont équilibrées à 0g / 0g ?"
    answer: "Les équilibreuses classiques mesurent la répartition des masses du pneu tournant dans le vide sans contrainte. Elles ne détectent pas les défauts d'uniformité sous charge (U/F). Si la variation de force radiale (RFV / RFV 1H) est excessive, le pneu se comporte sous le poids du véhicule comme une came excentrique créant de violentes résonances."
  - question: "Une équilibreuse classique peut-elle résoudre les problèmes de RFV ou de LFV ?"
    answer: "Non. La RFV et la LFV proviennent de raideurs internes de carcasse et de l'assemblage des nappes. Ajouter des plombs ne peut ni assouplir une gomme trop dure ni modifier l'angle des câbles d'acier. Seule une équilibreuse Road Force à rouleau presseur avec optimisation ForceMatch permet de les corriger."
  - question: "Comment résout-on concrètement les défauts de RFV et de tirage latéral ?"
    answer: "Pour la RFV, on applique un rouleau presseur (~500 kg) pour repérer la zone rigide du pneu, puis on dégonfle et fait pivoter le pneu sur la jante (ForceMatch) afin que le creux de jante absorbe la bosse de raideur. Pour le tirage latéral, on permute ou retourne les pneus avant pour annuler mutuellement leurs poussées latérales."
---

![Équilibreuse de roues de précision](/images/wheel-balancer.webp)

De nombreux conducteurs se heurtent à ce paradoxe déconcertant : **les roues sortent parfaitement équilibrées à 0g / 0g de l'atelier, et pourtant le volant tremble à 110 km/h ; la géométrie est réglée au millimètre près, et pourtant la voiture tire obstinément de côté lorsqu'on lâche le volant.** Pour vaincre ces vibrations parasites à haute vitesse, il faut dépasser la simple répartition des masses et comprendre la physique de l'uniformité des pneumatiques (Tire Uniformity - U/F).

## 1. Principes de fonctionnement de l'équilibreuse de roues
Lorsqu'une roue tourne à grande vitesse, la moindre asymétrie de masse est amplifiée de façon exponentielle par la force centrifuge. L'équilibreuse a pour mission d'isoler et de neutraliser ces perturbations dynamiques.

*   **Correction de deux types de balourd :**
    *   **Balourd statique (saut vertical) :** Le centre de gravité est décalé par rapport à l'axe de rotation. La force centrifuge radiale qui en résulte tire la roue vers l'extérieur, provoquant un **sautillement vertical**.
    *   **Balourd dynamique (frétillement latéral / shimmy) :** Une dissymétrie de masse entre les plans intérieur et extérieur engendre un **couple de forces rotatif**, provoquant des **oscillations latérales et un tremblement** autour du pivot de direction.
*   **Acquisition des signaux et résolution sur deux plans :**
    *   **Capteurs piézoélectriques :** Des capteurs à quartz haute rigidité placés sur les paliers de l'arbre mesurent des micro-déplacements ($$\mu\text{m}$$) et l'amplitude des forces alternées.
    *   **Encodeur rotatif optique :** Il suit l'angle de rotation avec une précision inférieure au demi-degré ($$< 0,5^\circ$$) pour caler la phase angulaire exacte du balourd.
    *   **Algorithme à deux plans :** Résout simultanément l'équilibre des forces ($$\sum \vec{F} = 0$$) et l'équilibre des moments ($$\sum \vec{M} = 0$$) afin de déterminer la masse en grammes et l'orientation horaire des plombs sur les plans intérieur et extérieur de la jante.

## 2. Que signifient les points rouge et jaune sur le flanc d'un pneu ?
Ces repères de couleur apposés sur les pneus neufs sont les témoins des tests d'uniformité en sortie d'usine. Ils constituent la première ligne de défense lors du montage :
![Points de repère de couleur sur le flanc du pneu](/images/wheel_dot.webp)
*   **Point Rouge (RFV 1H / Point de faux-rond radial maximal) :**
    *   Marque spécifiquement le pic du **premier harmonique de variation de force radiale (RFV 1H)**, c'est-à-dire le point de raideur maximale par tour qui déclenche le plus facilement la résonance du châssis.
    *   **Règle de montage :** Aligner impérativement le point rouge avec le **point le plus bas du faux-rond de la jante (creux usiné)**. Le creux géométrique de la roue compense et absorbe le pic de raideur du pneu.
*   **Point Jaune (Point le plus léger en masse) :**
    *   Repère l'endroit le plus léger sur la circonférence du pneu.
    *   **Règle de montage :** Si la jante ne possède aucun repère de creux, aligner le point jaune avec la **valve de gonflage** (le point le plus lourd de la jante) pour minimiser la quantité de masselottes de plomb nécessaires.
*   **Lequel privilégier en cas de conflit entre le rouge et le jaune ?**
    *   **Le point rouge est toujours prioritaire.** Un balourd de masse (point jaune) se compense très facilement avec des plombs d'équilibrage, alors qu'une variation structurelle de raideur (point rouge) mal montée ne pourra jamais être effacée avec du plomb.

## 3. Pourquoi une roue à 0g tremble encore : RFV, LFV et vraies solutions
La limite majeure des équilibreuses standard est que le pneu tourne **en l'air, sans aucune contrainte de charge**. Elles n'équilibrent que la masse, laissant **la RFV et la LFV totalement intactes**.
![Forces RFV et LFV](/images/LFV-RFV.webp)

*   **RFV et RFV 1H (Variation de force radiale, à minimiser absolument) :**
    *   **Cause :** Irrégularité des jonctions de nappes ou raideur non uniforme des flancs. Dans le vide, le pneu tourne parfaitement rond ; mais sous le poids de la voiture (~500 kg), la section la plus rigide refuse de s'écraser et agit comme une came qui secoue le châssis de haut en bas à chaque tour.
*   **LFV, CONG et PLY (Variation de force latérale et conicité, à approcher de zéro) :**
    *   **CONG (Conicité) :** Provoquée par un profil légèrement tronconique (différence de diamètre gauche/droite). Le pneu roule comme un gobelet en carton, tirant vers le petit côté. **Retourner le pneu sur la jante inverse la direction de poussée**.
    *   **PLY (Effet de nappe / Ply Steer) :** Cisaillement latéral généré par la déformation des ceintures d'acier inclinées sous charge. **Retourner le pneu N'INVERSE PAS la poussée** (biais structurel intrinsèque).
    *   **Poussée latérale totale :** Définie par la somme vectorielle :
        $$\text{Force Latérale Totale} = \text{CONG} + \text{PLY}$$
        *   **Exemple :** Un pneu sort d'usine avec $$CONG = +80\text{ N}$$ (poussée à droite) et $$PLY = +40\text{ N}$$ (poussée à droite) :

            $$\text{Poussée nette d'usine} = (+80\text{ N}) + (+40\text{ N}) = +120\text{ N} \quad (\text{fort tirage vers la droite})$$

            Si le technicien démonte et **retourne le pneu sur la jante**, CONG s'inverse à $$-80\text{ N}$$, tandis que PLY reste à $$+40\text{ N}$$ :

            $$\text{Poussée nette après retournement} = (-80\text{ N}) + (+40\text{ N}) = -40\text{ N} \quad (\text{tirage fortement atténué})$$

            La dérive au volant est spectaculairement réduite !
    *   **RAT (Couple d'alignement résiduel) :** Le décalage de force latérale engendre un couple parasite autour du pivot de fusée, décentrant le volant ou créant un rappel asymétrique.

### Comment éliminer définitivement la RFV et le tirage latéral
1. **Diagnostic sur équilibreuse Road Force :**  
   Les machines de type Hunter Road Force appliquent un rouleau presseur de 500 à 600 kg contre le pneu pour mesurer la RFV dynamique et les poussées latérales en conditions réelles de route.
2. **Optimisation de phase ForceMatch (Suppression de la RFV) :**  
   L'appareil mesure le point bas de la jante et le point dur du pneu. Le technicien décolle les talons et tourne le pneu sur la jante (ex. 180°) pour **faire correspondre le creux géométrique de la roue avec la bosse de raideur du pneu**, éliminant physiquement la vibration.
3. **Appariement stratégique des pneumatiques :**  
   En combinant les forces latérales (CONG + PLY), les deux pneus avant sont disposés de manière à annuler mutuellement leurs poussées résiduelles. Les pneus ayant la plus faible variation de RFV/LFV sont systématiquement réservés à l'essieu directeur avant.

## 4. Les 5 critères d'un équilibrage de qualité professionnelle
1. **État du cône et de la bague de centrage :** Un cône usé ou sale induit un jeu de centrage de 0,1 mm, générant un faux balourd fantôme de 10 à 15 g.
2. **Nettoyage des portées :** Les anciens plombs collants et traces d'adhésif doivent être totalement retirés, et les gravillons coincés dans les sculptures éliminés.
3. **Respect strict des points de couleur :** Les pneus doivent être indexés méticuleusement d'après leurs repères rouge/jaune, et non posés au hasard avec une avalanche de masselottes.
4. **Contrôle systématique par un second lancer :** Le monteur doit toujours abaisser le carter pour un lancer de vérification confirmant le double « 0g / 0g ».
5. **Recours au Road Force pour les vibrations rebelles :** Si une vibration persiste à 110-120 km/h malgré un affichage 0g, exigez un diagnostic à rouleau presseur ForceMatch.

## En résumé
La stabilité à haute vitesse repose sur trois piliers :
1. **L'équilibreuse standard** gère les masses libres en rotation pour supprimer sautillements et frétillements avec des plombs.
2. **Les points rouge et jaune** optimisent l'assemblage initial pour limiter le faux-rond et réduire le recours au plomb.
3. **La RFV et la LFV** sont des raideurs internes sous charge que le plomb ne peut pas compenser : seules l'équilibreuse Road Force et l'optimisation ForceMatch permettent d'en venir à bout.
