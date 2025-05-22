---
layout: post
title: "La ciencia del envejecimiento de las baterías: voltaje, resistencia interna y pérdida de potencia"
date: 2026-03-30 22:30:00 +0800
categories: Auto
lang: es
image: /images/battery_aging.webp
tags: [Batería de coche, Conocimiento de coche]
description: "Profundice en la verdad física detrás del deterioro de las baterías. A través de modelos de circuito equivalente y la ley de Ohm, analice cómo el aumento repentino de la resistencia interna provoca sobrecalentamiento anómalo durante la carga, voltaje terminal artificialmente elevado y colapso de tensión al descargar. Este artículo ofrece ejemplos sencillos de fórmulas para que comprenda los principios científicos detrás del fenómeno «no se cargan completamente ni mantienen su carga» en baterías de iones de litio y ácido plomo, así como sus criterios de evaluación de seguridad."
keywords: "Causas del envejecimiento de la batería, aumento de la resistencia interna, circuito equivalente, vida útil de las baterías de litio, mantenimiento de baterías de plomo-ácido, cálculo de caída de tensión, fórmula de pérdida de potencia, principio de calentamiento de la batería, impedancia interna, detección del estado de salud de la batería"
math: true
faq:
  - question: "¿Por qué la batería parece envejecer más rápido cuando hace frío?"
    answer: "Las bajas temperaturas aumentan la viscosidad del electrolito, lo que provoca un aumento temporal de la resistencia interna R. Según $$V_{measured} = V_{ocv} - (I \times R)$$, el mayor caída de voltaje hace que el dispositivo detecte una tensión antes por debajo del umbral de apagado."
  - question: "¿La carga rápida acelera el aumento de la resistencia interna de la batería?"
    answer: "Sí. La gran corriente de carga rápida genera calor residual en proporción al cuadrado ($$P = I^2 R$$), y las altas temperaturas aceleran las reacciones químicas secundarias internas, produciendo sustancias no conductoras que cubren los electrodos, lo que provoca un aumento permanente de la resistencia interna."
  - question: "¿Por qué la batería muestra un 100% y luego se descarga rápidamente si se desconecta inmediatamente?"
    answer: "Cuando R es grande, el voltaje de carga se ve arrastrado artificialmente. Una vez que la corriente I cesa, la caída de tensión $$(I \times R)$$ desaparece y el voltaje terminal cae instantáneamente al valor real $$V_{ocv}$$, provocando un descenso repentino del porcentaje."
  - question: "¿Son efectivos los reparadores de baterías disponibles en el mercado?"
    answer: "Tienen un efecto débil de desecristalización en las baterías al ácido sulfúrico, pero no son eficaces contra la degradación estructural de las baterías de litio. Además, debido a que las baterías viejas tienen una resistencia interna elevada, intentar repararlas forzosamente puede provocar riesgos de seguridad por mala disipación del calor."
---

Ya sea que se trate de una batería de iones de litio o de plomo-ácido, la característica más evidente tras el envejecimiento es **"se llena con un solo recarga y se vacía al usarla"**, acompañada a menudo por un calentamiento severo. Para comprender estos fenómenos, hay que partir del **resistencia interna (R)** de las baterías.


## I. Fenómenos de carga tras el envejecimiento: ¿Por qué se calienta más cuanto más la cargamos?


Cuando cargamos una batería con un cargador, la potencia total de salida del cargador ($$P_{potencia\_total}$$) se divide en dos partes:

$$P_{\text{potencia total}} = P_{\text{calor}} + P_{\text{carga real}}$$


### El salto vertical en la eficiencia energética
Supongamos que utilizamos un cargador de 5 V/2 A (potencia total de 10 W) para comparar la conversión de energía entre las baterías nuevas y antiguas:

| Estado de la batería | Resistencia interna ($R$) | Potencia disipada como calor ($I^2 R$) | Potencia real de carga | Eficiencia |
| :--- | :--- | :--- | :--- | :--- |
| **Batería nueva** | 0,1 Ω | **0,4 W** | **9,6 W** | **96 %** (muy alto) |
| **Batería vieja** | 1,5 Ω | **6,0 W** | **4,0 W** | **40 %** (muy bajo) |

**Páuse y piense:** En una batería vieja, más de la mitad del poder se consume en el resistencia interna $$R$$ convirtiéndose en calor desperdiciado. Esta es la razón por la que las baterías antiguas parecen convertirse en "bolsitas térmicas" al cargarse, y porque la velocidad de carga parece ralentizarse: ya que solo queda menos de la mitad del poder realmente almacenada como energía química.

---


### 2. Engaño de voltaje: el error crítico al determinar la carga completa


[![Símbolo de batería](/images/battery-symbol.webp)](url)

