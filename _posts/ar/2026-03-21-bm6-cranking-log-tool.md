---
layout: post
title: "أداة تحليل سجلات بدء تشغيل المحرك بتردد 100 هرتز BM6/BM200"
lang: ar
date: 2026-03-21 10:00:00
categories: Auto
tags: [بطارية السيارة, مراقب البطارية, أدوات تصنعها بنفسك, تحليل البيانات]
description: "أداة متخصصة لتحليل شكل موجة بدء التشغيل (Cranking) لمراقب بطارية BM6 بلوتوث. تقوم بفك تشفير حزم Hex من ملفات السجلات الخام لرسم منحنى جهد بدء التشغيل بدقة فائقة 100 هرتز، وتحديد أدنى نقطة جهد ونقطة فصل بادئ الحركة (السلف) تلقائياً عبر خوارزمية العتبة الديناميكية."
keywords: "BM6, مراقب بطارية بلوتوث, شكل موجة بدء التشغيل, جهد بدء التشغيل, Cranking, محلل سجلات, بطارية سيارة, بطارية LiFePO4"
image: /images/bm6-cranking-preview2.webp
faq:
  - question: "ما المشكلة التي تحلها هذه الأداة؟"
    answer: "لا يتيح التطبيق الرسمي تصدير أشكال موجات بدء التشغيل عالية الدقة. تقرأ هذه الأداة ملفات السجلات الخام الملتقطة عبر البلوتوث، وتفك حزم Hex المشفرة لإعادة بناء منحنى الجهد بدقة 100 هرتز، مما يتيح تقييم قدرة التفريغ اللحظي للبطارية وحالة بادئ الحركة (السلف)."
  - question: "ماذا تعني النقطتان الحمراء والبرتقالية على الرسم البياني؟"
    answer: "تمثل النقطة الحمراء (Min) أدنى جهد تنخفض إليه البطارية تحت الحمل الثقيل لبادئ الحركة. بينما تمثل النقطة البرتقالية (فصل بادئ الحركة) نقطة الانعطاف المحسوبة بالخوارزمية عندما ينقطع التيار عن بادئ الحركة ويبدأ المحرك بالدوران ذاتياً."
  - question: "كيف أحصل على ملف Log لرفعه إلى الأداة؟"
    answer: "يمكنك استخدام تطبيق تحليل حزم البلوتوث على هاتفك أو ميزة تصدير السجلات المدمجة في تطبيق BM6 الرسمي لحفظ بيانات البث كملف .txt أو .log، مع التأكد من أن الملف يشمل لحظة تشغيل المحرك."
  - question: "هل هناك أي مخاوف تتعلق بالخصوصية أو تسريب البيانات عند رفع الملف؟"
    answer: "لا توجد أي مخاوف على الإطلاق. تعمل هذه الأداة بالكامل داخل المتصفح من جهة العميل (JavaScript)، وتتم معالجة البيانات وتحليلها ورسمها محلياً دون إرسال أي معلومة إلى خوادم خارجية."
  - question: "ما هو الحد الأدنى لجهد بدء التشغيل (Min) الذي يشير إلى ضعف البطارية؟"
    answer: "بالنسبة لبطارية الرصاص أو AGM السليمة بجهد 12 فولت في درجة حرارة الغرفة، يظل أدنى جهد لبدء التشغيل عادةً فوق 9.6 فولت. إذا انخفضت النقطة الحمراء باستمرار إلى ما دون 9.0 فولت، فقد يشير ذلك إلى تقادم البطارية وارتفاع مقاومتها الداخلية."
  - question: "لماذا تظهر رسالة 'لم يتم العثور على شكل موجة بدء تشغيل صالح'؟"
    answer: "يحدث هذا عادةً إذا لم يلتقط ملف السجل الحزم في لحظة التشغيل بدقة، أو بسبب فقدان حزم البلوتوث عند ابتعاد الهاتف عن السيارة. تأكد من وجود علامة 'cranking.add:ok' في السجل."
  - question: "كيف تحدد الخوارزمية النقطة البرتقالية (نقطة فصل بادئ الحركة)؟"
    answer: "تعتمد الأداة خوارزمية 'العتبة الديناميكية'. يكتشف البرنامج تلقائياً جهد الاستقرار المبدئي قبل التشغيل، وعندما يرتد الجهد مقترباً من هذا المستوى، يتعقب عكساً آخر قاع محلي، مما يضمن التوافق التام مع بطاريات الرصاص وبطاريات LiFePO4."
---

