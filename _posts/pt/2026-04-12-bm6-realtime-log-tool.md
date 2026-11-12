---
layout: post
title: "Ferramenta de Análise de Dados em Tempo Real 1Hz BM6/BM200"
lang: pt
date: 2026-04-12 10:00:00
categories: Auto
tags: [Bateria Automotiva, Monitor de Bateria, Ferramentas DIY, Análise de Dados]
description: "Converta pacotes hexadecimais de logs brutos do BM6 em registros legíveis de tensão e temperatura por segundo, com exportação para CSV e gráficos interativos com zoom sincronizado."
keywords: "BM6, Monitor de Bateria, Dados em Tempo Real, Registro de Tensão, Registro de Temperatura, Análise de Log, Decodificação Hexadecimal, Exportação CSV, Bateria LiFePO4"
image: /images/bm6-cranking-preview.webp
faq:
  - question: "Qual a diferença entre esta ferramenta e o analisador de partida?"
    answer: "A ferramenta de partida foi concebida para amostragem de alta frequência a 100 Hz durante o arranque do motor (cranking.add). Esta ferramenta processa as transmissões contínuas a 1 Hz (pacotes d15507), ideal para acompanhar a tensão do alternador ou a temperatura durante viagens."
  - question: "Como a ferramenta localiza os dados corretos no arquivo de log?"
    answer: "Ela busca automaticamente pacotes iniciados por `d15507`, identificados no protocolo BM6 como dados de status em tempo real. Basta que o arquivo contenha os registros de recepção Bluetooth para ser processado."
  - question: "É possível baixar os dados processados?"
    answer: "Sim. Ao término do processamento, surge o botão 'Baixar Arquivo CSV'. Você pode exportar as medições para o Excel ou softwares de análise gráfica."
  - question: "Por que os gráficos são exibidos separadamente?"
    answer: "Para evitar sobreposição e distorção de escalas, 'Tensão (V)' e 'Temperatura (°C)' ficam em gráficos verticais independentes, porém com eixo de tempo e zoom perfeitamente sincronizados."
  - question: "Há riscos de vazamento de dados no envio dos logs?"
    answer: "Nenhum. A ferramenta roda integralmente no navegador em JavaScript. Todo o processamento ocorre no seu computador, sem transmissão para servidores."
---

<div id="bm6-realtime-container" style="max-width: 950px; margin: 20px auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #ffffff; color: #333333; padding: 25px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e5e7eb; position: relative;">

    <h2 id="ui-title" style="text-align: center; color: #04384c !important; margin-bottom: 22px; margin-top: 5px; font-weight: 800; font-size: 22px; background: none; border: none;">Ferramenta de Análise em Tempo Real BM6</h2>

    <div
        style="background: rgba(4, 56, 76, 0.05); padding: 15px 20px; border-radius: 10px; margin-bottom: 25px; border-left: 5px solid #04384c; font-size: 14.5px; line-height: 1.6; color: #475569;">
        <strong id="ui-desc-title" style="color: #04384c;">Suporte à extração de dados 1Hz e exportação em CSV</strong><br>
        <span id="ui-desc-body">Esta ferramenta localiza automaticamente <b style="color:#04384c;">pacotes d15507</b> no Log, converte dados hexadecimais em registros de tensão e temperatura por segundo e gera gráficos interativos com zoom sincronizado.</span>
    </div>

    <div
        style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 20px; border-radius: 10px; margin-bottom: 25px; display: flex; flex-direction: column; align-items: center; gap: 15px;">
        <div style="display: flex; gap: 10px;">
            <button id="uploadTrigger"
                style="background: #04384c; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 15px; transition: 0.2s;">📁 Carregar Arquivo Log (.txt / .log)</button>
            <button id="downloadBtn" style="background: #16a34a; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 15px; display: none;">📥 Baixar Arquivo CSV</button>
        </div>
        <input type="file" id="logFileInput" accept=".txt,.log" style="display:none">
        <div id="status-text" style="color: #64748b; font-size: 14px; font-weight: bold;">Selecione um arquivo de log contendo transmissões em tempo real</div>
    </div>

    <div style="background: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e2e8f0; box-sizing: border-box; box-shadow: 0 1px 4px rgba(0,0,0,0.04);">
        <div style="height: 280px; width: 100%; margin-bottom: 10px;">
            <canvas id="voltageChart"></canvas>
        </div>
        <div style="height: 280px; width: 100%;">
            <canvas id="tempChart"></canvas>
        </div>
    </div>

</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns"></script>
<script src="https://cdn.jsdelivr.net/npm/hammerjs"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-zoom"></script>

