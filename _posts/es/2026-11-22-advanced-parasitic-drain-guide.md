---
layout: post
title: "Prueba de fuga de batería (4) Diagnóstico avanzado: Despertares intermitentes y CAN-BUS"
lang: es
date: 2026-11-22 10:00:00
categories: Auto
tags: [Electricidad del Automóvil, Mantenimiento de coche, Tutorial DIY]
related_posts:
  - 2026-11-01-parasitic-drain-tester-guide.md
  - 2026-11-02-dc-clamp-meter-parasitic-drain-guide.md
  - 2026-11-03-fuse-voltage-drop-parasitic-drain-guide.md
description: "¿La batería se descarga en dos días aunque el consumo parásito parece normal? Guía avanzada DIY: prueba de autodescarga en 24h vs. carga inteligente IBS, los 5 puntos ciegos de 0.0 mV en fusibles, despertares fantasma nocturnos, medición CAN-BUS en OBD2 y cámara térmica."
image: /images/advanced-parasitic-drain.webp
faq:
  - question: "¿Por qué la batería se descarga en dos días si el consumo en reposo marca normal (menos de 30mA)?"
    answer: "Hay dos causas habituales: primero, 'despertares fantasma intermitentes' durante la noche por manijas Keyless húmedas, llaves inteligentes demasiado cerca, dispositivos OBD2 o módulos telemáticos; segundo, autodescarga interna de la batería o carga incompleta por el sistema IBS en trayectos cortos."
  - question: "¿Cómo sé si el problema es la batería vieja o una fuga eléctrica del coche?"
    answer: "Haz la prueba de autodescarga de 24 horas: carga la batería al 100%, desconecta el borne negativo, espera 1 hora y anota el voltaje inicial (12.6V–12.7V). Déjala desconectada 24 horas y vuelve a medir: si baja menos de 0.05V, la batería está sana y la fuga está en el coche; si cae a 12.2V o menos, la batería está dañada."
  - question: "El consumo total es de cientos de mA, pero todos los fusibles marcan 0.0 mV. ¿Qué hago?"
    answer: "La corriente circula por rutas que la caída de tensión en fusibles de cuchilla no detecta: cables directos sin fusible (alternador B+, motor de arranque, electroventilador, fusible principal Megafuse), fusibles de 30A+ con resistencia mínima, fusibles JCASE/Maxi sellados, cajas de fusibles ocultas (maletero, bajo asiento) o accesorios conectados directo a batería. Usa una pinza amperimétrica DC de 2A en esos cables."
  - question: "¿Cómo saber si la red CAN-BUS del coche está dormida sin desmontar paneles?"
    answer: "Con el multímetro en DC V, mide el Pin 6 (CAN-H) y el Pin 14 (CAN-L) del puerto OBD2 respecto a masa (Pin 4/5). En coches directos baja cerca de 0V al dormir; si oscila alrededor de 2.5V (unos 2.2V–2.8V), la red sigue despierta. En coches modernos con Gateway central (SGW), el OBD2 se aísla en 0V en reposo y deberás medir en el concentrador CAN interior."
  - question: "Encontré un fusible del cuadro o BCM consumiendo, pero cambiar el módulo no resolvió la fuga. ¿Por qué?"
    answer: "En redes CAN-BUS / LIN-BUS los módulos se despiertan entre sí. A menudo el módulo que consume está sano y otro sensor averiado (como un sensor de lluvia húmedo o antena de manija) lo mantiene despierto. Desconecta los conectores de comunicación uno a uno en el CAN Hub en lugar de quitar fusibles."
  - question: "¿Sirve una cámara térmica para móvil para encontrar fugas eléctricas?"
    answer: "Sí, especialmente en mazos estrechos o humedad bajo la alfombra. Cualquier componente con consumo continuo de 100mA–300mA+ (bobina de relé energizada, chip con fuga, conector sulfatado) estará 2°C–5°C más caliente que su entorno. Deja enfriar el coche 2–3 horas (mejor toda la noche) antes de escanear y evita metales brillantes por los reflejos."
---

![Diagnóstico Avanzado de Consumo Parásito Automotriz](/images/advanced-parasitic-drain.webp)