<div id="car-app-container" dir="rtl" style="max-width: 950px; margin: 20px auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #ffffff; color: #333333; padding: 25px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e5e7eb; position: relative;">

    <h2 id="ui-title" style="text-align: center; color: #04384c !important; margin-bottom: 22px; margin-top: 5px; font-weight: 800; font-size: 22px; background: none; border: none;">أداة تحليل شكل موجة بدء تشغيل المحرك BM6</h2>

    <div
        style="background: rgba(210, 153, 34, 0.08); padding: 15px 20px; border-radius: 10px; margin-bottom: 25px; border-right: 5px solid #d29922; font-size: 14.5px; line-height: 1.6; color: #475569;">
        <strong id="ui-desc-title" style="color: #b45309;">تدعم كشف العتبة الديناميكية (متوافقة مع بطاريات الرصاص و LiFePO4)</strong><br>
        <span id="ui-desc-body">تقرأ هذه الأداة ملفات <b style="color:#04384c;">.log</b> الخام مباشرة، وتحول حزم Hex إلى شكل موجة عالي الدقة بتردد 100 هرتز، مع تحديد أدنى نقطة جهد ونقطة فصل بادئ التشغيل تلقائياً.</span>
    </div>

    <div
        style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 15px 25px; border-radius: 10px; gap: 10px; margin-bottom: 25px; display: flex; align-items: center; justify-content: center; flex-wrap: wrap;">
        <button id="uploadTrigger"
            style="background: #04384c; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 15px; transition: 0.2s;">📁
            رفع ملف السجل (.txt / .log)</button>
        <input type="file" id="logFileInput" accept=".txt,.log" style="display:none">
        <button id="loadSampleBtn" style="background: #ffffff; color: #04384c; border: 1px solid #cbd5e1; padding: 9px 20px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 14px; text-decoration: none; display: flex; align-items: center; transition: 0.2s;">📄 تحميل ملف تجريبي</button>

    </div>

    <div id="status-text" style="text-align: center; color: #64748b; margin-bottom: 20px; font-size: 14px; font-weight: bold;">يرجى رفع ملف سجل يحتوي على بيانات البث لبدء التحليل</div>

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
            statusText.innerHTML = `جاري تحميل <b style="color:#58a6ff;">الملف التجريبي (bm6_100Hz.log)</b> ...`;
            chartsWrapper.innerHTML = ''; 

            fetch('/files/bm6_100Hz.log')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('فشل استرداد الملف التجريبي (HTTP ' + response.status + ')');
                    }
                    return response.text();
                })
                .then(text => {
                    processLogData(text);
                })
                .catch(error => {
                    statusText.innerHTML = `<span style="color:#f85149;">❌ فشل تحميل الملف التجريبي: ${error.message}</span>`;
                });
        };

        fileInput.addEventListener('change', function (e) {
            const file = e.target.files[0];
            if (!file) return;

            statusText.innerHTML = `جاري تحليل <b style="color:#58a6ff;">${file.name}</b> ...`;
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
            let currentLogTime = "غير معروف";
            let rollingRealTimeTemp = "غير معروف";

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
                                    let eventTemp = "غير معروف";

                                    if (isHistorical && activeTimeline) {
                                        let ts = parseInt(activeTimeline);
                                        let date = new Date(ts * 1000);
                                        let mm = String(date.getMonth() + 1).padStart(2, '0');
                                        let dd = String(date.getDate()).padStart(2, '0');
                                        let hh = String(date.getHours()).padStart(2, '0');
                                        let min = String(date.getMinutes()).padStart(2, '0');
                                        let ss = String(date.getSeconds()).padStart(2, '0');
                                        eventTimeStr = `${mm}/${dd} ${hh}:${min}:${ss} (سجل سابق)`;

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
                statusText.innerHTML = '<span style="color:#f85149;">❌ لم يتم العثور على شكل موجة بدء تشغيل صالح في الملف. يرجى التأكد من احتواء السجل على بيانات التشغيل.</span>';
                return;
            }

            statusText.innerHTML = `✅ اكتمل التحليل! تم اكتشاف <b style="color:#58a6ff;">${crankingEvents.length}</b> سجل بدء تشغيل.`;

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
                            ctx.fillText(`الحد الأدنى: ${minPoint.y.toFixed(2)}V`, ptMin.x + 10, ptMin.y);
                        }
                        
                        const ptStarter = meta.data[1];
                        if (ptStarter.x >= chart.chartArea.left && ptStarter.x <= chart.chartArea.right) {
                            ctx.textAlign = 'left';
                            ctx.fillText(` فصل بادئ الحركة: ${starterPoint.y.toFixed(2)}V`, ptStarter.x + 10, ptStarter.y);
                        }
                        ctx.restore();
                    }
                }
            };

            const wrapperDiv = document.createElement('div');
            wrapperDiv.style.cssText = "background: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e2e8f0; width: 100%; box-sizing: border-box; box-shadow: 0 1px 4px rgba(0,0,0,0.04);";
            
            const titleElement = document.createElement('div');
            titleElement.style.cssText = "color: #04384c; font-size: 16px; font-weight: bold; text-align: center; margin-bottom: 15px;";
            titleElement.innerHTML = `تحليل بدء التشغيل - سجل #${eventNumber} (الوقت: ${eventTime} | الحرارة: ${eventTemp}°C | الجهد المبدئي: ${vInitial.toFixed(2)}V)`;
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
                            label: 'الجهد (فولت)',
                            data: chartData,
                            borderColor: '#1176d4',
                            borderWidth: 2,
                            pointRadius: 0,
                            tension: 0.2,
                            order: 2
                        },
                        {
                            label: 'نقاط رئيسية',
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
                            title: { display: true, text: 'الوقت (ثواني)' },
                            max: times[times.length - 1],
                        },
                        y: {
                            title: { display: true, text: 'الجهد (V)' },
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
                                        return `الجهد: ${item.parsed.y}V`;
                                    }
                                    return '';
                                },
                                label: function(context) {
                                    if (context.dataIndex !== context.chart.tooltip.dataPoints[0].dataIndex || 
                                        context.datasetIndex !== context.chart.tooltip.dataPoints[0].datasetIndex) {
                                        return null;
                                    }
                                    return `الوقت: ${context.raw.x.toFixed(2)} ثانية`;
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
