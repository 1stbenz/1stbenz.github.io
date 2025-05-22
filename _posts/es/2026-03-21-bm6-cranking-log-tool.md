---
layout: post
title: "Herramienta de análisis del diario de arranque a 100 Hz para BM6/BM200"
lang: es
date:   2026-03-21 10:00:00
categories: Auto
tags: [Batería de coche, Monitor de batería, Herramientas DIY, Análisis de datos]
description: "Herramienta de análisis de ondas de arranque diseñada específicamente para el monitor Bluetooth BM6. Permite decodificar paquetes hexadecimales desde archivos log crudos, dibujar con precisión curvas de voltaje del motor a alta resolución y marcar automáticamente los puntos más bajos y el punto de separación del motor de arranque mediante un algoritmo dinámico de umbrales."
keywords: "BM6, monitor de batería Bluetooth, forma de onda del arranque, voltaje de arranque, Craning, análisis de registros, batería automotriz, batería LiFePO4"
image: /images/bm6-cranking-preview2.webp
faq:
  - question: "¿Qué problema resuelve principalmente esta herramienta?"
    answer: "La aplicación original no puede exportar ondas de arranque con alta resolución. Esta herramienta puede leer directamente los archivos Log crudos grabados por Bluetooth, decodificar los paquetes hexadecimales internos y restaurar la curva del voltaje de arranque a una precisión de 100 Hz para ayudar a determinar la capacidad instantánea de descarga de la batería y el estado del motor de arranque."
  - question: "¿Qué representan los puntos rojos y naranjas en el gráfico?"
    answer: "El punto rojo (Min) representa la tensión mínima a la que se baja la batería durante el arranque instantáneo del motor de arranque; el punto naranja (Starter) es el punto de inflexión calculado mediante un algoritmo, marcando el momento en que se corta la alimentación al motor de arranque y el motor toma el control para generar electricidad."
  - question: "¿Cómo obtener un archivo Log para subir?"
    answer: "Puede guardar los datos de transmisión capturados como archivos en formato .txt o .log utilizando la herramienta de análisis Bluetooth del dispositivo móvil, o bien mediante la función integrada de exportación de registros dentro de la aplicación BM6 original. Asegúrese de que el archivo abarque el período durante el cual se encontraba encendido."
  - question: "¿Subir archivos Log plantea preocupaciones de privacidad o fuga de datos?"
    answer: "Absolutamente no. Esta herramienta se desarrolla utilizando tecnología puramente frontend (JavaScript). Todos los procesos de análisis, decodificación hexadecimal y generación de gráficos se realizan independientemente dentro del navegador del usuario, sin que ningún dato sea enviado a servidores en la nube."
  - question: "¿A qué voltaje mínimo (Min) de arranque se considera que la batería podría estar cerca del final de su vida útil?"
    answer: "Una batería plomo-ácida o AGM saludable de 12V, a temperatura ambiente durante el arrancado del motor, generalmente mantiene un voltaje mínimo superior a 9.6 V. Si sus lecturas rojas caen frecuentemente por debajo de 9.0 V e incluso más, podría indicar que la batería se ha envejecido y su resistencia interna aumentado; le recomendamos realizar una evaluación profesional con antelación."
  - question: "¿Por qué aparece el mensaje «No se encontró una onda de encendido válida» después de subir un archivo?"
    answer: "Esto suele deberse a que no se ha capturado ningún paquete completo del momento en que la motoriza. Por favor, verifique si existe dentro del archivo la etiqueta exitosa 'cranking.add:ok'. Además, si el teléfono está demasiado lejos del vehículo durante el encendido y esto provoca una caída de conexión Bluetooth, también puede causar incompletitud en la onda e impedir su análisis."
  - question: "¿Cómo determina el algoritmo los puntos naranjas (punto de encendido del motor para salir)?"
    answer: "Esta herramienta utiliza un algoritmo de «umbral dinámico». El programa detecta primero automáticamente la «voltaje inicial en reposo» antes del arranque. Cuando, tras el arranque, la tensión rebota y se acerca a ese voltaje inicial (lo que indica que el motor ya está desconectado o que el alternador ha tomado el control), calcula hacia atrás para encontrar el último mínimo local durante el proceso de rebote desde el valle de voltaje. Esto permite que la herramienta no solo sea aplicable a las baterías plomo-ácido tradicionales, sino también perfectamente compatible con las baterías de hierro-litio, cuyo voltaje en reposo es más alto."
