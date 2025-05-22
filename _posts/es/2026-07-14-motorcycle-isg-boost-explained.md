---
layout: post
title: "Análisis del sistema de asistencia eléctrica ISG en motocicletas: funcionamiento, mejora del rendimiento con baterías de litio-ferrofosfato y límites físicos"
lang: es
date: 2026-07-14 20:00:00
categories: Moto
tags: [Conocimiento de motocicleta, Sistemas electrónicos, Modificación de motocicleta]
description: "Análisis en profundidad del principio de funcionamiento y las limitaciones físicas del sistema ISG (Generador de Arranque Integrado) en motocicletas, incluyendo el arranque silencioso y la asistencia eléctrica (boost). También exploramos por qué sustituir la batería tradicional de plomo-ácido por una de fosfato de hierro y litio (LiFePO4) mejora notablemente la respuesta del motor de asistencia, y por qué esta modificación no puede superar los cuellos de botella inherentes al hardware del vehículo."
keywords: "moto ISG, sistema de asistencia eléctrica, generador de arranque integrado, modificación de batería LiFePO4, comparación de batería de plomo-ácido, moto mild hybrid, arranque silencioso, asistencia de aceleración instantánea, caída de voltaje, caída óhmica"
image: /images/isg-motorcycle-system.webp
faq:
  - question: "¿Qué es el sistema de asistencia eléctrica ISG en una motocicleta y cuál es su función principal?"
    answer: "El ISG (Integrated Starter Generator, generador de arranque integrado) unifica el motor de arranque y el alternador convencionales en una sola unidad instalada directamente en el extremo del cigüeñal. Permite un arranque silencioso y sin vibraciones, el sistema de parada y arranque automático (start-stop) en ralentí, y proporciona un par de torsión instantáneo (asistencia eléctrica o boost) al arrancar o acelerar a fondo, mejorando el consumo de combustible y la respuesta de aceleración."
  - question: "¿Por qué sustituir la batería de plomo-ácido tradicional por una de «fosfato de hierro y litio» mejora notablemente la sensación de empuje del ISG?"
    answer: "Las baterías de fosfato de hierro y litio (LiFePO4) tienen una resistencia interna extremadamente baja y una tasa de descarga (C-rate) muy alta. En el momento en que el ISG demanda una corriente elevada para la asistencia eléctrica, la batería de litio no sufre la gran caída de voltaje óhmico típica de las de plomo-ácido. Proporciona de inmediato una corriente estable y suficiente, permitiendo que el motor ISG entregue su par máximo de diseño; al mismo tiempo, su alta aceptación de carga recupera la energía de desaceleración de forma más eficiente."
  - question: "Tras instalar una batería de litio, ¿se puede aumentar el efecto de aceleración del ISG indefinidamente o usar la moto como una eléctrica pura?"
    answer: "No. Aunque la batería de litio elimina el cuello de botella del suministro de energía, el límite de potencia del sistema ISG depende del diseño del bobinado del motor, la limitación de corriente y disipación térmica del controlador (ECU/MCU), y los límites físicos del sistema de baja tensión de 12V (el exceso de corriente genera calor excesivo en el cableado). La mejora de la batería solo libera la potencia máxima diseñada de fábrica del ISG, pero no puede superar los márgenes de seguridad del hardware."
---

En los últimos años, marcas líderes de motocicletas (como SYM, Kymco o Yamaha) han integrado la tecnología **ISG (Integrated Starter Generator, generador de arranque integrado)** en sus modelos. Además de ofrecer un arranque silencioso y sin vibraciones junto con el sistema de parada en ralentí, la asistencia eléctrica (Motor Assist / Mild Hybrid) se ha convertido en un gran atractivo para mejorar la calidad de conducción.

Sin embargo, muchos usuarios notan que la asistencia eléctrica se siente algo tímida con la batería de plomo-ácido original, pero al cambiar a una batería de **fosfato de hierro y litio (LiFePO4)**, el empuje al arrancar o recuperar velocidad es notablemente más enérgico. ¿Cuál es el mecanismo detrás de esto? ¿Y por qué siguen existiendo límites físicos infranqueables incluso tras mejorar la batería? En este artículo te ofrecemos un análisis completo.

---

