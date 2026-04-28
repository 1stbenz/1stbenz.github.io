---
layout: post
title: "The Fatal Flaws of LTO in Automotive Use: Why 5S Overcharges and 6S Undercharges"
lang: en
date:   2025-06-12 10:00:29
categories: Auto
tags: [Lithium Titanate, LTO, Car Battery, Battery Modification, 5-Series, 6-Series, DIY, Voltage Matching]
description: "Thinking about modifying with a Lithium Titanate (LTO) battery? Understand the hard truths of voltage matching first. This article analyzes why a car alternator's 14V output causes long-term overcharge damage to 5S LTOs, leaves 6S LTOs with only 30% capacity, and debunks the myth of high CCA data in commercial LTO batteries."
keywords: "Lithium Titanate, LTO, SCiB, 5S, 6S, Voltage Mismatch, Overcharge, Car Modification, Lithium Battery, Toshiba"
image: /images/mobile01-73a3f73994754009670d4e7b1e13c046.webp
faq:
  - question: "What is the charging voltage range of a car alternator?"
    answer: "Most car and motorcycle alternators output approximately 13.5V to 14.4V when operating, designed for float charging or recharging lead-acid batteries."
  - question: "Why is a 5-series (5S) LTO battery unsuitable for car alternator charging?"
    answer: "The recommended full charge voltage for a 5S LTO battery is about 13.5V (2.7V per cell). When the alternator outputs 13.5V–14.4V, each cell reaches 2.7V–2.88V, meaning it constantly overcharges while driving. Long-term overvoltage charging leads to capacity degradation, increased internal resistance, gas swelling, and structural deformation."
  - question: "Why is a 6-series (6S) LTO battery unsuitable for car alternator charging?"
    answer: "The recommended full charge voltage for a 6S LTO battery is about 16.2V (2.7V per cell). However, the alternator maxes out at 14.4V (2.4V per cell), far below the recommended charging voltage. This prevents the battery from fully charging, potentially leaving only 30% usable capacity and aggravating polarization."
  - question: "Are the extremely high CCA readings of LTO batteries real?"
    answer: "No. Toshiba's official LTO specification sheet shows a discharge rate of only 20C. Furthermore, the internal resistance of a lithium battery does not equate to its discharge capability, making CCA tester measurements meaningless for lithium batteries."
  - question: "Besides voltage matching issues, what are the hidden flaws of LTO batteries?"
    answer: "LTO batteries have low energy density; their capacity is less than half that of a Lithium Iron Phosphate (LiFePO4) battery of the same volume. Low capacity means a higher consumption ratio per cycle, leading to faster cycle wear. Additionally, many commercial LTO batteries use salvaged/scrapped cells, meaning their actual lifespan is often worse than LiFePO4 batteries."
  - question: "What should car owners pay attention to when choosing an LTO battery as a starter battery?"
    answer: "Owners must ensure the battery's series count matches the car alternator's charging voltage and should demand the manufacturer provide detailed cell specification sheets to verify performance and safety information."
---

## The Core Issue: Car Alternator Charging Voltage

Most car and motorcycle alternators output a voltage around 13.5V to 14.4V when operating, which is intended for float charging or recharging lead-acid batteries.

---

## LTO Series Count vs. Voltage Matching

| Series Count | Nominal Voltage | Recommended Full Charge Voltage | Operating Voltage Range | Result |
|------|-----------|----------------|----------------|------|
| 5S | 11.5–12V | Approx. 13.5V (2.7V/cell) | 10V–13.5V | **Constant Overcharge** (Alternator voltage too high) |
| 6S | 13.8–14.4V | Approx. 16.2V (2.7V/cell) | 12V–16.2V | **Undercharged, low capacity** (Alternator voltage insufficient) |

<br>

---

## Why Do 5-Series (5S) Overcharge?

* The alternator outputs 13.5V–14.4V, divided by 5 cells = 2.7V–2.88V per cell.
* The minimum 13.5V already hits the **upper voltage limit**, resulting in **continuous overcharging** while driving.
* Long-term overvoltage charging leads to:
  * Capacity degradation.
  * Increased internal resistance.
  * Gas swelling and structural deformation.
* If a seller claims it can be charged above 2.7V, be sure to ask them for the **cell specification sheet** as proof.

---

## Why Do 6-Series (6S) Undercharge?

* The alternator maxes out at an output of 14.4V, divided by 6 cells = 2.4V per cell.
* 2.4V is only the **nominal voltage**, far below the recommended 2.7V for charging.
* The essence of charging is "using an external power source to reverse a chemical reaction," which requires applying a voltage higher than the battery's natural output.
* If the voltage isn't high enough, there isn't enough pushing force to change the battery's internal chemical state.

### Results may cause:

* [**Usable capacity drops to only 30% ⬇️**](/images/mobile01-f1b4345d1112dee159b1baa62a8da6ef.webp)
* Aggravated polarization phenomenon.

