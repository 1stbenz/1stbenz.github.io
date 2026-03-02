---
layout: post
title:  "超級電容內阻計算器"
date:   2026-01-11 10:00:10
categories: Auto
tags: [超級電容, 汽車改裝, 電池內阻, DIY工具, 電路計算]
description: "店家宣稱加裝超級電容後內阻大幅下降？本頁面提供線上並聯電阻計算器，只要輸入電池原內阻與並聯後總阻抗，即可反推超級電容的真實內阻值，協助車友判斷改裝效益是否為智商稅。"
keywords: "超級電容, 內阻計算, 並聯電阻, 汽車電系, 逆電流, 穩壓器, R總阻抗"
image: /images/ir_caculator.webp
faq:
  - question: "這個頁面提供了什麼工具？它的主要目的是什麼？"
    answer: "這個頁面提供了一個線上並聯電阻計算器，主要目的是協助車友透過輸入電池原始內阻和並聯後的總阻抗，反推算出所加裝超級電容的真實內阻值。"
  - question: "為什麼會需要這個超級電容內阻計算器？"
    answer: "許多店家在推銷超級電容時會展示加裝前後的內阻數據。這個計算器能讓車友根據這些數據，反向驗證超級電容的實際內阻性能，判斷改裝效益是否如宣稱般顯著，避免花費在低效益的產品上。"
  - question: "使用這個計算器需要輸入哪些數據？"
    answer: "您需要輸入兩個數據：原始電池的內阻 (R<sub>電池</sub>) 和加裝超級電容後的並聯總阻抗 (R<sub>總阻抗</sub>)。"
  - question: "這個計算器是基於什麼電學原理來運作的？"
    answer: "計算器是基於並聯電阻的總阻抗公式：R<sub>總阻抗</sub> = (R<sub>電池內阻</sub> × R<sub>電容內阻</sub>) / (R<sub>電池內阻</sub> + R<sub>電容內阻</sub>) 來反推超級電容的內阻值。"
  - question: "在輸入數值時，有什麼單位上的注意事項嗎？"
    answer: "是的，請務必保持輸入的數值單位一致，例如都使用 Ω (歐姆) 或都使用 mΩ (毫歐姆)。"
  - question: "如果輸入的「並聯後總阻抗」大於或等於「電池內阻」，會發生什麼情況？"
    answer: "如果輸入的「並聯後總阻抗」大於或等於「電池內阻」，計算器會顯示錯誤訊息，因為在並聯電路中，總阻抗的數值必然會小於任何一個單獨的並聯元件的阻抗。"
  - question: "計算出超級電容的內阻後，對車主有什麼實際意義？"
    answer: "透過反推計算出的超級電容真實內阻值，車主可以更客觀地評估該超級電容的性能，與其市場價格和鋰鐵電池的整體效益進行比較，從而判斷改裝是否真的划算，避免成為「智商稅」的受害者。"
---

[![電阻並聯公式](/images/ir_caculator.webp)](/images/ir_caculator.webp)

在上篇指出[超級電容已成為智商稅](/2025/dont-use-supercap.html)之後，有車友私訊我詢問：有沒有快速計算超級電容內阻的方式。

觀察大部分超級電容裝機文，店家會拍攝兩個數據：**「原始電池內阻」** 以及加裝超級電容後的 **「並聯總內阻」**。

透過這兩個已知數據，就能利用並聯電路公式，反推算出那顆超級電容**實際的內阻值**。

<div id="supercap-calculator" style="max-width: 500px; margin: 20px auto; background: #fff; padding: 25px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); font-family: sans-serif; border: 1px solid #eee; color: #333;">

  <style>
    /* 避免污染外部樣式，限定範圍 */
    #supercap-calculator * { box-sizing: border-box; }
    #supercap-calculator h3 { text-align: center; margin-top: 0; color: #333; margin-bottom: 15px; }
    #supercap-calculator .formula-display { background-color: #f1f4f6; padding: 10px; border-radius: 6px; text-align: center; margin-bottom: 20px; color: #555; font-size: 0.95em; line-height: 1.5; }
    #supercap-calculator .input-row { margin-bottom: 15px; }
    #supercap-calculator label { display: block; margin-bottom: 5px; font-weight: bold; color: #444; font-size: 0.9em; }
    #supercap-calculator input[type="number"], #supercap-calculator input[type="text"] { width: 100%; padding: 8px 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 16px; background: #fff; color: #333; }
    #supercap-calculator input:focus { border-color: #2196F3; outline: none; }
    #supercap-calculator .result-box input { background-color: #e8f5e9; border-color: #81c784; color: #2e7d32; font-weight: bold; }
    #supercap-calculator .err-msg { color: #d32f2f; font-size: 0.85em; margin-top: 4px; display: none; }
    #supercap-calculator .unit-hint { font-size: 0.8em; color: #888; margin-top: 2px; }
  </style>

  <h3>並聯內阻計算器</h3>

  <div class="formula-display">
    R<sub>總阻抗</sub> = 
    <span style="display: inline-block; vertical-align: middle; text-align: center;">
      <span style="display: block; border-bottom: 1px solid currentColor; padding: 0 2px;">R<sub>電池</sub> × R<sub>電容</sub></span>
      <span style="display: block; padding: 0 2px;">R<sub>電池</sub> + R<sub>電容</sub></span>
    </span>
  </div>

  <div class="input-row">
    <label>輸入：電池內阻 (R<sub>電池</sub>)</label>
    <input type="number" id="sc_r_battery" placeholder="輸入數值" step="any" oninput="runSuperCapCalc()">
    <div class="unit-hint">※ 請保持單位一致 (例如皆為 Ω 或 mΩ)</div>
  </div>

  <div class="input-row">
    <label>輸入：並聯後總阻抗 (R<sub>總</sub>)</label>
    <input type="number" id="sc_r_total" placeholder="必須小於電池內阻" step="any" oninput="runSuperCapCalc()">
    <div id="sc_error" class="err-msg">⚠️ 錯誤：總阻抗必須小於電池內阻</div>
  </div>

  <div class="input-row result-box">
    <label>計算結果：超級電容內阻 (R<sub>電容</sub>)</label>
    <input type="text" id="sc_r_cap" readonly placeholder="等待輸入...">
  </div>

  <script>
    function runSuperCapCalc() {
      var elBat = document.getElementById('sc_r_battery');
      var elTot = document.getElementById('sc_r_total');
      var elRes = document.getElementById('sc_r_cap');
      var elErr = document.getElementById('sc_error');

      var rBat = parseFloat(elBat.value);
      var rTot = parseFloat(elTot.value);

      elErr.style.display = 'none';

      if (isNaN(rBat) || isNaN(rTot)) {
        elRes.value = "";
        return;
      }

      if (rTot >= rBat) {
        elErr.style.display = 'block';
        elRes.value = "無效數值";
        return;
      }

      var rCap = (rTot * rBat) / (rBat - rTot);
      rCap = Number.isInteger(rCap) ? rCap : rCap.toFixed(2);
      elRes.value = rCap; 
    }
  </script>
</div>
