---
layout: post
title: "Analyse du Système d'Assistance Électrique ISG Moto : Fonctionnement, Gains avec Batterie LiFePO4 et Limites Physiques"
lang: fr
date: 2026-07-14 20:00:00
categories: Moto
tags: [Connaissances Auto, Électricité Automobile, Modification Automobile]
description: "Analyse approfondie des principes de fonctionnement et des limites physiques du système ISG (alterno-démarreur intégré) sur deux-roues : démarrage silencieux et boost électrique. Découvrez pourquoi le remplacement d'une batterie au plomb par une batterie LiFePO4 décuple le couple d'assistance, et pourquoi les contraintes de conception subsistent."
keywords: "moto ISG, boost électrique, alterno démarreur intégré, batterie LiFePO4 moto, comparatif batterie plomb, moto hybride légère, démarrage silencieux, couple au démarrage, chute de tension, IR drop"
image: /images/isg-motorcycle-system.webp
faq:
  - question: "Qu'est-ce que le système de boost électrique ISG sur une moto et quelle est sa fonction ?"
    answer: "L'ISG (Integrated Starter Generator) regroupe le démarreur traditionnel et l'alternateur en un composant unique monté directement en bout de vilebrequin. Il autorise un 'démarrage silencieux' sans cliquetis d'engrenage et la coupure automatique au ralenti. Lors des départs arrêtés ou des fortes accélérations, il puise dans la batterie pour délivrer un couple moteur d'assistance (boost électrique), soulageant le moteur thermique à bas régime."
  - question: "Pourquoi remplacer la batterie au plomb par une batterie LiFePO4 amplifie-t-il si nettement la poussée de l'ISG ?"
    answer: "Les batteries au phosphate de fer lithié (LiFePO4) affichent une résistance interne infime et un pouvoir de décharge instantané (C-rate) colossal. Quand l'ISG appelle un fort courant d'assistance, la batterie LiFePO4 ne subit pas l'effondrement de tension ohmique (chute IR) typique du plomb. Elle délivre instantanément sa pleine puissance, permettant au moteur électrique d'exprimer son couple maximal théorique."
  - question: "Peut-on augmenter le boost de l'ISG indéfiniment ou rouler en 100% électrique grâce à une batterie LiFePO4 ?"
    answer: "Non. Bien que la batterie LiFePO4 lève le goulot d'étranglement de la source d'énergie, le plafond de puissance reste dicté par le dimensionnement du bobinage du stator, le courant bridé par le contrôleur moteur (MCU/ECU), la dissipation thermique du moteur et l'architecture basse tension 12V (où de trop forts ampérages feraient fondre le faisceau)."
---

Ces dernières années, de grands constructeurs de deux-roues (tels que SYM, Kymco ou Yamaha) ont intégré la technologie **ISG (Integrated Starter Generator)** sur leurs scooters et motos. Au-delà du confort offert par le démarrage silencieux sans secousse et la coupure automatique au ralenti (Start & Stop), la fonction d'**assistance électrique au démarrage (Motor Assist / Hybridation Légère)** est devenue un argument commercial majeur.

Néanmoins, de nombreux motards constatent qu'avec la batterie d'origine au plomb-acide, ce coup de pouce électrique paraît timide. En revanche, après être passés à une **batterie au phosphate de fer lithié (LiFePO4)**, l'effet de poussée au démarrage ou à la remise des gaz est nettement amplifié. Comment s'explique ce mécanisme physique ? Et pourquoi des limites infranchissables subsistent-elles malgré l'amélioration de la batterie ? Analyse technique détaillée.

---

