---
layout: post
title: "Outil d'Analyse des Logs de Démarrage 100Hz BM6/BM200"
lang: fr
date: 2026-03-21 10:00:00
categories: Auto
tags: [Batterie de Voiture, Moniteur de Batterie, Outils Bricolage, Analyse de Données]
description: "Un outil d'analyse des formes d'onde de démarrage conçu spécifiquement pour le moniteur de batterie Bluetooth BM6. Il décode les paquets hexadécimaux des fichiers journaux bruts pour tracer avec précision une courbe de tension de démarrage haute résolution à 100 Hz, identifiant automatiquement la tension minimale et le désengagement du démarreur."
keywords: "BM6, Moniteur de Batterie Bluetooth, Forme d'Onde de Démarrage, Tension de Démarrage, Cranking, Analyseur de Log, Batterie Automobile, Batterie LiFePO4"
image: /images/bm6-cranking-preview2.webp
faq:
  - question: "Quel problème cet outil résout-il ?"
    answer: "L'application officielle ne permet pas d'exporter les courbes de démarrage à haute résolution. Cet outil lit directement les fichiers journaux bruts capturés via Bluetooth, décode les paquets hexadécimaux et reconstitue la courbe de tension de démarrage à haute fréquence (100 Hz). Cela permet d'évaluer la capacité de décharge instantanée de la batterie et l'état mécanique du démarreur."
  - question: "Que représentent les points rouge et orange sur le graphique ?"
    answer: "Le point rouge (Min) indique la tension la plus basse atteinte lors de la forte charge du démarreur. Le point orange (Démarreur désengagé) est le point d'inflexion calculé par algorithme où l'alimentation du démarreur est coupée et où le moteur thermique commence à tourner de manière autonome."
  - question: "Comment obtenir un fichier journal (Log) à téléverser ?"
    answer: "Vous pouvez utiliser un outil d'analyse de paquets Bluetooth sur smartphone ou la fonction d'exportation de logs intégrée à l'application officielle BM6 pour enregistrer les données diffusées sous forme de fichier .txt ou .log. Veillez à ce que l'enregistrement couvre le moment précis du démarrage."
  - question: "Le téléversement présente-t-il un risque pour la confidentialité de mes données ?"
    answer: "Aucun risque. Cet outil fonctionne entièrement côté client via JavaScript. L'analyse des données, le décodage hexadécimal et le rendu graphique sont exécutés localement dans votre navigateur sans aucun transfert vers un serveur distant."
  - question: "À quel niveau de tension minimale (Min) doit-on s'inquiéter de l'état de la batterie ?"
    answer: "Pour une batterie 12V au plomb ou AGM en bon état à température ambiante, la tension minimale lors du démarrage reste généralement supérieure à 9,6 V. Si le point rouge descend régulièrement sous les 9,0 V, cela traduit un vieillissement ou une résistance interne élevée nécessitant un contrôle."
  - question: "Pourquoi le message 'Aucune forme d'onde valide trouvée' s'affiche-t-il après téléversement ?"
    answer: "Cela arrive généralement quand le fichier journal n'a pas capturé les paquets au moment exact du lancement, ou en cas de perte de paquets Bluetooth si le téléphone était trop éloigné du véhicule. Vérifiez la présence de l'indicateur 'cranking.add:ok' dans le journal."
  - question: "Comment l'algorithme détecte-t-il le point orange (désengagement du démarreur) ?"
    answer: "L'outil applique un algorithme à 'seuil dynamique'. Il mesure la tension de repos initiale avant démarrage. Dès que la tension remonte près de ce seuil initial, il recherche en amont le dernier minimum local dans la vallée de rebond. Cela garantit une compatibilité parfaite avec les batteries au plomb comme avec les batteries LiFePO4."
---

