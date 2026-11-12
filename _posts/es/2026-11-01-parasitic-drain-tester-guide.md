---
layout: post
title: "Prueba de fuga de batería (En serie): Medir corriente parásita con interruptor de bypass"
lang: es
date: 2026-11-01 10:00:00
categories: Auto
tags: [Electricidad del Automóvil, Reparación de Autos, Guía DIY, Corriente Parásita, Descarga de Batería]
related_posts:
  - 2026-11-02-dc-clamp-meter-parasitic-drain-guide.md
  - 2026-11-03-fuse-voltage-drop-parasitic-drain-guide.md
  - 2025-09-17-memory-saving-battery.md
description: "¿Se descarga la batería de tu auto tras unos días parado? Descubre cómo medir la corriente parásita (consumo en reposo) de forma segura con un interruptor de bypass y multímetro, sin fundir fusibles ni desconfigurar las computadoras del auto."
keywords: "medir corriente parásita, descarga de batería auto, interruptor bypass, parasitic drain tester, consumo en reposo, multímetro fusible fundido, extraer fusibles, fuga de corriente batería"
image: /images/howtoconnect.webp
faq:
  - question: "¿Qué es la corriente parásita (consumo en reposo) y cuál es su valor normal?"
    answer: "La corriente parásita es el pequeño consumo eléctrico residual que los módulos del vehículo (alarma, receptor de llave, reloj) siguen extrayendo de la batería después de apagar el motor, cerrar las puertas y entrar en reposo profundo. En vehículos modernos, el consumo en reposo normal suele situarse entre 20 mA y 60 mA (0,02 A - 0,06 A). Valores superiores a 60 mA - 80 mA de forma continua indican una fuga anómala."
  - question: "¿Por qué no se debe conectar directamente un multímetro en serie sin un interruptor de bypass?"
    answer: "Al soltar el borne se corta la corriente del auto, y al colocar el multímetro directamente se despiertan súbitamente todas las computadoras. Este pico de corriente de entrada puede alcanzar decenas de amperios, fundiendo al instante el fusible interno de 10A del multímetro y provocando la pérdida de memorias del vehículo. El interruptor de bypass absorbe este pico por una vía sólida y solo deriva la corriente al multímetro cuando el auto ya está dormido."
  - question: "¿Por qué se deben bajar las ventanillas y trabar manualmente la cerradura del capó?"
    answer: "Bajar las cuatro ventanillas evita quedarse fuera si el auto se cierra automáticamente y garantiza el acceso a los fusibles interiores. Trabar la cerradura del capó con un destornillador engaña al sensor del capó para que la computadora crea que está cerrado, permitiendo que la alarma y los módulos BCM entren en reposo profundo."
  - question: "¿Por qué hay que esperar entre 15 y 45 minutos y alejar la llave inteligente a 5 metros?"
    answer: "Los autos modernos cuentan con decenas de unidades de control (ECU, BCM, pasarela CAN) que ejecutan rutinas de apagado y tardan de 15 a 45 minutos en dormirse por completo. Si la llave inteligente (Keyless) permanece cerca, el auto mantiene activas las antenas de comunicación inalámbrica y nunca entra en reposo."
  - question: "¿Cómo localizar el circuito que descarga la batería si la lectura supera los 60 mA?"
    answer: "Mantén el multímetro conectado y activo. Accede a las cajas de fusibles (motor o habitáculo) y retira los fusibles uno por uno con una pinza de plástico observando la pantalla del multímetro. Cuando al quitar un fusible específico el consumo caiga bruscamente por debajo de 50 mA, habrás localizado el circuito culpable (causas comunes: cámaras dashcam mal conectadas, pantallas Android o cerraduras defectuosas)."
  - question: "¿Cuál es el procedimiento correcto de desconexión al finalizar la prueba?"
    answer: "El orden es fundamental: primero pon el interruptor en posición ON (Cerrado / Bypass). Luego desconecta los conectores banana del multímetro. Retira el cartón aislante, asienta firmemente el terminal original en el borne negativo y aprieta la tuerca M10. Finalmente retira las pinzas de prueba y tira de la palanca interior del capó para destrabar la cerradura antes de cerrarlo."
