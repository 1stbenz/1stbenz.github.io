---
layout: post
title: "Bilan de Santé Complet du Système Électrique Automobile : Analyse Long Terme BM6"
lang: fr
date: 2026-04-14 09:52:00
categories: Auto
tags: [Batterie de Voiture, Moniteur de Batterie, Connaissances Auto]
description: "Comment déterminer scientifiquement quand remplacer sa batterie ? Cet article présente un système de diagnostic électrique automobile. En combinant les données de veille à 1 Hz et les courbes haute fréquence à 100 Hz au démarrage, il évalue le courant de fuite, la recharge par l'alternateur et la puissance de crête."
keywords: "Santé de Batterie, LiFePO4, Batterie Plomb-Acide, Test Courant de Fuite, Tension de Démarrage, Contrôle Alternateur, Analyse Log Bluetooth, Alimentation Véhicule"
image: /images/battery-health-report-analysis.webp
faq:
  - question: "Quels paramètres clés ce système évalue-t-il ?"
    answer: "Le système examine quatre indicateurs fondamentaux : 1. Santé du stockage (Tension au repos), 2. Courant de fuite parasite (Chute de tension journalière), 3. Circuit de charge (Tension moyenne en roulant), 4. Puissance de démarrage (Tension minimale sous le démarreur)."
  - question: "Quelle est la différence d'évaluation entre le LiFePO4 et le plomb-acide ?"
    answer: "Le système applique un double barème étalonné. Par exemple, une excellente tension de repos pour le LiFePO4 est >13,2 V, alors qu'elle est de 12,5 V pour le plomb. Pour la tension minimale de démarrage, le seuil optimal est de 11,5 V en LiFePO4 contre 10,5 V en plomb-acide."
  - question: "Comment détecter un courant de fuite anormal (courant résiduel veille) ?"
    answer: "Le système calcule la 'chute journalière (V/jour)' sur les logs de veille prolongée. Si la chute dépasse 0,3 V (LiFePO4) ou 0,4 V (plomb), une fuite sévère est diagnostiquée (caméra embarquée restée active, alarme ou boîtier OBD2 empêchant la mise en sommeil)."
  - question: "Pourquoi la capture à 100 Hz est-elle indispensable pour l'analyse du démarrage ?"
    answer: "L'allumage moteur s'effectue en une fraction de seconde. Un échantillonnage standard à 1 Hz saute immanquablement le point de tension le plus bas. L'enregistrement à 100 Hz fige la chute exacte sous l'effort du démarreur pour révéler une hausse de résistance interne ou la fatigue du démarreur."
  - question: "Sur quelle base les anomalies d'alternateur sont-elles jugées ?"
    answer: "L'algorithme filtre les données dès que le moteur tourne. Si la tension moyenne en conduite est inférieure à 13,5 V (ou supérieure à 15,0 V), une fatigue d'alternateur ou une panne du régulateur est signalée, en tenant compte des stratégies AMS/Start-Stop modernes."
  - question: "Que faire si le rapport signale un 'Stockage Faible' sur une batterie LiFePO4 ?"
    answer: "Si la tension de repos descend sous 13,2 V, un long trajet routier ou l'utilisation d'un chargeur externe dédié est préconisé pour saturer la batterie et déclencher l'équilibrage actif des cellules par le BMS."
---

<script src="https://cdn.jsdelivr.net/npm/xlsx/dist/xlsx.full.min.js"></script>

