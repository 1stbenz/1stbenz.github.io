---
layout: post
title:  "超級電容內阻計算器"
date:   2026-01-11 10:00:10
categories: Auto
tags: [超級電容, 汽車改裝, 電池內阻, DIY工具, 電路計算]
description: "店家宣稱加裝超級電容後內阻大幅下降？本頁面提供線上並聯電阻計算器，只要輸入電池原內阻與並聯後總阻抗，即可反推超級電容的真實內阻值，協助車友判斷改裝效益是否為智商稅。"
keywords: "超級電容, 內阻計算, 並聯電阻, 汽車電系, 逆電流, 穩壓器, R總阻抗"
image: /images/ir_caculator.webp
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