<div id="car-app-container" style="max-width: 950px; margin: 20px auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #ffffff; color: #333333; padding: 25px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e5e7eb; position: relative;">

    <h2 id="ui-title" style="text-align: center; color: #04384c !important; margin-bottom: 22px; margin-top: 5px; font-weight: 800; font-size: 22px; background: none; border: none;">Outil d'Analyse de Forme d'Onde de Démarrage BM6</h2>

    <div
        style="background: rgba(210, 153, 34, 0.08); padding: 15px 20px; border-radius: 10px; margin-bottom: 25px; border-left: 5px solid #d29922; font-size: 14.5px; line-height: 1.6; color: #475569;">
        <strong id="ui-desc-title" style="color: #b45309;">Prend en charge la détection à seuil dynamique (Compatible Plomb-Acide & LiFePO4)</strong><br>
        <span id="ui-desc-body">Cet outil lit directement les fichiers <b style="color:#04384c;">.log</b> bruts et convertit les paquets hexadécimaux en une onde haute résolution à 100 Hz. Son algorithme dynamique identifie automatiquement le point de tension le plus bas et le moment de désengagement du démarreur.</span>
    </div>

    <div
        style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 15px 25px; border-radius: 10px; gap: 10px; margin-bottom: 25px; display: flex; align-items: center; justify-content: center;">
        <button id="uploadTrigger"
            style="background: #04384c; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 15px; transition: 0.2s;">📁
            Téléverser un Fichier Log (.txt / .log)</button>
        <input type="file" id="logFileInput" accept=".txt,.log" style="display:none">
        <button id="loadSampleBtn" style="background: #ffffff; color: #04384c; border: 1px solid #cbd5e1; padding: 9px 20px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 14px; text-decoration: none; display: flex; align-items: center; transition: 0.2s;">📄 Charger l'Échantillon Test</button>

    </div>

    <div id="status-text" style="text-align: center; color: #64748b; margin-bottom: 20px; font-size: 14px; font-weight: bold;">Veuillez téléverser un fichier Log contenant les données de diffusion pour lancer l'analyse</div>

    <div id="chartsWrapper" style="display: flex; flex-direction: column; gap: 20px;"></div>

</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/hammerjs"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-zoom"></script>

