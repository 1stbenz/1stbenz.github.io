---
layout: post
title:  "Engine Oil SDS CAS Numbers Reference Table: Base Oils and Additives"
lang: en
date:   2024-05-24 10:00:00
categories: Auto
tags: [Engine Oil, SDS, CAS Number, Base Oil, Additives, Lubricants]
description: "A practical reference table of common chemical ingredients and CAS numbers found in engine oil Safety Data Sheets (SDS). Includes Group I to Group V base oils and core additives to help you decode engine oil formulations."
keywords: "Engine Oil, SDS, CAS Number, Base Oil, PAO, VHVI, GTL, Additives, ZDDP, Esters, Reference Table"
image: /images/engine-oil-sds.webp
faq:
  - question: "What is an engine oil SDS (Safety Data Sheet)?"
    answer: "An SDS (Safety Data Sheet) is a document that lists the main chemical components and CAS numbers of an engine oil. It serves as a crucial reference for enthusiasts and professionals to understand the types of base oils (e.g., PAO, hydrocracked oils) and the proportion of additives used."
  - question: "Why does the same base oil category have multiple different CAS numbers?"
    answer: "Base oils are complex mixtures of hydrocarbons. Different manufacturing processes (like hydrocracking, isomerization), carbon chain lengths, and viscosities correspond to different chemical registry numbers. Note that a CAS number alone cannot determine the base oil group with 100% certainty; sometimes the Viscosity Index (VI) must also be considered."
  - question: "What is the function of ZDDP, which frequently appears on the list?"
    answer: "ZDDP (Zinc Dialkyl Dithiophosphate) is the most critical anti-wear and anti-oxidation additive in engine oils. It forms an ultra-thin phosphorus/zinc protective film on metal surfaces inside the engine, significantly reducing direct metal-to-metal contact and wear under extreme high temperatures and pressures."
---

When choosing engine oil, many car enthusiasts often wonder whether the "Full Synthetic" label on the bottle actually uses true PAO (Group IV), Esters (Group V), or highly hydrocracked VHVI (Group III) base oils. The most objective and direct way to uncover the mystery of an engine oil's formulation is to check its **Safety Data Sheet (SDS / MSDS)**.

<figure>
  <img src="/images/sds_mobil_1_0w40_2026.webp" alt="美孚1號0W40 SDS">
  <figcaption align="center">figure：Mobil 1 0W-40</figcaption>
</figure>

In an SDS document, each chemical component is labeled with a unique **CAS Number (Chemical Abstracts Service Registry Number)**, which acts as the "ID card" for chemical substances. To help you quickly decode these cryptic codes, this article compiles a reference table of CAS numbers for the most common base oils (Group I ~ V) and core additives (such as ZDDP, detergents, dispersants, etc.) found in engine oil formulations. Whether you want to verify the actual ingredients or are simply interested in the science of lubricants, this table will be a practical lookup tool.

<div style="margin-bottom: 20px; padding: 15px; background-color: #161b22; border-radius: 5px; border: 1px solid #ddd;">
  <label for="casSearchInput" style="font-weight: bold; margin-right: 10px;">Quick Search:</label>
  <input type="text" id="casSearchInput" placeholder="Enter CAS Number (e.g., 68037-01-4)" style="padding: 8px; width: 250px; border: 1px solid #ccc; border-radius: 4px;">
  <button onclick="searchCAS()" style="padding: 8px 15px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer;">Search</button>
  <span id="searchResultMsg" style="color: #dc3545; margin-left: 10px; font-weight: bold;"></span>
</div>

<script>
function searchCAS() {
    // Get the user input and trim leading/trailing whitespace
    const input = document.getElementById("casSearchInput").value.trim().toLowerCase();
    const msg = document.getElementById("searchResultMsg");
    msg.innerText = ""; // Clear previous messages

    if (input === "") {
        msg.innerText = "Please enter a CAS number!";
        return;
    }

    // Get the first table on the page
    const table = document.querySelector("table");
    if (!table) return;

    const rows = table.getElementsByTagName("tr");
    let found = false;

    // Iterate through all data rows (skipping the header at row 0)
    for (let i = 1; i < rows.length; i++) {
        // Reset the background color of all rows
        rows[i].style.backgroundColor = "";
        rows[i].style.transition = "background-color 0.5s ease";

        // The CAS number is in the second column (index 1)
        const casCell = rows[i].getElementsByTagName("td")[1];
        if (casCell) {
            const casText = casCell.innerText || casCell.textContent;
            
            // If a match is found
            if (casText.toLowerCase().includes(input)) {
                // Smoothly scroll to the row and center it
                rows[i].scrollIntoView({ behavior: 'smooth', block: 'center' });
                // Add a highlight background color
                rows[i].style.backgroundColor = "#007A00"; 
                found = true;
                break; // Stop after finding the first match
            }
        }
    }

    if (!found) {
        msg.innerText = "CAS number not found. Please check your input format.";
    }
}

// Bind the Enter key event
document.addEventListener("DOMContentLoaded", function() {
    const inputField = document.getElementById("casSearchInput");
    if (inputField) {
        inputField.addEventListener("keypress", function(event) {
            // Check if the pressed key is Enter
            if (event.key === "Enter") {
                event.preventDefault(); // Prevent default form submission if within a form
                searchCAS();            // Execute the search
            }
        });
    }
});
</script>

