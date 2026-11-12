---
layout: post
title: "Guía técnica: Principios de las equilibradoras y uniformidad del neumático"
lang: es
date: 2026-11-08 10:20:00
categories: Auto
tags: [Equilibrado de Ruedas, Conocimiento Automotriz, Vibraciones del Chasis, Mantenimiento de Neumáticos]
description: "Análisis exhaustivo de las equilibradoras de neumáticos, el significado de los puntos rojos y amarillos, y la solución definitiva a las vibraciones y desvíos por RFV y LFV."
keywords: "Equilibradora de neumáticos, Equilibrado dinámico, Equilibrado estático, Punto rojo neumático, RFV, LFV, Conicidad, Ply Steer, Road Force, ForceMatch, Uniformidad del neumático, Vibración volante"
image: /images/wheel-balancer.webp
faq:
  - question: "¿Cuál es el principio fundamental de una equilibradora de neumáticos?"
    answer: "Una equilibradora mide las fuerzas centrífugas dinámicas y los momentos de par mediante sensores piezoeléctricos montados en el eje. Junto con un codificador óptico que registra la fase angular, un algoritmo calcula la masa exacta (en gramos) y el ángulo de los contrapesos necesarios en los planos interior y exterior de la llanta."
  - question: "¿Qué significan los puntos rojo y amarillo en un neumático nuevo?"
    answer: "El punto rojo marca el pico del primer armónico de variación de fuerza radial (RFV 1H / punto de mayor rigidez y salto radial). El punto amarillo indica el punto más ligero del neumático. Siempre que exista marca de punto bajo en la llanta, el punto rojo tiene máxima prioridad de alineación frente al amarillo."
  - question: "¿Por qué el coche se desvía lateralmente si la alineación de las ruedas es perfecta?"
    answer: "Suele deberse a fuerzas laterales del neumático. El empuje lateral total es la suma de la Conicidad (CONG, cuya dirección se invierte al dar la vuelta al neumático) y el Ply Steer (PLY, cuya dirección se mantiene invariable). Además, el Par de Autoalineación Residual (RAT) puede torcer el volante o generar resistencias asimétricas de retorno."
  - question: "¿Por qué el coche vibra a 110-120 km/h si las ruedas marcaron 0g/0g en la máquina?"
    answer: "Las equilibradoras estándar giran la rueda en el aire sin carga. No pueden detectar defectos de uniformidad (U/F) bajo el peso del coche. Si la variación de fuerza radial (RFV) es elevada, el neumático se comporta como una leva, botando verticalmente y provocando resonancias intensas en la suspensión."
  - question: "¿Puede una equilibradora convencional solucionar la RFV o la LFV?"
    answer: "No. La RFV y la LFV son problemas de rigidez interna y estructura de lonas. Añadir plomos a la llanta no ablanda la goma dura. Se necesita una equilibradora de carga de carretera (Road Force) con rodillo de presión y optimización ForceMatch."
  - question: "¿Cómo se corrigen en la práctica la RFV y el desvío lateral?"
    answer: "La RFV se diagnostica aplicando unos 500 kg de presión con un rodillo. Se gira el neumático sobre la llanta (ForceMatch) haciendo coincidir el punto bajo geométrico de la llanta con el punto duro del neumático para cancelarse mutuamente. El desvío lateral se neutraliza rotando o invirtiendo los neumáticos de eje."
---
![Equilibradora de neumáticos](/images/wheel-balancer.webp)

Muchos conductores se enfrentan a esta frustrante paradoja: **las ruedas salen de la equilibradora marcando un impecable 0g / 0g, pero al superar los 110 km/h en autopista el volante vibra; la alineación de la dirección está perfecta, pero al soltar el volante el coche se desvía con terquedad hacia un lado.** Para eliminar estas anomalías, es imprescindible comprender la física de la Uniformidad del Neumático (Tire Uniformity, U/F).

