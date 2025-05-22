---
layout: post
title: "The Physics of Battery Aging: Voltage, Internal Resistance, and Power Loss"
date: 2026-03-30 22:30:00 +0800
categories: Auto
lang: en
image: /images/battery-symbol.webp
tags: [Battery Aging, Internal Resistance, Equivalent Circuit, Lithium-ion Battery, Lead-acid Battery]
description: "An in-depth look at the physical truth behind battery aging. Through the equivalent circuit model and Ohm's law, we analyze how a surge in internal resistance causes abnormal heating during charging, falsely high terminal voltage, and voltage collapse during discharge. This article provides simple formula examples to help you understand the scientific principles and safety assessments of why lithium and lead-acid batteries 'won't fully charge and drain fast'."
keywords: "causes of battery aging, internal resistance increase, equivalent circuit, lithium battery lifespan, lead-acid battery maintenance, voltage drop calculation, power loss formula, battery heating principle, internal impedance, battery health check"
math: true
faq:
  - question: "Why do batteries seem to age faster in cold weather?"
    answer: "Low temperatures increase the viscosity of the electrolyte, causing a temporary spike in internal resistance $$R$$. According to $$V_{measured} = V_{ocv} - (I \times R)$$, the increased voltage drop causes the device to detect a voltage that falls below the shutdown threshold prematurely."
  - question: "Does fast charging accelerate the increase in battery internal resistance?"
    answer: "Yes. The high current of fast charging generates square-fold waste heat ($$P = I^2 R$$). High temperatures accelerate internal chemical side reactions, creating non-conductive substances that cover the plates, leading to a permanent increase in internal resistance."
  - question: "Why does the battery drain so fast if I unplug it right after it hits 100%?"
    answer: "When $$R$$ is extremely high, the charging voltage is falsely elevated. Once the current $$I$$ stops, the voltage drop $$(I \times R)$$ disappears, and the terminal voltage immediately falls back to the true $$V_{ocv}$$, causing the percentage to dive instantly."
  - question: "Do the battery repair devices on the market actually work?"
    answer: "They have a weak de-crystallization effect on lead-acid batteries, but are ineffective against the structural aging of lithium batteries. Moreover, aged batteries have high internal resistance; forcibly repairing them can easily trigger safety risks due to poor heat dissipation."
---

Whether it's a lithium-ion or lead-acid battery, the most obvious characteristic of aging is **"charging quickly but dying instantly,"** accompanied by severe heating. To understand these phenomena, we must start with the battery's **internal resistance** and the equivalent circuit model.

## 1. The Equivalent Circuit Model of a Battery

![Battery Symbol](/images/battery-symbol.webp)

In physics, a battery is not a single energy storage component. Its equivalent circuit consists of two core parts connected in series:

* **Chemical Electromotive Force ($$V_{ocv}$$)**: The voltage observed at the battery terminals under open-circuit conditions, with no load and no current flow..
* **Internal Resistance ($$R$$)**: The physical obstruction generated when current flows through the plates, the electrolyte, and the separator.

---

