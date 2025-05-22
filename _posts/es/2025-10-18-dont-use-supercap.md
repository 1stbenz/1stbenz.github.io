---
layout: post
title: "Baterías de hierro-litio versus supercondensadores: ¿cómo elegir?"
lang: es
date:   2025-10-18 10:08:30
categories: Auto
tags: [Litio-ferro-bato, supercapacitores, modificacións automotrices, actualización do sistema eléctrico, CCA, impuesto de la estúpida inteligencia (o "impuesto a los tontos")]
description: "¿Sigue dudando entre actualizar a una batería de iones de litio o instalar un supercondensador? Este artículo analiza mediante fórmulas en paralelo, principios de división de corriente y datos reales de resistencia interna para revelar por qué las baterías de iones de litio vencen claramente al supercondensador y por qué los condensadores externos pueden ser una \"actualización negativa\" que cuesta dinero y daña el vehículo."
keywords: "Litio-ferro-bato, supercapacitor, sistema eléctrico automotriz, corriente inversa, regulador de voltaje, resistencia interna, beneficios del tuning, CCA, impuesto a la inteligencia artificial (o simplemente: impuestos innecesarios)"
image: /images/mobile01-4354e3784c5b7a8a13113354d8a13b2f.webp
faq:
  - question: "¿Qué recomendación hace el artículo sobre la elección entre supercondensadores y baterías de litio-ferro-fosfato para una actualización del sistema eléctrico automotor?"
    answer: "El artículo señala directamente que instalar un supercondensador no solo es costoso, sino incluso una \"actualización negativa\", y recomienda actualizar directamente a baterías de litio-ferro-fosfato (LiFePO₄)."
  - question: "¿Qué explica la fórmula de la impedancia total en paralelo?"
    answer: "La fórmula de la impedancia total en paralelo muestra que si una componente tiene una impedancia mucho menor que otra, entonces el margen de mejora de la impedancia total será muy limitado."
  - question: "¿Qué significa el principio de división de corriente en las actualizaciones del sistema eléctrico?"
    answer: "La corriente prefiere seguir la ruta con menor impedancia (resistencia interna). Cuando una carga necesita un gran flujo de corriente instantáneo, quien tenga menor resistencia interna es quien se encarga de proveer la energía."
  - question: "¿Por qué las baterías de hierro-litio por sí mismas son suficientes para satisfacer los requisitos de rendimiento del vehículo?"
    answer: "Las baterías de hierro-litio tienen una resistencia interna extremadamente baja, un alto factor de descarga (C-rate) y una velocidad de reacción muy rápida; su capacidad de descarga supera la función «asistencia» que puede proporcionar el supercondensador."
  - question: "¿Qué efecto tiene conectar en paralelo una batería de hierro-litio con un supercondensador?"
    answer: "La resistencia interna directa de la batería de hierro-litio es aproximadamente 2–3 mΩ, mientras que la del módulo de condensadores comercializado oscila entre 20 y 30 mΩ. Según las fórmulas de conexión en paralelo y el principio de división de corriente, la mejora total en la resistencia interna tras conectarlos en paralelo es mínima (aproximadamente 0,15 mΩ), por lo que la corriente sigue siendo asumida principalmente por la batería de hierro-litio debido a su menor resistencia, dejando al condensador prácticamente sin utilidad."
  - question: "¿Cuál es la capacidad de los supercondensadores para el sistema eléctrico del automóvil?"
    answer: "La capacidad comercial de los supercondensadores automotrices es muy pequeña; por ejemplo, 15V / 86F equivale a aproximadamente 0.36Ah y 15V / 20F equivale a aproximadamente 0.08Ah. Estas capacidades son mucho menores que las de la batería de hierro-litio del automóvil (que puede alcanzar los 100Ah) y, tras una descarga instantánea, el voltaje cae rápidamente."
  - question: "¿Por qué es engañoso lo que el vendedor afirma sobre el «aumento instantáneo del CCA»?"
    answer: "Lo que muestra el vendedor como un aumento en el CCA, de hecho, son solo números obtenidos cuando el instrumento de prueba se engaña con una baja resistencia interna. La verdadera capacidad de arranque es la entrega continua y estable de grandes corrientes eléctricas, lo cual es precisamente la fortaleza de las baterías LiFePO4, no algo que pueda compararse con supercondensadores de muy pequeña capacidad."
  - question: "¿Cómo se comporta la vida útil de los supercondensadores en el entorno de alta temperatura del compartimento del motor?"
    answer: "En un ambiente a 65°C, la vida útil de los supercondensadores es solo aproximadamente 1000 horas. El calor acelera la evaporación del electrolito, lo que resulta en un aumento de la resistencia interna y una degradación de la capacidad, acortando significativamente su duración. En comparación, las baterías de hierro-litio pueden mantener miles de ciclos a temperaturas entre 45°C y 60°C, con una vida útil calculada en años."
  - question: "¿Cómo afecta el problema de la autodescarga del supercondensador al sistema eléctrico automotor?"
    answer: "Los supercondensadores tienen una tasa de autodescarga más alta (del orden de varios mA hasta cientos de mA), por lo que incluso sin uso, continúan perdiendo carga. Después de días de estacionar el vehículo, la tensión disminuye significativamente y se convierte en una carga adicional para la batería principal, obligándola a recargar al condensador."
  - question: "¿Qué riesgos adicionales podrían traer los supercondensadores externos?"
    answer: "Los supercondensadores externos conllevan riesgos de instalación (el cableado adicional puede sufrir desgaste y cortocircuitos, o convertirse en proyectiles durante una colisión) y riesgos del producto (existen fallos que han provocado cortocircuitos, altas temperaturas e incluso incendios). Por otro lado, las baterías de hierro-litio son actualizaciones originales con un sistema 'cambio por uno', tienen alta integración relativa seguridad."
  - question: "¿Por qué se dice que el mercado de los supercondensadores ha terminado?"
    answer: "Cuando las baterías de hierro-litio eran caras, existía un nicho para los supercondensadores. Sin embargo, ahora la marca automotriz ofrece baterías de 100Ah a un precio mucho más bajo, alrededor de NT$12.000, y las baterías de 5,5Ah para motocicletas cuestan aproximadamente NT$2.500, lo que ha reducido significativamente el valor por dólar de los supercondensadores."
  - question: "¿Qué recomendación hace el artículo sobre cómo «invertir en lo esencial»?"
    answer: "Se recomienda ahorrar del presupuesto destinado a comprar supercondensadores e invertir directamente en una batería de hierro-litio de buena calidad. Esto se considera la forma más directa y efectiva de mejorar el sistema eléctrico, ya que los condensadores paralelos son ineficaces para las baterías de hierro-litio, mientras que cambiar por una batería de hierro-litio es más rentable y seguro que usar condensadores en paralelo con baterías de plomo-ácido."
  - question: "¿La parte inicial del artículo dice que la capacidad de los supercondensadores es pequeña, pero luego afirma que son demasiado grandes para filtrar; ¿no sería eso contradictorio?"
    answer: "No hay contradicción; se trata de diferentes referencias. La capacidad de un supercondensador es extremadamente pequeña «en comparación con una batería automotriz» (menos de 0,4 Ah), por lo que no puede alimentar durante largos periodos; pero es inmensa «en comparación con los condensadores de filtrado de alta frecuencia» (son millones de veces más grandes que un condensador de filtrado ordinario). Debido a que la capacidad y la inductancia interna son demasiado altas, reaccionan lentamente ante las interferencias de alta frecuencia, por lo tanto no pueden lograr el efecto de «purificación del suministro eléctrico para audio», entre otros efectos de filtrado de alta frecuencia, que se suelen anunciar en los anuncios comerciales."
