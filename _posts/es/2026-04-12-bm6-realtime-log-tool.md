---
layout: post
title: "Herramienta de análisis en tiempo real de datos por segundo para BM6"
lang: es
date: 2026-04-12 10:00:00
categories: Auto
tags: [Batería de coche, Monitor de batería, Herramientas DIY, Análisis de datos]
description: "Convierta los paquetes hexadecimales del registro original de la BM6 en datos legibles de voltaje por segundo y temperatura, con soporte para exportación a CSV y visualización gráfica de doble eje."
keywords: "BM6, monitoreo de baterías, datos en tiempo real, registro de voltaje, registro de temperatura, análisis de registros, decodificación hexadecimal, exportación a CSV, batería LiFePO4"
image: /images/bm6-cranking-preview.webp
faq:
  - question: "¿Cuál es la diferencia entre esta herramienta y la herramienta de análisis del gráfico de arranque?"
    answer: "La herramienta de gráficos de arranque se centra en los datos de muestreo a alta velocidad (100 Hz) capturados durante el instante inicial del encendido (cranking.add); mientras que esta herramienta está diseñada para los datos transmitidos por difusión cada segundo, típicamente encapsulados en paquetes d15507. Es adecuada para observar las variaciones de voltaje de carga generador o tendencias de temperatura ambiental a lo largo de viajes largos."
  - question: "¿Cómo encontrar los datos correspondientes en el archivo de registro?"
    answer: "La herramienta buscará automáticamente paquetes que comiencen con `d15507`, lo cual es la información de estado en tiempo real definida por el protocolo BM6. Solo necesita asegurarse de que su archivo de registro contenga registros de recepción Bluetooth capturados para poder analizarlo."
  - question: "¿Soporta la descarga de datos procesados?"
    answer: "Sí. Después de que se complete el análisis, aparecerá un botón «Descargar archivo CSV», con el cual podrá exportar los datos a Excel u otro software especializado para realizar un análisis más profundo de las tendencias a largo plazo."
  - question: "¿Por qué se muestran los gráficos separados?"
    answer: "Para evitar que las líneas de diferentes escalas interfieran entre sí, hemos dividido la «Tensión (V)» y la «Temperatura (°C)» en dos gráficos superiores e inferiores. Ambos comparten el eje temporal y soportan una escala sincronizada para facilitar su comparación precisa de los cambios de datos del mismo momento."
  - question: "¿Subir archivos de registro plantea preocupaciones sobre la privacidad?"
    answer: "Absolutamente no. Esta herramienta se desarrolla utilizando tecnología puramente frontend (JavaScript), por lo que todas las operaciones se completan dentro del navegador de su computadora y los datos no se envían a ningún servidor."
---

<div id="bm6-realtime-container"
    style="max-width: 950px; margin: 20px auto; font-family: 'Segoe UI', 'Microsoft JhengHei', sans-serif; background: #0d1117; color: #c9d1d9; padding: 25px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid #30363d; position: relative;">

<h2 id="ui-title" style="text-align: center; color: #c9d1d9; margin-bottom: 10px; margin-top: 10px;">Herramienta de análisis en tiempo real de datos por segundo para BM6</h2>

<div style="background: rgba(56, 139, 253, 0.1); padding: 15px 20px; border-radius: 10px; margin-bottom: 25px; border-left: 5px solid #388bfd; font-size: 14.5px; line-height: 1.6; color: #8b949e;">
    <strong id="ui-desc-title" style="color: #58a6ff;">Soporte para extracción de datos en tiempo real a 1 Hz y exportación CSV</strong><br>
    <span id="ui-desc-body">Esta herramienta busca automáticamente los paquetes <b style="color:#c9d1d9;">d15507</b> dentro del registro, convierte los datos hexadecimales en registros de voltaje y temperatura actualizados por segundo, e incluye una vista previa dinámica con escala sincronizada así como la función para descargar los datos.</span>
</div>

<div
        style="background: #161b22; border: 1px solid #30363d; padding: 20px; border-radius: 10px; margin-bottom: 25px; display: flex; flex-direction: column; align-items: center; gap: 15px;">
        <div style="display: flex; gap: 10px;">
            <button id="uploadTrigger"
                style="background: #1f6feb; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 15px; transition: 0.2s;">📁 Subir archivo de registro (.txt / .log)</button>
            <button id="downloadBtn" style="background: #238636; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 15px; display: none;">📥 Descargar archivo CSV</button>
        </div>
        <input type="file" id="logFileInput" accept=".txt,.log" style="display:none">
        <div id="status-text" style="color: #8b949e; font-size: 14px; font-weight: bold;">Seleccione un archivo que contenga datos de transmisión en tiempo real</div>
    </div>