<style>
    .app-container {
        font-family: 'Segoe UI', sans-serif;
        background: #ffffff; color: #333333; max-width: 1000px; margin: 0 auto; padding: 30px; border-radius: 12px; border: 1px solid #e5e7eb; box-shadow: 0 4px 20px rgba(0,0,0,0.06);
    }
    .app-container h1 { text-align: center; color: #04384c; margin-bottom: 25px; font-weight: 800; font-size: 24px; border: none; background: none; }
    .control-panel {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
        margin-bottom: 30px;
        background: #f8fafc;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
    }
    .file-input-group {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }
    .file-input-group label { font-weight: bold; color: #04384c; font-size: 14px; }
    .app-container input[type="file"], .app-container select {
        background: #ffffff; padding: 10px; border-radius: 6px; border: 1px solid #cbd5e1; color: #333333;
    }
    .file-hint { font-size: 12px; color: #64748b; margin-top: -5px; }
    .btn-generate {
        width: 100%; padding: 15px; background: #04384c; color: white; border: none; border-radius: 8px;
        font-size: 18px; font-weight: bold; cursor: pointer; transition: 0.2s; margin-top: 10px;
    }
    .btn-generate:hover { background: #064e6b; }
    
    .report-section { display: none; margin-top: 40px; }
    .patient-info {
        display: flex; justify-content: space-between; border-bottom: 2px solid #e2e8f0;
        padding-bottom: 10px; margin-bottom: 20px; color: #64748b;
    }
    .app-container table {
        width: 100%; border-collapse: collapse; margin-bottom: 30px;
        background: #ffffff; border-radius: 8px; overflow: hidden; border: 1px solid #dcdcdc;
    }
    .app-container th, .app-container td { padding: 15px; text-align: center; border: 1px solid #dcdcdc; }
    .app-container th { background: rgba(4, 56, 76, 0.06); color: #04384c; font-weight: bold; }
    .app-container td:first-child { text-align: left; font-weight: bold; color: #04384c; }
    .app-container tr:nth-child(even) { background-color: #fafafa; }
    .app-container tr:nth-child(odd) { background-color: #ffffff; }
    .app-container tr:hover { background-color: rgba(4, 56, 76, 0.03); }
    
    .status-good { color: #3fb950; font-weight: bold; }
    .status-warn { color: #d29922; font-weight: bold; }
    .status-bad { color: #f85149; font-weight: bold; }
    .status-none { color: #8b949e; font-style: italic; }

    .doctor-notes {
        background: rgba(4, 56, 76, 0.05); padding: 20px; border-radius: 10px;
        border-left: 5px solid #04384c; line-height: 1.6; color: #334155;
    }
</style>

<div class="app-container">
    <h1>Système de Bilan de Santé Électrique Automobile</h1>

    <div class="control-panel">
        <div class="file-input-group">
            <label>📁 1. Relevés Historiques Hors Ligne (Évaluation Fuite)</label>
            <input type="file" id="fileOffline" accept=".xls,.xlsx,.csv">
            <span class="file-hint">Prend en charge les exports Excel (.xlsx, .xls)</span>
        </div>
        <div class="file-input-group">
            <label>📁 2. Fichiers Logs Bluetooth Bruts (Charge & Démarrage)</label>
            <input type="file" id="fileRaw" accept=".txt,.log" multiple>
            <span class="file-hint">Sélection multiple possible. Décode 1Hz et 100Hz</span>
        </div>
        <div class="file-input-group">
            <label>⚙️ Chimie de la Batterie</label>
            <select id="batteryType">
                <option value="lifepo4">Phosphate de Fer Lithié (LiFePO4)</option>
                <option value="leadacid">Plomb-Acide Standard / AGM</option>
            </select>
        </div>
    </div>
    
    <button class="btn-generate" onclick="generateReport()">Générer le Bilan de Santé Complet</button>

    <div class="report-section" id="reportSection">
        <div class="patient-info">
            <span id="reportDate">Date du bilan : AAAA/MM/JJ</span>
            <span id="reportConfig">Configuration : Norme LiFePO4</span>
        </div>

        <table id="reportTable">
            <thead>
                <tr>
                    <th width="20%">Point de Contrôle</th>
                    <th width="20%">Donnée Relevée</th>
                    <th width="20%">Norme Optimale</th>
                    <th width="20%">Seuil d'Alerte</th>
                    <th width="20%">Verdict</th>
                </tr>
            </thead>
            <tbody id="tableBody">
            </tbody>
        </table>

        <div class="doctor-notes">
            <h3 style="margin-top:0; color:#58a6ff;">📋 Diagnostic Global du Système</h3>
            <div id="aiDiagnosis">Veuillez charger des fichiers pour générer l'analyse diagnostique.</div>
        </div>
    </div>
</div>

<script>
    const thresholds = {
        lifepo4: {
            restV: { good: 13.2, bad: 13.0, unit: 'V' },
            dropV: { excellent: 0.01, good: 0.02, bad: 0.05, unit: 'V/Jour' },
            chargeV: { goodMin: 13.8, goodMax: 14.4, badMin: 13.5, unit: 'V' },
            crankV: { good: 11.5, bad: 10.0, unit: 'V' }
        },
        leadacid: {
            restV: { good: 12.5, bad: 12.0, unit: 'V' },
            dropV: { good: 0.15, bad: 0.4, unit: 'V/Jour' },
            chargeV: { goodMin: 13.8, goodMax: 14.8, badMin: 13.3, unit: 'V' },
            crankV: { good: 10.5, bad: 9.0, unit: 'V' }
        }
    };

    async function processXlsFile(file, bType) {
        return new Promise((resolve) => {
            const reader = new FileReader();
            reader.onload = function(e) {
                const data = new Uint8Array(e.target.result);
                const workbook = XLSX.read(data, {type: 'array'});
                const sheetName = workbook.SheetNames[0];
                const json = XLSX.utils.sheet_to_json(workbook.Sheets[sheetName], {header: 1});

                const allVoltages = json.slice(1)
                    .map(row => parseFloat(row[1]))
                    .filter(v => !isNaN(v) && v > 5.0 && v < 16.0);

                if (allVoltages.length < 20) {
                    resolve({ rest: null, drop: null });
                    return;
                }

                const filterThreshold = (bType === 'lifepo4') ? 13.6 : 13.2;
                const stableStartV = (bType === 'lifepo4') ? 13.3 : 12.7;

                const sortedV = [...allVoltages].sort((a, b) => a - b);
                const restV = sortedV[Math.floor(sortedV.length * 0.05)];

                const staticVs = allVoltages.filter(v => v < filterThreshold);

                if (staticVs.length < 10) {
                    resolve({ rest: restV.toFixed(2), drop: 0 });
                    return;
                }

                let startIndex = staticVs.findIndex(v => v <= stableStartV);
                if (startIndex === -1 || (staticVs.length - startIndex) < 10) {
                    startIndex = 0;
                }

                const endIndex = staticVs.length - 1;
                const headRange = staticVs.slice(startIndex, startIndex + 5);
                const tailRange = staticVs.slice(-5);
                
                const avgFirstV = headRange.reduce((a, b) => a + b, 0) / headRange.length;
                const avgLastV = tailRange.reduce((a, b) => a + b, 0) / tailRange.length;

                const effectivePoints = endIndex - startIndex;
                const totalDays = (effectivePoints > 0) ? (effectivePoints * 2) / 1440 : (allVoltages.length * 2) / 1440; 

                let realDrop = (avgFirstV - avgLastV) / totalDays;
                if (realDrop < 0) realDrop = 0;

                resolve({ 
                    rest: restV.toFixed(2), 
                    drop: realDrop.toFixed(2)
                });
            };
            reader.readAsArrayBuffer(file);
        });
    }

    async function generateReport() {
        const btn = document.querySelector('.btn-generate');
        btn.innerText = "Analyse en cours...";
        btn.disabled = true;

        const bType = document.getElementById('batteryType').value;
        const std = thresholds[bType];

        let metrics = { restingV: null, leakageDrop: null, avgChargeV: null, minCrankV: null };

        const fileXls = document.getElementById('fileOffline').files[0];
        if (fileXls) {
            const xlsResult = await processXlsFile(fileXls, bType);
            metrics.restingV = xlsResult.rest;
            metrics.leakageDrop = xlsResult.drop;
        }

        const rawFiles = document.getElementById('fileRaw').files;
        if (rawFiles.length > 0) {
            let sum1Hz = 0, count1Hz = 0;
            let crankMinList = []; 
            let fallback1HzMin = 99.0; 

            const engineOnThreshold = bType === 'lifepo4' ? 13.6 : 13.5;
            const engineOffThreshold = bType === 'lifepo4' ? 13.3 : 12.8;

            for (let i = 0; i < rawFiles.length; i++) {
                const text = await rawFiles[i].text();
                const lines = text.split('\n');
                const pattern1Hz = /d1550700[0-9a-fA-F]{6}([0-9a-fA-F]{4})/i;

                let isEngineRunning = false;
                let window15s = []; 
                let tempHexStream = ""; 

                lines.forEach(line => {
                    let lowerLine = line.trim().toLowerCase();

                    const match1Hz = lowerLine.match(pattern1Hz);
                    if (match1Hz) {
                        let v = parseInt(match1Hz[1], 16) / 100;
                        
                        window15s.push(v);
                        if (window15s.length > 15) window15s.shift();

                        if (v >= engineOnThreshold) {
                            isEngineRunning = true;
                        } 
                        
                        if (isEngineRunning) {
                            if (v < engineOnThreshold && window15s.length === 15) {
                                let v15sAgo = window15s[0];
                                if ((v15sAgo - v) >= 0.10) isEngineRunning = false;
                            }
                            if (v <= engineOffThreshold) isEngineRunning = false;
                        }

                        if (isEngineRunning && v > 10.0 && v < 16.0) { 
                            sum1Hz += v; 
                            count1Hz++; 
                        }

                        if (v > 6.0 && v < 15.0 && v < fallback1HzMin) fallback1HzMin = v;
                    } 
                    
                    if (lowerLine.includes('receive:')) {
                        let content = lowerLine.split("receive:")[1].trim();
                        if (/^[0-9a-f]+$/.test(content) && !content.startsWith("d15507")) {
                            tempHexStream += content;
                        }
                    }

                    if (lowerLine.includes('cranking.add:ok')) {
                        let parts = tempHexStream.split("fffffe");
                        if (parts.length > 1) {
                            let lastPart = parts[parts.length - 1];
                            if (lastPart.includes("fffefe")) {
                                let curveData = lastPart.split("fffefe")[0];
                                let localMin = 99.0; 
                                
                                for (let j = 0; j < curveData.length - 2; j += 3) {
                                    let voltage = parseInt(curveData.substring(j, j + 3), 16) / 100.0;
                                    if (!isNaN(voltage) && voltage >= 3.0 && voltage <= 15.0) {
                                        if (voltage < localMin) {
                                            localMin = voltage;
                                        }
                                    }
                                }
                                
                                if (localMin < 99.0) {
                                    crankMinList.push(localMin);
                                }
                            }
                        }
                        tempHexStream = ""; 
                    }
                });
            }

            if (count1Hz > 0) metrics.avgChargeV = (sum1Hz / count1Hz).toFixed(2);
            
            if (crankMinList.length > 0) {
                crankMinList.sort((a, b) => a - b);
                let takeCount = Math.min(3, crankMinList.length);
                let sumCrank = 0;
                
                for (let i = 0; i < takeCount; i++) {
                    sumCrank += crankMinList[i];
                }
                
                metrics.minCrankV = (sumCrank / takeCount).toFixed(2);
            } else if (fallback1HzMin < 99.0) {
                metrics.minCrankV = fallback1HzMin.toFixed(2);
            }
        }

        renderTable(metrics, std, bType);

        btn.innerText = "Générer le Bilan de Santé Complet";
        btn.disabled = false;
        document.getElementById('reportSection').style.display = 'block';
    }

    function evaluate(value, goodRule, badRule, type) {
        if (value === null) return { text: "Donnée non fournie", class: "status-none" };
        let v = parseFloat(value);
        if (type === 'higher_is_better') {
            if (v >= goodRule) return { text: "Excellent", class: "status-good" };
            if (v <= badRule) return { text: "Contrôle Requis", class: "status-bad" };
            return { text: "Moyen", class: "status-warn" };
        } else if (type === 'lower_is_better') {
            if (v <= goodRule) return { text: "Excellent", class: "status-good" };
            if (v >= badRule) return { text: "Forte Fuite", class: "status-bad" };
            return { text: "Légère Décharge", class: "status-warn" };
        } else if (type === 'range') {
            if (v >= goodRule[0] && v <= goodRule[1]) return { text: "Charge Optimale", class: "status-good" };
            if (v < badRule || v > 15.0) return { text: "Alternateur Anormal", class: "status-bad" };
            return { text: "Charge Faible", class: "status-warn" };
        }
    }

    function renderTable(m, std, bType) {
        document.getElementById('reportDate').innerText = `Bilan généré le : ${new Date().toLocaleString()}`;
        document.getElementById('reportConfig').innerText = `Configuration : ${bType === 'lifepo4' ? 'Norme LiFePO4' : 'Plomb-Acide Standard'}`;

        const tbody = document.getElementById('tableBody');
        tbody.innerHTML = "";

        const items = [
            {
                name: "Santé du Stockage<br>(Tension Statique)",
                val: m.restingV, unit: "V",
                goodStr: `> ${std.restV.good}V`, badStr: `< ${std.restV.bad}V`,
                eval: evaluate(m.restingV, std.restV.good, std.restV.bad, 'higher_is_better')
            },
            {
                name: "Courant de Veille<br>(Chute Journalière)",
                val: m.leakageDrop, unit: "V/Jour",
                goodStr: `< ${std.dropV.good}V`, badStr: `> ${std.dropV.bad}V`,
                eval: evaluate(m.leakageDrop, std.dropV.good, std.dropV.bad, 'lower_is_better')
            },
            {
                name: "Circuit de Charge (Moyenne)",
                val: m.avgChargeV, unit: "V",
                goodStr: `${std.chargeV.goodMin} - ${std.chargeV.goodMax}V`, badStr: `< ${std.chargeV.badMin}V`,
                eval: evaluate(m.avgChargeV, [std.chargeV.goodMin, std.chargeV.goodMax], std.chargeV.badMin, 'range')
            },
            {
                name: "Tension Min Démarrage (Moy.)",
                val: m.minCrankV, unit: "V",
                goodStr: `> ${std.crankV.good}V`, badStr: `< ${std.crankV.bad}V`,
                eval: evaluate(m.minCrankV, std.crankV.good, std.crankV.bad, 'higher_is_better')
            }
        ];

        items.forEach(i => {
            let valStr = i.val !== null ? `<strong style="font-size:18px;">${i.val}</strong> <span style="font-size:12px;color:#8b949e;">${i.unit}</span>` : "-";
            let tr = `<tr>
                <td>${i.name}</td>
                <td>${valStr}</td>
                <td style="color:#8b949e;">${i.goodStr}</td>
                <td style="color:#8b949e;">${i.badStr}</td>
                <td class="${i.eval.class}">${i.eval.text}</td>
            </tr>`;
            tbody.innerHTML += tr;
        });

        let diagnosis = "";
        if (m.restingV === null && m.avgChargeV === null && m.minCrankV === null) {
            diagnosis = "Données insuffisantes pour un diagnostic complet. Veuillez charger les fichiers requis.";
        } else {
            let issues = [];
            let warnings = [];
            let goodPoints = [];

            if (m.restingV !== null) {
                if (m.restingV < std.restV.bad) {
                    if (bType === 'lifepo4') {
                        issues.push(`<strong>[Stockage Anormal]</strong> La tension statique (${m.restingV}V) est trop basse. Les cellules peuvent être vieillissantes (forte résistance interne) ou la batterie n'a pas atteint l'équilibrage actif du BMS.`);
                    } else {
                        issues.push(`<strong>[Stockage Anormal]</strong> La tension statique (${m.restingV}V) est trop faible. Sulfatation probable des plaques ou décharge profonde.`);
                    }
                } else if (m.restingV < std.restV.good) {
                    if (bType === 'lifepo4') {
                        warnings.push(`<strong>[Stockage Faible]</strong> Tension statique (${m.restingV}V) sous l'optimum. Envisagez un long trajet ou une charge complète externe pour rééquilibrer le pack.`);
                    } else {
                        warnings.push(`<strong>[Stockage Faible]</strong> Tension statique (${m.restingV}V) modérée. Effectuez une recharge d'entretien.`);
                    }
                } else {
                    goodPoints.push(`Tension statique exemplaire (${m.restingV}V), rétention d'énergie optimale.`);
                }
            }

            if (m.leakageDrop !== null) {
                const dropVal = parseFloat(m.leakageDrop);
                const dStd = std.dropV;

                if (dropVal > dStd.bad) {
                    issues.push(`<strong>[Alerte Décharge]</strong> Chute de tension journalière (${dropVal}V/Jour) excessive. Vérifiez les accessoires de bord (dashcam en veille, boîtiers OBD).`);
                } else if (dropVal > dStd.good) {
                    warnings.push(`<strong>[Décharge Légère]</strong> Chute journalière (${dropVal}V/Jour) légèrement haute. Prudence lors des stationnements prolongés.`);
                } else if (dropVal <= dStd.excellent) {
                    goodPoints.push(`Chute journalière imperceptible (${dropVal}V/Jour). Aucune fuite parasite, mise en veille parfaite.`);
                } else {
                    goodPoints.push(`Chute de veille (${dropVal}V/Jour) conforme aux tolérances constructeur.`);
                }
            }

            if (m.avgChargeV !== null) {
                if (m.avgChargeV < std.chargeV.badMin || m.avgChargeV > 15.0) {
                    issues.push(`<strong>[Alternateur Anormal]</strong> Tension moyenne de conduite (${m.avgChargeV}V) hors tolérance. Si <13.5V : usure des charbons ou glissement courroie ; si >15V : risque de surtension du régulateur !`);
                } else if (m.avgChargeV < std.chargeV.goodMin) {
                    warnings.push(`<strong>[Charge Modérée]</strong> Tension moyenne (${m.avgChargeV}V) basse. Si équipé d'un système intelligent AMS/Start-Stop, ce comportement éco-énergie peut être normal.`);
                } else {
                    goodPoints.push(`Système de charge sain. Tension stabilisée à (${m.avgChargeV}V).`);
                }
            }

            if (m.minCrankV !== null) {
                if (m.minCrankV < std.crankV.bad) {
                    issues.push(`<strong>[Démarrage Difficile]</strong> Chute de tension minimale (${m.minCrankV}V) alarmante. Forte résistance interne ou fatigue mécanique du démarreur.`);
                } else if (m.minCrankV < std.crankV.good) {
                    warnings.push(`<strong>[Démarrage Faible]</strong> Tension de lancement (${m.minCrankV}V) basse. Risque de difficultés par temps glacial.`);
                } else {
                    goodPoints.push(`Excellente tenue au démarrage (${m.minCrankV}V résiduels), preuve d'une très faible impédance.`);
                }
            }

            if (issues.length > 0) {
                diagnosis += `<h4 style="color: #f85149; margin-top: 0;">🚨 Anomalies critiques nécessitant une inspection :</h4><ul style="margin-top: 5px;">`;
                issues.forEach(issue => diagnosis += `<li>${issue}</li>`);
                diagnosis += `</ul>`;
            }
            
            if (warnings.length > 0) {
                diagnosis += `<h4 style="color: #d29922;">⚠️ Points d'attention ou d'entretien recommandés :</h4><ul style="margin-top: 5px;">`;
                warnings.forEach(warn => diagnosis += `<li>${warn}</li>`);
                diagnosis += `</ul>`;
            }

            if (issues.length === 0 && warnings.length === 0) {
                 diagnosis = `<h4 style="color: #3fb950; margin-top: 0;">✅ Circuit électrique en excellente santé !</h4>`;
                 diagnosis += `<p>L'analyse multi-paramètres confirme un fonctionnement irréprochable :</p><ul>`;
                 goodPoints.forEach(pt => diagnosis += `<li>${pt}</li>`);
                 diagnosis += `</ul>`;
                 if (bType === 'lifepo4') {
                     diagnosis += `<p style="color: #58a6ff; font-size: 14px; margin-top: 10px;">💡 <strong>Note Ingénierie :</strong> Les avantages de la batterie LiFePO4 sont parfaitement exploités (autodécharge nulle et puissance instantanée maximale).</p>`;
                 }
            } else if (goodPoints.length > 0) {
                 diagnosis += `<h4 style="color: #3fb950;">✅ Paramètres Conformes :</h4><ul style="margin-top: 5px;">`;
                 goodPoints.forEach(pt => diagnosis += `<li>${pt}</li>`);
                 diagnosis += `</ul>`;
            }
        }
        document.getElementById('aiDiagnosis').innerHTML = diagnosis;
    }
</script>