---

## The LTO CCA Readings are Super High, Are They Real?

* ❌ False:
  * [Toshiba LTO official spec sheet](https://www.global.toshiba/ww/products-solutions/battery/scib/product-next/product/cell/high-energy.html): The discharge rate is only 20C.
  * The internal resistance of a lithium battery does not equal its discharge capability.
  * Reference: [Why measuring CCA for lithium batteries is meaningless](/2025/about-cca.html).

---

## Hidden Trap: Low Capacity Leads to High Cycle Wear

* **Low energy density**: At the same volume, LTO capacity is less than half that of a Lithium Iron Phosphate (LiFePO4) battery.
* **Fast cycle wear**: Because the capacity is small, the consumption ratio per cycle is high, doubling the lifespan degradation.
* **Worse in reality**: Most LTO batteries on the market use salvaged/scrapped cells, further reducing their lifespan.

LTO is advertised as having a high cycle count, but due to its low capacity, high discharge ratio, and the fact that most commercial units use salvaged cells, its actual lifespan is often worse than LiFePO4.

---
## Comparison of Common Batteries in the Market

<style>
    /* RWD Responsive Scrolling Container */
    .table-responsive {
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch; /* Smooth scrolling for iOS */
        margin-bottom: 20px;
    }
    
    .battery-table {
        border-collapse: collapse;
        width: 100%;
        min-width: 500px; /* Ensures text doesn't crowd on mobile screens */
        max-width: 600px;
        font-family: sans-serif;
        font-size: 16px;
    }
    
    .battery-table th, .battery-table td {
        border: 1px solid #b3c6e7; /* Soft border matching the header color */
        padding: 10px 15px;
        text-align: left;
        vertical-align: top;
        line-height: 1.5;
    }
    
    /* Header coloring (Cornflower blue referencing original theme) */
    .battery-table th {
        font-weight: bold;
        text-align: center;
        background-color: #6495ED; /* Header background */
        color: #ffffff; /* Header text: White for contrast */
    }
    
    /* Alternating row colors (Zebra striping) */
    .battery-table tbody tr:nth-child(even) {
        background-color: #f2f7ff; /* Even rows: Very light blue */
    }
    .battery-table tbody tr:nth-child(odd) {
        background-color: #ffffff; /* Odd rows: White */
    }
    
    /* Hover effect */
    .battery-table tbody tr:hover {
        background-color: #e6f0ff;
    }
</style>

<div class="table-responsive">
    <table class="battery-table">
        <thead>
            <tr>
                <th>Size LN3</th>
                <th>Lead-Acid</th>
                <th>LTO (Lithium Titanate)</th>
                <th>LiFePO4</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Capacity</td>
                <td>70Ah</td>
                <td><span style="color: red;">46Ah</span></td>
                <td><b>100Ah</b></td>
            </tr>
            <tr>
                <td>Charge Efficiency</td>
                <td>7A (0.1C)</td>
                <td><b>920A (20C)</b></td>
                <td>200A (2C)</td>
            </tr>
            <tr>
                <td>Discharge Efficiency</td>
                <td>10C</td>
                <td>20C</td>
                <td><b>50-80C</b></td>
            </tr>
            <tr>
                <td>Voltage Tolerance</td>
                <td>16.2V</td>
                <td><span style="color: red;">13.5V (5S)</span></td>
                <td>14.6V</td>
            </tr>
            <tr>
                <td>Cycle Life</td>
                <td>1000 times</td>
                <td>
                    Ideal 20,000 times<br>
                    x Capacity 0.46<br>
                    <span style="color: red;">x Used wear 0.7</span><br>
                    <span style="color: red;">x Chronic overcharge 0.7</span><br>
                    = <b>4,500 times</b>
                </td>
                <td>5000 times</td>
            </tr>
            <tr>
                <td>Cell Condition</td>
                <td>Brand New</td>
                <td><span style="color: red;">Mostly Salvaged/Used</span></td>
                <td>Brand New</td>
            </tr>
            <tr>
                <td>Manufacturer</td>
                <td>Regular Factory</td>
                <td><span style="color: red;">Mostly Underground Factories</span></td>
                <td>Regular Factory</td>
            </tr>
            <tr>
                <td>Price</td>
                <td>Low</td>
                <td><span style="color: red;">High</span></td>
                <td>Medium</td>
            </tr>
            <tr>
                <td colspan="4">
                    Euro Car Alternator: <b>190A</b><br>
                    Japanese Car Alternator: <b>120A</b>
                </td>
            </tr>
        </tbody>
    </table>
</div>

---

> Recommendation: If you are choosing a Lithium Titanate battery as a car starter, please make absolutely sure the series count matches the charging voltage, and require the manufacturer to provide the cell specification sheet.