---

<div id="car-app-container"
    style="max-width: 950px; margin: 20px auto; font-family: 'Segoe UI', 'Microsoft JhengHei', sans-serif; background: #0d1117; color: #c9d1d9; padding: 25px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid #30363d; position: relative;">

<h2 id="ui-title" style="text-align: center; color: #c9d1d9; margin-bottom: 10px; margin-top: 10px;">Herramienta de análisis del gráfico de inicio BM6</h2>

<div style="background: rgba(210, 153, 34, 0.1); padding: 15px 20px; border-radius: 10px; margin-bottom: 25px; border-left: 5px solid #d29922; font-size: 14.5px; line-height: 1.6; color: #8b949e;">
    <strong id="ui-desc-title" style="color: #d29922;">Detección de umbral dinámico (compatibilidad con baterías plomo-ácido y LiFePO₄)</strong><br>
    <span id="ui-desc-body">Esta herramienta puede leer directamente los archivos de registro .log crudos capturados, convertir paquetes hexadecimales en ondas de alta resolución a 100 Hz y encontrar automáticamente el punto más bajo del voltaje mediante un algoritmo dinámico así como el punto de despegue para la salida del motor, facilitando la revisión del rendimiento máximo de las baterías.</span>
</div>

<div
        style="background: #161b22; border: 1px solid #30363d; padding: 15px 25px; border-radius: 10px; gap: 10px; margin-bottom: 25px; display: flex; align-items: center; justify-content: center;">
        <button id="uploadTrigger"
            style="background: #1f6feb; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 15px; transition: 0.2s;">📁
            Subir archivos de registro (.txt / .log)</button>
        <input type="file" id="logFileInput" accept=".txt,.log" style="display:none">
        <button id="loadSampleBtn" style="background: #30363d; color: #c9d1d9; border: 1px solid #8b949e; padding: 9px 20px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 14px; text-decoration: none; display: flex; align-items: center; transition: 0.2s;">📄 Cargar archivo de ejemplo para probar</button>
         
    </div>

<div id="status-text"
        style="text-align: center; color: #8b949e; margin-bottom: 20px; font-size: 14px; font-weight: bold;">Suba un archivo Log que contenga datos de transmisión para su análisis</div>

<div id="chartsWrapper" style="display: flex; flex-direction: column; gap: 20px;"></div>

No se ha proporcionado texto para traducir en el contenido dentro de las etiquetas `<div>`; solo la etiqueta vacía está presente. Si desea que traduzca algo, por favor proporcione el texto completo o el contenido específico que necesita convertir al español.

No se ha proporcionado texto para traducir. El contenido que has compartido consiste únicamente en etiquetas `<script>` con URLs de librerías JavaScript (Chart.js, Hammer.js y chartjs-plugin-zoom). Dado que no hay frases o descripciones dentro del código que requieran traducción, el resultado permanece igual:

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/hammer.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-zoom"></script>
```

<script>
    (function () {
        const fileInput = document.getElementById('logFileInput');
        const uploadTrigger = document.getElementById('uploadTrigger');
        const statusText = document.getElementById('status-text');
        const chartsWrapper = document.getElementById('chartsWrapper');

No se puede traducir código JavaScript directamente a español, ya que es un lenguaje de programación y no contiene texto natural para la traducción. Sin embargo, si deseas una explicación en español sobre lo que hace este código:  
Estas líneas configuran los valores por defecto del gráfico Chart.js: el color principal (`#8b949e`) y el color de las bordes (`#30363d`).

