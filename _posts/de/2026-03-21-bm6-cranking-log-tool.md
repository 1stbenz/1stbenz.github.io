---
layout: post
title: "Werkzeug zur Analyse des Startprotokolls für BM6/BM200 bei 100 Hz"
lang: de
date:   2026-03-21 10:00:00
categories: Auto
tags: [BM6, Batterieüberwachung, Startwellenform, Datenanalyse, Konvertierungstool, Autobatterie]
description: "Ein Startwellen-Analyse-Tool, das speziell für den BM6 Bluetooth-Akku-Monitor entwickelt wurde. Es kann 16-Bit-Pakete aus Rohlogdateien decodieren und präzise hochauflösende Kurven des Starter-Voltage während der Motorstartphase zeichnen, wobei ein dynamischer Schwellenwertalgorithmus automatisch die Tiefpunkte sowie den Trennpunkt vom Startmotor markiert."
keywords: "BM6, Bluetooth-Batterie-Monitoring, Startwellenform, Starterspannung, Cranking, Log-Parser, Automobilbatterie, Lithium-Eisenphosphat-Batterie"
image: /images/bm6-cranking-preview2.webp
faq:
  - question: "Welches Problem löst dieses Tool hauptsächlich?"
    answer: "Das Original-APP kann keine hochauflösenden Startwellenausgaben bereitstellen. Dieses Tool kann die ursprünglichen Logdateien direkt vom Bluetooth-Lesegerät lesen, die internen 16-bit-Pakete decodieren und den 100-Hz-präzisen Spannungsverlauf beim Start wiederherstellen, um die momentane Entladeleistung des Akkus und den Zustand des Startermotors zu beurteilen."
  - question: "Was bedeuten die roten und orangen Punkte auf dem Diagramm?"
    answer: "Der rote Punkt (Min) repräsentiert den niedrigsten Spannungswert, zu dem der Akku beim Startvorgang des Motors gezogen wird. Der orange Punkt (Starter) markiert hingegen den durch Algorithmen berechneten Übergangspunkt, an dem die Stromversorgung für den Starter abgeschaltet und das Motorwerk erfolgreich mit der Generierung von elektrischer Energie übergeben wurde."
  - question: "Wie kann man eine zum Hochladen geeignete Log-Datei erhalten?"
    answer: "Sie können die abgefangenen Broadcast-Daten entweder mit einem Bluetooth-Analysegerät für mobile Endgeräte oder über den integrierten Funktion zur Exportierung von Protokolldateien in der BM6-Urheberrechts-App als .txt- oder .log-Format archivieren. Stellen Sie sicher, dass das Archiv den Zeitraum des aktuellen Betriebszeitraums umfasst."
  - question: "Gibt es bei der Hochladung von Log-Dateien Bedenken hinsichtlich des Datenschutzes oder einer Datenlecks?"
    answer: "Das ist absolut nicht der Fall. Dieses Tool wurde rein mit Frontend-Technologien (JavaScript) entwickelt. Alle Datenerfassungen, die 16-Bit-Decodierung und das Erstellen von Diagrammen finden ausschließlich innerhalb Ihres Browsers statt. Keine Daten werden an Cloud-Server übermittelt."
  - question: "Auf welchen Mindestspannungswert (Min) fällt der Starter, damit die Batterie möglicherweise bald defekt ist?"
    answer: "Eine gesunde 12V Blei-Säure- oder AGM-Batterie hält unter Raumtemperatur beim Starten des Motors in der Regel eine Spannung von mindestens 9,6 V aufrecht. Wenn Ihre roten Punkte häufig bei 9,0 V oder niedriger liegen, könnte dies darauf hindeuten, dass die Batterie altert und ihr Innenwiderstand zunimmt; wir empfehlen einen früheren professionellen Check."
  - question: "Warum wird nach dem Hochladen eines Dateis \"Kein gültiger Startwellenform\" angezeigt?"
    answer: "Dies liegt meist daran, dass im Log-Datei kein vollständiges Paket des Anlaufmomentes erfasst wurde. Bitte überprüfen Sie, ob in der Datei ein erfolgreicher Marker für 'cranking.add:ok' vorhanden ist. Darüber hinaus kann es auch zu unvollständigen Wellenformen kommen, wenn das Handy während des Startens aufgrund einer zu großen Entfernung vom Fahrzeug den Bluetooth-Verbindung verliert."
  - question: "Wie ermittelt der Algorithmus den orangen Punkt (Startpunkt für das Abkuppeln des Motors)?"
    answer: "Dieses Tool verwendet einen „dynamischen Schwellwert\"-Algorithmus. Das Programm misst zunächst automatisch die „initialer Ruhe-Spannung\" vor dem Start. Wenn sich nach dem Start die Spannung wieder auf den Wert der initialen Ruhespannung annähert (was bedeutet, dass der Motor abgeschaltet wurde oder der Generator übernimmt), wird rückwärts gerechnet, um das letzte lokale Minimum im Prozess des Spannungsabfalls und -anstiegs zu finden. Dies ermöglicht es dem Tool nicht nur bei herkömmlichen Blei-Säure-Akkus zu funktionieren, sondern auch vollständig mit Lithium-Eisenphosphat-Akkus kompatibel zu sein, die eine höhere Ruhespannung aufweisen."
