---
layout: post
title:  "W205 尋油之路（4）-機油參數整理"
date:   2021-01-16 12:58:29
categories: Auto
tags: [機油, 汽車保養, API SQ, API SP, MB 229.5, HTHS, PAO, GTL, LSPI]
description: "買機油別被包裝騙了！本文整理最新 API SQ/SP 與車廠認證 (MB 229.5) 的差異，教你分辨 Approval 真假認證。深入解析 HTHS、TBN、Noack 數據意義，以及 PAO/GTL 基礎油與添加劑成分，避開來路不明的神油。"
keywords: "機油認證, API SQ, API SP, MB 229.5, HTHS, TBN, Noack, PAO, GTL, LSPI, 基礎油, 添加劑"
image: /images/mobile01-6c9f3d5e1626b191b75230bf6dd0eda6.webp
faq:
  - question: "API 認證中，哪些是針對 LSPI 問題的？"
    answer: "API SN Plus 和 API SP 都要求通過 LSPI 測試。最新的 API SQ (ILSAC GF-7) 更強化了 LSPI 防護、正時鏈條耐磨性、燃油經濟性，並限制硫酸鹽灰分以保護 GPF。"
  - question: "車廠認證與 API 認證有何差異？"
    answer: "車廠認證（如 MB 229.5）通常對 HTHS、TBN、Noack 等參數有更具體的標準，例如 MB 229.5 抗磨損標準高但沒有防 LSPI 測試。API SP/SQ 則抗磨損標準較低但有防 LSPI 測試。理想情況下，機油同時具備車廠與 API SP/SQ 認證，能提供最佳的抗磨損與 LSPI 防護。"
  - question: "如何分辨機油是否真的通過車廠認證？"
    answer: "有通過認證的標示通常為 'Approvals' 或 'Freigaben'。應避免使用標示為 'Performance Level'、'OEM Performances'、'Recommendations'、'OEM Compatibility' 或 'Suitable' 的機油，這些通常未實際通過認證。"
  - question: "在比較相同認證的機油時，哪些參數是重要的？"
    answer: "應比較 Flash Point (越高越好)、100°C黏度 (同認證同號數下越低越好)、40°C黏度 (越低越好)、Noack (越低越好，建議10以下)、HTHS (越高越耐高轉，2.9以上為佳)、TBN (機油耐用度，8以上為佳)、Pour Point (低於-50度可能PAO含量高)。"
  - question: "機油中的「鈣」成分有什麼影響？"
    answer: "鈣是清潔劑，但容易誘發 LSPI。因此，通過 API SP/SQ 認證的機油，其鈣含量通常會限制在 2000ppm 以下，並可能以鎂取代部分鈣來作為清潔劑。"
  - question: "什麼是 PAO 和 GTL 基礎油？"
    answer: "PAO（聚α烯烴）和 GTL（天然氣轉化液）都是頂級的合成基礎油。PAO 通常會加少量酯類以融入添加劑。GTL 則是天然氣經費托合成技術轉換而來，性能接近 PAO。"
  - question: "有哪些機油品牌是推薦的？"
    answer: "日常使用可選美孚 (Mobil)、殼牌 (Shell)、嘉實多 (Castrol) 等大型品牌，但建議購買代理商貨以防仿冒。追求性能可選力魔 (Liqui Moly)、摩特 (Motul)、安索 (AMSOIL)、紅線 (Redline)、和光 (Wako)、日耳曼 (Ravenol)。台灣製則有台塑、國宏、各車廠原廠油。"
  - question: "選購機油時應該避開哪些品牌？"
    answer: "應避開本土混油、找國外小廠代工的品牌，以及沒看過的品牌。若遇到不熟悉的品牌，可在 Mercedes-Benz Bevo 網站搜尋，若其認證數量少於 10 個則不建議購買。"
---


## 主要認證

### API 認證
- **SN Plus/SP**：要求通過 LSPI 測試
- **SQ (ILSAC GF-7)**：2025年新標準，強化 LSPI 防護、正時鏈條耐磨性、燃油經濟性，並限制硫酸鹽灰分 ≤0.9%，保護 GPF

### 車廠認證

