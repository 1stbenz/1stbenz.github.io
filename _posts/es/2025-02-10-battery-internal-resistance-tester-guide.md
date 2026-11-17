---
layout: post
title: "¿Cómo interpretar un comprobador simple de resistencia interna? Mitos sobre el CCA y el valor de referencia"
lang: es
date: 2025-02-10 09:40:00
categories: Auto
tags: [Batería de coche, Conocimiento de coche]
description: "¿Son fiables el CCA y el SOH de un comprobador portátil de resistencia interna? Aprende cómo funcionan en baterías de plomo-ácido, qué cambia el valor de referencia, el impacto del voltaje y cómo medir correctamente."
keywords: "Comprobador resistencia interna batería, Medidor de conductancia, CCA, SOH, Salud de batería, Resistencia interna, Valor de referencia, Mantenimiento automotriz"
image: /images/batterytool01.webp
math: true
faq:
  - question: "¿El CCA que muestra un comprobador simple es la corriente real de arranque en frío?"
    answer: "No. Estos equipos no realizan una descarga de alta corriente; solo miden el voltaje en reposo y, mediante una señal débil (conductancia CA o pequeño pulso), la resistencia interna. El CCA y el SOH son estimaciones basadas en fórmulas empíricas para baterías de plomo-ácido."
  - question: "¿Cambiar el valor de referencia de CCA (p. ej., 415 o 500) afecta la medición real?"
    answer: "Bajo el mismo estándar y tipo de batería, no modifica la resistencia interna medida ni el CCA estimado, pero sí altera el porcentaje SOH (lineal o cuadrático según la marca) y el veredicto Bueno/Reemplazar. Cambiar de estándar o tipo de batería puede variar el cálculo en algunos equipos."
  - question: "¿Por qué varían las lecturas de resistencia interna o CCA de la misma batería en distintos momentos?"
    answer: "La temperatura, el estado de carga y voltaje en reposo (recién cargada, recién conducida o descargada), así como el punto donde sujetan las pinzas influyen directamente en la lectura."
  - question: "¿Cuál es la forma más útil de usar un comprobador simple de resistencia interna?"
    answer: "Cargar completamente la batería, dejarla reposar, sujetar directamente los bornes de plomo y usar siempre el mismo equipo para seguir la tendencia al alza de la resistencia interna (mΩ)."
  - question: "¿Se puede comparar la resistencia interna entre distintas marcas o modelos de baterías?"
    answer: "No tiene sentido. Cada marca, diseño de placas y tiempo de almacenaje tiene una resistencia base distinta. Compara primero contra la referencia de esa misma batería cuando era nueva (cargada y en reposo), o bien contra el rango de fábrica de un modelo nuevo idéntico."
  - question: "¿Cuál es la resistencia interna normal de una batería de coche? ¿Existe un estándar único?"
    answer: "No hay un umbral universal. A mayor capacidad y superficie de placas, menor resistencia interna; evalúa el desgaste comparando contra su referencia de nueva o el rango de un modelo nuevo de la misma marca."
  - question: "¿Es fiable medir justo después de apagar el motor o terminar de cargar?"
    answer: "Los datos suelen distorsionarse. Recién apagado, la carga superficial y el calor dan lecturas optimistas y menor resistencia; recién desconectado del cargador, la polarización y microburbujas pueden hacer oscilar la resistencia. Conviene esperar a que repose."
  - question: "¿Es preciso el comprobador si el voltaje de la batería es bajo (inferior a 12,5 V)?"
    answer: "El error aumenta y tiende a ser pesimista. Por debajo de ~12,4 V–12,5 V (mayor umbral en AGM) hay falta de carga: baja la densidad del electrolito y se forma sulfato de plomo reversible que eleva temporalmente la resistencia, pudiendo dar un falso reemplazo. Carga al 100 % y reposa antes de medir."
  - question: "¿Sirve un comprobador simple para baterías de litio LiFePO4?"
    answer: "No aplica para su lectura de CCA y SOH. La lógica comercial de CCA es solo para plomo-ácido y además sufre interferencias del BMS integrado en baterías LiFePO4 (emparejar celdas de litio por mΩ requiere un medidor dedicado de resistencia interna CA)."
---

![Comprobador simple de resistencia interna de batería](/images/batterytool01.webp)

Muchos juzgan la salud de una batería por el CCA y el SOH que marca un comprobador de resistencia interna, pero casi siempre son «valores estimados». Si entiendes la lógica y los límites aplicados a las baterías tradicionales de plomo-ácido, interpretarás los datos con criterio (sobre por qué no aplica el CCA al litio, consulta **[Sobre la inutilidad de medir el CCA en las baterías de iones de litio](/es/2025/about-cca.html)**).