## 1. Principio y función de la equilibradora de ruedas
Al rodar a altas velocidades, las mínimas asimetrías de masa se multiplican de forma exponencial por la fuerza centrífuga. La equilibradora está diseñada para anular estas fuerzas dinámicas parásitas.

*   **Eliminación de dos tipos de desequilibrio:**
    *   **Desequilibrio Estático (Salto vertical):** El centro de gravedad no coincide con el eje de giro. La fuerza centrífuga empuja hacia afuera en un solo plano, provocando **botes verticales de la rueda (Hop)**.
    *   **Desequilibrio Dinámico (Bamboleo lateral):** Una distribución de masa asimétrica entre los planos interior y exterior crea un **par de fuerzas (Force Couple)** en rotación, haciendo que la rueda oscile de lado a lado alrededor del pivote de dirección **(Shimmy / Wobble)**.
*   **Sensores y resolución en dos planos:**
    *   **Sensores piezoeléctricos:** Montados en los apoyos del eje, captan deformaciones dinámicas a nivel micrométrico ($$\mu\text{m}$$) y miden la amplitud de las fuerzas alternas.
    *   **Codificador óptico rotatorio:** Monitorea el ángulo del eje con precisión submétrica ($$< 0.5^\circ$$) para ubicar la posición angular exacta del desequilibrio.
    *   **Algoritmo de dos planos:** Resuelve el equilibrio de fuerzas ($$\sum \vec{F} = 0$$) y de momentos ($$\sum \vec{M} = 0$$) para determinar el gramaje exacto de plomo y su posición horaria tanto en el labio interior como en el exterior de la llanta.

## 2. ¿Qué significan el «punto rojo» y el «punto amarillo»?
Las marcas de color en el flanco de los neumáticos nuevos proceden de los ensayos de uniformidad de fábrica y constituyen la primera línea de defensa en el montaje:
![Puntos de color en el flanco del neumático](/images/wheel_dot.webp)
*   **Punto Rojo (RFV 1H / Máxima rigidez y salto radial):**
    *   Indica el punto de mayor rigidez estructural del **primer armónico de variación de fuerza radial (RFV 1H)**, cuya frecuencia de un impacto por vuelta entra en resonancia directa con el chasis.
    *   **Regla de montaje:** Debe alinearse de forma prioritaria con la **marca de punto bajo radial de la llanta (rebaje geométrico)**. La depresión de la llanta neutraliza físicamente el punto más rígido del neumático.
*   **Punto Amarillo (Punto de menor peso):**
    *   Marca el punto más liviano en la circunferencia del neumático.
    *   **Regla de montaje:** Si la llanta carece de marca de punto bajo, alinee el punto amarillo con la **válvula de inflado** (el punto más pesado de la llanta) para reducir el gasto de plomos.
*   **¿Cuál tiene prioridad si entran en conflicto?**
    *   **El punto rojo siempre tiene prioridad absoluta.** El desequilibrio de masa (amarillo) se compensa fácilmente añadiendo contrapesos; sin embargo, una rigidez estructural mal orientada (rojo) no puede solucionarse con plomos.

## 3. Por qué una rueda a 0g aún vibra: RFV, LFV y su solución real
La gran limitación de las equilibradoras convencionales es que hacen girar la rueda **en el aire y sin carga**. Corrigen la masa, pero son **totalmente incapaces de solucionar la RFV y la LFV**.
![RFV y LFV](/images/LFV-RFV.webp)

*   **RFV y RFV 1H (Variación de fuerza radial, cuanto menor, mejor):**
    *   **Causa:** Variaciones de espesor en los empalmes de lonas o disparidad de vulcanización. En el aire el neumático gira redondo, pero con 500 kg de peso encima, la zona más dura no cede y actúa como una leva, generando sacudidas verticales. Los sensores ópticos miden el **RRO (Salto radial geométrico en mm)** para separar fallos de forma de fallos de rigidez interna.
