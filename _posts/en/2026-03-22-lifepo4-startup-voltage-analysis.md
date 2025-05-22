---
layout: post
title: "Automotive Starting Voltage Analysis (2.3 NA x LiFePO4 Battery)"
lang: en
date: 2026-03-22 16:00:00
categories: Auto
tags: [Car Maintenance, Automotive Electrical System, LiFePO4 Battery, Empirical Analysis, Circuit Principles]
description: "Breaking the 'starting voltage' myth! Using 100Hz high-frequency empirical data, we dissect the physical performance of a 4-cell LiFePO4 battery during engine startup, and use the V = V0 - (I x R) formula to analyze how battery internal resistance affects voltage drop and alternator charging efficiency."
keywords: "LiFePO4 starter battery, car battery, voltage drop, internal resistance, CCA, starting current, alternator, LiFePO4, voltage drop formula"
image: /images/voltage_record_image.svg
faq:
  - question: "Why does the battery voltage suddenly drop significantly the moment the engine starts?"
    answer: "This is because the starter motor requires an enormous instantaneous current (I) to overcome the engine's static friction. According to the terminal voltage formula $V = V_0 - (I \times R)$, the current passing through the battery's internal physical resistance (R) creates an unavoidable voltage loss."
  - question: "Why does the voltage show a regular sawtooth fluctuation when a four-cylinder engine starts?"
    answer: "Because out of the two pistons pushing upwards, only one is in the 'compression stroke' with both intake and exhaust valves completely closed, creating a massive wall of resistance. The crankshaft encounters extreme compression resistance every 180 degrees of rotation, causing the current drawn by the starter motor to fluctuate accordingly, which in turn forms regular voltage fluctuations."
  - question: "How can I tell if a battery is aging from its voltage after 52,000 kilometers of use?"
    answer: "Mainly observe the 'resting voltage' and the 'starting drop depth'. If the voltage remains above 13.2V after resting for a week (a LiFePO4 characteristic), and the starting voltage drop is kept within 1.2V (indicating low internal resistance), it means the battery's SOH (State of Health) is still excellent."
---

In the study of automotive electrical systems, the starting moment is the phase with the most drastic load changes. Through high-frequency 100Hz millisecond-level voltage sampling, we can observe the physical interaction between the battery and the alternator within an extremely short timeframe. This analysis uses a vehicle equipped with a 4-cylinder 2.3L naturally aspirated engine and a 50Ah GreenRun2 LiFePO4 battery as the observation subject to explore the principles behind the starting voltage curve.

---

## I. Starting Transient Voltage Analysis

[![Voltage Record chart](/images/voltage_record_image.svg)](/images/voltage_record_image.svg)


The starting process can be broken down into four key physical turning points, reflecting the alternation between mechanical load and electrical supply:

### 1. Initial Voltage Drop Caused by Inrush Current
The moment the starter motor's electromagnetic coil closes and the motor begins to rotate from a standstill, a massive **inrush current** is generated.
* **Data Performance:** The voltage drops instantly from a resting state of **13.24V** to **12.07V**.
* **Technical Explanation:** The magnitude of this voltage drop depends on the battery's internal resistance $R$ and the motor's initial impedance. According to the formula:
$$V_{terminal} = V_{ocv} - (I_{start} \times R_{internal})$$
* **Analysis:** Due to its chemical characteristics, a lithium iron phosphate (LiFePO4) battery has extremely low internal resistance. Therefore, under the same starting current $I$, the voltage drop is much smaller than that of a traditional lead-acid battery. This test shows a voltage drop of only about **1.17V**, demonstrating an excellent discharge rate.

### 2. Voltage Fluctuations from the Compression Stroke
While the starter motor is continuously running, the voltage exhibits regular fluctuations between **12.07V and 12.5V**.

