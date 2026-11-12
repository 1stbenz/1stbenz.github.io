---
layout: post
title: "أداة تحليل بيانات الوقت الفعلي بتردد 1 هرتز BM6/BM200"
lang: ar
date: 2026-04-12 10:00:00
categories: Auto
tags: [بطارية السيارة, مراقب البطارية, أدوات تصنعها بنفسك, تحليل البيانات]
description: "تحويل حزم Hex من سجلات BM6 الخام إلى بيانات جهد ودرجة حرارة واضحة لكل ثانية، مع دعم تصدير ملفات CSV ورسم بياني تفاعلي مزدوج المحاور بتكبير متزامن."
keywords: "BM6, مراقب البطارية, بيانات الوقت الفعلي, تسجيل الجهد, تسجيل درجة الحرارة, تحليل السجلات, فك ترميز Hex, تصدير CSV, بطارية LiFePO4"
image: /images/bm6-cranking-preview.webp
faq:
  - question: "ما الفرق بين هذه الأداة ومحلل شكل موجة بدء التشغيل (Cranking)؟"
    answer: "صُممت أداة بدء التشغيل لتحليل بيانات التردد العالي 100 هرتز أثناء دوران المحرك (cranking.add). أما هذه الأداة، فهي مخصصة لبيانات البث المباشر المستمرة بتردد 1 هرتز (حزم d15507)، وهي مثالية لمراقبة جهد شحن الدينامو وتقلبات الحرارة أثناء القيادة الطويلة."
  - question: "كيف تكتشف الأداة البيانات الصحيحة داخل ملف السجل؟"
    answer: "تبحث الأداة تلقائياً عن الحزم التي تبدأ بـ `d15507` المعرفة في بروتوكول BM6 كبيانات حالة آنية. وطالما أن ملفك يتضمن سجلات استقبال البلوتوث receive، فسيتم التحليل بنجاح."
  - question: "هل يمكن تحميل البيانات الناتجة للاستخدام الخارجي؟"
    answer: "نعم. بمجرد انتهاء التحليل، يظهر زر 'تحميل ملف CSV'. يمكنك تصدير كافة القياسات إلى برامج Excel لدراسة الاتجاهات طويلة الأمد."
  - question: "لماذا تم فصل الرسمين البيانيين؟"
    answer: "لتفادي تداخل المقاييس المختلفة، فُصل 'الجهد (فولت)' و'الحرارة (مئوية)' في مخططين علوي وسفلي، مع مشاركة نفس محور الزمن وخاصية التكبير المتزامن لتسهيل المقارنة اللحظية."
  - question: "هل هناك أي مخاوف تتعلق بالخصوصية عند رفع السجلات؟"
    answer: "لا توجد مخاوف إطلاقاً. تعمل الأداة بتقنيات الواجهة الأمامية الخالصة (JavaScript) داخل متصفحك دون إرسال أي بايت إلى خوادم خارجية."
---

<div id="bm6-realtime-container" dir="rtl" style="max-width: 950px; margin: 20px auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #ffffff; color: #333333; padding: 25px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e5e7eb; position: relative;">

    <h2 id="ui-title" style="text-align: center; color: #04384c !important; margin-bottom: 22px; margin-top: 5px; font-weight: 800; font-size: 22px; background: none; border: none;">أداة تحليل بيانات الوقت الفعلي BM6</h2>

    <div
        style="background: rgba(4, 56, 76, 0.05); padding: 15px 20px; border-radius: 10px; margin-bottom: 25px; border-right: 5px solid #04384c; font-size: 14.5px; line-height: 1.6; color: #475569;">
        <strong id="ui-desc-title" style="color: #04384c;">تدعم استخراج بيانات 1 هرتز وتصدير ملفات CSV</strong><br>
        <span id="ui-desc-body">تقوم الأداة باكتشاف <b style="color:#04384c;">حزم d15507</b> في ملفات السجلات، وتحويل بيانات Hex إلى سجلات جهد وحرارة لكل ثانية، مع رسوم بيانية تفاعلية متزامنة وخاصية التنزيل.</span>
    </div>

    <div
        style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 20px; border-radius: 10px; margin-bottom: 25px; display: flex; flex-direction: column; align-items: center; gap: 15px;">
        <div style="display: flex; gap: 10px; flex-wrap: wrap; justify-content: center;">
            <button id="uploadTrigger"
                style="background: #04384c; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 15px; transition: 0.2s;">📁 رفع ملف السجل (.txt / .log)</button>
            <button id="downloadBtn" style="background: #16a34a; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 15px; display: none;">📥 تحميل ملف CSV</button>
        </div>
        <input type="file" id="logFileInput" accept=".txt,.log" style="display:none">
        <div id="status-text" style="color: #64748b; font-size: 14px; font-weight: bold;">يرجى اختيار ملف يحتوي على بيانات البث اللحظي</div>
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

    vChart = new Chart(document.getElementById('voltageChart'), createChartConfig('الجهد (فولت)', '#1176d4', 'الجهد (فولت)'));
    tChart = new Chart(document.getElementById('tempChart'), createChartConfig('الحرارة (مئوية)', '#dc2626', 'الحرارة (مئوية)'));

    uploadTrigger.onclick = () => fileInput.click();

    fileInput.onchange = function(e) {
        const file = e.target.files[0];
        if (!file) return;

        statusText.innerHTML = `جاري تحليل <b style="color:#58a6ff;">${file.name}</b>...`;
        
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
            statusText.innerHTML = `✅ تم التحليل بنجاح! تم استخراج <b style="color:#3fb950;">${parsedData.length}</b> نقطة قياس.`;
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
            statusText.innerHTML = `<span style="color:#f85149;">❌ لم يتم العثور على بيانات صالحة. يرجى التأكد من احتواء السجل على حزم d15507.</span>`;
            downloadBtn.style.display = 'none';
        }
    }

    downloadBtn.onclick = function() {
        if (parsedData.length === 0) return;
        let csvContent = "الوقت,الجهد(فولت),الحرارة(مئوية)\n";
        parsedData.forEach(row => { csvContent += row.join(",") + "\n"; });
        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.setAttribute("href", url);
        link.setAttribute("download", "بيانات_bm6_ثانية.csv");
        link.click();
    };
})();
</script>