*   **LFV, CONG y PLY (Fuerzas laterales y conicidad, menor / próximo a 0 es mejor):**
    *   **CONG (Conicidad):** El neumático adopta una forma ligeramente cónica, rodando como un vaso de papel. **Dar la vuelta al neumático en la llanta invierte la dirección del empuje** (se neutraliza volteando o rotando ruedas).
    *   **PLY (Ply Steer / Empuje de lonas):** Esfuerzo cortante lateral generado al aplastarse las lonas de acero diagonales contra el suelo. **Dar la vuelta al neumático NO invierte la dirección del empuje**.
    *   **Fuerza lateral resultante:** Dicta hacia dónde derivará el vehículo:
        $$\text{Fuerza Lateral Total} = \text{CONG} + \text{PLY}$$
        *   **Ejemplo práctico:** Un neumático sale de fábrica con $$CONG = +80\text{ N}$$ (hacia la derecha) y $$PLY = +40\text{ N}$$ (hacia la derecha):

            $$\text{Empuje total de fábrica} = (+80\text{ N}) + (+40\text{ N}) = +120\text{ N} \quad (\text{marcado desvío a la derecha})$$

            Si el técnico desmonta el neumático y **lo monta del revés en la llanta**, el valor de CONG se invierte a $$-80\text{ N}$$, pero PLY se mantiene en $$+40\text{ N}$$:

            $$\text{Empuje tras voltear} = (-80\text{ N}) + (+40\text{ N}) = -40\text{ N} \quad (\text{empuje drásticamente reducido, leve deriva izquierda})$$

            ¡La molesta tendencia a desviarse se reduce de inmediato!
    *   **RAT (Par de autoalineación residual):** Desplazamientos del centro de empuje lateral crean un momento torsor sobre el eje de dirección que tuerce el volante o genera resistencias asimétricas al girar.

### Procedimiento profesional para anular RFV y desvíos
1. **Diagnóstico con equilibradora de carga de carretera (Road Force):**
   * Sistemas como Hunter Road Force presionan un rodillo con 500–600 kg sobre la banda de rodadura para medir la RFV y las fuerzas laterales reales.
2. **Optimización de fase ForceMatch (Anulación de RFV):**
   * Se escanean el punto más bajo de la llanta y el punto de mayor rigidez del neumático (punto rojo).
   * Se desinfla el neumático y se gira sobre la llanta el ángulo exacto (ej. 180°), **haciendo que el hueco de la llanta absorba la joroba de rigidez del neumático**.
3. **Distribución inteligente de ruedas contra el desvío:**
   * Conforme a las fuerzas laterales medidas (CONG + PLY), se intercambian las ruedas delanteras entre sí para cancelar el empuje lateral mutuo. Las gomas con menor variación de LFV/RFV se destinan al eje directriz.

## 4. Cinco claves para evaluar la calidad del equilibrado
1. **Estado de conos y adaptadores:** Un cono sucio o golpeado genera 0,1 mm de holgura excéntrica, induciendo de 10 a 15 g de falso desequilibrio.
2. **Limpieza profunda de la llanta:** Eliminar por completo restos de adhesivo antiguo, piedras en las ranuras y condensación de agua en el interior.
3. **Respeto a los puntos rojo y amarillo:** Montar orientando las marcas con criterio en lugar de compensar errores de montaje con exceso de plomo.
4. **Verificación de puesta a cero:** Al terminar de clavar o pegar plomos, es obligatorio bajar la capota y realizar un giro de comprobación en «0g / 0g».
5. **Uso de rodillo de carga en casos rebeldes:** Si la vibración persiste a 110–120 km/h pese a marcar 0g, solicite un servicio ForceMatch con rodillo.

## Conclusión
La lógica de una rodadura perfecta:
1. **Las equilibradoras estándar** solucionan la masa en el aire mediante contrapesos.
2. **El emparejamiento de puntos rojos y amarillos** reduce el salto inicial y el uso de plomos desde el primer minuto.
3. **La RFV y la LFV** son características estructurales y geométricas bajo carga que ningún contrapeso puede eliminar: exigen medición bajo presión y emparejamiento ForceMatch.
