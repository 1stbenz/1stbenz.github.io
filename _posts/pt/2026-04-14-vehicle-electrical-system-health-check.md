---
layout: post
title: "Diagnóstico Completo do Sistema Elétrico Automotivo: Análise de Dados BM6"
lang: pt
date: 2026-04-14 09:52:00
categories: Auto
tags: [Bateria Automotiva, Monitor de Bateria, Conhecimento Automotivo]
description: "Como saber cientificamente a hora certa de trocar a bateria? Este artigo apresenta um sistema de diagnóstico elétrico veicular. Analisando dados em repouso de 1 Hz e curvas de partida em alta frequência a 100 Hz, avalia fuga de corrente, eficiência do alternador e pico de partida."
keywords: "Saúde da Bateria, LiFePO4, Bateria Chumbo-Ácido, Teste Corrente de Fuga, Tensão de Partida, Verificação do Alternador, Análise Log Bluetooth, Elétrica Veicular"
image: /images/battery-health-report-analysis.webp
faq:
  - question: "Quais indicadores cruciais este sistema avalia?"
    answer: "O sistema analisa quatro métricas centrais: 1. Saúde do armazenamento (Tensão estática em repouso), 2. Corrente de fuga (Queda diária de tensão), 3. Eficiência do alternador (Tensão média em trânsito), 4. Potência de partida (Menor tensão sob arranque)."
  - question: "Qual a diferença nos padrões entre baterias LiFePO4 e chumbo-ácido?"
    answer: "O sistema adota padrões duplos. Por exemplo, a tensão estática ideal para LiFePO4 é >13,2 V, contra 12,5 V para chumbo-ácido. Já para o pico mínimo de partida, a referência para LiFePO4 é 11,5 V e para chumbo é 10,5 V."
  - question: "Como identificar fuga de corrente (corrente parasita em repouso)?"
    answer: "O sistema calcula a 'queda diária de tensão (V/dia)' em períodos de repouso contínuo. Se ultrapassar 0,3 V (LiFePO4) ou 0,4 V (Chumbo), aponta-se fuga elevada, sugerindo verificar câmeras veiculares, rastreadores ou módulos OBD2."
  - question: "Por que dados a 100 Hz são indispensáveis na análise de partida?"
    answer: "O arranque do motor dura menos de um segundo. Um log comum de 1 Hz perde facilmente o vale mais baixo de tensão. A amostragem de 100 Hz registra o colapso exato sob o motor de arranque, detectando resistência interna alta ou motor de partida desgastado."
  - question: "Qual a base de avaliação para falhas no alternador?"
    answer: "O sistema monitora a tensão com o motor em funcionamento. Se a média em rodagem ficar abaixo de 13,5 V (ou acima de 15,0 V), aponta-se desgaste do alternador ou falha no regulador, considerando veículos com sistemas inteligentes AMS."
  - question: "O que fazer se o relatório indicar 'Armazenamento Fraco' para LiFePO4?"
    answer: "Se a tensão estática cair abaixo de 13,2 V, recomenda-se uma viagem longa ou recarga externa com carregador apropriado para ativar o balanceamento ativo de células do BMS."
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
    <h1>Diagnóstico do Sistema Elétrico Automotivo</h1>

    <div class="control-panel">
        <div class="file-input-group">
            <label>📁 1. Registros Offline de Longo Prazo (Teste de Fuga)</label>
            <input type="file" id="fileOffline" accept=".xls,.xlsx,.csv">
            <span class="file-hint">Compatível com planilhas Excel (.xlsx, .xls)</span>
        </div>
        <div class="file-input-group">
            <label>📁 2. Arquivos de Log Bluetooth (Alternador e Partida)</label>
            <input type="file" id="fileRaw" accept=".txt,.log" multiple>
            <span class="file-hint">Permite seleção múltipla. Processa dados 1Hz e 100Hz</span>
        </div>
        <div class="file-input-group">
            <label>⚙️ Química da Bateria</label>
            <select id="batteryType">
                <option value="lifepo4">Fosfato de Ferro-Lítio (LiFePO4)</option>
                <option value="leadacid">Chumbo-Ácido Padrão / AGM</option>
            </select>
        </div>
    </div>
    
    <button class="btn-generate" onclick="generateReport()">Gerar Relatório de Saúde Elétrica</button>

    <div class="report-section" id="reportSection">
        <div class="patient-info">
            <span id="reportDate">Data do Relatório: AAAA/MM/DD</span>
            <span id="reportConfig">Configuração: LiFePO4 Padrão</span>
        </div>

        <table id="reportTable">
            <thead>
                <tr>
                    <th width="20%">Item de Avaliação</th>
                    <th width="20%">Dado Medido</th>
                    <th width="20%">Padrão Ideal</th>
                    <th width="20%">Limite de Alerta</th>
                    <th width="20%">Diagnóstico</th>
                </tr>
            </thead>
            <tbody id="tableBody">
            </tbody>
        </table>

        <div class="doctor-notes">
            <h3 style="margin-top:0; color:#58a6ff;">📋 Parecer Diagnóstico Abrangente</h3>
            <div id="aiDiagnosis">Envie os arquivos para obter a análise completa.</div>
        </div>
    </div>
