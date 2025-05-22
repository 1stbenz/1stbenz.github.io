---
layout: post
title: "Análisis de voltaje para el arranque del vehículo (2.3 NA con batería LiFePO4)"
lang: es
date:   2026-03-22 16:00:00
categories: Auto
tags: [Batería de coche, Conocimiento de coche]
description: "¡Rompa el mito único de la «tensión de arranque»! Mediante datos medidos a alta frecuencia en un intervalo de solo 0,05 segundos, desmontamos profundamente el comportamiento físico de cuatro baterías de litio-ferro en el instante del encendido del motor y analizamos cómo la resistencia interna afecta la caída de tensión y la eficiencia de recarga mediante el generador utilizando la fórmula V = V0 - (I x R)."
keywords: "Batería de hierro-litio para arranque, batería automotriz, caída de voltaje, resistencia interna, CCA, corriente de arranque, alternador, LiFePO4, fórmula de caída de voltaje"
image: /images/voltage_record_image.svg
faq:
  - question: "¿Por qué la tensión de la batería cae bruscamente al instante de encender el motor?"
    answer: "Esto se debe a que el motor de arranque necesita una corriente instantánea (I) muy grande para superar la fricción estática del motor. Según la fórmula de voltaje en circuito abierto $$V = V_0 - (I \times R)$$, la corriente que pasa por la resistencia eléctrica interna real de la batería (R) produce un consumo inevitable de tensión."
  - question: "¿Por qué aparece una fluctuación en forma de diente de sierra regular en la tensión cuando se enciende un motor de cuatro cilindros?"
    answer: "Esto ocurre porque, entre los dos pistones que suben, solo uno está en el ciclo de compresión con las válvulas de admisión y escape completamente cerradas, lo que genera una gran resistencia. El cigüeñal encuentra esta enorme resistencia a la compresión cada vez que gira 180 grados, haciendo que la corriente extraída por el motor de arranque fluctúe en consecuencia, formando así una onda de tensión regular."
  - question: "La batería ha recorrido 52.000 kilómetros; ¿cómo determinar si se está degradando observando el voltaje?"
    answer: "Principalmente observe la 'voltaje en reposo' y la 'profundidad de caída al encender'. Si después de una semana en reposo el voltaje sigue manteniéndose por encima de 13,2V (característica LiFePO4) y la caída de tensión durante el arranque se mantiene dentro de los 1,2V (indicador de baja resistencia interna), representa que el SOH (salud de la batería) sigue siendo excelente."
---

En la investigación de los sistemas eléctricos automotrices, el instante del arranque es la fase en que las variaciones de carga son más drásticas. Mediante una muestreo de alta frecuencia a 100 Hz con resolución milisegundal, podemos observar la interacción física entre la batería y el generador dentro de un intervalo temporal extremadamente breve. Este análisis se centra en vehículos equipados con un motor de cuatro cilindros de 2.3 litros y una batería de ion de litio GreenRun2 de 50 Ah para examinar los principios que subyacen a las curvas de voltaje durante el arranque.

---


## I. Análisis del voltaje transitorio de arranque


[Gráfico de récords de voltaje](/images/voltage_record_image.svg)

El proceso de encendido puede descomponerse en cuatro puntos físicos clave, que reflejan la alternancia entre carga mecánica y suministro eléctrico:


### Caída de tensión inicial causada por la corriente de inyección
Cuando se cierra el bobinado electromagnético del motor, en el instante en que este comienza a girar desde el reposo, surge una corriente de arranque muy alta (**corriente de inrush**).  
* **Comportamiento eléctrico**: La tensión cae instantáneamente desde los **13.24 V** (en estado estático) hasta los **12.07 V**.  
* **Explicación técnica**: Esta caída de tensión depende de la resistencia interna del batería $$R$$ y de la impedancia inicial del motor. Según la fórmula:  
  $$V_{terminal} = V_{ocv} - (I_{start} \times R_{internal})$$  
* **Análisis**: Debido a sus características químicas, las baterías de ion de litio con fosfato de hierro y litio tienen una resistencia interna muy baja; por tanto, para la misma corriente de arranque $$I$$, la caída de tensión es mucho menor que en las baterías tradicionales al ácido plomo. Esta prueba muestra una caída de solo unos **1.17 V**, lo que demuestra un excelente factor de potencia de descarga.


### Oscilaciones de voltaje generadas por el compresor del motor
Durante el periodo de funcionamiento continuo del motor, la tensión oscila regularmente entre **12.07 V y 12.5 V**.  
*   **Explicación técnica**: Esta fluctuación es una respuesta directa del motor al superar el **suelo compresivo** (compresión).
    *   **Valle de onda**: El pistón se mueve hacia la fase de compresión, donde la resistencia a la presión es máxima y la demanda de corriente aumenta drásticamente, provocando una caída más profunda en la tensión.
    *   **Pico de onda**: Al pasar el punto muerto superior del pistón durante las fases de escape o admisión, se reduce la resistencia y disminuye el consumo eléctrico, lo que provoca un repunte en la tensión.  