| 認證 | HTHS | TBN | Noack |
|------|------|------|------|
| **API SP/SQ** | >2.6 | 無 | 無 |
| **AECA A3/B4** | >3.5 | >10 | <13 |
| **AECA A5/B5** | 2.9-3.5 | >8 | <13 |
| **AECA C3** | >3.5 | >6 | <13 |
| **MB 229.5** | >3.5 | >10 | <10 |
| **MB 229.51/52** | >3.5 | >6 | <10 |
| **VW 502/505** | >3.7 | >7 | - |
| **VW 504/507** | >3.5 | >6 | <11 |
| **BMW LL-98** | >3.5 | >9.5 | - |
| **BMW LL-01** | >3.5 | >10 | - |
| **BMW LL-01 FW** | >3.0 | >9.5 | - |

## 認證可疊加

- **229.5**：抗磨損標準高，但沒有防LSPI的測試
- **API SP/SQ**：抗磨損標準低，但有防LSPI的測試
- **同時具有 229.5 及 API SP/SQ 認證** → 抗磨損佳，且有防LSPI
- **認證疊加可參考**：[Lubrizol 八邊形](https://online.lubrizol.com/relperftool/pc.html)

## 認證標示的文字遊戲

**有通過認證的標示：**
- Approvals
- Freigaben

**沒通過認證的標示（盡量別用）：**
- Performance Level
- OEM Performances
- Recommendations
- OEM Compatibility
- Suitable

## 【相同認證】機油比較指標

- **Flash Point**：機油閃燃點，越高越好
- **100°C黏度**：同認證同黏度號數，低的為佳
- **40°C黏度**：越低越好
- **Noack**：機油揮發率，低的為佳，建議挑10以下
- **HTHS**：越高越耐高轉，越低越省油，依照駕駛模式挑選，2.9以上為佳
- **TBN**：機油耐用度，8以上為佳
- **MRV**：越低越好（台灣可忽略）
- **CCS**：越低越好（台灣可忽略）
- **Pour Point**：最低流動溫度，粗判基礎油種類，低於-50度多為PAO含量高
- **VI**：黏度變化指數，無參考價值

## 基礎油種類

- **多元酯**：頂級，耐高轉，潤滑性好，衰退極快，紅外線峰值 1710>2
- **烷基萘ANs**：頂級，少見，取代酯類加入PAO做調製劑，紅外線峰值 740-890
- **PAO**：頂級，通常會加少量酯類以融入添加劑，紅外線峰值 720>1
- **GTL**：頂級，天然氣經F-T化學合成，性能接近PAO，紅外線峰值 720<=1
- **XTL**：煤、有機物轉換為天然氣，再走F-T合成潤滑油
- **VHVI**：氫裂解礦物油，純化後的礦物油

## 添加劑成份

- **鈣 (Ca)**：清潔劑，易誘發LSPI，通過SP/SQ認證通常小於 2000ppm
- **鎂 (Mg)**：清潔劑，取代易誘發LSPI的鈣
- **鉬 (Mo)**：抗研磨劑
- **磷 (P)**：抗研磨劑
- **鋅 (Zn)**：抗研磨劑，化合物稱ZDDP，潤滑性良好
- **硼 (B)**：抗研磨劑
- **鎢 (W)**：抗研磨劑
- **鈦 (Ti)**：抗研磨劑

## 建議品牌

### 日常用 **(世界各地仿冒品極多，建議買代理商貨)**
- **美孚 Mobil**
- **殼牌 Shell**
- **嘉實多 Castrol**

### 拉轉適用
- **力魔 Liqui Moly**
- **摩特 Motul**
- **安索 AMSOIL**
- **紅線 Redline**
- **和光 Wako**
- **日耳曼 Ravenol**

### 台灣製
- **台塑**
- **國宏 (出光)**
- **各車廠原廠油**

### **避開**
- 本土混油、找國外小廠代工品牌
- 沒看過的品牌，到 [Bevo](https://bevo.mercedes-benz.com/bevolisten/bevo-sheets-sort1.html) 輸入品牌英文搜尋，Count欄位加起來超過10以上再買。

## **推薦閱讀**
- [法拉利論壇：技術 QA 精華](https://www.ferrarichat.com/forum/threads/motor-oil-all-chapters-inclusive-copy-and-save-this.136052/)

![機油相關圖示](/images/mobile01-6c9f3d5e1626b191b75230bf6dd0eda6.webp)