* **Tensión de circuito abierto (Vocv):** La tensión medida entre los extremos cuando la batería no tiene carga y no circula corriente.
* **Resistencia interna ($$R$$):** El obstáculo físico que se produce a través del paso de la corriente por las placas, el electrolito y la membrana separadora.

El cargador detecta el **voltaje de terminal**:

$$V_{voltaje\_detectado} = V_{ocv} + (I \times R)$$

* **El engaño de las baterías viejas**: Cuando se introduce corriente ($$I$$) en una batería, si la batería ha envejecido y su resistencia interna ($$R$$) aumenta, la corriente encuentra un bloqueo severo. Este gran obstáculo genera directamente una tensión virtualmente elevada $$(I \times R)$$ que se superpone a la tensión real.

* **Resultado**: Si imaginamos la carga como el llenado de una torre de agua, una resistencia interna alta es similar a un "obstáculo grave en la entrada". Cuando se introduce agua, la presión del agua en la boca del tubo (voltaje detectado) aumenta bruscamente. El cargador, al medirlo, cree erróneamente que "el tanque está lleno hasta el borde" y detiene inmediatamente la carga mientras enciende una luz verde. Sin embargo, la capacidad de almacenamiento real interna $$V_{ocv}$$ puede seguir estando en un estado de baja carga.

Esta es la razón por la que las baterías envejecidas siempre parecen **"llenarse al instante"**: se trata de una ilusión provocada cuando el voltaje real se ve "inflado artificialmente" debido a la resistencia interna.

---


## II. El colapso de voltaje durante la descarga: el culpable principal del apagón


Cuando el dispositivo extrae corriente, la fórmula se invierte:

$$V_{voltaje\_detectado} = V_{ocv} - (I \times R)$$

**Un ejemplo de la vida cotidiana:**  
Tu teléfono se apaga automáticamente cuando detecta que el voltaje es inferior a 3,3 V. Supongamos que la batería aún tiene un residuo de carga de 3,7 V:

* **Nueva batería (R=0,1Ω)**: Al usar una gran corriente de 2A para jugar, la tensión cae a 3,7-(0,1×2) = **3,5V** → **funcionamiento fluido**.
* **Batería vieja (R=0,5Ω)**: Con la misma gran corriente de 2A, la tensión cae a 3,7-(0,5×2) = **2,7V** → **por debajo del umbral, el teléfono se apaga instantáneamente**.

Esta es la razón por la que los teléfonos antiguos indican un 20 % de batería restante, pero se apagan o reinician instantáneamente al abrir la cámara o jugar a juegos debido a una caída brusca en el voltaje.

---


## Conclusión: El envejecimiento es un «bloqueo» irreversible.


Si se compara la batería con una **torre de agua**, la resistencia interna es como el **óxido y los obstrucciones en las tuberías de salida**:
*   **Durante el recarga:** Las tuberías están tapadas, por lo que la presión del agua (voltaje) alcanza rápidamente su límite máximo, haciéndole creer que está llena, pero en realidad no entra agua.
*   **Durante la descarga:** Cuando quieres usar el agua, las obstrucciones de las tuberías (resistencia interna) son demasiado grandes; sale muy poca agua y es imposible atender a una demanda repentina.

Este aumento de la impedancia causado por materiales físicos (como cristales en las placas o degradación del electrolito) es irreversible; el único método para garantizar la seguridad y un suministro eléctrico estable del equipo consiste en reemplazar a tiempo la batería.

> **Conceptos avanzados: ¿La resistencia interna se divide realmente en «corriente alterna (CA)» y «corriente continua (CC)»?****
> 
> Si consultas los datos técnicos de una batería, es común encontrar dos tipos diferentes de resistencia interna indicados. Para no complicar demasiado la física, podemos entenderlo así:
> 
> * **Resistencia interna en corriente alterna (ACIR):** El instrumento suele aplicar una débil señal de CA a 1 kHz para medir. Solo se mide el obstáculo físico puro (como los contactos o la conductividad del electrolito). Dado que el tiempo es extremadamente corto, las reacciones químicas aún no tienen tiempo de ocurrir; por lo tanto, el valor medido suele ser muy bajo y atractivo. La mayoría de los dispositivos portátiles en el mercado miden este tipo.
> 
> * **Resistencia interna en corriente continua (DCIR):** En realidad se conecta al dispositivo para extraer una gran corriente durante un período prolongado mientras se mide. Además del obstáculo físico original, también se suma la «resistencia interna de polarización» generada cuando las reacciones químicas no pueden seguir el ritmo de suministro eléctrico. Este valor es mucho mayor que la resistencia en CA, pero es este el **verdadero obstáculo** de tu teléfono o coche.
> 
> *Nota: Para acercarse a los escenarios reales de uso cotidiano, todas las fórmulas para caída de tensión y generación de calor discutidas en este artículo se basan fundamentalmente en la «resistencia interna en corriente continua (DCIR)».*