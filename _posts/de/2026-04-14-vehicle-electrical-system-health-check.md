---
layout: post
title: "Ganzheitliche Gesundheitsprüfung des Fahrzeugelektriksystems: Langzeitdatenanalyse BM6"
lang: de
date: 2026-04-14 09:52:00
categories: Auto
tags: [Auto-Batterie, Lithium-Eisen-Phosphat-Akku, Blei-Säure-Akkumulator, Generator-Diagnose, Datenanalyse, Parallellaufstrom (Leckage), Startspannung]
description: "Wie kann man wissenschaftlich beurteilen, ob eine Batterie ausgetauscht werden sollte? Dieser Artikel stellt ein System zur Gesundheitsüberprüfung des Fahrzeugstromnetzes vor. Durch die Analyse von 1-Hz-Monitoringdaten und Hochfrequenz-Startprotokollen bei 100 Hz wird das Stillstandsleakage, der Ladeeffizienz während der Fahrt sowie die Explosionskraft beim Startmoment in tieferer Ebene bewertet."
keywords: "Batteriegesundheit, Lithium-Eisenphosphat-Batterie, LiFePO4, Blei-Säure-Akku, Dunkelstrom-Test, Startspannung, Generatorprüfung, Bluetooth-Tagebuchanalyse, Fahrzeugenergie"
image: /images/battery-health-report-analysis.webp
faq:
  - question: "Welche Schlüsselindizes überprüft dieses System hauptsächlich?"
    answer: "Das System bewertet vier Kernindizes: 1. Batteriengesundheit (Leerlaufspannung), 2. Leckstromzustand (Spannungsabfall in der Nacht), 3. Generatorsystem (Durchschnittsfahrerspannung), 4. Startimpulsstärke (Startminimalspannung)."
  - question: "Was ist der Unterschied bei den Kriterien zur Unterscheidung von Lithium-Eisenphosphat- und Blei-Säure-Akkus?"
    answer: "Das System verfügt über zwei Referenzwerte. Beispielsweise muss die gute Ruhespannung eines Lithium-Eisenphosphat-Akus (LiFePO4) größer als 13,2 V sein, während sie bei einem normalen Blei-Säure-Aku 12,5 V beträgt; beim Startimpulsspannungsanteil liegt der Standard für Lithium-Eisenphosphat bei 11,5 V und für Blei-Säure bei 10,5 V."
  - question: "Wie kann man feststellen, ob ein Fahrzeug einen Leckage (Nachtstrom) aufweist?"
    answer: "Das System berechnet den \"Täglichen Spannungsabfall (V/Tag)\" über eine längere Ruhezeit. Wenn der Abfall größer als 0,3 V (Lithium-Eisenphosphat) oder 0,4 V (Blei-Säure-Akku) ist, wird ein zu hoher Leckagezustand festgestellt; es wird empfohlen, den Zustand des Fahrzeugschreibers, Diebstahlschutzgeräts oder OBD2-Geräts auf eine korrekte Schlafphase zu überprüfen."
  - question: "Warum ist eine Datenrate von 100 Hz zur Analyse der Startspannung erforderlich?"
    answer: "Der Moment des Motorstarts dauert weniger als eine Sekunde. Eine Standardaufzeichnung mit 1 Hz (ein Mal pro Sekunde) kann leicht den Tiefpunkt der Spannung übersehen. Durch die Hochfrequenzabtastung bei 100 Hz lässt sich der Spannungsabfall während des Betriebs des Startmotors präzise erfassen, um festzustellen, ob der Innenwiderstand der Zelle zugenommen hat oder ob der Startmotor altert."
  - question: "Was ist die Grundlage für die Feststellung eines Fehlfunktionierens des Generators?"
    answer: "Das System filtert Daten nach dem Starten des Motors. Wenn der durchschnittliche Spannungswert während der Fahrt unter 13,5 V liegt oder über 15,0 V steigt, wird dies als Alterung des Generators oder ein Defekt am Regler eingestuft. Für Fahrzeuge mit einem Ladesystem (AMS) werden zudem spezielle Hinweise für niedrige Spannungen im Energiesparmodus gegeben."
  - question: "Was ist zu tun, wenn das Lithium-Eisen-Phosphat-Akku im Bericht als 'schwache Speicherkapazität' angezeigt wird?"
    answer: "Wenn die Ruhevoltspannung des Lithium-Eisen-Phosphat-Akkus 13,2 V nicht erreicht hat, empfehlen wir eine lange Fahrt oder das Aufladen mit einem speziellen Ladegerät bis zum Vollladestand, um die aktive Zellenausgleichsfunktion der BMS zu aktivieren und so die Lebensdauer und Leistung des Akkus sicherzustellen."