* **Technical Explanation:** This is the direct response of the motor overcoming the engine's **compression stroke**.
    * **Trough:** As the piston moves into the compression stroke, the compression resistance is at its peak, the current demand surges, and the voltage drop deepens.
    * **Peak:** As the piston passes top dead center and enters the power or intake stroke, the resistance decreases, power consumption drops, and the voltage recovers.
* **Physical Significance:** The frequency and duration of these fluctuations reflect the speed and efficiency of the starter motor. In this case, ignition is completed in about **0.55 seconds**, indicating a highly efficient starting system.

### 3. Load Dump and Inductive Jump
When the engine successfully ignites and the RPM rises above the starter motor's design limit, the starter motor's one-way clutch disengages and breaks the circuit.
* **Data Performance:** The voltage quickly jumps from **12.64V** to **13.31V** and rapidly stabilizes around **13.30V**.
* **Principle:** This is the **load dump** phenomenon. As a large inductive component, the motor releases residual energy the moment the circuit is broken. Simultaneously, the battery instantly loses hundreds of amps of heavy load, causing the terminal voltage to immediately return near its static platform.

### 4. Excitation Build-up and Alternator Takeover
After the engine starts, system voltage does not immediately spike but briefly stabilizes in the **13.28V – 13.41V** range before rising more noticeably (to **13.69V**).

* **Excitation Build‑Up**: As the alternator begins turning with the engine, the internal voltage regulator requires a short time to establish the rotor’s magnetic field. During this period, the output voltage remains below the battery’s own level, so the system continues to rely primarily on the battery.  

* **Alternator Takeover**: Once the magnetic field is established, the alternator’s output surpasses the battery’s standby voltage. The LiFePO₄ battery, with its very low internal resistance, instantly draws a large charging current, temporarily clamping system voltage around 13.3–13.4V. Because the engine start consumed only about 0.55 seconds of power and the battery was already near full charge, the deficit is replenished within a few seconds. Charging current then drops sharply, the clamp effect is released, and voltage rises smoothly into the steady 13.69V+ recharge zone.  

---

## II. Voltage Balance Observation in Long-Term Operating Voltage

In the continuous monitoring after startup, the voltage performance demonstrates the system's electrical stability:

| Monitoring Phase | Voltage (V) | Technical Status Description |
| :--- | :--- | :--- |
| **Pre-start** | 13.24 | Battery OCV is at a high-potential platform; excellent health. |
| **Initial Start** | 13.69 | Alternator begins output, potential pulled down by LiFePO4 high-current charging. |
| **Steady State** | 13.80 - 13.90 | Enters regulator constant voltage range; extremely low line loss. |

### Technical Summary
1. **Voltage Regulation Logic:** The system ultimately stabilizes in the **13.80V - 13.90V** range. For a LiFePO4 battery, this voltage avoids the high-stress fully charged zone above 14.6V, allowing it to replenish power while extending cell lifespan.
2. **Aging Assessment:** After 3 years and 52,000 kilometers of use, this vehicle's battery still maintains a platform above 12V during the starting moment. Furthermore, maintaining 13.24V before starting after sitting for a week proves that its internal resistance has not significantly increased, indicating a good SOH (State of Health).

---

## III. Energy Density and Discharge Rate

Understanding how LiFePO4 batteries improve starting performance through their physical characteristics:



1. **High Energy Density**
   The energy density of lithium iron phosphate is about 3–5 times that of lead-acid batteries. Within the same volume, it provides lighter weight and more efficient electrode materials. The static voltage stably maintains at **13.2V - 13.3V**, providing a higher initial potential energy during startup.

2. **High Discharge Rate**
   LiFePO4 batteries have low internal resistance and can support a very high C-Rate. Coupled with high density and capacity, they can release massive currents during an instantaneous start with almost no noticeable voltage drop, far outperforming lead-acid batteries that rely on slow chemical diffusion.

---

*The data in this report was collected from a real vehicle, with a sensor precision of 0.01V and a sampling frequency of 100Hz.*