Para empezar con tranquilidad: **los métodos básicos de las tres guías anteriores resuelven más del 80% de las fugas eléctricas** (cámaras dashcam, luces interiores o alternador). No te abrumes con esta guía: recurre a estas cinco técnicas avanzadas solo cuando las pruebas básicas no logren dar con el culpable.

> **Repaso de la serie:**
> - Medición total sin cortar corriente: [Guía con Interruptor Bypass](/es/2026/parasitic-drain-tester-guide.html) | [Guía con Pinza Amperimétrica DC](/es/2026/dc-clamp-meter-parasitic-drain-guide.html)
> - Localización sin sacar fusibles: [Guía de Caída de Tensión](/es/2026/fuse-voltage-drop-parasitic-drain-guide.html)

---

## 1. Descarta "falsas fugas": Autodescarga y carga inteligente IBS

Antes de invertir horas buscando una fuga, confirma que la pérdida de carga no venga de la propia batería:

### 1. Prueba de autodescarga de la batería
Si las placas internas tienen microcortos, la batería se descargará sola aunque esté desconectada:
1. Cárgala al 100%, **desconecta el borne negativo** y espera 1 hora a que baje la carga superficial (voltaje sano: `12.6V ~ 12.7V`).
2. Déjala desconectada 24 horas y vuelve a medir: una caída `< 0.05V` indica batería sana; si cae notablemente (p. ej. bajo `12.2V`), cámbiala.

### 2. "Falsa descarga" por sistema IBS / BMS
Los coches modernos con sensor IBS / BMS suelen cargar la batería solo al **75% ~ 80%** para ahorrar combustible. Si solo haces trayectos cortos de 10–15 minutos, la batería vive al límite y falla con el frío o tras pocos días parado. **Carga la batería al 100% y verifica su estado CCA antes de buscar fugas.**

---

## 2. Todos los fusibles marcan `0.0 mV`, pero sigue habiendo fuga: 5 puntos ciegos

Si el consumo total es de cientos de mA pero cada fusible marca `0.0 mV`, la corriente va por caminos invisibles para esa prueba:

1. **Circuitos directos de alta corriente (sin fusible de cuchilla)**: El más típico es el **cable B+ del alternador** con diodos en corto (ver [Guía de Pinza DC](/es/2026/dc-clamp-meter-parasitic-drain-guide.html)), seguido de **motor de arranque, electroventilador/bomba eléctrica** y **fusibles principales atornillados (Megafuse / Multi-block Fuse)** en el borne positivo.
2. **Fusibles de alto amperaje (30A ~ 60A+)**: Su resistencia interna es mínima (`< 2 mΩ`). Una fuga de `100mA` genera menos de `0.1mV`, que el multímetro lee como `0.0 mV`. **Solución**: usa una pinza DC de 2A directamente sobre el cable grueso trasero.
3. **Fusibles tipo caja sin puntos de prueba (JCASE / Maxi)**: Tienen la parte superior sellada; debes usar pinza amperimétrica en el cable de salida o cámara térmica.
4. **Cajas de fusibles ocultas**: Muchos coches esconden cajas adicionales en el **lateral del maletero, bajo el asiento trasero, junto a la batería o bajo la guantera/piso del copiloto**.
5. **Accesorios instalados directo a batería**: Dashcams, amplificadores o luces auxiliares cableados directo al positivo nunca pasan por la caja de fusibles original.

---

## 3. Marca normal (`30mA`) en el momento, pero muere en dos días: "Despertares fantasma"

Al cerrar el coche, el consumo baja en escalones (`3A` → `0.8A` → `0.03A`). Si baja de `30mA` frente a ti pero amanece sin batería, algo despierta al coche de noche con picos periódicos de `0.5A ~ 3A`.

**Revisa primero estos 4 culpables frecuentes:**
* **Sensores de manija Keyless**: Humedad tras lavar el coche o llover provoca falsos toques nocturnos.
* **Llave inteligente demasiado cerca**: Guardar la llave en casa a menos de 3–5 metros del coche mantiene la comunicación activa.
* **Dispositivos en el puerto OBD2**: HUDs Bluetooth, rastreadores GPS o escáneres conectados consultan la red periódicamente (**desconecta todo antes de probar**).
* **Módulos telemáticos / SOS**: Poca cobertura en garajes subterráneos provoca reconexiones constantes.