---

<div id="car-app-container" style="max-width: 950px; margin: 20px auto; font-family: 'Segoe UI', 'Microsoft JhengHei', sans-serif; background: #0d1117; color: #c9d1d9; padding: 25px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid #30363d; position: relative;">

<h2 id="ui-title" style="text-align: center; color: #c9d1d9; margin-bottom: 10px; margin-top: 10px;">Welle-Analyse-Tool für BM6</h2>

<div style="background: rgba(210, 153, 34, 0.1); padding: 15px 20px; border-radius: 10px; margin-bottom: 25px; border-left: 5px solid #d29922; font-size: 14.5px; line-height: 1.6; color: #8b949e;">
    <strong id="ui-desc-title" style="color: #d29922;">Unterstützung für dynamische Schwellwerterkennung (kompatibel mit Blei-Säure- und Lithium-Eisenphosphat-Akkus)</strong><br>
    <span id="ui-desc-body">Dieses Tool kann direkt die extrahierten <b style="color:#c9d1d9;">.log</b>-Rohprotokolldateien lesen, 16-Bit-Pakete in hochauflösende Wellenformen mit einer Frequenz von 100 Hz umwandeln und über dynamische Algorithmen automatisch den niedrigsten Spannungswert sowie den Punkt zum Start des Motors identifizieren. Dies erleichtert die Überprüfung der Grenzwerte der Akkuleistung.</span>
</div>

<div style="background-color:#161b22;border:1px solid #30363d;padding:15px 25px; border-radius:10px;display:flex;align-items:center;justify-content:center;"> <button id="uploadTrigger" style="background-color:#1f6feb;color:white;border:none;padding:12px 24px;border-radius:8px;cursor:pointer;font-weight:bold;font-size:15px;transition-duration:.2s">📁 Log-Datei hochladen (.txt / .log)</button> <input type="file" id="logFileInput" accept=".txt,.log" style="display:none"/> <button id="loadSampleBtn" style="background-color:#30363d;color:#c9d1d9;border:1px solid #8b949e;padding:9px 20px;border-radius:8px;cursor:pointer;font-weight:bold;font-size:14px;text-decoration:none;display:flex;align-items:center;transition-duration:.2s">📄 Beispieldatei laden zum Testen</button> </div>

<div id="status-text"
        style="text-align: center; color: #8b949e; margin-bottom: 20px; font-size: 14px; font-weight: bold;">Bitte laden Sie eine Log-Datei mit Broadcast-Daten hoch, um sie zu analysieren</div>

<div id="chartsWrapper" style="display: flex; flex-direction: column; gap: 20px;"></div>

<div></div>

Es liegen keine Textpassagen vor, die in Markdown-Klammern ([alt](url) oder [![alt](img)](url)) enthalten sind. Die angegebenen Zeilen bestehen ausschließlich aus HTML- und JavaScript-Skripten mit URLs, die gemäß den Regeln unverändert bleiben müssen.

