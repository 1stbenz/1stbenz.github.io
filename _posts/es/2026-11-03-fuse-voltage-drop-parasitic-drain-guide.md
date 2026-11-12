---
layout: post
title: "Prueba de fuga de batería (Caída de tensión): Localizar consumo parásito sin quitar fusibles con multímetro y Fuse Voltage Drop Chart"
lang: es
date: 2026-11-03 10:00:00
categories: Auto
tags: [Electricidad del Automóvil, Reparación de Autos, Guía DIY, Corriente Parásita, Caída de Tensión, Prueba de Fusibles, Descarga de Batería]
related_posts:
  - 2026-11-01-parasitic-drain-tester-guide.md
  - 2026-11-02-dc-clamp-meter-parasitic-drain-guide.md
  - 2025-09-17-memory-saving-battery.md
description: "¿Aún quitas fusibles uno a uno para buscar consumos parásitos? En vehículos modernos con CAN-Bus, esto despierta las centralitas y arruina el diagnóstico. Aprende a medir la microcaída de tensión en milivoltios (mV) para localizar fugas en 2 minutos sin extraer fusibles."
keywords: "caída de tensión en fusibles, Fuse Voltage Drop Chart, corriente parásita auto, fuga de batería auto, medir fuga sin quitar fusibles, multímetro mV, Power Probe tabla fusibles, consumo en reposo"
image: /images/FuseVoltageMethod.webp
faq:
  - question: "¿Qué es el método de caída de tensión en fusibles (Fuse Voltage Drop)?"
    answer: "Cada fusible automotriz de cuchilla posee una resistencia interna diminuta y fija (en miliohmios, mΩ). Según la Ley de Ohm (V = I × R), cualquier corriente que pase por el fusible genera una microcaída de tensión en milivoltios (mV) en sus puntos de prueba. Al medir este valor en mV y consultar una tabla, se obtiene la corriente exacta sin desconectar el circuito."
  - question: "¿Por qué es mejor que quitar los fusibles uno por uno?"
    answer: "Los autos modernos utilizan redes de comunicación (CAN-Bus / LIN-Bus). Al retirar un fusible, se corta la alimentación de un módulo, lo que activa las alarmas de la red y despierta a todas las centralitas que estaban dormidas. Al volver a colocarlo, hay que esperar otros 15 a 45 minutos para que el vehículo vuelva al reposo. La caída de tensión no interrumpe la corriente ni despierta la electrónica."
  - question: "¿Es normal obtener lecturas negativas (ej. -0.5 mV)?"
    answer: "Es completamente normal. El signo negativo solo indica la polaridad con la que se apoyaron las puntas del multímetro. Los fusibles no tienen polaridad; simplemente ignore el signo negativo y tome el valor absoluto (0.5 mV) para buscarlo en la tabla."
---

![Medir microcaída de tensión en fusibles de auto](/images/FuseVoltageMethod.webp)

Cuando un auto descarga la batería tras pocos días sin uso, el método tradicional de ir quitando fusibles uno por uno suele convertirse en una trampa. En vehículos modernos con redes CAN-Bus, quitar un fusible **despierta inmediatamente las centralitas en reposo**, disparando el consumo y arruinando la prueba.

El **método de caída de tensión en fusibles (Fuse Voltage Drop)** es la técnica de referencia de los profesionales: **sin quitar fusibles, sin cortes de energía y sin despertar las centralitas**. Con un multímetro digital común en escala de milivoltios, es posible escanear toda la fusilera en menos de dos minutos.

> **Navegación de la serie:**
> - Para medir la corriente parásita total: [Guía con interruptor bypass](/es/2026/parasitic-drain-tester-guide.html) | [Guía con pinza amperimétrica DC](/es/2026/dc-clamp-meter-parasitic-drain-guide.html)

---

## Principio fundamental: Ley de Ohm $$V = I \times R$$

Los fusibles de cuchilla no tienen resistencia cero. Su elemento metálico fusible posee una resistencia interna pequeña, calibrada y conocida (generalmente entre 2mΩ y 30mΩ).

Según la **Ley de Ohm**:

$$V = I \times R \quad \Longrightarrow \quad I = \frac{V}{R}$$

- $$R$$ (Resistencia interna del fusible): Fija y conocida según el tipo y amperaje.
- $$V$$ (Caída de tensión): Diferencia de potencial en milivoltios ($$mV$$) entre los puntos de prueba.
- $$I$$ (Corriente parásita): Intensidad real que atraviesa el circuito en miliamperios ($$mA$$).

En la parte superior de cada fusible hay **dos pequeños puntos de prueba metálicos al descubierto**. Al medir los milivoltios ($$mV$$) entre ambos puntos, se determina de inmediato si el circuito consume energía:
- **`0.0 mV`** → No pasa corriente; el circuito está completamente dormido.
- **Lectura numérica (ej. `0.6 mV`)** → Hay corriente circulando; la tabla indica los miliamperios exactos.

---

## Herramientas necesarias

![Puntas finas tipo aguja para multímetro](/images/sharppoint.webp)

1. **Multímetro digital**: En escala **DC mV (milivoltios corriente continua)** (resolución de 0.1 mV o 0.01 mV).
2. **Puntas finas tipo aguja (imprescindibles)**: Las puntas gruesas convencionales no entran en los orificios del fusible. Se requieren agujas de 0.7mm–1.0mm que perforen la capa de óxido superficial.
3. **Tabla de conversión**: Las tablas incluidas más abajo.

---

## Procedimiento paso a paso

