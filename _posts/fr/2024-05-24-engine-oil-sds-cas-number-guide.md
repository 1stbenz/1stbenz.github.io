---
layout: post
title: "Tableau de Référence des Numéros CAS des Fiches SDS d'Huile Moteur : Huiles de Base et Additifs"
lang: fr
date: 2024-05-24 10:00:00
categories: Auto
tags: [Entretien Automobile, Spécifications d'Huile]
description: "Un tableau pratique des composants chimiques et numéros CAS usuels extraits des fiches de données de sécurité (FDS / SDS) des huiles moteur. Couvre les huiles de base du Groupe I au Groupe V et les additifs essentiels pour décoder la chimie des lubrifiants."
keywords: "Huile moteur, SDS, FDS, Numéro CAS, Huile de base, PAO, VHVI, GTL, Additifs, ZDDP, Esters, Tableau de référence"
image: /images/engine-oil-sds.webp
faq:
  - question: "Qu'est-ce qu'une FDS (Safety Data Sheet / SDS) d'huile moteur ?"
    answer: "Une FDS (Fiche de Données de Sécurité) est un document technique et réglementaire répertoriant les substances chimiques et numéros CAS d'un lubrifiant. C'est l'outil le plus objectif pour déterminer la nature réelle des huiles de base (PAO, hydrocraquage, GTL) et la composition des additifs."
  - question: "Pourquoi une même famille d'huile de base possède-t-elle plusieurs numéros CAS différents ?"
    answer: "Les huiles de base sont des coupes complexes d'hydrocarbures. Les procédés de raffinage (isomérisation, hydrocraquage poussé), la longueur des chaînes carbonées et la viscosité intrinsèque génèrent des immatriculations chimiques CAS distinctes."
  - question: "Quelle est la fonction du composé ZDDP omniprésent dans ces tableaux ?"
    answer: "Le ZDDP (dialkyldithiophosphate de zinc) est l'additif anti-usure et antioxydant de référence. Sous forte température et contrainte de contact métal contre métal, il forme un film protecteur sacrificiel phospho-zingué microscopique empêchant le grippage mécanique."
---

Lors du choix d'une huile moteur, de nombreux automobilistes et passionnés s'interrogent : l'appellation commerciale « 100% Synthèse » masque-t-elle une véritable base PAO (Groupe IV), des Esters (Groupe V) ou une huile minérale hydrocraquée VHVI (Groupe III) ? Le moyen le plus fiable et impartial pour percer les secrets de formulation d'un lubrifiant consiste à analyser sa **Fiche de Données de Sécurité (FDS / SDS)**.

<figure>
  <img src="/images/sds_mobil_1_0w40_2026.webp" alt="FDS Mobil 1 0W-40">
  <figcaption align="center">Illustration : FDS Mobil 1 0W-40</figcaption>
</figure>

Dans une FDS, chaque composé chimique est identifié par un identifiant universel : le **Numéro CAS (Chemical Abstracts Service)**, véritable numéro d'immatriculation de la matière. Ce guide vous fournit un tableau récapitulatif complet des numéros CAS des principales huiles de base (Groupes I à V) et des additifs de pointe (ZDDP, modificateurs de friction MoDTC, détergents, dispersants).

<div style="margin-bottom: 20px; padding: 15px; background-color: #f8fafc; border-radius: 8px; border: 1px solid #e2e8f0; color: #262626;">
  <label for="casSearchInput" style="font-weight: bold; margin-right: 10px;">Recherche Instantanée :</label>
  <input type="text" id="casSearchInput" placeholder="Entrez un numéro CAS (ex. 68037-01-4)" style="padding: 8px; width: 250px; border: 1px solid #ccc; border-radius: 4px;">
  <button onclick="searchCAS()" style="padding: 8px 15px; background-color: #04384c; color: white; border: none; border-radius: 4px; cursor: pointer;">Rechercher</button>
  <span id="searchResultMsg" style="color: #dc3545; margin-left: 10px; font-weight: bold;"></span>
</div>

<script>
function searchCAS() {
    const input = document.getElementById("casSearchInput").value.trim().toLowerCase();
    const msg = document.getElementById("searchResultMsg");
    msg.innerText = "";

    if (input === "") {
        msg.innerText = "Veuillez entrer un numéro CAS !";
        return;
    }

    const table = document.querySelector("table");
    if (!table) return;

    const rows = table.getElementsByTagName("tr");
    let found = false;

    for (let i = 1; i < rows.length; i++) {
        rows[i].style.backgroundColor = "";
        rows[i].style.transition = "background-color 0.5s ease";

        const casCell = rows[i].getElementsByTagName("td")[1];
        if (casCell) {
            const casText = casCell.innerText || casCell.textContent;
            if (casText.toLowerCase().includes(input)) {
                rows[i].scrollIntoView({ behavior: 'smooth', block: 'center' });
                rows[i].style.backgroundColor = "rgba(4, 56, 76, 0.15)"; 
                found = true;
                break;
            }
        }
    }

    if (!found) {
        msg.innerText = "Numéro CAS non trouvé dans ce tableau.";
    }
}

document.addEventListener("DOMContentLoaded", function() {
    const inputField = document.getElementById("casSearchInput");
    if (inputField) {
        inputField.addEventListener("keypress", function(event) {
            if (event.key === "Enter") {
                event.preventDefault();
                searchCAS();
            }
        });
    }
});
</script>

| Catégorie de Base / Additif | <span style="display: inline-block; width:110px">Numéro CAS</span> | Description Chimique |
| :--- | :--- | :--- |
| **Groupe IV<br>(Synthèse PAO)** | 68037-01-4 | 1-Décène, homopolymère hydrogéné |
| | 68649-12-7 | Tétramère de 1-décène mélangé avec trimère de 1-décène, hydrogéné |
| | 68649-11-6 | 1-Décène, dimère hydrogéné |
| | 163149-29-9<br>*(et 8002-05-9)* | 1-Décène, homopolymère hydrogéné ; copolymères d'oléfines C8, C12 |
| | 151006-63-2 | 1-Dodécène, homopolymère hydrogéné |
| | 151006-62-1 | 1-Dodécène, trimère hydrogéné |
| | 151006-60-9 | 1-Dodécène polymérisé avec 1-décène, hydrogéné |
| | 163149-28-8 | 1-Décène polymérisé avec 1-octène et 1-dodécène, hydrogéné |
| **Groupe III<br>(GTL Gas-to-Liquid)**| 848301-69-9 | Distillats de synthèse Fischer-Tropsch, lourds, C18-50 ramifiés et linéaires |
| | 1262661-88-0| Distillats de synthèse Fischer-Tropsch, lourds, C18-50 ramifiés |
| **Groupe III<br>(Hydrocraquage VHVI)** | 64741-89-5 | Huiles de base paraffiniques hautement hydrotraitées |
| | 64742-54-7 | Huiles de base paraffiniques lourdes hautement hydrotraitées |
| | 64742-55-8 | Huiles de base paraffiniques légères hautement hydrotraitées |
| | 64742-70-7 | Huiles paraffiniques déparaffinées catalytiquement |
| | 72623-87-1 | Hydrocarbures paraffiniques sévèrement hydrotraités (C20-50) |
| | 72623-85-9 | Huiles lubrifiantes neutres hydrotraitées haute viscosité |
| | 72623-86-0 | Huiles de base neutres hydrotraitées |
| | 178603-64-0 | Gasoils sous vide hydrocraqués et hydroisomérisés C15-30, haut indice VI |
| | 178603-65-1 | Gasoils sous vide hydrocraqués et hydroisomérisés C20-40, haut indice VI |
| | 178603-66-2 | Gasoils sous vide hydrocraqués et hydroisomérisés C25-55, haut indice VI |
| **Groupe I / II<br>(Bases Minérales)** | 64741-50-0 | Distillats paraffiniques légers |
| | 64741-50-5 | Distillats pétroliers légers de raffinage |
| | 64741-52-2 | Distillats naphténiques légers |
| | 64742-65-0 | Distillats paraffiniques lourds déparaffinés au solvant |
| | 64742-58-1 | Huiles lubrifiantes hydrotraitées régénérées |
| | 64742-56-9 | Distillats paraffiniques légers déparaffinés au solvant |
| | 64742-62-7 | Huiles résiduelles déparaffinées au solvant |
| **Groupe V<br>(Esters / Divers)** | 27178-16-1 | Adipate de di-isodécyle |
| | 16958-92-2 | Huiles de base synthétiques de type ester |
| | 28472-97-1 | Azélate de di-isodécyle (base di-ester) |
| | 9003-13-8 | Polyalkylène glycol (PAG) |
| **Additifs Anti-usure<br>(ZDTP / ZDDP)** | 68649-42-3 | Dialkyldithiophosphate de zinc ZDTP |
| | 84605-29-8 | Sels de zinc de l'acide phosphorodithioïque, esters bis(1,3-diméthylbutyle et iso-Pr) |
| **Modificateurs de Friction<br>(MoDTC / MoDTP)**| 68958-92-7 | Dithiophosphate de molybdène |
| | 68958-92-9 | Di(2-éthylhexyl)phosphorodithioate de molybdène |
| **Antioxydants**| 36878-20-3 | Bis(nonylphényl)amine |
| | 128-39-2 | 2,6-di-tert-butylphénol |
| **Détergents**| 61789-86-4 | Sulfonate de calcium pétrolier |
| | 68783-96-0 | Sulfonates de calcium surbasés |
| | 115733-09-0 | Phénate sulfure d'alkyle à chaîne longue et calcium |
| **Dispersants** | Sans CAS | Succinimide de polyoléfine polyamine, polyol |
| | 296-404-1<br>*(N° CE)*| Esters d'acide phosphorique |
| | 84605-20-9 | Polyisobutylène succinimide (PIBSI) |
| **Améliorants de Viscosité<br>(VM)** | 25038-36-2 | Copolymère d'oléfines (OCP) |
| | 127883-08-3 | Polyoléfine aromatique éthylène/propylène |
| **Abaisseurs de Point d'Écoulement<br>(PPD)** | Sans CAS | Polyméthacrylate d'alkyle (PMA) |
| **Antimousse**| 63148-62-9 | Polydiméthylsiloxane (huile de silicone) |

## Références Techniques
* [Étude de la composition des huiles - Bases PAO, GTL, Hydrocraquage VHVI, Esters - Forum Oil-Club.ru](https://www.oil-club.ru/forum/topic/2120-izuchaem-sostav-masla-pao-group-iv-gtl-gidrokreking-vhvi-group-iii-mineralnoe-maslo-group-i-ili-ii-estery-itd/page/31/)
