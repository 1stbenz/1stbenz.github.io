---
layout: post
title:  "車用鈦酸鋰 (LTO) 致命缺點解析：為何 5 串過充、6 串充不飽？"
lang: zh-Hant
date:   2025-06-12 10:00:29
categories: Auto
tags: [汽車電池, 電瓶監控, 汽車改裝, 汽車知識, DIY教學, LTO]
description: "想改裝鈦酸鋰 (LTO) 啟動電瓶？本文深度解析電壓匹配硬傷（5 串過充、6 串充不飽）、1kHz 交流內阻的測量盲點、退役 B/C 級散料木桶效應，以及小容量大幅加速 EFC 等效全循環的壽命陷阱。"
keywords: "鈦酸鋰, LTO, SCiB, 5串, 6串, 電壓不合, 過充, 汽車改裝, 鋰電池, 東芝, 內阻測試, 極化壓降, 等效全循環, EFC, 電芯分容"
image: /images/mobile01-73a3f73994754009670d4e7b1e13c046.webp
faq:
  - question: "車用發電機的充電電壓範圍是多少？"
    answer: "多數汽機車的發電機在運作時會輸出約 13.5V～14.4V（歐系或動能回充可能達 14.8V~15.0V），這是為鉛酸/AGM 電池設計的充電策略。"
  - question: "為什麼 5 串鈦酸鋰 (LTO) 電池不適合車用發電機充電？"
    answer: "5 串 LTO 電池的滿電電壓約為 13.5V (每顆 2.7V)。發電機輸出 13.5V～14.4V+ 時，單芯電壓常被推升至 2.7V～2.9V+，在行駛中全程處於過電壓浮充狀態，加速電解液分解與劣化。"
  - question: "為什麼 6 串鈦酸鋰 (LTO) 電池不適合車用發電機充電？"
    answer: "6 串 LTO 電池滿電需 16.2V (每顆 2.7V)。發電機最多輸出 14.4V (每顆 2.4V)，僅達標稱電壓，導致電池永遠充不飽，可用容量僅剩約 30%~40%。"
  - question: "為什麼手持 1kHz 內阻儀測不出二手 LTO 的老化？"
    answer: "LTO 屬零應變材料，老化時『只掉容量、不漲歐姆內阻』。1kHz 交流內阻儀只能測金屬接點與電解液的純歐姆阻抗，完全測不出衰退的化學容量、自放電微短路，以及大電流抽載時的動態極化壓降。"
  - question: "為什麼二手 LTO 宣稱萬次循環，用在汽車上壽命卻消耗極快？"
    answer: "主要是小容量放大等效全循環（EFC）。原廠鉛酸約 70Ah，改裝 LTO 模組常僅 10~20Ah。同樣消耗 10Ah 暗電流與啟動耗電，對鉛酸僅 15% 淺放電，對 10Ah LTO 卻是 100% 深放電的一整次循環，循環消耗速度被直接放大 4~6 倍，加上二手電芯殘值差，加速短板崩潰。"
---

## 問題核心：車用發電機的充電電壓

多數汽油與柴油車的發電機在引擎運轉時會輸出 **13.5V～14.4V** 左右的電壓（部分歐系車或動能回充模式可達 **14.8V～15.0V**），這是專門為鉛酸/AGM 電池所設計的充電策略。

---

## 鈦酸鋰串數與電壓對應

<style>
    /* RWD 響應式滾動容器 */
    .table-responsive {
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch; /* 讓 iOS 裝置滑動更順暢 */
        margin-bottom: 20px;
    }
    
    .battery-table {
        display: table;
        border-collapse: collapse;
        width: 100%;
        min-width: 500px; /* 確保在手機上縮小時，文字不會全部擠在一起 */
        max-width: 680px;
        font-family: sans-serif;
        font-size: 16px;
    }
    
    .battery-table th, .battery-table td {
        border: 1px solid #b3c6e7; /* 配合標題顏色的柔和邊框 */
        padding: 10px 15px;
        text-align: left;
        vertical-align: top;
        line-height: 1.5;
        color: #333333; /* 強制將表格內的文字設定為深灰色 */
    }

    .battery-table td strong {
        color: #333333;
    }
    
    /* 標題上色 (參考原圖的藍色系) */
    .battery-table th {
        font-weight: bold;
        text-align: center;
        background-color: #6495ED; /* 標題底色：矢車菊藍 */
        color: #ffffff; /* 標題文字：白色，增加對比度 */
    }
    
    /* 單雙背景色有區別 (斑馬紋) */
    .battery-table tbody tr:nth-child(even) {
        background-color: #f2f7ff; /* 雙數行：極淺的藍色 */
    }
    .battery-table tbody tr:nth-child(odd) {
        background-color: #ffffff; /* 單數行：白色 */
    }
    
    /* 滑鼠懸停效果 (稍微提亮，增加互動感) */
    .battery-table tbody tr:hover {
        background-color: #e6f0ff;
    }