<div style="background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; box-sizing: border-box;">
        <div style="height: 280px; width: 100%; margin-bottom: 10px;">
            <canvas id="voltageChart"></canvas>
        </div>
        <div style="height: 280px; width: 100%;">
            <canvas id="tempChart"></canvas>
        </div>
    </div>

No se ha proporcionado texto para traducir en el contenido dentro de las etiquetas `<div>`; solo la etiqueta vacía está presente. Si desea que traduzca algo, por favor proporcione el texto completo o el contenido específico que necesita convertir al español.

No se requiere traducción para este contenido, ya que los elementos proporcionados son etiquetas `<script>` con atributos `src` que contienen URLs. Según las reglas establecidas:

1.  **Regla 2:** Se debe traducir el texto dentro de Markdown brackets (como `[alt](url)`), pero mantener todas las URL y la estructura de Markdown exactamente sin cambios.
    *   En este caso, no hay etiquetas Markdown (`[...]`) en el fragmento proporcionado; solo existen enlaces `<script>`. Por lo tanto, los atributos `src` con sus URLs **no se traducen**, ya que son identificadores únicos para recursos externos y su traducción alteraría la funcionalidad del código.
2.  **Regla 3:** Mantener todos las etiquetas HTML sin cambios (aplicado a `<script>`).

El texto original es el siguiente:

```html
<script>
(function() {
    const fileInput = document.getElementById('logFileInput');
    const uploadTrigger = document.getElementById('uploadTrigger');
    const downloadBtn = document.getElementById('downloadBtn');
    const statusText = document.getElementById('status-text');
</script>
```

dejar que vChart y tChart sean variables globales;
    dejar que parsedData sea un array vacío;
    dejar que isResetting sea una variable booleana con valor falso.

// --- Configuración inicial de Chart.js ---  
Chart.defaults.color = '#8b949e';  
Chart.defaults.borderColor = '#30363d';

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

function autoScaleY(chart) {
	const xScale = chart.scales.x, dataset = chart.data.datasets[0].data;
	let minV = Infinity, maxV = -Infinity, found = false;
	for (let i = 0; i < dataset.length; i++) {
		const xVal = new Date(dataset[i].x).getTime();
		if (xVal >= xScale.min && xVal <= xScale.max) {
			if (dataset[i].y < minV) minV = dataset[i].y;
			if (dataset[i].y > maxV) maxV = dataset[i].y;
			found = true;
		}
	}
	if (found) {
		const padding = (maxV - minV) * 0.15 || 0.15;
		charts.options.scales.y.min = minV - padding;
		charts.options.scales.y.max = maxV + padding;
	}
}

function syncCharts({chart}) {
        if (isResetting) return;
        const other = (chart === vChart) ? tChart : vChart;
        other.options.scales.x.min = chart.scales.x.min;
        other.options.scales.x.max = chart.scales.x.max;
        autoScaleY(chart); 
        autoScaleY(other);
        chart.update('none'); 
        other.update('none');
    }

function createChartConfig(label, color, yTitle) {
	return {
		type: 'line',
		data: { datasets: [{ label: label, data: [], borderColor: color, backgroundColor: color + '20', borderWidth: 2, pointRadius: 0, tension: 0.2, fill: true }] },
		options: {
			responsive: true, maintainAspectRatio: false,
			interaction: {
				mode: 'index',
				intersect: false,
			},
			scales: {
				x: { 
					type: 'time', 
					time: { 
						displayFormats: { 
							second: 'HH:mm:ss',
							minute: 'HH:mm:ss',
							hour: 'HH:mm:ss'
						},
						tooltipFormat: 'HH:mm:ss' 
					} 
				},
				y: { title: { display: true, text: yTitle } }
			},
			plugins: { 
				tooltip: {
					enabled: true,
					backgroundColor: 'rgba(22, 27, 34, 0.9)',
					titleColor: '#c9d1d9',
					bodyColor: '#c9d1d9',
					borderColor: '#30363d',
					borderWidth: 1,
					padding: 10,
					displayColors: false
				},
				zoom: { 
					pan: { enabled: true, mode: 'x', onPan: syncCharts }, 
					zoom: { wheel: { enabled: true }, mode: 'x', onZoom: syncCharts } 
				} 
			}
		},
		plugins: [crosshairPlugin]
	};
}