---

<!-- Externe Bibliotheken zum Laden zur Analyse von Excel-Dateien -->  
<script src="https://cdn.jsdelivr.net/npm/xlsx/dist/xlsx.full.min.js"></script>

<style>
    /* Die folgenden Stile werden nur auf die Elemente dieser Seite angewendet */
    .app-container {
        font-family: 'Segoe UI', 'Microsoft JhengHei', sans-serif;
        background: #0d1117;
        color: #c9d1d9;
        max-width: 1000px;
        margin: 0 auto;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #30363d;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .app-container h1 { text-align: center; color: #58a6ff; margin-bottom: 30px; }
    .control-panel {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
        margin-bottom: 30px;
        background: #0d1117;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #30363d;
    }
    .file-input-group {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }
    .file-input-group label { font-weight: bold; color: #8b949e; font-size: 14px; }
    .app-container input[type="file"], .app-container select {
        background: #21262d; padding: 10px; border-radius: 6px; border: 1px solid #30363d; color: #c9d1d9;
    }
    .file-hint { font-size: 12px; color: #8b949e; margin-top: -5px; }
    .btn-generate {
        width: 100%; padding: 15px; background: #238636; color: white; border: none; border-radius: 8px;
        font-size: 18px; font-weight: bold; cursor: pointer; transition: 0.2s; margin-top: 10px;
    }
    .btn-generate:hover { background: #2ea043; }
    
    .report-section { display: none; margin-top: 40px; }
    .patient-info {
        display: flex; justify-content: space-between; border-bottom: 2px solid #30363d;
        padding-bottom: 10px; margin-bottom: 20px; color: #8b949e;
    }
    .app-container table {
        width: 100%; border-collapse: collapse; margin-bottom: 30px;
        background: #0d1117; border-radius: 8px; overflow: hidden;
    }
    .app-container th, .app-container td { padding: 15px; text-align: center; border: 1px solid #30363d; }
    .app-container th { background: #21262d; color: #c9d1d9; font-weight: bold; }
    .app-container td:first-child { text-align: left; font-weight: bold; color: #58a6ff; }
    
    .status-good { color: #3fb950; font-weight: bold; }
    .status-warn { color: #d29922; font-weight: bold; }
    .status-bad { color: #f85149; font-weight: bold; }
    .status-none { color: #8b949e; font-style: italic; }

.doctor-notes {
        background: rgba(90, 247, 255, 0.1); padding: 20px; border-radius: 10px;
        border-left: 5px solid #388bfd; line-height: 1.6;
    }

<div class="app-container">
    <h1>System zur Gesundheitsüberprüfung des Fahrzeug-Netzwerksystems</h1>
</div>

<div class="control-panel">
        <div class="file-input-group">
            <label>📁 1. Langzeit-Offline-Aufzeichnungen (Statische Leckstromprüfung)</label>
            <input type="file" id="fileOffline" accept=".xls,.xlsx,.csv">
            <span class="file-hint">Unterstützte Excel-Tabelleformate für die Exportfunktion</span>
        </div>
        <div class="file-input-group">
            <label>📁 2. Roh-Bluetooth-Protokolle (Erzeugungs- und Startanalyse)</label>
            <input type="file" id="fileRaw" accept=".txt,.log" multiple>
            <span class="file-hint">Mehrere Dateien auswählbar. Automatische Dekodierung gemischter 1-Hz- und 100-Hz-Pakete über mehrere Tage</span>
        </div>
        <div class="file-input-group">
            <label>⚙️ Batteriechemie-Einstellungen</label>
            <select id="batteryType">
                <option value="lifepo4">Lithium-Eisenphosphat-Batterie (LiFePO4)</option>
                <option value="leadacid">Standard-Säurebatterien (Lead-Acid)</option>
            </select>
        </div>
    </div>

<button class="btn-generate" onclick="generateReport()">Generiere umfassende Gesundheitsbericht</button>

<div class="report-section" id="reportSection">
    <div class="patient-info">
        <span id="reportDate"><b>Berichtsdatum:</b> YYYY/MM/DD</span>
        <span id="reportConfig"><b>Analyse-Einstellungen:</b> Lithium-Eisen-Phosphat-Basis</span>
    </div>

<table id="reportTable">
            <thead>
                <tr>
                    <th width="20%">Prüfungsposten</th>
                    <th width="20%">Aktuelle Daten</th>
                    <th width="20%">Gute Standards</th>
                    <th width="20%">Abweichungsstandards</th>
                    <th width="20%">Gesamtbewertung</th>
                </tr>
            </thead>
            <tbody id="tableBody">
            </tbody>
        </table>

<div class="doctor-notes">
            <h3 style="margin-top:0; color:#58a6ff;">📋 Systematische Diagnoseempfehlungen</h3>
            <div id="aiDiagnosis">Bitte laden Sie Daten hoch, um eine umfassende Analyse zu erhalten.</div>
        </div>
    </div>
</div>

<script>
    const thresholds = {
        lifepo4: {
            restV: { gut: 13.2, schlecht: 13.0, Einheit: 'V' },
            dropV: { hervorragend: 0.01, gut: 0.02, schlecht: 0.05, Einheit: 'V/Tag' },
            chargeV: { gutMin: 13.8, gutMax: 14.4, schlechtMin: 13.5, Einheit: 'V' },
            crankV: { gut: 11.5, schlecht: 10.0, Einheit: 'V' }
        },
        leadacid: {
            restV: { gut: 12.5, schlecht: 12.0, Einheit: 'V' },
            dropV: { gut: 0.15, schlecht: 0.4, Einheit: 'V/Tag' },
            chargeV: { gutMin: 13.8, gutMax: 14.8, schlechtMin: 13.3, Einheit: 'V' },
            crankV: { gut: 10.5, schlecht: 9.0, Einheit: 'V' }
        }
    };
</script>

async function processXlsFile(file, bType) {
            return new Promise((resolve) => {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const data = new Uint8Array(e.target.result);
                    const workbook = XLSX.read(data, {type: 'array'});
                    const sheetName = workbook.SheetNames[0];
                    const json = XLSX.utils.sheet_to_json(workbook.Sheets[sheetName], {header: 1});

// 1. Alle ursprünglichen Spannungen abrufen (Überschriftenzeile und Ausreißer ausschließen)
                    const allVoltages = json.slice(1)
                        .map(row => parseFloat(row[1]))
                        .filter(v => !isNaN(v) && v > 5.0 && v < 16.0);

if (allVoltages.length < 20) {
                        resolve({ rest: null, drop: null });
                        return;
                    }

// 2. Schwellenwerte nach Batterietyp festlegen
                    // filterThreshold: Werte darüber deuten darauf hin, dass der Generator lädt – diese werden bei der Analyse des Ruhezustands nicht berücksichtigt
                    // stableStartV: Nur unter diesem Wert wird angenommen, dass die „Oberflächenladung" abgeklungen ist; hier beginnt die Berechnung des tatsächlichen Spannungsabfalls
                    const filterThreshold = (bType === 'lifepo4') ? 13.6 : 13.2;
                    const stableStartV = (bType === 'lifepo4') ? 13.3 : 12.7;

// 3. Berechnung der Batteriengesundheit (Leerlaufspannung)
                    // Nehmen Sie den 5. Wert des sortierten Arrays, was bedeutet, dass dies die häufigste stabile niedrige Spannung während der Ruhezustandsperiode ist
                    const sortedV = [...allVoltages].sort((a, b) => a - b);
                    const restV = sortedV[Math.floor(sortedV.length * 0.05)];

// 4. Filtern Sie statische Datenintervalle, die nicht im Ladevorgang sind
const staticVs = allVoltages.filter(v => v < filterThreshold);

if (staticVs.length < 10) {
                        resolve({ rest: restV.toFixed(2), drop: 0 });
                        return;
                    }

// 5. Suche nach dem „echten" Spannungsabfall-Startpunkt: Überspringe den Bereich der Oberflächenspannung, die unmittelbar nach dem Ausschalten von 13,6 V auf 13,3 V fällt  
                    let startIndex = staticVs.findIndex(v => v <= stableStartV);
                    
                    // Fehlervermeidung: Wenn alle Daten über dem Stabilisierungsschwellenwert liegen oder verbleibende Daten zu wenige sind, wird vom Anfang ausgehend berechnet.
                    if (startIndex === -1 || (staticVs.length - startIndex) < 10) {
                        startIndex = 0;
                    }

const endIndex = staticVs.length - 1;

// 6. Start- und Endspannung ermitteln (5 Messwerte im Mittel nehmen, um Rauschen einzelner Punkte zu vermeiden)
                    const headRange = staticVs.slice(startIndex, startIndex + 5);
                    const tailRange = staticVs.slice(-5);
                    
                    const avgFirstV = headRange.reduce((a, b) => a + b, 0) / headRange.length;
                    const avgLastV = tailRange.reduce((a, b) => a + b, 0) / tailRange.length;

// 7. Berechnung der Anzahl von Tagen für den gültigen Analysebereich (BM6 Offline-Aufzeichnungen sind typischerweise alle 2 Minuten eine Eintrag)
                    const effectivePoints = endIndex - startIndex;
                    const totalDays = (effectivePoints > 0) ? (effectivePoints * 2) / 1440 : (allVoltages.length * 2) / 1440;

// 8. Berechnung des täglichen Druckabfalls: (Startmittelwert – Endemittelwert) / Anzahl der Tage
                    let realDrop = (avgFirstV - avgLastV) / totalDays;

// Korrektur des Problems mit negativen Werten: Steigt die Spannung stattdessen an, bedeutet dies, dass die Daten für eine Analyse von Leckströmen nicht geeignet sind. Setzen wir den Wert zwingend auf Null.
                    if (realDrop < 0) realDrop = 0;

resolve({ 
                        rest: restV.toFixed(2), 
                        drop: realDrop.toFixed(2)
                    });
                };
                reader.readAsArrayBuffer(file);
            });
        }

```javascript
async function generateReport() {
    const btn = document.querySelector('.btn-generate');
    btn.innerText = "Datenanalyse läuft...";
    btn.disabled = true;
}
```

const bType = document.getElementById('batteryType').value;
        const std = thresholds[bType];

let metrikken = { ruhevoltage: null, leckagedrop: null, durchschnittsladevoltage: null, minimalestartvoltage: null };

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

const engineOnThreshold = bType === 'lifepo4' ? 13,6 : 13,5;
            const engineOffThreshold = bType === 'lifepo4' ? 13,3 : 12,8;

for (let i = 0; i < rawFiles.length; i++) {
                const text = await rawFiles[i].text();
                const lines = text.split('\n');
                
                const pattern1Hz = /d1550700[0-9a-fA-F]{6}([0-9a-fA-F]{4})/i;

let istMotorLaufend = false;
                let fenster15Sekunden = []; 
                let vorläufigerHexDatenstrom = "";

lines.forEach((line) => {
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

if (istMotorLaufend && v > 10,0 && v < 16,0) { 
                            sum1Hz += v; 
                            count1Hz++; 
                        }

if (v > 6.0 && v < 15.0 && v < fallback1HzMin) {
    fallback1HzMin = v;
} 

if (lowerLine.includes('receive:')) {
    let content = lowerLine.split("receive:")[1].trim();
    if (/^[0-9a-f]+$/.test(content) && !content.startsWith("d15507")) {
        tempHexStream += content;
    }
}

if ('cranking.add:ok'.includes('lowerLine')) { // Hinweis: Der Originalcode verwendet `.includes()` auf einem String, der als Array behandelt wird. Da `lowerLine` ein String ist und `'cranking.add:ok'` auch ein String ist, sollte die Bedingung eigentlich sein: `if (lowerLine.includes('cranking.add:ok'))`. Die obige Zeile zeigt den korrekten Logikfluss auf Deutsch im Kontext der Übersetzung.
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

renderTable(Metriken, Std, TypB);

btn.innerText = „Gesamtes Gesundheitsbericht erstellen“;  
        btn.disabled = false;  
        document.getElementById('reportSection').style.display = 'block';

function evaluate(value, goodRule, badRule, type) {
        if (value === null) return { text: "Keine Daten verfügbar", class: "status-none" };
        let v = parseFloat(value);
        if (type === 'higher_is_better') {
            if (v >= goodRule) return { text: "Gut", class: "status-good" };
            if (v <= badRule) return { text: "Instandsetzung erforderlich", class: "status-bad" };
            return { text: "Akzeptabel", class: "status-warn" };
        } else if (type === 'lower_is_better') {
            if (v <= goodRule) return { text: "Gut", class: "status-good" };
            if (v >= badRule) return { text: "Leckstrom zu hoch", class: "status-bad" };
            return { text: "Erhöht", class: "status-warn" };
        } else if (type === 'range') {
            if (v >= goodRule[0] && v <= goodRule[1]) return { text: "Generator gesund", class: "status-good" };
            if (v < badRule || v > 15.0) return { text: "Generatorenbefund unregelmäßig", class: "status-bad" };
            return { text: "Ladeleistung zu niedrig", class: "status-warn" };
        }
    }

function renderTable(m, std, bType) {
    document.getElementById('reportDate').innerText = `Berichtserstellungszeitpunkt: ${new Date().toLocaleString()}`;
    document.getElementById('reportConfig').innerText = `${bType === 'lifepo4' ? 'Lithium-Eisenphosphat-Batterie' : 'Herkömmliche Blei-Säure-Akku'}-Analyse`;

Es ist nicht möglich, diesen Code in Deutsch zu übersetzen, da es sich um JavaScript-Code handelt und keine natürliche Sprache enthält. Die Zeilen können jedoch im Kontext einer deutschen Anwendungsoberfläche (z.B. für Fehlermeldungen oder Labels) mit deutscher Texten versehen werden.

const items = [
    {
        name: "Ladezustand<br>(Leerlaufspannung)",
        val: m.restingV, unit: "V",
        goodStr: `> ${std.restV.good}V`, badStr: `< ${std.restV.bad}V`,
        eval: evaluate(m.restingV, std.restV.good, std.restV.bad, 'higher_is_better')
    },
    {
        name: "Leckstromzustand<br>(Nachtspannungsabfall)",
        val: m.leakageDrop, unit: "V/Tag",
        goodStr: `< ${std.dropV.good}V`, badStr: `> ${std.dropV.bad}V`,
        eval: evaluate(m.leakageDrop, std.dropV.good, std.dropV.bad, 'lower_is_better')
    },
    {
        name: "Ladesystem (Durchschnitt)",
        val: m.avgChargeV, unit: "V",
        goodStr: `${std.chargeV.goodMin} - ${std.chargeV.goodMax}V`, badStr: `< ${std.chargeV.badMin}V`,
        eval: evaluate(m.avgChargeV, [std.chargeV.goodMin, std.chargeV.goodMax], std.chargeV.badMin, 'range')
    },
    {
        name: "Startminimale Spannung (Durchschnitt)",
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
    diagnosis = "Es liegen keine ausreichenden Daten für eine umfassende Bewertung vor. Bitte überprüfen Sie, ob das entsprechende Datei hochgeladen wurde.";
} else {
    let issues = [];
    let warnings = [];
    let goodPoints = [];

if (m.restingV !== null) {
    if (m.restingV < std.restV.bad) {
        if (bType === 'lifepo4') {
            issues.push(`<strong>[Akkubefehldung]</strong> Die Ruhevoltage (${m.restingV} V) ist zu niedrig. Die Zellen könnten altert sein und ihre Kapazität verloren haben (zu hoher Innenwiderstand), oder das Fahrzeug wurde über längere Zeit nur auf kurzen Strecken gefahren, wodurch die BMS nicht effektiv eine Gleichlastladung der Zellen durchführen konnte.`);
        } else {
            issues.push(`<strong>[Akkubefehldung]</strong> Die Ruhevoltage (${m.restingV} V) ist zu niedrig. Die Batterieplättchen könnten altert sein (Verschwärzung), was die Speicherkapazität verringert, oder das Fahrzeug wurde über längere Zeit nur auf kurzen Strecken gefahren, wodurch eine chronische unvollständige Aufladung eintritt.`);
        }
    } else if (m.restingV < std.restV.good) {
        if (bType === 'lifepo4') {
            warnings.push(`<strong>[Akkubefehldung]</strong> Die Ruhevoltage (${m.restingV} V) entspricht nicht dem optimalen Zustand. Es wird empfohlen, eine lange Fahrt vorzunehmen oder einen speziellen Ladevorgang mit einem dedizierten Ladegerät durchzuführen, um die Batterie vollständig aufzuladen und damit die aktive Zellentrennungsfunktion der BMS auszulösen.`);
        } else {
            warnings.push(`<strong>[Akkubefehldung]</strong> Die Ruhevoltage (${m.restingV} V) entspricht nicht dem optimalen Zustand. Es wird empfohlen, eine lange Fahrt auf Autobahn vorzunehmen oder mit einem externen Ladegerät einen tiefgreifenden Wartungsaufladung durchzuführen, um die Plättchen zu aktivieren.`);
        }
    } else {
        goodPoints.push(`Die Ruhevoltage bleibt bei (${m.restingV} V) stabil; die Speicherkapazität der Batterie ist ausgezeichnet.`);
    }
}

if (m.leakageDrop !== null) {
const dropVal = parseFloat(m.leakageDrop);
const dStd = std.dropV;

if (dropVal > dStd.bad) {
    issues.push(`<strong>[Leckwarnung]</strong> Der tägliche Spannungsabfall (${dropVal} V/Tag) ist zu hoch. Bitte überprüfen Sie den Parkmonitor des Aufzeichners oder das OBD2-Gerät.`);
} else if (dropVal > dStd.good) {
    warnings.push(`<strong>[Leichte Leckage]</strong> Der tägliche Spannungsabfall (${dropVal} V/Tag) ist leicht erhöht; bei längerem Parken auf die Batterieladung achten.`);
} else if (dropVal <= dStd.excellent) {
    goodPoints.push(`Der tägliche Spannungsabfall beträgt nur ${dropVal} V/Tag, das elektrische System leckt nicht vollständig aus und der Schlafmodus ist perfekt!`);
} else {
    goodPoints.push(`Die Ruhestandspannung (${dropVal} V/Tag) zeigt ein gutes Ergebnis an und entspricht den Gesundheitsstandards.`);
}

if (m.avgChargeV !== null) {
    if (m.avgChargeV < std.chargeV.badMin || m.avgChargeV > 15.0) {
        issues.push(`<strong>[Ladeabweichung]</strong> Die durchschnittliche Ladespannung während der Fahrt (${m.avgChargeV} V) liegt außerhalb des normalen Bereichs. Ist sie zu niedrig, könnte dies auf ein Alterungsproblem des Generators, Verschleiß der Kohlebürsten oder Schlupf in der Antriebskette zurückzuführen sein; ist sie ungewöhnlich hoch (über 15 V), dann kann es an einem Defekt im Laderegulator liegen!`);
    } else if (m.avgChargeV < std.chargeV.goodMin) {
        warnings.push(`<strong>[Niedrige Ladung]</strong> Die durchschnittliche Ladespannung während der Fahrt (${m.avgChargeV} V) ist zu niedrig.<strong>Hinweis:</strong> Falls ein „Ladesteuerungssystem (AMS)" vorhanden ist, handelt es sich um einen normalen Energiespar-Effekt; fehlt dieses System, sollte die Effizienz des Generators auf Verschleiß überprüft werden.`);
    } else {
        goodPoints.push(`Das Ladesystem funktioniert ordnungsgemäß. Die durchschnittliche Ladespannung während der Fahrt bleibt stabil bei (${m.avgChargeV} V) und die Leistung ist ausgezeichnet.`);
    }
}

if (m.minCrankV !== null) {
    if (m.minCrankV < std.crankV.bad) {
        issues.push(`<strong>[Startschwierigkeiten]</strong> Die Mindestspannung beim Start (${m.minCrankV} V) ist zu niedrig. Dies liegt meist an einem vergrößerten Innenwiderstand der Batterie oder einer reduzierten Leistungsfähigkeit bei kurzzeitiger Entladung; wenn die Batterie neu ist, prüfen Sie bitte den Zustand des Anlassers auf Alterungsschäden oder eine schlechte Berührung mit dem Massepunkt.`);
    } else if (m.minCrankV < std.crankV.good) {
        warnings.push(`<strong>[Start schwach]</strong> Die Spannung beim Start (${m.minCrankV} V) liegt etwas niedrig. Es ist noch kein gefährlicher Wert erreicht, aber unter niedrigen Temperaturen kann es zu Verzögerungen beim Start kommen.`);
    } else {
        goodPoints.push(`Der Spannungsabfall während des Starts ist minimal (die Endspannung bleibt bei ${m.minCrankV} V) ausreichend; dies zeigt einen sehr geringen Innenwiderstand der Batterie und eine hohe Leistungsfähigkeit bei großem Stromfluss.`);
    }
}

if (issues.length > 0) {
    diagnosis += `<h4 style="color: #f85149; margin-top: 0;">🚨 Hochrisikoanomalien festgestellt, Werkstattinspektion empfohlen:</h4><ul style="margin-top: 5px;">`;
    issues.forEach(issue => diagnosis += `<li>${issue}</li>`);
    diagnosis += `</ul>`;
}

if (warnings.length > 0) {
    diagnosis += `<h4 style="color: #d29922;">⚠️ Gegenstände zur weiteren Beobachtung oder Wartung erforderlich:</h4><ul style="margin-top: 5px;">`;
    warnings.forEach(warn => diagnosis += `<li>${warn}</li>`);
    diagnosis += `</ul>`;
}

if (issues.length === 0 && warnings.length === 0) {
                 diagnosis = `<h4 style="color: #3fb950; margin-top: 0;">✅ Das System ist sehr gesund!</h4>`;
                 diagnosis += `<p>Die umfassende Datenanalyse über mehrere Tage zeigt ein hervorragendes Verhalten Ihres Fahrzeug-Elektrosystems:</p><ul>`;
                 goodPoints.forEach(pt => diagnosis += `<li>${pt}</li>`);
                 diagnosis += `</ul>`;
                 if (bType === 'lifepo4') {
                     diagnosis += `<p style="color: #58a6ff; font-size: 14px; margin-top: 10px;">💡 <strong>Technische Anmerkung:</strong> Die Eigenschaften Ihres Lithium-Eisenphosphat-Bettes zeigen sich positiv mit einem extrem niedrigen Selbstentladewert und einer hohen Fähigkeit zur momentanen Entladung, was perfekt auf die aktuellen Bedingungen im Fahrzeug passt.</p>`;
                 }
            } else if (goodPoints.length > 0) {
                 diagnosis += `<h4 style="color: #3fb950;">✅ Gute Leistungsbereiche:</h4><ul style="margin-top: 5px;">`;
                 goodPoints.forEach(pt => diagnosis += `<li>${pt}</li>`);
                 diagnosis += `</ul>`;
            }
        }
        document.getElementById('aiDiagnosis').innerHTML = diagnosis;
    }
</script>