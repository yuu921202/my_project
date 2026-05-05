
# 🏭 Smart Factory MES with AI Copilot

這是一個結合 **工業 4.0 概念** 與 **生成式 AI (LLM)** 的智慧工廠執行系統 (MES) 模擬專案。透過整合 **Google Gemini 3 Flash**，系統不只提供視覺化的機台監控，更實現了透過自然語言直接操控產線的 **AI Agent** 功能。

---

## 🌟 核心特色

### 🤖 AI 廠長 (AI Factory Manager)
*   **自然語言理解 (NLU)**：無需記憶複雜指令，直接輸入「幫我插一個急單」即可操作。
*   **上下文感知 (Context Awareness)**：AI 能夠即時讀取工廠的 JSON 狀態（機台是否故障、隊列長短），並給出專業建議。
*   **函式呼叫 (Function Calling)**：AI 不只是聊天，它能直接調用系統內部的 `create_job` 函式，精準提取參數（如：產品名稱、優先級、工時）。

### ⚙️ 數位雙生模擬 (Digital Twin Simulation)
*   **即時監控儀表板**：動態呈現機台的加工進度（Progress Bar）與狀態。
*   **隨機故障邏輯**：模擬真實產線可能遇到的機台失效與維修流程。
*   **多樣化下單**：支援手動輸入、CSV 批次匯入以及 AI 自動化排單。

---

## 🛠️ 技術棧
*   **Frontend**: HTML5, CSS3 (Modern UI/UX), Vanilla JavaScript.
*   **AI Engine**: [Google Gemini 3 Flash Preview](https://aistudio.google.com/).
*   **Communication**: REST API (Fetch API) with Async/Await.

---

## 🚀 快速開始

1.  **取得 API KEY**：
    前往 [Google AI Studio](https://aistudio.google.com/) 申請免費的 Gemini API Key。
2.  **設定環境變數**：
    在 `index.html` 的 `<script>` 區塊中，找到 `GEMINI_API_KEY` 並填入你的 Key。
    ```javascript
    const GEMINI_API_KEY = "YOUR_API_KEY_HERE";
    ```
3.  **啟動系統**：
    直接使用瀏覽器開啟 `index.html` 即可看到智慧工廠開始運作。

---

## 📖 AI 操作範例

你可以試著在 AI 指令介面輸入以下內容：
*   **狀態詢問**：「目前廠區運作正常嗎？有沒有機台在維修？」
*   **自動化下單**：「廠長，幫我加一個台積電的緊急訂單，優先級設為最高，加工時間 20 秒。」
*   **複雜決策**：「現在有兩台機器故障了，我該優先處理哪個訂單？」

---

## ⚠️ 安全性規範
*   本專案僅供開發與展示使用。
*   **嚴禁**將包含真實 `API_KEY` 的代碼推送到 GitHub 等公開倉庫。
*   建議使用 `.env` 或其他加密方式管理敏感資訊。

---

## 📈 未來擴充計劃
*   [ ] **自主維修代理**：當 AI 發現機台故障且訂單堆積時，自動調用維修函數。
*   [ ] **多模態監控**：上傳機台照片，讓 AI 判斷物理損壞情況。
*   [ ] **數據可視化**：整合 Chart.js 呈現全廠稼動率 (OEE) 統計圖表。

---