---

[alt]Título de la imagen[/alt]

Si dispone de un presupuesto y desea mejorar el rendimiento eléctrico del vehículo, podría encontrarse con una decisión difícil:

👉 ¿Es mejor invertir en instalar un «supercondensador»?  
👉 O simplemente actualizar a una batería de litio-ferro-fosfato (LiFePO₄)?

Te lo digo directamente: instalar un supercondensador no es solo una inversión costosa, sino incluso una "desaceleración".

---


## Principios básicos de electricidad: fórmulas en paralelo y efecto divisorio de corriente


Antes de discutir, repasemos dos conceptos clave:


### 1. Fórmula en paralelo
La fórmula para la impedancia total de los resistores en paralelo es: ([calculadora de resistencia interna en paralelo](/es/2026/ir-caculator.html))  
<p>
  R<sub>impedancia_total</sub> = 
  <span style="display: inline-block; vertical-align: middle; text-align: center;">
    <span style="display: block; border-bottom: 1px solid currentColor; padding: 0 2px;">R<sub>resistencia_interna_batería</sub> × R<sub>resistencia_interna_capacitor</sub></span>
    <span style="display: block; padding: 0 2px;">R<sub>resistencia_interna_batería</sub> + R<sub>resistencia_interna_capacitor</sub></span>
  </span>