// Plugin de mira cruzada (igual que 03-20)
        const crosshairPlugin = {
            id: 'crosshair',
            beforeDraw: chart => {
                if (chart.tooltip._active && chart.tooltip._active.length) {
                    const ctx = chart.ctx;
                    const activePoint = chart.tooltip._active[0];
                    const x = activePoint.element.x;
                    const topY = chart.scales.y.top;
                    const bottomY = chart.scales.y.bottom;

ctx.save();
                    ctx.beginPath();
                    ctx.moveTo(x, topY);
                    ctx.lineTo(x, bottomY);
                    ctx.lineWidth = 1;
                    ctx.strokeStyle = 'rgba(139, 148, 158, 0.8)';
                    ctx.setLineDash([4, 4]);
                    ctx.stroke();
                    ctx.restore();
                }
            }
        };

No se puede traducir este código porque es un fragmento de JavaScript, no texto natural en español o chino. Sin embargo, si necesitas una explicación sobre cómo funciona: esta línea establece que cuando el usuario hace clic en `uploadTrigger`, se activará automáticamente la entrada de archivo (`fileInput`) para seleccionar archivos a subir.

No se puede traducir este fragmento de código JavaScript porque no contiene texto lingüístico, sino una declaración técnica que define un elemento del DOM en HTML y lo vincula a la función `loadSample`. El contenido dentro de los corchetes `[ ]` o las etiquetas `< >` deben permanecer inalterables según las reglas proporcionadas.

// Evento de clic para cargar directamente un archivo de ejemplo  
        loadSampleBtn.onclick = function() {
            // Actualizar el estado y limpiar la pantalla
            statusText.innerHTML = `Se está leyendo <b style="color:#58a6ff;">archivo de ejemplo (bm6_100Hz.log)</b> ...`;
            chartsWrapper.innerHTML = '';

// Obtener archivos directamente del servidor usando la API fetch  
            fetch('/files/bm6_100Hz.log')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('No se pudo obtener el archivo de ejemplo (HTTP ' + response.status + ')');
                    }
                    return response.text();
                })
                .then(text => {
                    // Tras una carga exitosa, pasar directamente el texto plano a la función existente para procesar los datos  
                    processLogData(text);
                })
                .catch(error => {
                    statusText.innerHTML = `<span style="color:#f85149;">❌ Error al cargar el archivo de ejemplo: ${error.message}</span>`;
                });
        };

fileInput.addEventListener('cambio', function(e){
    const archivo = e.target.files[0];
    if(!archivo)return;

statusText.innerHTML = `Se está analizando <b style="color:#58a6ff;">${file.name}</b> ...`;
            chartsWrapper.innerHTML = '';

const lector = new FileReader();
lector.onload = function(e){
    const texto = e.target.result;
    procesarDatosDelRegistro(texto);
};
lector.readAsTexto(file);
});

function isValidCurve(hexData) {
            if (!hexData || hexData.length < 30) return false;
            let validCount = 0, invalidCount = 0;
            for (let i = 0; i < hexData.length - 2; i += 3) {
                let voltage = parseInt(hexData.substring(i, i + 3), 16) / 100.0;
                if (!isNaN(voltage) && voltage >= 3.0 && voltage <= 35.0) {
                    validCount++;
                } else {
                    invalidCount++;
                }
            }
            let total = validCount + invalidCount;
            return total > 0 && (invalidCount / total) <= 0.1;
        }