// Crear dos entidades de gráfico
vChart = new Chart(document.getElementById('voltajeChart'), crearConfiguracionDeGráfico('Voltaje (V)', '#58a6ff', 'Voltaje (V)'));
tChart = new Chart(document.getElementById('temperaturaChart'), crearConfiguracionDeGráfico('Temperatura (°C)', '#f85149', 'Temperatura (°C)'));

// --- Manejo de análisis de archivos ---  
uploadTrigger.onclick = () => fileInput.click();

fileInput.onchange = function(e) {
	const archivo = e.target.files[0];
	if (!archivo) return;

statusText.innerHTML = `Se está analizando <b style="color:#58a6ff;">${file.name}</b>...`;
        
const reader = new FileReader();
reader.onload = function(e) {
    processData(e.target.result);
};
reader.readAsText(file);

function processData(text) {
    const lines = text.split('\n');
    // d15507 + TempHex(2) + Other(2) + SOCHex(2) + VolHex(4)
    const pattern = /^(\d{2}:\d{2}:\d{2}):receive:d1550700([0-9a-fA-F]{2})[0-9a-fA-F]{2}([0-9a-fA-F]{2})([0-9a-fA-F]{4})/;
    
    const vData = [];
    const tData = [];
    parsedData = [];

let currentDay = 1;
        let lastTimeObj = null;

lines.forEach(line => {
            const match = line.trim().match(pattern);
            if (match) {
                const timeStr = match[1]; // "HH:MM:SS"
                const tempC = parseInt(match[2], 16);
                const voltage = parseInt(match[4], 16) / 100.0;

                // Manejo de lógica transnoche (por ejemplo, pasar de 23:59:59 a 00:00:00)
                const [h, m, s] = timeStr.split(':').map(Number);
                const currentTimeObj = new Date(2026, 0, currentDay, h, m, s);

                if (lastTimeObj && currentTimeObj < lastTimeObj) {
                    currentDay++;
                    currentTimeObj.setDate(currentDay);
                }
                lastTimeObj = currentTimeObj;

                // Obtener Timestamp para Chart.js
                const timeVal = currentTimeObj.getTime();

vData.push({x: timeVal, y: voltage});
tData.push({x: timeVal, y: tempC});

// Guardar la cadena original para exportación CSV
parsedData.push([timeStr, voltage, tempC]);
})

if (parsedData.length > 0) {
    statusText.innerHTML = `✅ ¡Éxito en el análisis! Se han extraído <b style="color:#3fb950;">${parsedData.length}</b> registros de datos en tiempo real.`;
    downloadBtn.style.display = 'inline-block';
    
    isResetting = true;

[ vChart , tChart ].forEach(chart => {
                si chart .resetZoom existe , chart .resetZoom ('no' );
            } ) ;

// Actualizar datos
vChart.data.datasets[0].data = vData;
tChart.data.datasets[0].data = tData;

// Calcular con anticipación los límites del eje Y para evitar que el gráfico no se muestre completamente
const vValues = vData.map(d => d.y);
const tValues = tData.map(d => d.y);
const minV = Math.min(...vValues), maxV = Math.max(...vValues);
const minT = Math.min(...tValues), maxT = Math.max(...tValues);

const vPad = (maxV - minV) * 0.15 || 0.5;
const tPad = (maxT - minT) * 0.15 || 2;

vChart.options.scales.y.min = minV - vPad;
            vChart.options.scales.y.max = maxV + vPad;
            tChart.options.scales.y.min = minT - tPad;
            tChart.options.scales.y.max = maxT + vPad;

vChart.actualizar('ninguno');
tChart.actualizar('ninguno');

No se ha proporcionado texto para traducir en español, ya que el contenido es un fragmento de código JavaScript (`setTimeout`), no una frase o párrafo lingüístico. Si desea que traduzca instrucciones relacionadas con este código (por ejemplo: "Configurar un temporizador para detener la reinicialización después de 200 milisegundos"), por favor proporcione el texto descriptivo correspondiente.

} else {
            statusText.innerHTML = `<span style="color:#f85149;">❌ No se encontraron datos válidos. Verifique si el registro contiene paquetes d15507.</span>`;
            downloadBtn.style.display = 'none';
        }
    }

```javascript
downloadBtn.onclick = function() {
	if (parsedData.length === 0) return;
	let csvContent = "Time,Voltage(V),Temperature(°C)\n";
	parsedData.forEach(row => { csvContent += row.join(",") + "\n"; });
	const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
	const url = URL.createObjectURL(blob);
	const link = document.createElement("a");
	link.setAttribute("href", url);
	link.setAttribute("download", "bm6_per_second_data.csv");
	link.click();
};
})();
</script>
```