</p>

Esto significa que: **si la impedancia de uno es mucho menor que la del otro, el margen de mejora de la impedancia total es muy limitado**.


### 2. Principio de división del flujo
La corriente, como el agua, siempre prefiere seguir la ruta con **menor impedancia (resistencia interna)**. Cuando una carga (como un motor de arranque o graves profundos) necesita un gran flujo de corriente instantáneo, quien tenga menor resistencia interna es quien se encarga de suministrarla.

---


## Razón 1: Las baterías de hierro-litio son en sí mismas bestias de rendimiento.


El diseño original de los supercondensadores fue para compensar las deficiencias de las baterías aluminio-hidrógeno tradicionales, como la alta resistencia interna y la lenta reacción química.

Pero las baterías de ion de litio poseen intrínsecamente:

- Bajas resistencias internas [(imagen)](/images/greenrun_ir.webp)
- Alta tasa de descarga (tasa C)
- Respuesta muy rápida [(análisis)](/es/2025/lithium-vs-lead-analysis.html)

La capacidad de descarga del LiFePO₄ **ya supera con creces la «ayuda» que pueden proporcionar los supercondensadores**.


## Razón 2: La velocidad de respuesta real del módulo de supercondensadores es en realidad más lenta que la de las baterías de hierro-litio.


Los supercondensadores deberían poseer la ventaja física de una «respuesta ultrarrápida», pero los modelos comerciales, tras su modularización, presentan resistencias internas que alcanzan hasta **20 mΩ** (en comparación con las baterías de ion de litio, cuya resistencia interna es solo de aproximadamente **2–3 mΩ**).

Cuando se requiere un gran flujo de corriente instantáneo, una resistencia interna excesiva puede provocar:

- Caída repentina de la presión instantánea  
- La energía no puede entregarse inmediatamente a la carga  
- Grandes cantidades se disipan internamente y se convierten en calor residual

👉 La energía queda bloqueada en la resistencia interna; de hecho, el rendimiento real del descargo transitorio con alta corriente de los supercondensadores es mucho peor que el de las baterías de iones de litio.


## Razón tres: la conexión en paralelo de iones de litio y supercondensores tiene un efecto insignificante


Volvamos a la fórmula en paralelo y al principio de división del flujo mencionados anteriormente:

- Resistencia interna en corriente continua de la batería de hierro-litio: aproximadamente [2–3 mΩ](/images/greenrun_ir.webp).

- Resistencia interna de los módulos capacitores comerciales: aproximadamente [20–30 mΩ](/images/supercap_ir.webp).

Al calcular con la fórmula de paralelo, el GreenRun batería al hierro litio en paralelo con los supercondensadores Eaton reduce solo **aproximadamente 0.15 mΩ** su resistencia interna total; incluso podría ser compensada por la impedancia del cableado. Según el principio de división de corriente, la carga eléctrica es asumida principalmente por las baterías al hierro litio debido a su menor resistencia interna, mientras que los condensadores prácticamente no contribuyen.

La próxima vez que veas a un fabricante hacer propaganda sobre los "efectos mágicos" de los supercondensadores, fíjate bien en sus objetos de comparación. La gran mayoría son **"capacitores en paralelo vs. plomo-ácido original"** (o sea: el propio sistema del fabricante).
Casi nunca muestran datos como **"capacitores en paralelo vs. una sola celda de litio"**, porque eso demostraría que se ha gastado mucho dinero y, sin embargo, **no hay prácticamente ninguna diferencia**.


## Cuarto motivo: la alta autodescarga del condensador