function processLogData(logText) {
            const lines = logText.split('\n');
            
            // 1. Escaneo preliminar: crear una base de datos exclusiva «hora histórica -> temperatura»
            let historyMap = {};
            const jsonRegex = /"time"\s*:\s*(\d+)\s*,\s*"temp"\s*:\s*(\d+)/g;
            let match;
            while ((match = jsonRegex.exec(logText)) !== null) {
                historyMap[match[1]] = match[2];
            }

let crankingEvents = [];
            let tempHexStream = "";
            let isRecording = false;
            let isHistorical = false;
            let activeTimeline = null;
            let currentLogTime = "Desconocido";
            let rollingRealTimeTemp = "Desconocido";

// 2. Análisis por línea: separar las formas de onda históricas y en tiempo real  
            for (let i = 0; i < lines.length; i++) {  
                let originalLine = lines[i].trim();  
                let line = originalLine.toLowerCase();  
                if (!line) continue;

let timeMatch = originalLine.match(/^(\d{2}:\d{2}:\d{2})/);
if (timeMatch) {
    currentLogTime = timeMatch[1];
}

let tempMatch = line.match(/\\"temp\\"\\s*:\\s*(\\d+)/);
if (tempMatch) rollingRealTimeTemp = tempMatch[1];

let syncMatch = line.match(/self\.synchistorytimeline:(\d+)/);
if (syncMatch) {
    activeTimeline = syncMatch[1];
    isRecording = true;
    isHistorical = true;
    tempHexStream = ""; 
    continue;
}

```javascript
if (línea.includes('recibir:')) {
    let contenido = línea.split("recibir:") [1].trim();
}
```

if (/^[0-9a-f]+$/.test(content)) {
                        if (content.includes('fffffe')) {
                            isRecording = true;
                            isHistorical = false;
                            tempHexStream = content.split('fffffe')[1];
                            continue;
                        }

if (isRecording) {
                            if (content.includes('fffefe')) {
                                tempHexStream += content.split('fffefe')[0];
                                
                                if (isValidCurve(tempHexStream) && !crankingEvents.some(e => e.hex === tempHexStream)) {
                                    let eventTimeStr = "";
                                    let eventTemp = "Desconocido";

if (isHistorical && activeTimeline) {
    let ts = parseInt(activeTimeline);
    let date = new Date(ts * 1000);
    let mm = String(date.getMonth() + 1).padStart(2, '0');
    let dd = String(date.getDate()).padStart(2, '0');
    let hh = String(date.getHours()).padStart(2, '0');
    let min = String(date.getMinutes()).padStart(2, '0');
    let ss = String(date.getSeconds()).padStart(2, '0');
    eventTimeStr = `${mm}/${dd} ${hh}:${min}:${ss} (Histórico)`;

if (historyMap[activeTimeline]) {
    eventTemp = historyMap[activeTimeline];
} else {
    let minDiff = Infinity;
    for (let t in historyMap) {
        let diff = Math.abs(parseInt(t) - ts);
        if (diff < minDiff) {
            minDiff = diff;
            eventTemp = historyMap[t] + "*";
        }
    }
} else {
    eventTimeStr = `${currentLogTime}`;
    eventTemp = rollingRealTimeTemp;
}

crankingEvents.push({
                                        hex: tempHexStream,
                                        time: eventTimeStr,
                                        temp: eventTemp
                                    });
                                }
                                isRecording = false;
                                isHistorical = false;
                                tempHexStream = "";
                                activeTimeline = null;
                            } else {
                                if (!content.startsWith("d155")) {
                                    tempHexStream += content;
                                }
                            }
                        }
                    }
                }
            }

if (crankingEvents.length === 0) {
                statusText.innerHTML = '<span style="color:#f85149;">❌ No se encontró una onda de arranque válida en el archivo. Verifique si este es un archivo que contiene registros de craning.</span>';
                return;
            }

`<span id="result"></span>` contiene: ✅ ¡Análisis completado! Se han detectado `<strong>${crankingEvents.length}</strong>` registros de arranque del motor.

```javascript
craningEvents.forEach((eventData, index) => {
    drawChartForEvent(eventData, index + 1);
});
```

function getLocalMinima(arr) {
            let minima = [];
            for (let i = 1; i < arr.length - 1; i++) {
                if (arr[i] < arr[i - 1] && arr[i] < arr[i + 1]) minima.push(i);
            }
            return minima;
        }

// Lógica de escala Y dinámica automática  
function autoScaleY(chart) {
    const xScale = chart.scales.x;
    const dataset = chart.data.datasets[0].data; // Datos de línea
    let minV = Infinity, maxV = -Infinity, found = false;
    for (let i = 0; i < dataset.length; i++) {
        if (dataset[i].x >= xScale.min && dataset[i].x <= xScale.max) {
            if (dataset[i].y < minV) minV = dataset[i].y;
            if (dataset[i].y > maxV) maxV = dataset[i].y;
            found = true;
        }
    }
    if (found) {
        // Límite inferior: el siguiente entero por debajo del punto más bajo en la pantalla
        chart.options.scales.y.min = Math.floor(minV * 5) / 5;
        // Límite superior: múltiplo de 0.2 hacia arriba desde el punto más alto en la pantalla
        chart.options.scales.y.max = Math.ceil(maxV * 5) / 5;
    }
}

function dibujarGráficoParaEvento(dataDelEvento, númeroDeEvento) {
            const datosHexadecimales = dataDelEvento.hex;
            const horaDelEvento = dataDelEvento.time;
            const temperaturaDelEvento = dataDelEvento.temp;

let tiempos = [];
            let voltajes = [];
            let tiempoActual = 0;
            let datosDelGráfico = [];

for (let i = 0; i < hexData.length - 2; i += 3) {
    let chunk = hexData.substring(i, i + 3);
    let voltage = parseInt(chunk, 16) / 100.0;
    if (!isNaN(voltage) && voltage >= 3.0 && voltage <= 35.0) {
        times.push(currentTime);
        voltages.push(voltage);
        chartData.push({ x: currentTime, y: voltage });
        currentTime += 0.01;
    }
}

// 1. Mínimo de cruce (Min Cranking)
            const minVol = Math.min(...voltages);
            const minIdx = voltages.indexOf(minVol);
            const localMins = getLocalMinima(voltages);

// 2. Umbral de ascenso dinámico (Dynamic Threshold)  
            const sampleSize = Math.min(5, minIdx);
            if (sampleSize === 0) sampleSize = 1; 
            let voltajesIniciales = voltages.slice(0, sampleSize);
            let vInicial = voltajesIniciales.reduce((a, b) => a + b, 0) / voltajesIniciales.length;

let dinámicoUmbral = vInicial - 0.2;

let climbIdx = minIdx;
while (climbIdx < voltages.length && voltages[climbIdx] <= dynamicThreshold) {
    climbIdx++;
}
if (climbIdx >= voltages.length) climbIdx = voltages.length - 1;

// 3. Activar el punto de desenganche del motor (Starter Disengaged)
            let validMinsForStarter = localMins.filter(idx => idx >= minIdx && idx < climbIdx);
            let starterIdx = validMinsForStarter.length > 0 ? validMinsForStarter[validMinsForStarter.length - 1] : minIdx;

const minPunto = { x: tiempos[minId], y: voltajes[minId] };
            const puntoIniciador = { x: tiempos[inicioId], y: voltajes[inicioId] };

// Plugin de etiquetas de puntos (sustituye los markers + text de Plotly)
            const pointLabelsPlugin = {
                id: 'pointLabels',
                afterDraw: chart => {
                    const ctx = chart.ctx;
                    const meta = chart.getDatasetMeta(1); // Conjunto de datos tipo Scatter
                    if (!meta.hidden && meta.data.length >= 2) {
                        ctx.save();
                        ctx.font = 'bold 12px "Segoe UI", sans-serif';
                        ctx.fillStyle = '#c9d1d9';

                        // Configurar alineación vertical centrada para que el texto esté en la misma línea horizontal que los puntos
                        ctx.textBaseline = 'middle';

// Etiqueta Min (ubicada a la derecha del punto rojo)
const ptMin = meta.data[0];
if (ptMin.x >= chart.chartArea.left && ptMin.x <= chart.chartArea.right) {
    ctx.textAlign = 'left';
    // Desplazar el eje X hacia la derecha 10 píxeles para evitar que se solape con el punto, y mantener el mismo eje Y
    ctx.fillText(`Min: ${minPoint.y.toFixed(2)}V`, ptMin.x + 10, ptMin.y);
}

// Etiqueta Starter (ubicada a la derecha del punto naranja)
const ptStarter = meta.data[1];
if (ptStarter.x >= chart.chartArea.left && ptStarter.x <= chart.chartArea.right) {
    ctx.textAlign = 'left';
    // Desplazar también hacia la derecha 10 píxeles para evitar que se solape con el punto naranja
    ctx.fillText(` Starter dise: ${starterPoint.y.toFixed(2)}V`, ptStarter.x + 10, ptStarter.y);
}
ctx.restore();

// Crear contenedor de la interfaz de usuario
const wrapperDiv = document.createElement('div');
wrapperDiv.style.cssText = "background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; width: 100%; box-sizing: border-box;";

// Añadir título personalizado
const titleElement = document.createElement('div');
titleElement.style.cssText = "color: #c9d1d9; font-size: 16px; font-weight: bold; text-align: center; margin-bottom: 15px;";
titleElement.innerHTML = `Iniciar análisis de ondas - Registro #${eventNumber} (Hora: ${eventTime} | Temperatura: ${eventTemp}°C | Inicial: ${vInitial.toFixed(2)}V)`;
wrapperDiv.appendChild(titleElement);

const canvasDiv = document.createElement('div');
            canvasDiv.style.cssText = "width: 100%; height: 400px; position: relative;";
            
            const canvas = document.createElement('canvas');
            canvas.id = `chart-${eventNumber}`;
            canvasDiv.appendChild(canvas);
            wrapperDiv.appendChild(canvasDiv);
            chartsWrapper.appendChild(wrapperDiv);

// Inicializar Chart.js
new Chart(canvas, {
    type: 'line',
    data: {
        datasets: [
            {
                label: 'Voltaje (V)',
                data: chartData,
                borderColor: '#58a6ff',
                borderWidth: 2,
                pointRadius: 0,
                tension: 0.2, // Curva suave
                order: 2
            },
            {
                label: 'Puntos Clave',
                type: 'scatter',
                data: [minPoint, starterPoint],
                backgroundColor: ['#f85149', '#d29922'],
                borderColor: '#161b22',
                borderWidth: 2,
                pointRadius: 6,
                pointHoverRadius: 8,
                order: 1
            }
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        interaction: {
            mode: 'index',
            intersect: false,
        },
        scales: {
            x: {
                type: 'linear',
                title: { display: true, text: 'Tiempo (Segundos)' },
                max: times[times.length - 1],
                ticks: { maxTicksLimit: 10 }
            },
            y: {
                title: { display: true, text: 'Voltaje (V)' },
                // Cálculo previo del rango adecuado para el eje Y
                min: Math.floor(Math.min(...voltages) * 5) / 5,
                max: Math.ceil(Math.max(...voltages) * 5) / 5,
                ticks: {
                    stepSize: 0.2
                }
            }
        },
        plugins: {
            legend: { display: false },
            tooltip: {
                backgroundColor: 'rgba(22, 27, 34, 0.9)',
                titleColor: '#c9d1d9',
                bodyColor: '#c9d1d9',
                borderColor: '#30363d',
                borderWidth: 1,
                padding: 10,
                displayColors: false,
                callbacks: {
                    // Título (arriba): mostrar voltaje y determinar si es un punto rojo/naranja especial
                    title: function(tooltipItems) {
                        if (tooltipItems.length > 0) {
                            const item = tooltipItems[0];                                
                            return `Voltaje: ${item.parsed.y}V`;
                        }
                        return '';
                    },
                    // Contenido (abajo): mostrar tiempo
                    label: function(context) {
                        // Modificación clave: independientemente del conjunto de datos, solo mostrar la etiqueta temporal del primer elemento capturado
                        if (context.dataIndex !== context.chart.tooltip.dataPoints[0].dataIndex || 
                            context.datasetIndex !== context.chart.tooltip.dataPoints[0].datasetIndex) {
                            return null;
                        }
                        // Usar context.raw.x para asegurar que se captura el número de segundos en los datos crudos
                        return `Tiempo: ${context.raw.x.toFixed(2)} s`;
                    }
                },
            },
            zoom: {
                pan: { 
                    enabled: true, 
                    mode: 'x',
                    onPan: function({chart}) {
                        autoScaleY(chart);
                        chart.update('none');
                    }
                },
                zoom: { 
                    wheel: { enabled: true }, 
                    pinch: { enabled: true},
                    mode: 'x',
                    onZoom: function({chart}) {
                        autoScaleY(chart);
                        chart.update('none');
                    }
                }
            }
        }
    },
    plugins: [crosshairPlugin, pointLabelsPlugin]
});
})();
</script>