---
layout: post
title: "Werkzeug zur Echtzeit-Datenanalyse pro Sekunde für BM6"
lang: de
date: 2026-04-12 10:00:00
categories: Auto
tags: [Autobatterie, Batterieüberwachung, DIY Werkzeuge, Datenanalyse]
description: "Konvertieren Sie die hexagonalen Pakete aus dem ursprünglichen BM6-Protokoll in lesbare Daten für Spannung und Temperatur pro Sekunde, mit Unterstützung der CSV-Erfassung und Visualisierung durch Dual-Achsen-Diagramme."
keywords: "BM6, Batterieüberwachung, Echtzeitdaten, Spannungserfassung, Temperaturerfassung, Protokollierungsparsing, Hexadezimaldecodierung, CSV-Export, Lithium-Eisenphosphat-Batterie"
image: /images/bm6-cranking-preview.webp
faq:
  - question: "Wie unterscheidet sich dieses Werkzeug vom Startwellen-Analyse-Tool?"
    answer: "Das Startwellen-Tool erfasst hochauflösende Abtastdaten mit 100 Hz während des Starts (cranking.add); das vorliegende Tool verarbeitet hingegen Echtzeit-Broadcast-Daten, die einmal pro Sekunde gesendet werden (d15507-Paket). Es eignet sich besonders zur Beobachtung von Schwankungen der Generator-Lade Spannung oder Trends bei der Umgebungstemperatur im Rahmen einer Langstrecke."
  - question: "Wie finde ich die entsprechenden Daten in der Log-Datei?"
    answer: "Das Tool sucht automatisch nach Paketen, die mit `d15507` beginnen. Dies ist Echtzeitdaten gemäß dem BM6-Broadcastprotokoll definiert. Solange Ihre Log-Datei aufgezeichnete Bluetooth-Empfangsnotizen enthält, kann sie analysiert werden."
  - question: "Unterstützt das System die Verarbeitung heruntergeladener Daten?"
    answer: "Ja. Nach der Analyse erscheint ein Button zum Herunterladen einer CSV-Datei, mit dem Sie die Daten in Excel oder andere professionelle Grafiksoftware exportieren können, um eine tiefere langfristige Trendanalyse durchzuführen."
  - question: "Warum werden die Diagramme separat angezeigt?"
    answer: "Um gegenseitige Störungen durch unterschiedliche Skalen zu vermeiden, haben wir \"Spannung (V)\" und \"Temperatur (°C)\" in zwei separate obere und untere Diagramme aufgeteilt. Beide teilen sich eine gemeinsame Zeitachse und unterstützen das同步-Zoomen, was Ihnen ermöglicht, Schwankungen der Daten zum gleichen Zeitpunkt präzise zu vergleichen."
  - question: "Gibt es Datenschutzbedenken beim Hochladen von Logdateien?"
    answer: "Das ist absolut nicht der Fall. Dieses Tool wurde ausschließlich mit reinem Frontend (JavaScript) entwickelt, alle Berechnungen finden auf Ihrem Computer im Browser statt und die Daten werden nicht an einen Server gesendet."
---

<div id="bm6-realtime-container" style="max-width: 950px; margin: 20px auto; font-family: 'Segoe UI', 'Microsoft JhengHei', sans-serif; background-color: #0d1117; color: #c9d1d9; padding: 25px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid #30363d; position: relative;">

<h2 id="ui-title" style="text-align: center; color: #c9d1d9; margin-bottom: 10px; margin-top: 10px;">Werkzeug zur Echtzeit-Datenanalyse von BM6 pro Sekunde</h2>

<div style="background: rgba(56, 139, 253, 0.1); padding: 15px 20px; border-radius: 10px; margin-bottom: 25px; border-left: 5px solid #388bfd; font-size: 14.5px; line-height: 1.6; color: #8b949e;">
    <strong id="ui-desc-title" style="color: #58a6ff;">Unterstützung für Echtzeit-Datenextraktion bei 1 Hz und CSV-Export</strong><br>
    <span id="ui-desc-body">Dieses Tool sucht automatisch nach dem Paket <b style="color:#c9d1d9;">d15507</b> in den Protokolldateien, wandelt die hexadezimalen Daten in eine pro Sekunde aktualisierte Aufzeichnung von Spannung und Temperatur um und bietet einen dynamischen Chart-Vorschau mit synchroner Skalierung sowie Funktionen zum Herunterladen der Daten.</span>
</div>