</div>

<script>
    const thresholds = {
        lifepo4: {
            restV: { good: 13.2, bad: 13.0, unit: 'V' },
            dropV: { excellent: 0.01, good: 0.02, bad: 0.05, unit: 'V/Dia' },
            chargeV: { goodMin: 13.8, goodMax: 14.4, badMin: 13.5, unit: 'V' },
            crankV: { good: 11.5, bad: 10.0, unit: 'V' }
        },
        leadacid: {
            restV: { good: 12.5, bad: 12.0, unit: 'V' },
            dropV: { good: 0.15, bad: 0.4, unit: 'V/Dia' },
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
        btn.innerText = "Processando dados...";
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

        btn.innerText = "Gerar Relatório de Saúde Elétrica";
        btn.disabled = false;
        document.getElementById('reportSection').style.display = 'block';
    }

    function evaluate(value, goodRule, badRule, type) {
        if (value === null) return { text: "Sem dados fornecidos", class: "status-none" };
        let v = parseFloat(value);
        if (type === 'higher_is_better') {
            if (v >= goodRule) return { text: "Excelente", class: "status-good" };
            if (v <= badRule) return { text: "Revisão Necessária", class: "status-bad" };
            return { text: "Regular", class: "status-warn" };
        } else if (type === 'lower_is_better') {
            if (v <= goodRule) return { text: "Excelente", class: "status-good" };
            if (v >= badRule) return { text: "Fuga Elevada", class: "status-bad" };
            return { text: "Leve Fuga", class: "status-warn" };
        } else if (type === 'range') {
            if (v >= goodRule[0] && v <= goodRule[1]) return { text: "Carga Saudável", class: "status-good" };
            if (v < badRule || v > 15.0) return { text: "Alternador Anormal", class: "status-bad" };
            return { text: "Carga Fraca", class: "status-warn" };
        }
    }

    function renderTable(m, std, bType) {
        document.getElementById('reportDate').innerText = `Relatório gerado em: ${new Date().toLocaleString()}`;
        document.getElementById('reportConfig').innerText = `Configuração: ${bType === 'lifepo4' ? 'LiFePO4 Padrão' : 'Chumbo-Ácido Padrão'}`;

        const tbody = document.getElementById('tableBody');
        tbody.innerHTML = "";

        const items = [
            {
                name: "Saúde de Armazenamento<br>(Tensão Estática)",
                val: m.restingV, unit: "V",
                goodStr: `> ${std.restV.good}V`, badStr: `< ${std.restV.bad}V`,
                eval: evaluate(m.restingV, std.restV.good, std.restV.bad, 'higher_is_better')
            },
            {
                name: "Fuga em Repouso<br>(Queda Diária)",
                val: m.leakageDrop, unit: "V/Dia",
                goodStr: `< ${std.dropV.good}V`, badStr: `> ${std.dropV.bad}V`,
                eval: evaluate(m.leakageDrop, std.dropV.good, std.dropV.bad, 'lower_is_better')
            },
            {
                name: "Sistema de Carga (Média)",
                val: m.avgChargeV, unit: "V",
                goodStr: `${std.chargeV.goodMin} - ${std.chargeV.goodMax}V`, badStr: `< ${std.chargeV.badMin}V`,
                eval: evaluate(m.avgChargeV, [std.chargeV.goodMin, std.chargeV.goodMax], std.chargeV.badMin, 'range')
            },
            {
                name: "Tensão Mínima Partida (Méd.)",
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
            diagnosis = "Dados insuficientes para diagnóstico completo. Carregue os arquivos pertinentes.";
        } else {
            let issues = [];
            let warnings = [];
            let goodPoints = [];

            if (m.restingV !== null) {
                if (m.restingV < std.restV.bad) {
                    if (bType === 'lifepo4') {
                        issues.push(`<strong>[Armazenamento Crítico]</strong> Tensão estática (${m.restingV}V) excessivamente baixa. As células podem estar degradadas (alta resistência interna) ou a bateria não atingiu a carga completa com balanceamento ativo.`);
                    } else {
                        issues.push(`<strong>[Armazenamento Crítico]</strong> Tensão estática (${m.restingV}V) muito baixa. Placas com sulfatação severa ou descarga profunda.`);
                    }
                } else if (m.restingV < std.restV.good) {
                    if (bType === 'lifepo4') {
                        warnings.push(`<strong>[Armazenamento Fraco]</strong> Tensão estática (${m.restingV}V) abaixo do ideal. Recomenda-se viagem longa ou carga lenta externa.`);
                    } else {
                        warnings.push(`<strong>[Armazenamento Fraco]</strong> Tensão estática (${m.restingV}V) moderada. Realize recarga de manutenção.`);
                    }
                } else {
                    goodPoints.push(`Tensão estática em nível ótimo (${m.restingV}V), indicando excelente capacidade de retenção.`);
                }
            }

            if (m.leakageDrop !== null) {
                const dropVal = parseFloat(m.leakageDrop);
                const dStd = std.dropV;

                if (dropVal > dStd.bad) {
                    issues.push(`<strong>[Alerta de Fuga]</strong> Queda diária (${dropVal}V/Dia) muito alta. Inspecione dashcams em modo sentinela, rastreadores ou módulos OBD.`);
                } else if (dropVal > dStd.good) {
                    warnings.push(`<strong>[Leve Fuga]</strong> Queda diária (${dropVal}V/Dia) acima da média. Cuidado com longos períodos de inatividade.`);
                } else if (dropVal <= dStd.excellent) {
                    goodPoints.push(`Queda diária residual ínfima (${dropVal}V/Dia). Modo de espera veicular perfeito.`);
                } else {
                    goodPoints.push(`Queda em repouso (${dropVal}V/Dia) dentro dos limites normais.`);
                }
            }

            if (m.avgChargeV !== null) {
                if (m.avgChargeV < std.chargeV.badMin || m.avgChargeV > 15.0) {
                    issues.push(`<strong>[Alternador Anormal]</strong> Tensão média de condução (${m.avgChargeV}V) fora da tolerância. Se <13.5V: desgaste de escovas ou correia frouxa; se >15V: risco de sobretensão no regulador!`);
                } else if (m.avgChargeV < std.chargeV.goodMin) {
                    warnings.push(`<strong>[Carga Moderada]</strong> Tensão média (${m.avgChargeV}V) reduzida. Em carros com sistema inteligente AMS/Start-Stop, pode ser funcionamento normal de economia de combustível.`);
                } else {
                    goodPoints.push(`Sistema de carga em ordem. Tensão média estável em (${m.avgChargeV}V).`);
                }
            }

            if (m.minCrankV !== null) {
                if (m.minCrankV < std.crankV.bad) {
                    issues.push(`<strong>[Partida Pesada]</strong> Tensão mínima de partida (${m.minCrankV}V) perigosamente baixa. Resistência interna elevada ou motor de arranque desgastado.`);
                } else if (m.minCrankV < std.crankV.good) {
                    warnings.push(`<strong>[Partida Fraca]</strong> Tensão de disparo (${m.minCrankV}V) moderada. Atenção em dias muito frios.`);
                } else {
                    goodPoints.push(`Excelente firmeza de tensão na partida (${m.minCrankV}V restantes), comprovando resistência interna mínima.`);
                }
            }

            if (issues.length > 0) {
                diagnosis += `<h4 style="color: #f85149; margin-top: 0;">🚨 Anomalias graves detectadas, recomenda-se inspeção imediata:</h4><ul style="margin-top: 5px;">`;
                issues.forEach(issue => diagnosis += `<li>${issue}</li>`);
                diagnosis += `</ul>`;
            }
            
            if (warnings.length > 0) {
                diagnosis += `<h4 style="color: #d29922;">⚠️ Pontos que exigem atenção ou recarga de manutenção:</h4><ul style="margin-top: 5px;">`;
                warnings.forEach(warn => diagnosis += `<li>${warn}</li>`);
                diagnosis += `</ul>`;
            }

            if (issues.length === 0 && warnings.length === 0) {
                 diagnosis = `<h4 style="color: #3fb950; margin-top: 0;">✅ Sistema elétrico em perfeito estado!</h4>`;
                 diagnosis += `<p>Com base nos dados analisados, seu veículo apresenta excelente saúde elétrica:</p><ul>`;
                 goodPoints.forEach(pt => diagnosis += `<li>${pt}</li>`);
                 diagnosis += `</ul>`;
                 if (bType === 'lifepo4') {
                     diagnosis += `<p style="color: #58a6ff; font-size: 14px; margin-top: 10px;">💡 <strong>Nota Técnica:</strong> Os atributos da bateria LiFePO4 estão em pleno aproveitamento, com auto-descarga praticamente nula e forte potência de disparo.</p>`;
                 }
            } else if (goodPoints.length > 0) {
                 diagnosis += `<h4 style="color: #3fb950;">✅ Itens Conformes:</h4><ul style="margin-top: 5px;">`;
                 goodPoints.forEach(pt => diagnosis += `<li>${pt}</li>`);
                 diagnosis += `</ul>`;
            }
        }
        document.getElementById('aiDiagnosis').innerHTML = diagnosis;
    }
</script>