![shindengen](/images/isg-motorcycle-system.webp)
*Fuente de la imagen: [Shindengen](https://www.shindengen.com/products/electro/exhibition/private_exhibition/isg_ecu/)*

## ¿Qué es el ISG? Principio de funcionamiento y doble función

En la arquitectura eléctrica de una motocicleta convencional, el motor de arranque y el alternador son componentes separados. Al arrancar, el motor de arranque necesita mover el cigüeñal a través de engranajes, lo que suele producir un molesto ruido metálico y notables vibraciones.

**El ISG combina ambos elementos en una sola unidad**, montando el estátor y el rotor de un motor sin escobillas directamente en el extremo del cigüeñal del motor. Funciona en tres modos:

1. **Modo de arranque silencioso (operación como motor)**: Utiliza la energía de la batería para hacer girar el cigüeñal directamente y arrancar el motor. Prescinde por completo de los engranajes de arranque tradicionales, logrando un encendido ultra rápido, silencioso y sin vibraciones.
2. **Modo de asistencia eléctrica (Motor Assist)**: Al iniciar la marcha o al abrir el acelerador repentinamente, el controlador activa el motor ISG para aportar un par de torsión adicional directamente en el cigüeñal, ayudando al motor de combustión a superar la caída de par a bajas revoluciones.
3. **Modo de generación y recuperación de energía (operación como alternador)**: Cuando el motor funciona con normalidad o el vehículo desacelera en inercia, el ISG cambia a su función de alternador, convirtiendo la energía mecánica del motor o la energía cinética del vehículo en electricidad para recargar la batería.

---

## Limitaciones inherentes del sistema de asistencia ISG

Aunque el ISG proporciona asistencia de potencia instantánea, es fundamentalmente diferente de un sistema mild hybrid de 48V de un coche o de un vehículo eléctrico puro (EV), limitado principalmente por:

* **Cuello de botella de potencia del sistema de 12V**: Según la fórmula $$P = V \times I$$ (Potencia = Voltaje × Corriente), para entregar 1 kW (aprox. 1.35 CV) de asistencia en una arquitectura estándar de 12V, y considerando la eficiencia del controlador (MCU) y del motor, la corriente instantánea de la batería superará los **90 a 100 amperios**. Intentar aumentar más la potencia haría que la corriente se disparara, provocando un calentamiento extremo de los cables y daños en los componentes.
* **Espacio reducido y disipación de calor**: El motor ISG está pegado al cárter, en un entorno de alta temperatura y espacio muy restringido. Si la asistencia eléctrica de alta potencia se prolonga, el bobinado acumula calor excesivo, lo que puede quemar el aislamiento del cable o desmagnetizar los imanes permanentes.
* **Breve tiempo de asistencia**: Para proteger la batería de descargas excesivas y evitar el sobrecalentamiento del motor, la ECU original suele limitar el boost eléctrico a los primeros 3 o 5 segundos del arranque o de la aceleración, por lo que no proporciona un empuje continuo a alta velocidad como un EV.

---

## Batería de plomo-ácido vs. batería de litio LiFePO4: ¿Por qué mejora tanto la experiencia?

Si el sistema ISG tiene un límite superior claro, ¿por qué el simple reemplazo de la batería de plomo-ácido por una de **fosfato de hierro y litio (LiFePO4)** marca una diferencia tan evidente? La clave está en que **las propiedades físicas de la batería de litio liberan el potencial latente del motor** que antes estaba limitado por la caída de tensión.

```
【Comportamiento del voltaje bajo alta descarga】
Batería de plomo-ácido: 12.8V ──────► [Descarga de alta corriente] ──────► Caída óhmica a 10.0V~10.5V (Menor potencia)
Batería de litio:       13.2V ──────► [Descarga de alta corriente] ──────► Voltaje terminal estable a 12.5V~12.8V (Potencia máxima)
```

### 1. Resistencia interna y caída de voltaje óhmico (IR Drop)
* **Batería de plomo-ácido**: Su resistencia interna es relativamente alta. Cuando el ISG exige una gran corriente de 60 a 80A o más al arrancar, la ley de Ohm ($$\Delta V = I \times R_\text{internal}$$) provoca una severa **caída de voltaje (IR Drop)**. La tensión en bornes puede caer instantáneamente de 12.8V a menos de 10.5V. Esta pérdida de voltaje reduce notablemente la potencia real recibida por el motor ($$P = V \times I$$), haciendo que el boost se sienta débil.
* **Batería de litio LiFePO4**: Tiene una resistencia interna extremadamente baja (menos de 1/5 de la de plomo-ácido) y una excelente tasa de descarga (C-rate). Incluso con descargas de más de 100A, el voltaje terminal se mantiene estable por encima de 12.5V, garantizando que el motor ISG reciba energía abundante para entregar su par máximo de diseño.

### 2. Eficiencia en la aceptación de carga (Recuperación)
Durante las deceleraciones, el ISG convierte la inercia en corriente de carga. Las baterías de plomo-ácido absorben la corriente de forma lenta, perdiendo parte de esta energía. Las baterías LiFePO4 admiten recargas rápidas y eficientes, almacenando rápidamente la energía recuperada para asegurar que haya suficiente carga en el siguiente arranque.

| Característica / Parámetro | Batería tradicional de plomo-ácido (Lead-Acid) | Batería de fosfato de hierro y litio (LiFePO4) |
| :--- | :--- | :--- |
| **Resistencia interna** | Mayor; produce una caída de voltaje significativa con alta corriente | Extremadamente baja; voltaje terminal muy estable en alta descarga |
| **Tasa de descarga (C-Rate)** | Media (las descargas fuertes repetidas acortan su vida útil) | Muy alta (soporta descargas instantáneas de 20C a 40C) |
| **Rendimiento del boost ISG** | Limitado por la caída de tensión; el motor no rinde al máximo | Voltaje estable; libera el par máximo diseñado del motor |
| **Eficiencia de recuperación** | Absorción lenta; parte de la energía cinética no se recupera | Excelente aceptación de carga; alta eficiencia de recuperación |
| **Peso en el vehículo** | Pesada (aprox. 3 a 4 kg) | Ligera (aprox. 0.8 a 1.2 kg) |

---

## Límites insuperables incluso con batería de litio

Muchos usuarios creen erróneamente que la batería de litio «aumenta los caballos de potencia del motor». Sin embargo, desde el punto de vista de la ingeniería, **instalar una batería de litio solo elimina el cuello de botella del voltaje terminal deficiente, permitiendo al ISG rendir tal y como fue diseñado de fábrica, pero no aumenta la potencia del sistema en sí**. La mejora sigue topándose con los siguientes límites de hardware:

### 1. Limitación de corriente en el controlador (MCU/ECU)
La corriente máxima del ISG está regulada por el firmware y los transistores MOSFET del controlador (MCU). Aunque la batería de litio pueda entregar 200A instantáneos, si el controlador limita la corriente a 60A, el motor solo recibirá 60A. La batería no puede forzar al controlador a superar sus límites de protección.

### 2. Bobinado del motor y saturación magnética
El motor ISG está limitado por las dimensiones de su núcleo de acero al silicio, el número de vueltas de sus bobinas y el flujo magnético de sus imanes permanentes. Superado el punto de saturación magnética, un aumento de la corriente no producirá más par motor, sino que se disipará por completo en forma de calor perjudicial.

### 3. Transmisión CVT y características mecánicas a altas revoluciones
La asistencia del ISG se aplica directamente en el cigüeñal. Al arrancar desde parado, el variador (CVT) se encuentra en su relación más corta, lo que multiplica mecánicamente el par motor adicional del ISG y produce un empuje claro. Sin embargo, a velocidades medias o altas, la potencia térmica del propio motor domina por completo, haciendo que el pequeño aporte del ISG sea insignificante y carezca de la aceleración constante que tiene un vehículo eléctrico.

---

## Conclusión

El sistema de asistencia eléctrica ISG en motocicletas es un diseño excelente en la era moderna para mejorar el consumo y el confort. Su función de arranque silencioso y asistencia a bajas revoluciones compensa con eficacia la entrega irregular de par de los motores monocilíndricos al arrancar.

Actualizar la batería convencional a una de fosfato de hierro y litio elimina la caída de voltaje en descarga y permite al motor ISG **entregar toda la potencia para la que fue diseñado**. No obstante, debido a las restricciones de la arquitectura de 12V, los límites del controlador, la temperatura del motor y el funcionamiento de la transmisión CVT, el ISG siempre mantendrá un rol puramente auxiliar. Comprender con realismo el alcance de esta modificación permite disfrutar de una conducción más placentera garantizando al mismo tiempo la seguridad y durabilidad eléctrica de la motocicleta.

---

## Referencias

* IEEE Transactions on Transportation Electrification: *Analysis of Integrated Starter Generator (ISG) for Two-Wheelers*
* SAE International: *12V Mild-Hybrid Electric Boost Performance under Battery Internal Resistance Degradation*
* batteryuniversity.com: *How does Internal Resistance Affect Battery Performance?*