### Paso 1: Preparación y espera del reposo (Sleep Mode)
1. Apagar el motor, apagar luces y accesorios, y **bajar completamente todas las ventanillas** (para evitar bloqueos accidentales).
2. Dejar accesibles las fusileras y **bloquear manualmente con un destornillador las cerraduras de puertas, capó y maletero** para simular que están cerrados.
3. Bloquear el auto con el control remoto y **alejar la llave inteligente a más de 5 metros**.
4. **Esperar de 15 a 45 minutos** hasta que todas las centralitas (ECU, BCM, gateway) entren en sueño profundo.

---

### Paso 2: Ajuste del multímetro y medición
1. Conectar la punta roja en **V/Ω/mV** y la negra en **COM**.
2. Girar el selector a **DC mV**.
3. Apoyar con firmeza ambas agujas en los **dos puntos metálicos superiores del fusible**, presionando levemente para perforar el óxido.
4. Leer la pantalla:
   - **`0.0 mV`**: Sin consumo. Pasar de inmediato al siguiente fusible.
   - **Lectura numérica (ej. `0.6 mV`)**: ¡Circuito con fuga detectado! Anotar tipo de fusible (Mini o Estándar/ATO), amperaje (ej. 10A rojo) y valor en mV.

> **¿Lectura en negativo (ej. -0.5 mV)?**  
> El signo solo indica la polaridad con que se apoyaron las puntas. Los fusibles no tienen polaridad; **utilice el valor absoluto (`0.5 mV`)** para consultar la tabla.

---

## Tablas de conversión de caída de tensión

Con el valor en mV registrado, consulte las siguientes tablas para conocer el consumo en miliamperios (mA):

### 1. Fusibles Mini (ATM) - Tabla de caída de tensión (Unidad: mA)

| Amperaje | Resistencia aprox. | 0.2 mV | 0.4 mV | 0.6 mV | 0.8 mV | 1.0 mV | 1.5 mV | 2.0 mV |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **5A (Beige)** | ~15.2 mΩ | 13 mA | 26 mA | 39 mA | 53 mA | **66 mA** | 99 mA | 132 mA |
| **7.5A (Marrón)** | ~10.1 mΩ | 20 mA | 40 mA | 59 mA | 79 mA | **99 mA** | 149 mA | 198 mA |
| **10A (Rojo)** | ~7.1 mΩ | 28 mA | 56 mA | 85 mA | 113 mA | **141 mA** | 211 mA | 282 mA |
| **15A (Azul)** | ~4.6 mΩ | 43 mA | 87 mA | 130 mA | 174 mA | **217 mA** | 326 mA | 435 mA |
| **20A (Amarillo)** | ~3.3 mΩ | 61 mA | 121 mA | 182 mA | 242 mA | **303 mA** | 455 mA | 606 mA |
| **25A (Blanco/Transp)**| ~2.5 mΩ | 80 mA | 160 mA | 240 mA | 320 mA | **400 mA** | 600 mA | 800 mA |
| **30A (Verde)** | ~2.0 mΩ | 100 mA | 200 mA | 300 mA | 400 mA | **500 mA** | 750 mA | 1000 mA|

---

### 2. Fusibles Estándar (ATO / ATC) - Tabla de caída de tensión (Unidad: mA)

| Amperaje | Resistencia aprox. | 0.2 mV | 0.4 mV | 0.6 mV | 0.8 mV | 1.0 mV | 1.5 mV | 2.0 mV |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **5A (Beige)** | ~17.8 mΩ | 11 mA | 22 mA | 34 mA | 45 mA | **56 mA** | 84 mA | 112 mA |
| **7.5A (Marrón)** | ~10.9 mΩ | 18 mA | 37 mA | 55 mA | 73 mA | **92 mA** | 138 mA | 183 mA |
| **10A (Rojo)** | ~7.4 mΩ | 27 mA | 54 mA | 81 mA | 108 mA | **135 mA** | 203 mA | 270 mA |
| **15A (Azul)** | ~4.8 mΩ | 42 mA | 83 mA | 125 mA | 167 mA | **208 mA** | 313 mA | 417 mA |
| **20A (Amarillo)** | ~3.4 mΩ | 59 mA | 118 mA | 176 mA | 235 mA | **294 mA** | 441 mA | 588 mA |
| **25A (Blanco/Transp)**| ~2.6 mΩ | 77 mA | 154 mA | 231 mA | 308 mA | **385 mA** | 577 mA | 769 mA |
| **30A (Verde)** | ~2.1 mΩ | 95 mA | 190 mA | 286 mA | 381 mA | **476 mA** | 714 mA | 952 mA |

> **Cálculo mental rápido (Fusible Mini 10A común):**  
> **Cada 0.1 mV de caída equivale aproximadamente a 14 mA de corriente parásita.** Una lectura de `0.5 mV` representa unos $$0.5 \times 14 = 70\text{ mA}$$.

---

## Identificar y aislar el componente defectuoso

Una vez localizado el fusible con caída de tensión, **siga sin retirarlo**:

1. **Consultar el manual**: Identificar qué componentes alimenta ese fusible (ej. radio, cámara de bordo, centralita de confort, luces interiores).
2. **Desconectar el componente**: Desconectar el conector eléctrico directamente en el aparato sospechoso (no en la fusilera).
3. **Volver a medir el fusible**: Si la lectura cae inmediatamente de `1.2 mV` a **`0.0 mV`**, ¡el componente averiado queda confirmado!

---

## Resumen del proceso de diagnóstico

* **Paso 1 (Comprobación total)**: Medir con pinza amperimétrica DC en el cable de masa de la batería para confirmar si hay fuga (< 50mA es normal).
* **Paso 2 (Alternador)**: Medir el cable B+ del alternador para descartar diodos rectificadores en cortocircuito.
* **Paso 3 (Localización exacta)**: Medir los fusibles con multímetro en **DC mV** y consultar la tabla para localizar el circuito culpable en 2 minutos sin despertar el vehículo.