<script>
    (function () {
        const fileInput = document.getElementById('logFileInput');
        const uploadTrigger = document.getElementById('uploadTrigger');
        const statusText = document.getElementById('status-text');
        const chartsWrapper = document.getElementById('chartsWrapper');

Es gibt keine Übersetzung für diesen Code, da es sich um JavaScript-Code handelt und nicht um Text oder Bilder mit alternativen Beschreibungen. Die Variablennamen (`Chart`, `defaults`) sind englischsprachige Konventionen im Bereich der Programmierung und werden in diesem Kontext üblicherweise so belassen.

// Plugin für das Kreuzsichtfeld (siehe 03-20)
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

Der Klick auf `uploadTrigger` löst aus, dass der Dateiauswahl-Button geklickt wird: `() => fileInput.click()`

Es gibt keine Übersetzung für diesen Code-Schnipsel, da es sich um JavaScript handelt und nicht um Text oder Markdown-Inhalte. Die Anweisung zur Übersetzung von Inhalten in eckigen Klammern ([alt](url)) bezieht sich auf Bild-Alternativtexte innerhalb von Markdown-Bildreferenzen (z.B. `[![Alt Text](image.jpg)]`), was hier nicht vorkommt.

Falls Sie einen deutschen Kommentar für diesen Code benötigen, könnte er lauten:
```javascript
// Lade den Button mit der ID 'loadSampleBtn' aus dem DOM
const loadSampleBtn = document.getElementById('loadSampleBtn');
```

// Klickereignis für das Laden von Beispieldateien  
        loadSampleBtn.onclick = function() {
            // Status aktualisieren und Bildschirminhalt leeren
            statusText.innerHTML = `Lade <b style="color:#58a6ff;">Beispieldatei (bm6_100Hz.log)</b> ...`;
            chartsWrapper.innerHTML = '';

// Abrufen von Dateien direkt vom Server mit der Fetch-API
            fetch('/files/bm6_100Hz.log')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Beispieldatei konnte nicht abgerufen werden (HTTP ' + response.status + ')');
                    }
                    return response.text();
                })
                .then(text => {
                    // Nach erfolgreichem Abrufen wird das reine Textdatum direkt an den bestehenden Parse-Funktion übergeben
                    processLogData(text);
                })
                .catch(error => {
                    statusText.innerHTML = `<span style="color:#f85149;">❌ Ladevorgang der Beispieldatei fehlgeschlagen: ${error.message}</span>`;
                });
        };