![Système ISG moto](/images/isg-motorcycle-system.webp)
*Source image : [Shindengen](https://www.shindengen.com/products/electro/exhibition/private_exhibition/isg_ecu/)*

## Qu'est-ce que l'ISG ? Principe et Double Rôle Mécanique

Sur une moto conventionnelle, le démarreur électrique et l'alternateur (volant magnétique) sont deux organes indépendants. Lors de la mise en route, le démarreur doit entraîner le vilebrequin par un train d'engrenages et une roue libre, générant un cliquetis métallique bruyant et des vibrations.

**L'ISG fusionne ces deux éléments en un seul ensemble brushless**, dont le rotor et le stator sont fixés directement sur la queue du vilebrequin moteur. Il opère sous trois modes :

1. **Mode Démarrage Silencieux (Moteur)** : En tirant l'énergie de la batterie, il fait tourner directement le vilebrequin. L'absence de pignons de réduction procure un démarrage quasi instantané, fluide et totalement silencieux.
2. **Mode Assistance Électrique (Boost moteur)** : Au démarrage ou lors d'une ouverture brutale des gaz, le calculateur injecte du courant dans l'ISG pour fournir un couple d'appoint directement sur le vilebrequin, comblant le creux de couple à bas régime du moteur thermique.
3. **Mode Générateur et Recharge** : Lorsque le moteur tourne normalement, l'ISG bascule en mode alternateur pour convertir une partie de l'énergie mécanique du moteur en électricité afin de recharger la batterie et compenser la consommation du démarrage et du boost.

## Les Limites Physiques Intrinsèques du Boost ISG

Bien que l'ISG apporte un surcroît de dynamisme appréciable, il ne s'apparente en rien à une hybridation 48V automobile ou à un véhicule électrique pur, bridé par des contraintes matérielles strictes :

* **Le Goulot d'Étranglement de la Basse Tension 12V** : Selon la relation fondamentale de puissance $$P = V \times I$$, pour délivrer une puissance d'assistance de 1 kW (environ 1,35 ch) sous une tension nominale de 12V, le courant tiré sur la batterie dépasse **90 à 100 Ampères** en tenant compte des rendements de l'onduleur (MCU) et du moteur. Vouloir doubler cette puissance ferait exploser l'intensité, provoquant un échauffement destructeur du faisceau électrique.
* **Espace Restreint et Conduction Thermique** : Le moteur ISG est logé contre le carter moteur, dans un milieu confiné exposé aux calories de la combustion (souvent au-dessus de 90°C). Une assistance électrique prolongée accumulerait une chaleur excessive dans les enroulements du stator, risquant de brûler le vernis isolant ou de désaimanter les aimants permanents.
* **Durée d'Assistance Éc возможно limitative** : Pour ménager la batterie et prévenir la surchauffe, l'ECU d'origine limite généralement le boost aux 10 à 20 premières secondes de relance, sans jamais pouvoir propulser le scooter de manière autonome à vitesse stabilisée.

## Batterie Plomb vs LiFePO4 : Pourquoi le Gain Ressenti est si Spectaculaire ?

Si l'ISG est bridé par conception, pourquoi le remplacement de la batterie d'origine au plomb par un modèle **LiFePO4** transfigure-t-il la poussée au démarrage ? La réponse réside dans **les propriétés physiques de la batterie qui libèrent le couple réel étouffé par la batterie au plomb**.

```
【Comportement de la Tension sous Appel de Courant Massif】
Plomb Traditionnel : 12.8V ──► [Fort Appel de Courant] ──► Chute IR à 10.0V~10.5V (Puissance Électrique Réduite)
Batterie LiFePO4 :   13.2V ──► [Fort Appel de Courant] ──► Tension Maintenue à 12.5V~12.8V (Pleine Puissance Développée)
```

### 1. Résistance Interne et Chute de Tension Ohmique (Chute IR)
* **Batterie au Plomb** : Sa résistance interne élevée fait chuter sa tension aux bornes selon la loi d'Ohm ($$\Delta V = I \times R_{\text{interne}}$$) lorsqu'un courant de 60 à 80 A est requis. La tension s'écroule instantanément de 12,8V vers 10,5V ou moins. Cette baisse de tension ampute directement la puissance électrique disponible pour le moteur ($$P = V \times I$$), bridant le couple d'assistance.
* **Batterie LiFePO4** : Elle dispose d'une résistance interne cinq fois plus faible et d'un taux de décharge (C-rate) très élevé. Même sous un débit de 100 A, sa tension aux bornes reste solidement ancrée au-dessus de 12,5V. Le moteur ISG reçoit ainsi une tension élevée constante et déploie l'intégralité du couple pour lequel il a été calibré.

### 2. Niveau de Tension et « Seuil de Déclenchement » de l'ECU
L'ECU d'origine impose un seuil de protection basse tension (ex. : > 12,5V requis pour autoriser le boost). La batterie au plomb ayant une tension plus basse, la chute au démarrage provoque souvent une coupure prématurée. La LiFePO4 maintient un palier plus élevé (env. 13,2V–13,4V chargée), signalant à l'ECU une réserve saine pour un boost plus actif et constant.

### 3. Réceptivité de Charge lors de la Recharge par Alternateur
Après l'assistance, l'ISG recharge la batterie moteur tournant (note : sur les scooters CVT 12V courants, l'embrayage débraye en roue libre, il n'y a donc pas de freinage régénératif comme sur un véhicule électrique). Les cellules LiFePO4 acceptent la charge bien plus vite que le plomb, reconstituant rapidement la réserve pour le boost suivant.

| Propriété / Critère | Batterie Plomb Conventionnelle | Lithium Fer Phosphate (LiFePO4) |
| :--- | :--- | :--- |
| **Résistance Interne** | Élevée ; chute de tension sévère lors des fortes décharges | Infime ; maintien d'une tension très stable sous fort appel de courant |
| **Taux de Décharge (C-Rate)** | Moyen ; les fortes décharges répétées écourtent sa durée de vie | Exceptionnel ; encaisse des impulsions de 20C à 40C sans broncher |
| **Poussée ISG au Démarrage** | Étranglée par la chute de tension ; couple électrique incomplet | Pleine restitution du couple d'ingénierie prévu d'origine |
| **Efficacité de Recharge** | Absorption lente ; reconstitution plus longue de la charge | Réceptivité élevée ; recharge rapide après chaque boost |
| **Masse Embarquée** | Lourde (environ 3 à 4 kg) | Très légère (environ 0,8 à 1,2 kg) |

## Les Limites Techniques Indépassables

Certains conducteurs imaginent à tort qu'une batterie LiFePO4 « augmente les chevaux du moteur ». Sur le plan de l'ingénierie, **la batterie LiFePO4 supprime simplement le goulot d'étranglement de sous-tension pour permettre à l'ISG d'atteindre ses performances nominales d'usine, sans transformer la motorisation**. Le gain plafonne devant plusieurs verrous matériels :

### 1. Limiteur de Courant du Contrôleur Moteur (MCU/ECU)
Le débit électrique maximal est borné par les puces MOSFET et la cartographie interne du boîtier de contrôle (MCU). Même si une batterie LiFePO4 peut débiter 200 A, si l'onduleur est bridé à 60 A, l'intensité réelle injectée dans le moteur restera de 60 A.

### 2. Saturation Magnétique du Moteur
L'ISG est physiquement limité par la perméabilité de ses tôles d'acier et la densité de flux de ses aimants néodyme. Lorsque la saturation magnétique est atteinte, injecter davantage d'ampères ne génère aucun couple mécanique supplémentaire : l'énergie résiduelle se dissipe intégralement sous forme de chaleur nocive.

### 3. Limites Physiques à Haut Régime : Force Contre-Électromotrice et CVT
* **Force contre-électromotrice (Back-EMF)** : Plus le régime moteur grimpe, plus la tension inverse induite augmente et s'oppose aux 12V de la batterie ($$V_\text{net} = V_\text{bat} - E_\text{EMF}$$). À haut régime, 12V ne suffisent plus à « pousser » le courant dans le stator (d'où le passage au 48V en automobile).
* **Démultiplication CVT** : Au démarrage, le rapport court du variateur amplifie le modeste couple de l'ISG ; à moyenne et haute vitesse, le moteur thermique domine et l'appoint devient négligeable.

## Conclusion

Le système d'assistance électrique ISG moto est une remarquable innovation technique qui bonifie la souplesse et le rendement énergétique des deux-roues modernes.

Remplacer la batterie au plomb d'origine par une batterie LiFePO4 supprime l'effondrement de tension sous fort ampérage et permet au moteur ISG de **délivrer 100% de son potentiel d'origine**. Toutefois, l'architecture 12V, le bridage du contrôleur et l'évacuation thermique rappellent que l'ISG reste un assistant ponctuel. En comprenant ces équilibres physiques, chaque motard peut apprécier ce surcroît de brio tout en préservant la fiabilité de sa monture.

## Références

* Venkateshwaran B, Pushparajesh V, Kamalakannan D, [*Design and Optimization of mild hybrid BLDC based starter generator for two wheeler*](https://ijetcse.com/v24i6/), IJETCSE, Vol. 24, Issue 6, 2017.
* batteryuniversity.com: *How does Internal Resistance Affect Battery Performance?*