</style>

<div class="table-responsive">
    <table class="battery-table">
        <thead>
            <tr>
                <th>串數</th>
                <th>標稱電壓</th>
                <th>建議充滿電壓</th>
                <th>車載運作狀況</th>
                <th>結果</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><b>5 串</b></td>
                <td>11.5V～12.0V</td>
                <td>約 13.5V（2.7V/顆）</td>
                <td>發電機 13.5V～14.8V</td>
                <td><span style="color: red; font-weight: bold;">常態過充浮充</span>（電壓過高加速產氣劣化）</td>
            </tr>
            <tr>
                <td><b>6 串</b></td>
                <td>13.8V～14.4V</td>
                <td>約 16.2V（2.7V/顆）</td>
                <td>發電機僅 14.4V 封頂</td>
                <td><span style="color: red; font-weight: bold;">永遠充不飽</span>（可用容量僅剩 30%～40%）</td>
            </tr>
        </tbody>
    </table>
</div>

規格參考：[東芝 SCiB 原廠模組規格表](/images/lto_module.webp)

---

## 致命傷之一：電壓不匹配的硬傷（5 串過充、6 串充不飽）

在車載發電機的輸出特性下，LTO 電芯面臨著物理上的電壓兩難：

### 1. 為什麼 5 串會過充？
* 發電機輸出 13.5V～14.4V+，除以 5 顆 = 每顆 **2.7V～2.88V+**。
* 超過 13.5V 即達充滿上限，行駛時長時間處於「過電壓浮充」。
* 長期過壓充電會加速電解液分解、高溫產氣膨脹與容量劇烈衰減（**但致命的是：此時交流內阻幾乎不變**）。

### 2. 為什麼 6 串充不飽？
* 發電機最高輸出 14.4V，除以 6 顆 = 每顆平均僅 **2.4V**。
* 2.4V 僅是 LTO 的標稱平台電壓，外部電壓缺乏足夠推力逆轉化學反應。
* 電池長期處於半飢餓狀態，[**實際可用容量僅剩 30%～40%**](/images/mobile01-f1b4345d1112dee159b1baa62a8da6ef.webp)。

---

## 致命傷之二：超高 CCA 與內阻的數據假象

許多改裝玩家常被兩組漂亮數據迷惑：**超高的 CCA 儀器讀數** 與 **0.2 mΩ 的超低 1kHz 交流內阻**。

### 1. 漂亮的 CCA 與內阻數據，其實是「假的」
* **手持內阻儀（1kHz 小訊號）**：僅測量集電體金屬、極耳與外殼的**純歐姆電阻**。即便電芯內部活性物質萎縮，只要電路通暢，交流內阻依然漂亮。
* **動態極化阻抗（300A~500A 實抽）**：大電流抽載考驗鋰離子在電極的擴散速率（濃差極化）。二手電芯反應面積衰退，大電流下會產生巨大動態壓降，造成電壓斷崖式下跌。
* **可用壓降極窄**：LTO 標稱 2.3V、截止電壓 1.5V，可用壓降僅 0.8V（遠小於鋰鐵的 1.2V），些微極化壓降即會瞬間觸底判斷沒電。

### 2. 淘汰品的真面目：容量已衰減、內阻卻看似健康的「偽裝者」
* LTO 充放電晶格形變極小（零應變），老化特性是 **「只掉容量、不漲內阻」**。
* 工業大廠淘汰拆機的標準是「實際 Ah 容量衰退」與「自放電微短路」，這兩項用市售手持內阻儀 100% 測不出來。

---

## 致命傷之三：市售二手電芯的真面目（大廠挑剩的淘汰散料）

### 1. 供應鏈分級真相：好貨早已被大廠挑走
大廠淘汰電芯時早已透過自動化分容櫃完成篩選，散裝市集絕非「撿到寶」的天堂：

<div class="table-responsive">
    <table class="battery-table">
        <thead>
            <tr>
                <th>電芯分級</th>
                <th>檢測特徵</th>
                <th>主要流向</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><span style="color: #16a34a; font-weight: bold;">A 級（良品）</span></td>
                <td>容量 ≥ 80%~90%<br>動態 DCIR 低、一致性高</td>
                <td>定置儲能櫃、車廠整新電池包</td>
            </tr>
            <tr>
                <td><span style="color: #d97706; font-weight: bold;">B/C 級（散料）</span></td>
                <td>容量跌至 60%~75%<br>脈衝壓降大、一致性差</td>
                <td>網拍散裝、改裝工作室</td>
            </tr>
            <tr>
                <td><span style="color: red; font-weight: bold;">報廢級</span></td>
                <td>嚴重微短路、極柱損毀<br>自放電過大、電解液洩漏</td>
                <td>打碎回爐提煉金屬</td>
            </tr>
        </tbody>
    </table>