> **Truco avanzado**: No puedes cazar despertares nocturnos mirando la pantalla. Usa un **multímetro o pinza Bluetooth con Data Logging** junto al interruptor bypass ([Guía de Serie](/es/2026/parasitic-drain-tester-guide.html)) para grabar 12–24 horas y ver los picos en una gráfica.

---

## 4. Circuito localizado, pero la fuga sigue: CAN-BUS sin dormir

Los módulos modernos se despiertan entre sí por CAN-BUS / LIN-BUS. Si el cuadro o la BCM consumen `300mA`, muchas veces están sanos y **otro componente averiado en la red (p. ej. sensor de lluvia o antena de manija en LIN-BUS) los mantiene despiertos**.

### 1. Comprobación sin desmontar: medir reposo CAN-BUS en OBD2

![Diagrama de pines CAN-BUS OBD2](/images/obd2-pinout.webp)

Pon el multímetro en **DC V** y mide suavemente con puntas finas (sin forzar los pines hembra):
* **Medir CAN-H**: Punta roja al **Pin 6**, punta negra al **Pin 4** (o Pin 5 masa).
* **Medir CAN-L**: Punta roja al **Pin 14**, punta negra al **Pin 4** (o Pin 5).

Lectura:
* **Reposo profundo**: Ambas lecturas caen cerca de **`0.0V`**.
* **Red activa**: CAN-H ronda **`2.5V ~ 2.8V`** y CAN-L **`2.2V ~ 2.5V`** con ligeras variaciones; algún módulo sigue hablando.

> **Dos advertencias clave:**
> 1. **Aislamiento por Gateway**: Muchos coches recientes llevan **Central Gateway (SGW)** que aísla el OBD2 en `0.0V` cuando no hay escáner, aunque la red interior esté despierta. En ese caso mide en el **concentrador CAN (CAN Hub)**.
> 2. **Nunca uses ohmios o amperios**: Podrías dañar los transceptores de comunicación.

### 2. Aislamiento avanzado: desconectar "comunicación", no "fusibles"
Confirmado que la red no duerme, localiza el **CAN Hub** mientras vigilas el consumo total y desconecta sus conectores de comunicación uno a uno (sin cortar alimentación). Si al soltar uno el voltaje cae a `0V` y el consumo baja de `30mA` en segundos, ese nodo es el culpable.

---

## 5. Atajo visual: Cámara térmica

Para mazos estrechos o humedad bajo la moqueta y en puertas, una cámara térmica para móvil es ideal. Todo componente que disipe `100mA ~ 300mA+` de forma continua (bobina de relé energizada, chip con fuga, conector sulfatado) lucirá **2°C ~ 5°C** más caliente que el entorno.

* **Consejo práctico**: Deja enfriar el coche por completo (**2–3 horas** o toda la noche) antes de escanear. Revisa cajas de fusibles, relés, zonas de filtración (desagües del techo solar, piso, hueco de rueda de repuesto) y accesorios añadidos; evita apuntar a metal brillante desnudo por los reflejos.

---

## 6. Lista de verificación avanzada DIY

1. **Descartar batería**: Desconecta el negativo 24h y mide voltaje para descartar autodescarga o baja carga por IBS.
2. **Quitar externos**: Desenchufa todo del OBD2 y tomas de 12V, y aleja las llaves inteligentes.
3. **Consumo total y caída**: Mide consumo total y alternador B+ con [Pinza DC](/es/2026/dc-clamp-meter-parasitic-drain-guide.html), luego escanea todas las cajas de fusibles (incluidas ocultas) por [Caída de Tensión](/es/2026/fuse-voltage-drop-parasitic-drain-guide.html).
4. **Si todo da `0.0 mV`**: Revisa cables directos (alternador, ventilador, arranque), fusibles grandes/JCASE con pinza y cables directos de accesorios.
5. **Duerme ahora, muere mañana**: Graba 12–24h con data logger para cazar despertares (manijas Keyless, telemática).
6. **Fuga localizada sin solución**: Mide OBD2 Pin 6/14 (o CAN Hub) para ver si la red no duerme y usa cámara térmica para hallar puntos calientes.