<div
        style="background: #161b22; border: 1px solid #30363d; padding: 20px; border-radius: 10px; margin-bottom: 25px; display: flex; flex-direction: column; align-items: center; gap: 15px;">
        <div style="display: flex; gap: 10px;">
            <button id="uploadTrigger"
                style="background: #1f6feb; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 15px; transition: 0.2s;">📁 Log-Datei (.txt / .log) hochladen</button>
            <button id="downloadBtn" style="background: #238636; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 15px; display: none;">📥 CSV-Datei herunterladen</button>
        </div>
        <input type="file" id="logFileInput" accept=".txt,.log" style="display:none">
        <div id="status-text" style="color: #8b949e; font-size: 14px; font-weight: bold;">Bitte wählen Sie eine Datei mit Echtzeit-Broadcast-Daten aus</div>
    </div>

<div style="background: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; box-sizing: border-box;">
        <div style="height: 280px; width: 100%; margin-bottom: 10px;">
            <canvas id="voltageChart"></canvas>
        </div>
        <div style="height: 280px; width: 100%;">
            <canvas id="tempChart"></canvas>
        </div>
    </div>

<div></div>

Es liegen keine Textpassagen vor, die in Klammern ([alt](url) oder [![alt](img)](url)) enthalten sind und übersetzt werden müssen. Die angegebenen URLs wurden gemäß den Regeln unverändert belassen. Der Code bleibt wie folgt:

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns"></script>
<script src="https://cdn.jsdelivr.net/npm/hammerjs"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-zoom"></script>
```

```html
<script>
(function() {
    const fileInput = document.getElementById('logFileInput');
    const uploadTrigger = document.getElementById('uploadTrigger');
    const downloadBtn = document.getElementById('downloadBtn');
    const statusText = document.getElementById('status-text');
</script>
```

lassen Sie `vChart`, `tChart`;
    lassen Sie `parsedData` = [];
    lassen Sie `isResetting` = false;

// --- Konfiguration für die Initialisierung von Chart.js ---  
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

// Erstellen Sie zwei Diagramm-Entitäten
vChart = new Chart(document.getElementById('voltageChart'), createChartConfig('Spannung (V)', '#58a6ff', 'Spannung (V)'));
tChart = new Chart(document.getElementById('tempChart'), createChartConfig('Temperatur (°C)', '#f85149', 'Temperatur (°C)'));

// --- Datei-Verarbeitung verarbeiten ---
uploadTrigger.onclick = () => fileInput.click();

fileInput.onchange = function(e) {
	const datei = e.target.files[0];
	if (!datei) return;

statusText.innerHTML = `Wird <b style="color:#58a6ff;">${file.name}</b> analysiert...`;
        
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

                // Logik zur Behandlung von nächtlichen Übergängen (z.B. von 23:59:59 auf 00:00:00)
                const [h, m, s] = timeStr.split(':').map(Number);
                const currentTimeObj = new Date(2026, 0, currentDay, h, m, s);

                if (lastTimeObj && currentTimeObj < lastTimeObj) {
                    currentDay++;
                    currentTimeObj.setDate(currentDay);
                }
                lastTimeObj = currentTimeObj;

                // Abrufen des Timestamps für Chart.js
                const timeVal = currentTimeObj.getTime();

vData.push({ x: timeVal, y: voltage });
tData.push({ x: timeVal, y: tempC });

// Speichert den ursprünglichen String für die CSV-Exportfunktion
parsedData.push([timeStr, voltage, tempC]);
});

if (parsedData.length > 0) {
    statusText.innerHTML = `✅ Analyse erfolgreich! Es wurden <b style="color:#3fb950;">${parsedData.length}</b> Echtzeitdaten extrahiert.`;
    downloadBtn.style.display = 'inline-block';
    
    isResetting = true;

[vChart, tChart].forEach(chart => {
                if (chart.resetZoom) chart.resetZoom('keine');
            });

// Daten aktualisieren
vChart.data.datasets[0].data = vData;
tChart.data.datasets[0].data = tData;

// Vorkalkulieren des Y-Achsenbereichs, um ein unvollständiges Diagramm zu verhindern
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

vChart.update('keine Werte anzeigen');
tChart.update('keine Werte anzeigen');

setInterval(() => { isResetting = false; }, 200);

} else {
            statusText.innerHTML = `<span style="color:#f85149;">❌ Keine gültigen Daten gefunden. Bitte überprüfen Sie, ob das Log die Paket-ID d15507 enthält.</span>`;
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