| Category | <span style="display: inline-block; width:110px">CAS Number</span> | Description |
| :--- | :--- | :--- |
| **Group IV<br>(PAO Synthetics)** | 68037-01-4 | 1-Decene, homopolymer, hydrogenated |
| | 68649-12-7 | 1-decene Tetramer, Mixed With 1-decene Trimer, hydrogenated |
| | 68649-11-6 | 1-Decene, Dimer, Hydrogenated |
| | 163149-29-9<br>*(and 8002-05-9)* | 1-Decene, Homopolymer, Hydrogenated; Polymer of Octene, Decene, 163149-29-9; (8002-05-9), and Dodecene, Hydrogenated; C8, C12 Olefin Polymer, Hydrogenated |
| | 151006-63-2 | 1-Dodecene, Homopolymer, Hydrogenated |
| | 151006-62-1 | 1-Dodecene, Trimer, Hydrogenated |
| | 151006-60-9 | 1-DODECENE, POLYMER WITH 1-DECENE, HYDROGENATED |
| | 163149-28-8 | 1-DECENE, POLYMER WITH 1-OCTENE AND 1-DODECENE, HYDROGENATED |
| **Group III<br>(GTL Gas-to-Liquid)**| 848301-69-9 | Distillates (Fischer-Tropsch), heavy, C18-50–branched, cyclicand linear |
| | 1262661-88-0| Distillates (Fischer-Tropsch), heavy, C18-50-branched and linear |
| **Group III<br>(VHVI Hydrocracked)** | 64741-89-5 | HIGHLY HYDROTREATED PARAFFINIC BASE OILS |
| | 64742-54-7 | HIGHLY HYDROTREATED PARAFFINIC BASE OILS |
| | 64742-55-8 | HIGHLY HYDROTREATED PARAFFINIC BASE OILS |
| | 64742-70-7 | Paraffin oils (petroleum), catalytic dewaxed heavy |
| | 72623-87-1 | Severely Hydrotreated Paraffinic Hydrocarbons (Oil) |
| | 72623-85-9 | Lubricating oils (petroleum), C20-50, hydrotreated neutral oil-based, high-viscosity |
| | 72623-86-0 | Hydrotreated Neutral Oil-Based |
| | 178603-64-0 | Gas oils, petroleum, vacuum, hydrocracked, hydroisomerized, hydrogenated, C15-30, branched and cyclic, **high viscosity index**; Severely hydrotreated, hydorcracked, hydroisomerized, **high viscosity synthetic iso-alkane** |
| | 178603-65-1 | Gas oils, petroleum, vacuum, hydrocracked, hydroisomerized, hydrogenated, C20-40, branched and cyclic, **high viscosity index** |
| | 178603-66-2 | Gas oils, petroleum, vacuum, hydrocracked, hydroisomerized, hydrogenated, C25-55, branched and cyclic, **high viscosity index** |
| **Group I / II<br>(Mineral Oils)** | 64741-50-0 | Distillates, petroleum, light paraffinic |
| | 64741-50-5 | Distillates(Petroleum), Light Paraffinic |
| | 64741-52-2 | Distillates, petroleum, light naphthenic |
| | 64742-65-0 | Distillates (petroleum), solvent-dewaxed heavy paraffinic |
| | 64742-55-8 | HIGHLY HYDROTREATED PARAFFINIC BASE OILS |
| | 64742-58-1 | Lubricating oils (petroleum), hydrotreated spent |
| | 64742-56-9 | Distillates (petroleum), solvent-dewaxed light paraffinic |
| | 64742-62-7 | Residual oils (petroleum), solvent-dewaxed |
| **Group V<br>(Esters / Others)** | 27178-16-1 | DIISODECYL ADIPATE |
| | 16958-92-2 | ESTER SYNTHETIC BASE OILS |
| | 28472-97-1 | di-isodecyl azelate is a diester basestock |
| | 9003-13-8 | Polyalkylene glycol (PAG) |
| **Anti-wear Additives<br>(ZDTP / ZDDP)** | 68649-42-3 | ZINC DIALKYL DITHIOPHOSPHATE ZDTP |
| | 84605-29-8 | Phosphorodithioic acid, mixed O,O-bis(1,3-dimethylbutyl and iso-Pr) esters, zinc salts |
| **Friction Modifiers<br>(MoDTC / MoDTP)**| 68958-92-7 | Moly Dithiophosphate |
| | 68958-92-9 | molybdenum di(2-ethylhexyl) phosphorodithioate |
| **Antioxidants**| 36878-20-3 | Bis(nonylphenyl)amine |
| | 128-39-2 | 2,6-di-tert-butylphenol |
| **Detergents**| 61789-86-4 | Calcium petroleum sulfonate |
| | 68783-96-0 | Sulfonic acids, petroleum, calcium salts, overbased |
| | 115733-09-0 | Calcium long-chain alkyl phenate sulfide |
| **Dispersants** | No CAS | Polyolefin polyamine succinimide, polyol |
| | 296-404-1<br>*(EC Number)*| PHOSPHORIC ACID ESTERS |
| | 84605-20-9 | Polyisobutylene succinimide (PIBSI) |
| **Viscosity Modifiers<br>(VM)** | 25038-36-2 | Olefin Copolymer |
| | 127883-08-3 | Aryl polyolefin, Ethylene/Propylene |
| **Pour Point Depressants<br>(PPD)** | No CAS | POLY METHYL METHACRYLATE ESTER |
| **Anti-foam**| 63148-62-9 | Polydimethylsiloxane (Silicone oil) |

## References

* [Изучаем состав масла - ПАО Group IV, GTL, Гидрокрекинг - VHVI Group III, минеральное масло Group I; Group II, эстеры итд. Oil-Club.ru](https://www.oil-club.ru/forum/topic/2120-izuchaem-sostav-masla-pao-group-iv-gtl-gidrokreking-vhvi-group-iii-mineralnoe-maslo-group-i-ili-ii-estery-itd/page/31/)