---

![Comprobador de corriente parásita (Parasitic Drain Tester)](/images/tool.webp)

¿Tu auto se queda sin batería tras un par de días sin usarlo? Lo más probable es que tenga una **fuga de corriente parásita (consumo en reposo / Parasitic Drain)**.

En el método tradicional de medición en serie, al desconectar la batería se desconfiguran las memorias de la radio y los parámetros de la ECU. Peor aún: el pico de corriente instantáneo al reconectar suele **fundir de inmediato el fusible de 10A del multímetro**.

El **interruptor de prueba de corriente parásita (Parasitic Drain Tester / Bypass Switch)** resuelve este problema: permite insertar el multímetro en el circuito **sin cortar la corriente del vehículo**, protegiendo el multímetro contra picos y evitando que las computadoras se reseteen.

> 💡 **Guía de la serie:**  
> Si cuentas con una pinza amperimétrica de corriente continua (DC) y prefieres una medición sin herramientas ni desmontaje, consulta nuestro artículo complementario:  
> 👉 [Prueba de fuga de batería (Pinza amperimétrica): Medir corriente parásita con pinza DC](/es/2026/dc-clamp-meter-parasitic-drain-guide.html)

---

## Características del comprobador con bypass

Esta herramienta de diagnóstico cuenta con:

- **Interruptor de dos vías sin interrupción (Bypass)**:
  - **ON (I / Cerrado)**: La corriente fluye al 100 % por el cuerpo de la herramienta. El multímetro marca 0 A y queda protegido ante sobrecargas.
  - **OFF (O / Abierto)**: Se abre el bypass interno y toda la corriente pasa obligatoriamente por el multímetro para una medición de alta precisión en miliamperios (mA).
- **Pinzas diseñadas para batería**: Incluye una **pinza de resorte en forma de U** (se sujeta a la base del borne negativo antes de soltar cables) y una **pinza cocodrilo totalmente aislada** (para el terminal del cable del auto).
- **Doble fusible enchufable de 10A**: Protección externa sustituible contra descuidos o sobrecorrientes.
- **Conectores tipo banana de 4 mm de cobre puro**: Compatibles con cualquier multímetro estándar.

---

> [!CAUTION]
> ### ⚠️ Advertencia de cortocircuito y rotura de multímetro
> **Apaga el motor y retira la llave antes de empezar. ¡Prohibido arrancar el motor o poner el contacto en ACC/ON durante la prueba!**  
> **No enciendas aparatos de gran potencia (luces, ventilador, asientos calefactables).** De lo contrario, circularán decenas de amperios que quemarán los fusibles y cables de la herramienta.

---

## Procedimiento estándar (SOP) en 7 pasos

![Diagrama de conexión del comprobador y multímetro](/images/howtoconnect.webp)

### Paso 1: Preparación del vehículo y bloqueo simulado del capó
1. Apaga el motor, quita la llave y apaga todas las luces interiores.
2. **Baja por completo las cuatro ventanillas** (vital para evitar quedarse cerrado fuera).
3. Abre el capó. Con un destornillador, empuja el mecanismo del pestillo del capó hacia abajo hasta la **posición de "cerrado/bloqueado"**. Así la computadora del auto asumirá que el capó está cerrado.

---

### Paso 2: Poner el interruptor en posición ON (I / Cerrado)
Antes de realizar cualquier conexión eléctrica, coloca el interruptor en **ON (I / Cerrado)** para que el circuito esté puenteado internamente.

---

### Paso 3: Conectar las pinzas al borne negativo
1. Engancha firmemente la **pinza de resorte en forma de U** en la base del **borne negativo de metal de la batería**.
2. Conecta la **pinza cocodrilo aislada** de forma segura al **terminal del cable negativo original**.

---

### Paso 4: Conectar el multímetro
1. Conecta la banana negra de 4 mm en la toma **COM** del multímetro.
2. Conecta la banana roja de 4 mm en la toma de **alta corriente 10A / 20A** (nunca en la toma de mA al inicio).
3. Gira la rueda selectora a **Amperios en corriente continua (DC A)**.