Además de su baja capacidad y sensibilidad a altas temperaturas, los supercondensadores presentan el problema del "autodescarga rápida". Incluso cuando no se utilizan, siguen [descargándose continuamente](https://passive-components.eu/wp-content/uploads/2025/10/6_3_Vishay-How-to-Manage-Leakage-Current-and-Self-Discharge-of-EDLC-Capacitors.pdf), con un nivel de autodescarga que depende del tipo específico.

- Supercondensadores: de unos pocos mA hasta cientos de mA.
- Baterías de ion litio: solo decenas de µA.
*(1 mA = 1000 µA)*

Si el vehículo se estaciona durante varios días, la tensión de los supercondensadores disminuye significativamente, convirtiéndose en una carga adicional para las baterías (las cuales están obligadas a recargar los condensadores).


## Cinco razones: los parches traen riesgos adicionales


- **Riesgo de instalación**: Los cables adicionales pueden sufrir desgaste o cortocircuitos, y en caso de colisión incluso convertirse en proyectiles.
- **Riesgo del producto**: Se han registrado fallos en supercondensadores que provocaron cortocircuitos con altas temperaturas, lo que ha resultado en incendios vehiculares graves.

En contraste, las baterías de hierro litio son una actualización del fabricante con un reemplazo uno a uno:

- Alta integración  
- Estructura estable  
- En caso de fallo por envejecimiento, solo se produce expansión; alta seguridad.


## Seis razones: las baterías de iones de litio se han vuelto accesibles


En el pasado, las baterías de hierro-litio eran costosas y los supercondensadores tenían espacio en el mercado. Ahora, la precio del litio ha disminuido drásticamente:

- Batería de hierro-litio para automóviles de 100 Ah: aproximadamente [NT$12,000](https://www.facebook.com/share/1HUfunrZu2/)
- Batería de hierro-litio para motocicletas de 5.5 Ah: aproximadamente NT$2,500

👉 Dado que las baterías de ion litio son asequibles, **¿por qué gastar miles de dólares en un supercondensador con menos de 0.4 Ah, alta resistencia interna y respuesta lenta, sensible al calor y que «gasta electricidad»?**


## Razón 7: La capacidad de los supercondensadores es «demasiado grande» para el filtrado.


La capacidad de los supercondensadores se encuentra en una posición incómoda: son demasiado pequeños para las baterías y demasiado pesados para la filtración. En el mundo de la filtración, solo lo rápido es verdad.

* **Efectos secundarios de gran capacidad:** La estructura del supercondensador es compleja y su respuesta ante el ruido de alta frecuencia es extremadamente lenta. Antes incluso de poder reaccionar, el ruido ya ha penetrado.
* **Amortiguación de energía de baja frecuencia:** Las baterías de iones de litio son actualmente la solución óptima para el amortiguamiento de baja frecuencia; los supercondensadores resultan excesivos en este contexto.
* **Eliminación del ruido de alta frecuencia:** El filtrado verdaderamente efectivo requiere un enfoque "a medida". Como se ha visto con las corrientes inversas tempranas, es necesario combinar varios tipos de condensadores de pequeña capacidad (como los electrolíticos, cerámicos o de película) para interceptar con precisión diferentes frecuencias de ruido. Los supercondensadores son completamente inútiles frente al ruido de alta frecuencia debido a su gran tamaño, lentitud y un ESL asombrosamente alto.

La instalación de supercondensadores para el «filtrado» y la mejora del sistema eléctrico es completamente innecesaria en la actualidad, cuando las baterías de hierro litio se han vuelto accesibles.


## Invertir en el punto crítico del cuchillo


En resumen, la era de los supercondensadores en el mercado de modificaciones para automóviles ha terminado.

- Si utilizas una batería de ion de litio: el condensador en paralelo es **ineficaz**, ya que la densidad energética del ión de litio supera a la del condensador, por lo que su contribución es mínima.  
- Si utilizas baterías de plomo-ácido: conectar un condensador en paralelo no es rentable, porque reemplazarlas directamente con una batería de ion de litio ofrece un rendimiento superior y mayor seguridad.

💡 Ahorre el presupuesto para comprar un supercondensador e invierta directamente en una batería de hierro-litio de alta calidad. Es la forma **más directa y efectiva** de mejorar su sistema.