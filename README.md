# FastAPI 使用指南

## 介紹

FastAPI 是一個高性能的現代化 Web 框架，基於 Python 3.7+ 開發。它結合了快速（fast）的性能和直觀（API）的設計，使得構建 Web 應用程式和 API 變得簡單而高效。

本指南將詳細介紹如何使用 FastAPI 構建 Web 應用程式和創建 API。

## 快速開始

### 步驟 1: 創建專案目錄

首先，創建一個新的目錄作為你的 FastAPI 專案。

```bash
mkdir my_fastapi_project
cd my_fastapi_project
```

### 步驟 2: 建立虛擬環境

建立並啟用 Python 虛擬環境。

```bash
python3 -m venv venv
source venv/bin/activate  # Windows 上使用 venv\Scripts\activate.bat
```

### 步驟 3: 安裝 FastAPI 和相關套件

在虛擬環境中，使用 pip 安裝 FastAPI 和相關套件。

```bash
pip install fastapi uvicorn
```

### 步驟 4: 建立主程式檔案

創建一個 Python 檔案，例如 `main.py`，並編輯以下程式碼：

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

### 步驟 5: 啟動 FastAPI 伺服器

使用 uvicorn 啟動 FastAPI 伺服器。

```bash
uvicorn main:app --reload
```

現在，你可以在瀏覽器中打開 http://localhost:8000 來測試 API，或使用其他工具（如 curl 或 Postman）來發送請求。

## 進階使用

上述步驟僅為入門，FastAPI 還提供了許多進階功能，例如：

- 請求驗證和授權
- 處理 POST、PUT 和 DELETE 請求
- 使用路徑參數和查詢參數
- 使用 Pydantic 模型驗證請求和回應數據
- 處理異常和錯誤
- 使用資料庫和 ORM（例如 SQLAlchemy）
- 檔案上傳和處理
- 測試和文檔生成