---

### Paso 5: Aflojar y aislar el terminal negativo original
1. Usa una **llave fija M10** para aflojar la tuerca del terminal negativo.
2. Levanta con cuidado el terminal separándolo del borne de la batería (el auto sigue recibiendo corriente ininterrumpida a través de la herramienta).
3. **Coloca un trozo de cartón grueso o plástico entre el terminal y el borne metálico** para aislarlo completamente y evitar roces accidentales.

---

### Paso 6: Cerrar el auto y esperar el reposo profundo (15 - 45 minutos)
1. Cierra todas las puertas y pulsa el botón del mando para bloquear el auto.
2. **Aleja la llave inteligente (Keyless) al menos 5 metros del vehículo.**
3. **Espera de 15 a 45 minutos** con paciencia para que todas las computadoras (BCM, ECU, gateway) completen sus rutinas y se duerman.

---

### Paso 7: Cambiar el interruptor a OFF y leer el consumo
1. Comprueba que el multímetro siga encendido.
2. Cambia el interruptor a **OFF (O / Abierto)**.
3. El bypass se interrumpe y toda la corriente pasa por el multímetro. Lee el valor estable de corriente parásita en pantalla.

> [!TIP]
> **Cambio a escala de mA para mayor precisión decimal:**  
> Si el consumo es muy bajo y deseas ver más decimales en la escala de miliamperios, **pon SIEMPRE el interruptor de nuevo en ON (Cerrado)** antes de girar la rueda del multímetro o cambiar la clavija a la toma de mA. Una vez cambiado, vuelve a pasar a **OFF**.

| Lectura (DC A) | Estado | Evaluación y acción recomendada |
| :--- | :--- | :--- |
| **20 mA - 60 mA (0,02 A - 0,06 A)** | ✅ **Normal** | Consumo correcto de memoria y alarma; la batería resistirá semanas. |
| **60 mA - 80 mA (0,06 A - 0,08 A)** | ⚠️ **Ligeramente alto** | Revisa accesorios auxiliares (ej. dashcam en modo vigilancia). |
| **> 80 mA (o cientos de mA)** | ❌ **Fuga severa** | Descarga grave. Agotará la batería en pocos días; ¡toca extraer fusibles! |

---

## Localización de la fuga mediante extracción de fusibles

Si el consumo medido supera los **60 mA**, deja el interruptor en OFF:

1. **Localiza las cajas de fusibles**: Compartimento del motor, salpicadero o maletero.
2. **Extracción individual**: Con una pinza extractora, **retira un fusible a la vez** observando la pantalla del multímetro.
3. **Identificación del circuito**:
   - Si la lectura no cambia, **vuelve a colocar el fusible** y pasa al siguiente.
   - Si al retirar un fusible determinado la lectura **cae de golpe por debajo de 50 mA**, ¡habrás descubierto el circuito responsable!
4. **Causas habituales**:
   - Transformadores de cámaras dashcam con corte de bajo voltaje averiado.
   - Pantallas multimedia Android o amplificadores con cable remoto (ACC) siempre activo.
   - Microinterruptores defectuosos en cerraduras de puertas.
   - Luces de guantera, parasoles o maletero que no se apagan.

---

## Procedimiento seguro de desmontaje (SOP)

Sigue este orden estrictamente para evitar chispas o reseteo de computadoras:

1. **Interruptor a ON**: Vuelve a poner el interruptor en **ON (I / Cerrado)**.
2. **Desconectar multímetro**: Desenchufa las clavijas banana del multímetro.
3. **Fijar terminal negativo**: Retira el cartón aislante, encaja firmemente el terminal original en el borne negativo y aprieta la tuerca M10.
4. **Retirar pinzas**: Tras verificar que el terminal original está bien apretado, retira la pinza en U y la pinza cocodrilo.
5. **Liberar cerradura del capó**: **¡Nunca azotes el capó con la traba echada!** Tira de la palanca interior del capó para liberar el pestillo y ciérralo con normalidad.