<script>
(function() {
    const fileInput = document.getElementById('logFileInput');
    const uploadTrigger = document.getElementById('uploadTrigger');
    const downloadBtn = document.getElementById('downloadBtn');
    const statusText = document.getElementById('status-text');

    let vChart, tChart;
    let parsedData = [];
    let isResetting = false;

    Chart.defaults.color = '#64748b';
    Chart.defaults.borderColor = '#e2e8f0';

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
                ctx.strokeStyle = 'rgba(4, 56, 76, 0.35)';
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
            chart.options.scales.y.min = minV - padding;
            chart.options.scales.y.max = maxV + padding;
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
                        backgroundColor: 'rgba(255, 255, 255, 0.96)',
                        titleColor: '#0f172a',
                        bodyColor: '#334155',
                        borderColor: '#cbd5e1',
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

    vChart = new Chart(document.getElementById('voltageChart'), createChartConfig('Tensão (V)', '#1176d4', 'Tensão (V)'));
    tChart = new Chart(document.getElementById('tempChart'), createChartConfig('Temperatura (°C)', '#dc2626', 'Temperatura (°C)'));

    uploadTrigger.onclick = () => fileInput.click();

    fileInput.onchange = function(e) {
        const file = e.target.files[0];
        if (!file) return;

        statusText.innerHTML = `Processando <b style="color:#58a6ff;">${file.name}</b>...`;
        
        const reader = new FileReader();
        reader.onload = function(e) {
            processData(e.target.result);
        };
        reader.readAsText(file);
    };

    function processData(text) {
        const lines = text.split('\n');
        const pattern = /^(\d{2}:\d{2}:\d{2}):receive:d1550700([0-9a-fA-F]{2})[0-9a-fA-F]{2}([0-9a-fA-F]{2})([0-9a-fA-F]{4})/;
        
        const vData = [];
        const tData = [];
        parsedData = [];

        let currentDay = 1;
        let lastTimeObj = null;

        lines.forEach(line => {
            const match = line.trim().match(pattern);
            if (match) {
                const timeStr = match[1];
                const tempC = parseInt(match[2], 16);
                const voltage = parseInt(match[4], 16) / 100.0;
                
                const [h, m, s] = timeStr.split(':').map(Number);
                const currentTimeObj = new Date(2026, 0, currentDay, h, m, s);
                
                if (lastTimeObj && currentTimeObj < lastTimeObj) {
                    currentDay++;
                    currentTimeObj.setDate(currentDay);
                }
                lastTimeObj = currentTimeObj;
                
                const timeVal = currentTimeObj.getTime();

                vData.push({ x: timeVal, y: voltage });
                tData.push({ x: timeVal, y: tempC });
                
                parsedData.push([timeStr, voltage, tempC]);
            }
        });

        if (parsedData.length > 0) {
            statusText.innerHTML = `✅ Concluído! Extraídos <b style="color:#3fb950;">${parsedData.length}</b> pontos de dados.`;
            downloadBtn.style.display = 'inline-block';
            
            isResetting = true;

            [vChart, tChart].forEach(chart => {
                if (chart.resetZoom) chart.resetZoom('none');
            });

            vChart.data.datasets[0].data = vData;
            tChart.data.datasets[0].data = tData;

            const vValues = vData.map(d => d.y);
            const tValues = tData.map(d => d.y);
            const minV = Math.min(...vValues), maxV = Math.max(...vValues);
            const minT = Math.min(...tValues), maxT = Math.max(...tValues);
            
            const vPad = (maxV - minV) * 0.15 || 0.5;
            const tPad = (maxT - minT) * 0.15 || 2;

            vChart.options.scales.y.min = minV - vPad;
            vChart.options.scales.y.max = maxV + vPad;
            tChart.options.scales.y.min = minT - tPad;
            tChart.options.scales.y.max = maxT + tPad;

            vChart.update('none');
            tChart.update('none');

            setTimeout(() => { isResetting = false; }, 200);

        } else {
            statusText.innerHTML = `<span style="color:#f85149;">❌ Nenhum dado válido encontrado. Certifique-se de que o log contém pacotes d15507.</span>`;
            downloadBtn.style.display = 'none';
        }
    }

    downloadBtn.onclick = function() {
        if (parsedData.length === 0) return;
        let csvContent = "Horário,Tensão(V),Temperatura(°C)\n";
        parsedData.forEach(row => { csvContent += row.join(",") + "\n"; });
        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.setAttribute("href", url);
        link.setAttribute("download", "dados_bm6_segundo.csv");
        link.click();
    };
})();
</script>