</div>

### 2. 小型工作室的分容困境：設備昂貴且耗時
* **無法進行真正的充放電分容**：依標準 0.5C 測試，單顆 20Ah 做一次完整滿充滿放至少需耗費 **4～5 小時**；要篩選配對出一組性能曲線一致的 5 串電芯，時間與多通道動力分容櫃成本極其高昂。
* **「快速分選」只適用全新電芯，用在二手散料是災難**：
  * **全新電芯**：大廠出廠時早已完成完整分容與化成，每顆健康度（SOH）皆為 100%。組裝廠只需花 2 秒量測開路電壓與交流內阻做「快速分選」，即可挑出同頻電芯配組。
  * **二手散料**：混批拆機電芯容量衰退不一（SOH 60%～85% 都有）。若套用全新電芯的「快速分選」模式，只花 2 秒量測電壓與內阻，根本測不出真實剩餘 Ah 容量與自放電微短路，等同於閉著眼睛「開盲盒」組裝。

---

## 致命傷之四：隱藏陷阱（容量小導致循環耗損加倍、停放猝死）

1. **暗電流停放猝死**：  
   同體積下 LTO 能量密度低，二手衰退後組裝容量常僅剩 **15Ah～25Ah**。面對現代車輛 30mA~50mA 暗電流與停車監控，往往**停放 3~5 天電量就被吸乾**。
2. **大幅加速等效全循環**：  
   * 原廠鉛酸容量為 60~70Ah，消耗 10Ah 暗電流與啟動電量僅是 **15% 的淺放電**。
   * 10~20Ah 的小容量 LTO 面臨相同 10Ah 消耗，卻等同於 **100% 的一次全循環（EFC）**。
   * 日常循環消耗速率被直接放大 4~6 倍；在木桶效應下，最弱單芯每天承受最深放電應力，遠未達理論萬次壽命即提早崩潰。

---

## 比較目前市場常見電池

<div class="table-responsive">
    <table class="battery-table">
        <thead>
            <tr>
                <th>尺寸LN3</th>
                <th>鉛酸</th>
                <th>鈦酸鋰</th>
                <th>鋰鐵</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>容量</td>
                <td>70Ah</td>
                <td><span style="color: red;">46Ah</span></td>
                <td><b>100Ah</b></td>
            </tr>
            <tr>
                <td>充電效能</td>
                <td>7A(0.1C)</td>
                <td><b>920A(20C)</b></td>
                <td>200A(2C)</td>
            </tr>
            <tr>
                <td>放電效能</td>
                <td>10C</td>
                <td>20C</td>
                <td><b>50-80C</b></td>
            </tr>
            <tr>
                <td>耐壓</td>
                <td>16.2V</td>
                <td><span style="color: red;">13.5V(5串)</span></td>
                <td>14.6V</td>
            </tr>
            <tr>
                <td>循環壽命</td>
                <td>1000次</td>
                <td>
                    理想20000次<br>
                    x容量0.46<br>
                    <span style="color: red;">x二手耗損0.7</span><br>
                    <span style="color: red;">x長期過充0.7</span><br>
                    =<b>4500次</b>
                </td>
                <td>5000次</td>
            </tr>
            <tr>
                <td>電芯品質</td>
                <td>全新</td>
                <td><span style="color: red;">多二手拆機</span></td>
                <td>全新</td>
            </tr>
            <tr>
                <td>生產商</td>
                <td>正規工廠</td>
                <td><span style="color: red;">多地下工廠</span></td>
                <td>正規工廠</td>
            </tr>
            <tr>
                <td>價格</td>
                <td>低</td>
                <td><span style="color: red;">高</span></td>
                <td>中</td>
            </tr>
            <tr>
                <td colspan="4">
                    歐系車發電機：<b>190A</b><br>
                    日系車發電機：<b>120A</b>
                </td>
            </tr>
        </tbody>
    </table>
</div>

---

> **建議**：若你正在選擇鈦酸鋰電池作為車用啟動用途，請務必確認串數與充電電壓是否匹配，並了解市售二手電芯「只掉容量、不漲內阻」的假健康特性。認清 5 串電壓常態過充、小容量大幅加速循環耗損，以及二手散料未經分容配對的硬傷。要求廠商提供電芯真實的放電容量測試報告，比內阻儀上的漂亮數字更有意義。