<script>
    (function () {
        const fileInput = document.getElementById('logFileInput');
        const uploadTrigger = document.getElementById('uploadTrigger');
        const statusText = document.getElementById('status-text');
        const chartsWrapper = document.getElementById('chartsWrapper');

        Chart.defaults.color = '#64748b';
        Chart.defaults.borderColor = '#e2e8f0';

        // Plugin Crosshair
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

        uploadTrigger.onclick = () => fileInput.click();
        const loadSampleBtn = document.getElementById('loadSampleBtn');

        loadSampleBtn.onclick = function() {
            statusText.innerHTML = `Chargement du <b style="color:#58a6ff;">fichier d'échantillon (bm6_100Hz.log)</b> ...`;
            chartsWrapper.innerHTML = ''; 

            fetch('/files/bm6_100Hz.log')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Échec de récupération du fichier échantillon (HTTP ' + response.status + ')');
                    }
                    return response.text();
                })
                .then(text => {
                    processLogData(text);
                })
                .catch(error => {
                    statusText.innerHTML = `<span style="color:#f85149;">❌ Échec du chargement du fichier : ${error.message}</span>`;
                });
        };

        fileInput.addEventListener('change', function (e) {
            const file = e.target.files[0];
            if (!file) return;

            statusText.innerHTML = `Analyse de <b style="color:#58a6ff;">${file.name}</b> ...`;
            chartsWrapper.innerHTML = '';

            const reader = new FileReader();
            reader.onload = function (e) {
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
            
            // 1. Base Timestamp -> Température
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
            let currentLogTime = "Inconnu";
            let rollingRealTimeTemp = "Inconnu";

            for (let i = 0; i < lines.length; i++) {
                let originalLine = lines[i].trim();
                let line = originalLine.toLowerCase();
                if (!line) continue;

                let timeMatch = originalLine.match(/^(\d{2}:\d{2}:\d{2})/);
                if (timeMatch) currentLogTime = timeMatch[1];

                let tempMatch = line.match(/"temp"\s*:\s*(\d+)/);
                if (tempMatch) rollingRealTimeTemp = tempMatch[1];

                let syncMatch = line.match(/self\.synchistorytimeline:(\d+)/);
                if (syncMatch) {
                    activeTimeline = syncMatch[1];
                    isRecording = true;
                    isHistorical = true;
                    tempHexStream = ""; 
                    continue;
                }

                if (line.includes('receive:')) {
                    let content = line.split("receive:")[1].trim();

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
                                    let eventTemp = "Inconnu";

                                    if (isHistorical && activeTimeline) {
                                        let ts = parseInt(activeTimeline);
                                        let date = new Date(ts * 1000);
                                        let mm = String(date.getMonth() + 1).padStart(2, '0');
                                        let dd = String(date.getDate()).padStart(2, '0');
                                        let hh = String(date.getHours()).padStart(2, '0');
                                        let min = String(date.getMinutes()).padStart(2, '0');
                                        let ss = String(date.getSeconds()).padStart(2, '0');
                                        eventTimeStr = `${mm}/${dd} ${hh}:${min}:${ss} (Historique)`;

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
                statusText.innerHTML = '<span style="color:#f85149;">❌ Aucune forme d\'onde de démarrage valide trouvée dans le fichier. Veuillez vérifier vos données.</span>';
                return;
            }

            statusText.innerHTML = `✅ Analyse terminée ! <b style="color:#58a6ff;">${crankingEvents.length}</b> enregistrement(s) de démarrage détecté(s).`;

            crankingEvents.forEach((eventData, index) => {
                drawChartForEvent(eventData, index + 1);
            });
        }

        function getLocalMinima(arr) {
            let minima = [];
            for (let i = 1; i < arr.length - 1; i++) {
                if (arr[i] < arr[i - 1] && arr[i] < arr[i + 1]) minima.push(i);
            }
            return minima;
        }

        function autoScaleY(chart) {
            const xScale = chart.scales.x;
            const dataset = chart.data.datasets[0].data;
            let minV = Infinity, maxV = -Infinity, found = false;
            for (let i = 0; i < dataset.length; i++) {
                if (dataset[i].x >= xScale.min && dataset[i].x <= xScale.max) {
                    if (dataset[i].y < minV) minV = dataset[i].y;
                    if (dataset[i].y > maxV) maxV = dataset[i].y;
                    found = true;
                }
            }
            if (found) {
                chart.options.scales.y.min = Math.floor(minV * 5) / 5;
                chart.options.scales.y.max = Math.ceil(maxV * 5) / 5;
            }
        }

        function drawChartForEvent(eventData, eventNumber) {
            let hexData = eventData.hex;
            let eventTime = eventData.time;
            let eventTemp = eventData.temp;

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

            let minVol = Math.min(...voltages);
            let minIdx = voltages.indexOf(minVol);
            let localMins = getLocalMinima(voltages);

            let sampleSize = Math.min(5, minIdx);
            if (sampleSize === 0) sampleSize = 1; 
            let initialVoltages = voltages.slice(0, sampleSize);
            let vInitial = initialVoltages.reduce((a, b) => a + b, 0) / initialVoltages.length;

            let dynamicThreshold = vInitial - 0.2;

            let climbIdx = minIdx;
            while (climbIdx < voltages.length && voltages[climbIdx] <= dynamicThreshold) {
                climbIdx++;
            }
            if (climbIdx >= voltages.length) climbIdx = voltages.length - 1;

            let validMinsForStarter = localMins.filter(idx => idx >= minIdx && idx < climbIdx);
            let starterIdx = validMinsForStarter.length > 0 ? validMinsForStarter[validMinsForStarter.length - 1] : minIdx;

            const minPoint = { x: times[minIdx], y: voltages[minIdx] };
            const starterPoint = { x: times[starterIdx], y: voltages[starterIdx] };

            const pointLabelsPlugin = {
                id: 'pointLabels',
                afterDraw: chart => {
                    const ctx = chart.ctx;
                    const meta = chart.getDatasetMeta(1);
                    if (!meta.hidden && meta.data.length >= 2) {
                        ctx.save();
                        ctx.font = 'bold 12px "Segoe UI", sans-serif';
                        ctx.fillStyle = '#475569';
                        ctx.textBaseline = 'middle'; 

                        const ptMin = meta.data[0];
                        if (ptMin.x >= chart.chartArea.left && ptMin.x <= chart.chartArea.right) {
                            ctx.textAlign = 'left';
                            ctx.fillText(`Min: ${minPoint.y.toFixed(2)}V`, ptMin.x + 10, ptMin.y);
                        }
                        
                        const ptStarter = meta.data[1];
                        if (ptStarter.x >= chart.chartArea.left && ptStarter.x <= chart.chartArea.right) {
                            ctx.textAlign = 'left';
                            ctx.fillText(` Démarreur désengagé: ${starterPoint.y.toFixed(2)}V`, ptStarter.x + 10, ptStarter.y);
                        }
                        ctx.restore();
                    }
                }
            };

            const wrapperDiv = document.createElement('div');
            wrapperDiv.style.cssText = "background: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e2e8f0; width: 100%; box-sizing: border-box; box-shadow: 0 1px 4px rgba(0,0,0,0.04);";
            
            const titleElement = document.createElement('div');
            titleElement.style.cssText = "color: #04384c; font-size: 16px; font-weight: bold; text-align: center; margin-bottom: 15px;";
            titleElement.innerHTML = `Analyse de Démarrage - Enregistrement #${eventNumber} (Heure : ${eventTime} | Temp : ${eventTemp}°C | Initiale : ${vInitial.toFixed(2)}V)`;
            wrapperDiv.appendChild(titleElement);

            const canvasDiv = document.createElement('div');
            canvasDiv.style.cssText = "width: 100%; height: 400px; position: relative;";
            
            const canvas = document.createElement('canvas');
            canvas.id = `chart-${eventNumber}`;
            canvasDiv.appendChild(canvas);
            wrapperDiv.appendChild(canvasDiv);
            chartsWrapper.appendChild(wrapperDiv);

            new Chart(canvas, {
                type: 'line',
                data: {
                    datasets: [
                        {
                            label: 'Tension (V)',
                            data: chartData,
                            borderColor: '#1176d4',
                            borderWidth: 2,
                            pointRadius: 0,
                            tension: 0.2,
                            order: 2
                        },
                        {
                            label: 'Points Clés',
                            type: 'scatter',
                            data: [minPoint, starterPoint],
                            backgroundColor: ['#e11d48', '#d97706'],
                            borderColor: '#ffffff',
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
                            grid: { color: '#e2e8f0' },
                            ticks: { color: '#64748b', maxTicksLimit: 10 },
                            title: { display: true, text: 'Temps (Secondes)' },
                            max: times[times.length - 1],
                        },
                        y: {
                            title: { display: true, text: 'Tension (V)' },
                            grid: { color: '#e2e8f0' },
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
                            backgroundColor: 'rgba(255, 255, 255, 0.96)',
                            titleColor: '#0f172a',
                            bodyColor: '#334155',
                            borderColor: '#cbd5e1',
                            borderWidth: 1,
                            padding: 10,
                            displayColors: false,
                            callbacks: {
                                title: function(tooltipItems) {
                                    if (tooltipItems.length > 0) {
                                        const item = tooltipItems[0];                                
                                        return `Tension : ${item.parsed.y}V`;
                                    }
                                    return '';
                                },
                                label: function(context) {
                                    if (context.dataIndex !== context.chart.tooltip.dataPoints[0].dataIndex || 
                                        context.datasetIndex !== context.chart.tooltip.dataPoints[0].datasetIndex) {
                                        return null;
                                    }
                                    return `Temps : ${context.raw.x.toFixed(2)} s`;
                                }
                            }
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
                                pinch: { enabled: true },
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
        }
    })();
</script>