## 1. ¿Qué mide realmente un comprobador simple?
Estos equipos electrónicos no hacen una descarga real de cientos de amperios: únicamente miden el **voltaje en reposo (V)** y, mediante una señal débil (conductancia CA o pequeño pulso), la **resistencia interna (mΩ)**.

En baterías tradicionales de plomo-ácido, el **SOC (%)** se estima principalmente por el voltaje en reposo, mientras que el **CCA estimado** y el **SOH (%)** se calculan a partir de la resistencia interna con fórmulas empíricas (similar a una báscula de bioimpedancia). Sirve para **detección rápida y seguimiento de tendencias**, no como prueba de carga real, y pierde validez fuera de la química plomo-ácido.

## 2. ¿Importa qué valor de referencia se configure?
Bajo un **mismo estándar de prueba (p. ej., CCA) y tipo de batería**, ajustar la referencia **no altera la resistencia interna medida (mΩ) ni el CCA estimado**; solo cambia el **porcentaje SOH** y el dictamen en pantalla:

$$\text{SOH (\%)} \approx \frac{\text{CCA estimado}}{\text{Referencia ingresada}} \times 100\%$$

La fórmula exacta varía según la marca (algunas usan proporción lineal, otras cuadrática como $$(400/500)^2 = 64\%$$, con tope habitual en `100%`; cambiar de norma o de batería líquida a AGM puede alterar el cálculo en ciertos modelos). Lo importante no es poner 400 o 500, sino **mantener el mismo ajuste para seguir la evolución**.

## 3. ¿Por qué cambian los valores de una misma batería?
Además de la tolerancia del equipo, cuatro condiciones alteran las lecturas:
* **Motor recién apagado o recién cargada:** La carga superficial y el calor suelen hacer que el SOC parezca optimista y baje la resistencia; recién terminada la carga, la polarización y microburbujas pueden hacer variar la resistencia.
* **Baja carga (por debajo de ~12,4 V–12,5 V):** La falta de carga (umbral mayor en AGM) eleva temporalmente la resistencia y facilita confundir «descargada» con «agotada».
* **Temperatura ambiente:** Las reacciones químicas dependen mucho de la temperatura, generando diferencias claras entre verano e invierno.
* **Resistencia de contacto:** La limpieza de las pinzas y su agarre firme al borne de plomo afectan directamente al valor en `mΩ`.

## 4. ¿Una resistencia alta significa mala batería?
No necesariamente (**Nota: válido solo para plomo-ácido; la lógica de CCA es [totalmente inaplicable](/es/2025/about-cca.html) a baterías que no son de plomo**). Las diferencias entre marcas del mismo formato suelen deberse a compromisos técnicos y de almacenaje:
* **Placas y densidad del ácido:** Más placas delgadas o mayor densidad mejoran las cifras iniciales, pero resisten peor el calor o aceleran la corrosión de la rejilla. Placas gruesas parten con algo más de resistencia, pero suelen ser más estables.
* **Frescura de inventario:** Una batería recién fabricada y otra almacenada meses tienen resistencias base distintas.

Por ello **comparar resistencias directamente entre marcas carece de sentido**; conviene revisar también el peso y el comportamiento del voltaje.

## 5. Cómo medir para obtener datos útiles
1. **Medir cargada al 100 % y en reposo:** Asegúrate de que esté cargada y reposada (plomo-ácido tradicional ~`12,6 V+`, AGM ~`12,8 V+`; al menos por encima de `12,5 V`).
2. **Sujetar directamente los bornes:** Evita tornillos de fijación y cables. Las **pinzas Kelvin de 4 hilos** eliminan la resistencia del cable y de la pinza, pero no la resistencia de transición u óxido entre el borne y la abrazadera.
3. **Comparar contra su propia referencia de nueva:** Contrasta primero con la lectura registrada cuando esa batería era nueva (cargada y en reposo); si no existe, usa el rango de fábrica de un modelo nuevo idéntico.
4. **Usar siempre el mismo comprobador:** Cada fabricante usa algoritmos distintos; solo un mismo equipo muestra la tendencia real de desgaste.

## Conclusión
El mayor valor de un comprobador simple no está en una lectura aislada de CCA o SOH, sino en **seguir la tendencia de la resistencia interna de la misma batería** cargada y en reposo. En baterías de plomo-ácido, observar esa evolución dice mucho más que obsesionarse con los porcentajes (por qué el CCA falla en litio se detalla en **[Sobre la inutilidad de medir el CCA en las baterías de iones de litio](/es/2025/about-cca.html)**).