*   **Significado físico**: La frecuencia y duración de estas fluctuaciones pueden reflejar la eficiencia de velocidad del motor de arranque. En este caso específico, se completa el encendido en aproximadamente **0.55 segundos**, lo que demuestra una alta eficiencia del sistema de arranque.


### 3. Rechazo de carga y rebote del inductor
Cuando el motor enciende con éxito y la velocidad aumenta por encima del valor de diseño, se activa el embrague unidireccional para separar las conexiones e interrumpir el circuito.
* **Rendimiento en datos**: El voltaje salta rápidamente desde **12.64V** hasta **13.31V**, estabilizándose luego cerca de los **13.30V**.
* **Principio**: Este es un fenómeno de **descarga por carga**. Al actuar como un gran componente inductivo, el motor libera su energía residual en el instante del corte; al mismo tiempo, la batería pierde súbitamente cientos de amperios bajo una sobrecarga, y su tensión terminal recupera inmediatamente cerca de su plataforma estática.


### 4. Establecimiento de la excitación y transferencia al generador
Después del salto, el voltaje no aumentó inmediatamente, sino que se mantuvo brevemente en el rango de **13.28 V - 13.41 V**, antes de comenzar a subir significativamente (hasta **13.69 V**).

* Período de establecimiento del campo magnético*: Al iniciar, el generador gira junto con el motor, pero el regulador interno de voltaje necesita tiempo para establecer el campo magnético en el rotor; por lo tanto, la tensión de salida aún no supera la tensión de la batería y el sistema depende principalmente de ella.

* **Inicio formal del generador**: Una vez completada la construcción del campo magnético, el voltaje de salida comienza a superar al voltaje de reposo de las baterías; debido a su baja resistencia interna, las baterías de ion de hierro absorben instantáneamente una corriente intensa, manteniendo temporalmente el voltaje del sistema en un rango aproximado de 13.3-13.4 V. Dada la mínima cantidad de energía consumida durante cada arranque de 0.55 segundos y su excelente eficiencia de carga, las baterías pueden compensar rápidamente la diferencia en cuestión de segundos; como consecuencia, la corriente de carga disminuye bruscamente, se libera el control sobre ella y el voltaje sube inmediatamente hasta alcanzar un rango estable de recarga superior a los 13.69 V.

---


## II. Observación del equilibrio de voltaje bajo operación prolongada


En la monitorización continua tras el inicio, las manifestaciones de voltaje demuestran la estabilidad del sistema:

| Fase de monitoreo | Voltaje (V) | Descripción del estado técnico |
| :--- | :--- | :--- |
| **Antes del arranque** | 13.24 | El OCV de la batería se encuentra en una plataforma de alto potencial, con un excelente estado de salud |
| **Inicio inicial** | 13.69 | El generador comienza a producir energía; el voltaje disminuye debido al gran flujo de corriente de recarga del LiFePO₄ |
| **Funcionamiento estable** | 13.80~13.90 | Se entra en la zona de regulación constante del regulador, con pérdidas mínimas en el circuito |


### Resumen técnico
1. **Lógica de regulación de voltaje**: El sistema se estabiliza finalmente en el intervalo de **13,80 V - 13,90 V**. Para las baterías de ion de litio con fosfato de hierro y litio (LiFePO4), este voltaje evita la zona de presión de carga completa por encima de los $$14.6\text{V}$$, permitiendo tanto recarga como una mayor vida útil de las celdas.
2. **Determinación del envejecimiento**: Esta batería ha sido utilizada durante 3 años y recorridos 52,000 kilómetros; sin embargo, aún mantiene un voltaje superior a los $$12\text{V}$$ al momento del arranque y se estabiliza en $$13.24\text{V}$$ antes de encender después de una semana de reposo, lo que demuestra que su resistencia interna no ha aumentado significativamente y que su estado SOH es bueno.

---


## III. Densidad energética y tasa de descarga


Comprender cómo las baterías de hierro litio mejoran el rendimiento del arranque mediante sus propiedades físicas:

1. **Alta densidad energética**  
   La energía específica de la batería al hierro-litio es aproximadamente 3 a 5 veces superior a la de las baterías plomo-ácido. En el mismo volumen, ofrece un peso más ligero y materiales electrodos más eficientes; su voltaje estático se mantiene estable en **13,2–13,3 V**, con una mayor energía potencial inicial durante el arranque.

2. **Alta tasa de descarga**  
Las baterías de hierro-litio tienen una baja resistencia interna, lo que les permite soportar tasas C muy altas. Además, su alta densidad y gran capacidad permiten liberar grandes corrientes durante arranques instantáneos sin que la tensión caiga significativamente, superando ampliamente a las baterías al ácido plomo, que dependen de un lento proceso de difusión química.

----

Los datos de este informe se recopilaron en vehículos reales, con una precisión del sensor de 0,01 V y una frecuencia de muestreo de 100 Hz.