*(Translator's note: Retaining your transitional note from the draft!)*
This is a great suggestion! Adding the concept of **"power distribution"** allows readers to see at a glance why aging batteries charge slowly—because most of the electricity is wasted as "heat."

Here is the optimized paragraph, integrating this energy formula:

---

## 2. The Charging Phenomenon After Aging: Why Does It Get Hotter the More You Charge?

When we use a charger to charge a battery, the total power output by the charger ($$P_{total}$$) is broken down into two parts:
$$P_{total} (V \times I) = P_{heat} (\text{wasted heat}) + P_{charge} (\text{actual power stored})$$

### 2.1 The Vertical Dive of Energy Efficiency
Let's assume we use a 5V / 2A (total power 10W) charger. Let's compare the energy conversion of a new vs. old battery:

| Battery State | Internal Resistance ($$R$$) | Heating Power ($$I^2 R$$) | Actual Charging Power | Efficiency |
| :--- | :--- | :--- | :--- | :--- |
| **New Battery** | $$0.1 \Omega$$ | $$2^2 \times 0.1 = \mathbf{0.4W}$$ | $$10 - 0.4 = \mathbf{9.6W}$$ | **96%** (Extremely High) |
| **Old Battery** | $$1.5 \Omega$$ | $$2^2 \times 1.5 = \mathbf{6.0W}$$ | $$10 - 6.0 = \mathbf{4.0W}$$ | **40%** (Extremely Low) |

**Stop and think:** In the old battery, over half of the power is consumed by the internal resistance $R$ and turns into waste heat. This is why an old battery feels like a "hand warmer" when charging, and the charging speed feels slower—because the power actually stored as chemical energy is less than half.

---

### 2.2 Voltage Deception: The Key to False Full Charges
The charger detects the **terminal voltage**:
$$V_{measured} = V_{ocv} + (I \times R)$$

* **The Illusion of an Old Battery**: Because $$R$$ is large, when a 2A current flows through, the resulting voltage drop $$(I \times R)$$ can be as high as 2V or more.
* **The Result**: As soon as the charger is connected, it detects the terminal voltage instantly soaring to 4.2V (the full charge threshold), immediately determines it is "fully charged," and turns green or reduces the current. But in reality, the internal true storage $$V_{ocv}$$ might still be at a very low power level.

This perfectly explains why an aging battery always **"fills up instantly"**—it's an illusion caused by the voltage being falsely pulled up by internal resistance.

---

## 3. Voltage Collapse During Discharge: The Culprit Behind Power Outages

When a device draws current, the formula reverses:
$$V_{measured} = V_{ocv} - (I \times R)$$

**A Real-life Example:**
Your phone detects that if the voltage drops below 3.3V, it will automatically shut down. Assume the battery still has a residual voltage of 3.7V:

* **New Battery ($$R=0.1$$)**: When playing a game and drawing a large current of 2A, the voltage drops to $$3.7 - 0.2 = \mathbf{3.5V}$$ → **Continues to run smoothly**.
* **Old Battery ($$R=0.5$$)**: Drawing the same large current of 2A, the voltage drops to $$3.7 - 1.0 = \mathbf{2.7V}$$ → **Falls below the threshold, and the phone instantly goes black**.

This is why an old phone shows 20% battery left, but as soon as you open the camera or play a game, it crashes and shuts down due to the massive instantaneous voltage drop.

---

## Conclusion: Aging is an Irreversible "Blockage"

If you compare a battery to a **water tower**, internal resistance is like **rust and blockage in the outlet pipe**:
* **When charging**: The pipe is clogged, so the water pressure (voltage) maxes out quickly, making you think it's full, but water isn't actually flowing in.
* **When discharging**: You want to use water, but the pipe blockage (internal resistance) is too large; the amount of water coming out is a trickle and can't meet the immediate demand.

This increase in impedance caused by physical materials (plate crystallization, electrolyte degradation) is irreversible. Timely replacement of the battery is the only solution to ensure equipment safety and a stable power supply.

> **💡 Advanced Concept: Did you know internal resistance is divided into "AC" and "DC"?**
>
> If you check a battery's spec sheet, you'll often see two different internal resistance ratings. To avoid overcomplicating the physics, we can break it down simply:
> 
> * **AC Internal Resistance (ACIR):** Instruments typically measure this by injecting a weak 1kHz alternating current. It only captures pure physical resistance (like contact points and electrolyte conductivity). Because the test is so brief, chemical reactions don't have time to occur. As a result, the measured values look very appealing (very low). Almost 100% of handheld testers on the market measure ACIR.
> 
> * **DC Internal Resistance (DCIR):** This is measured by actually connecting a load and continuously drawing a large direct current. In this state, the initial physical resistance is combined with "polarization resistance"—caused by the battery's chemical reactions struggling to keep up with the power demand. This number will be much higher than ACIR, but it represents the **actual, real-world resistance** your phone or car experiences.
> 
> *Note: To accurately reflect real-world usage scenarios, the voltage drop and heat generation formulas discussed in this article are all based on DC Internal Resistance (DCIR).*