fileInput.addEventListener('Änderung', function(e){
    const datei = e.target.files[0];
    if(!datei)return;

statusText.innerHTML = `Wird analysiert: <b style="color:#58a6ff;">${file.name}</b> ...`;
chartsWrapper.innerHTML = '';

const reader = new FileReader();
reader.onload = function(e){
    const text = e.target.result;
    processLogData(text);
};
reader.readAsText(file);
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
            
            // 1. Vorschau: Erstellung eines dedizierten Datenbanks für "historische Zeitstempel -> Temperatur"
            let historyMap = {};
            const jsonRegex = /"time"\s*:\s*(\d+)\s*,\s*"temp"\s*:\s*(\d+)/g;
            let match;
            while ((match = jsonRegex.exec(logText)) !== null) {
                historyMap[match[1]] = match[2];
            }

let crankingEvents = [];
            let tempHexStream = "";
            let istRecording = false;
            let isHistorical = false;
            let activeTimeline = null;
            let currentLogTime = "Unbekannt";
            let rollingRealTimeTemp = "Unbekannt";

// 2. Zeilenweise analysieren: Trennung von historischen und Echtzeitwellenformen
            for (let i = 0; i < lines.length; i++) {
                let originalLine = lines[i].trim();
                let line = originalLine.toLowerCase();
                if (!line) continue;

let timeMatch = originalLine.match(/^(\d{2}:\d{2}:\d{2})/);
                if (timeMatch) {
                    const currentLogTime = timeMatch[1];
                }

let tempMatch = line.match(/\"temp\"\s*:\s*(\d+)/);
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
if (line.includes('receive:')) {
    let content = line.split("receive:")[1].trim();
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
                                    let eventTemp = "Unbekannt";

if (isHistorical && activeTimeline) {
    let ts = parseInt(activeTimeline);
    let date = new Date(ts * 1000);
    let mm = String(date.getMonth() + 1).padStart(2, '0');
    let dd = String(date.getDate()).padStart(2, '0');
    let hh = String(date.getHours()).padStart(2, '0');
    let min = String(date.getMinutes()).padStart(2, '0');
    let ss = String(date.getSeconds()).padStart(2, '0');
    eventTimeStr = `${mm}/${dd} ${hh}:${min}:${ss} (historisch)`;

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
                statusText.innerHTML = '<span style="color:#f85149;">❌ In der Datei wurde kein gültiger Startwellenform gefunden. Bitte überprüfen Sie, ob es sich um eine Datei mit cranking-Einträgen handelt.</span>';
                return;
            }

statusText.innerHTML = `✅ Analyse abgeschlossen! Es wurden ${crankingEvents.length} Motorstart-Ereignisse erkannt.`;

```javascript
crankingEvents.forEach((eventData, index) => {
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

// Dynamische Y-Achsen-Skalierung-Logik
function autoScaleY(chart) {
    const xScale = chart.scales.x;
    const dataset = chart.data.datasets[0].data; // Linien-Daten
    let minV = Infinity, maxV = -Infinity, found = false;
    for (let i = 0; i < dataset.length; i++) {
        if (dataset[i].x >= xScale.min && dataset[i].x <= xScale.max) {
            if (dataset[i].y < minV) minV = dataset[i].y;
            if (dataset[i].y > maxV) maxV = dataset[i].y;
            found = true;
        }
    }
    if (found) {
        // Untere Grenze: Ganzzahliger Wert des nächsten Punktes unter dem niedrigsten Punkt im Bildbereich
        chart.options.scales.y.min = Math.floor(minV * 5) / 5;
        // Obere Grenze: Nächste Vielfache von 0,2 über dem höchsten Punkt im Bildbereich
        chart.options.scales.y.max = Math.ceil(maxV * 5) / 5;
    }
}

function zeichneDiagrammFürEreignis(eReignisseDaten, ereignisNummer) {
            let hexDaten = eReignisseDaten.hex;
            let ereignisZeit = eReignisseDaten.zeit;
            let ereignisTemperatur = eReignisseDaten.temperatur;

let times = [];
            let voltages = [];
            let currentTime = 0;
            let chartData = [];

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

// 1. Mindestwert (Min-Cranking)
            const minVol = Math.min(...voltages);
            const minIdx = voltages.indexOf(minVol);
            const localMins = getLocalMinima(voltages);

// 2. Dynamischer Schwellenwert (Dynamic Threshold)  
let sampleSize = Math.min(5, minIdx);  
if (sampleSize === 0) sampleSize = 1; 
let initialVoltages = voltages.slice(0, sampleSize);  
let vInitial = initialVoltages.reduce((a, b) => a + b, 0) / initialVoltages.length;

set dynamischerSchwellenwert auf Anfangswert minus 0,2;

let climbIdx = minIdx;
while (climbIdx < voltages.length && voltages[climbIdx] <= dynamicThreshold) {
    climbIdx++;
}
if (climbIdx >= voltages.length) climbIdx = voltages.length - 1;

// 3. Startmotor-Entkoppelung (Starter Disengaged)
            let gültigeMinutenFürStart = localMinuten.filter(idx => idx >= minIndex && idx < climbIndex);
            let startMotorIndex = gültigeMinutenFürStart.length > 0 ? gültigeMinutenFürStart[gültigeMinutenFürStart.length - 1] : minIndex;

const minPunkt = { x: times[minIdx], y: voltages[minIdx] };
            const startpunkt = { x: times[starterIdx], y: voltages[starterIdx] };

// Plugin zum Zeichnen von Beschriftungen (ersetzt die Marker+Text-Funktion von Plotly)
            const pointLabelsPlugin = {
                id: 'pointLabels',
                afterDraw: chart => {
                    const ctx = chart.ctx;
                    const meta = chart.getDatasetMeta(1); // Streudiagramm-Datensatz
                    if (!meta.hidden && meta.data.length >= 2) {
                        ctx.save();
                        ctx.font = 'bold 12px "Segoe UI", sans-serif';
                        ctx.fillStyle = '#c9d1d9';

                        // Vertikale Zentrierung einstellen, damit der Text auf derselben horizontalen Linie wie die Punkte liegt
                        ctx.textBaseline = 'middle';

// Min-Label (rechts vom roten Punkt)
const ptMin = meta.data[0];
if (ptMin.x >= chart.chartArea.left && ptMin.x <= chart.chartArea.right) {
    ctx.textAlign = 'left';
    // X-Koordinate um 10 px nach rechts verschieben, um den Körper des Punktes zu vermeiden; Y-Koordinate mit dem Punkt übereinstimmen lassen
    ctx.fillText(`Min: ${minPoint.y.toFixed(2)}V`, ptMin.x + 10, ptMin.y);
}

// Starter-Label (rechts vom orangen Punkt)
const ptStarter = meta.data[1];
if (ptStarter.x >= chart.chartArea.left && ptStarter.x <= chart.chartArea.right) {
    ctx.textAlign = 'left';
    // Ebenfalls um 10 px nach rechts verschieben, um den orangen Punkt zu vermeiden
    ctx.fillText(` Starter dise: ${starterPoint.y.toFixed(2)}V`, ptStarter.x + 10, ptStarter.y);
}
ctx.restore();

// UI-Container erstellen
const wrapperDiv = document.createElement('div');
wrapperDiv.style.cssText = "background: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; width: 100%; box-sizing: border-box;";

// Eigener Titel hinzufügen
const titleElement = document.createElement('div');
titleElement.style.cssText = "color: #c9d1d9; font-size: 16px; font-weight: bold; text-align: center; margin-bottom: 15px;";
titleElement.innerHTML = `Wellenformanalyse starten - Protokoll Nr. ${eventNumber} (Zeit: ${eventTime} | Temperatur: ${eventTemp}°C | Startwert: ${vInitial.toFixed(2)}V)`;
wrapperDiv.appendChild(titleElement);

const canvasDiv = document.createElement('div');
            canvasDiv.style.cssText = "width: 100%; height: 400px; position: relative;";
            
            const canvas = document.createElement('canvas');
            canvas.id = `chart-${eventNumber}`;
            canvasDiv.appendChild(canvas);
            wrapperDiv.appendChild(canvasDiv);
            chartsWrapper.appendChild(wrapperDiv);

// Initialisierung von Chart.js
new Chart(canvas, {
    type: 'line',
    data: {
        datasets: [
            {
                label: 'Spannung (V)',
                data: chartData,
                borderColor: '#58a6ff',
                borderWidth: 2,
                pointRadius: 0,
                tension: 0.2, // Glättete Kurve
                order: 2
            },
            {
                label: 'Wichtige Punkte',
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
                title: { display: true, text: 'Zeit (Sekunden)' },
                max: times[times.length - 1],
                ticks: { maxTicksLimit: 10 }
            },
            y: {
                title: { display: true, text: 'Spannung (V)' },
                // Vorabberechnung eines geeigneten Y-Achsenbereichs
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
                    // Überschrift (oben): Spannung anzeigen und prüfen, ob es sich um einen speziellen roten/orangen Punkt handelt.
                    title: function(tooltipItems) {
                        if (tooltipItems.length > 0) {
                            const item = tooltipItems[0];                                
                            return `Spannung: ${item.parsed.y}V`;
                        }
                        return '';
                    },
                    // Inhalt (unten): Zeit anzeigen.
                    label: function(context) {
                        // Wichtige Änderung: Unabhängig von der Datenset-Gruppe wird nur die Zeitmarke des „ersten" gefundenen Datenelements angezeigt.
                        if (context.dataIndex !== context.chart.tooltip.dataPoints[0].dataIndex || 
                            context.datasetIndex !== context.chart.tooltip.dataPoints[0].datasetIndex) {
                            return null;
                        }
                        // Verwenden von context.raw.x, um sicherzustellen, dass die Sekundenzahl aus den Rohdaten erfasst wird.
                        return `Zeit: ${context.raw.x.toFixed(2)} s`;
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