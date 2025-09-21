
# 📢 Poster & Caption Generation API — Developer Guide

This project provides a **Flask API** powered by **Google GenAI (Gemini)** to help with product marketing.
It includes:

* 🖼️ Poster generation (`/generate-poster`)
* ✍️ Storytelling caption generation (`/generate-caption`)

---

## 🛠 Setup Instructions (Developer Machine)

### 1. Unzip the project

Unzip the `poster_api.zip` you received into a folder, e.g.:

```
poster_api/
 ├── app.py
 ├── poster_generator.py     # Poster + Caption functions
 ├── requirements.txt
 └── README.md
```

---

### 2. Create a Virtual Environment

This project should run in its **own environment** to avoid dependency conflicts.

```bash
cd poster_api

python3 -m venv venv
```

Activate it:

* macOS/Linux:

  ```bash
  source venv/bin/activate
  ```
* Windows:

  ```bash
  venv\Scripts\activate
  ```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:

* `flask`
* `pillow`
* `google-genai`

---

### 4. Add Google API Key

In **poster\_generator.py**, set your **API key**:

```python
client = genai.Client(api_key="YOUR_API_KEY")
```

⚠️ Do **not** commit or share your real API key.

---

### 5. Run the API

```bash
python app.py
```

Server will start at:

```
http://127.0.0.1:8080
```

---

## 📡 API Endpoints

### 1️⃣ Generate Poster

```
POST /generate-poster
```

**Request Body (JSON):**

```json
{
  "product_name": "Luxury Watch",
  "price": "$499",
  "description": "Premium wristwatch with marble finish",
  "location": "New York",
  "industry": "Luxury",
  "product_image_base64": {YOUR BASE 64 STRING}
}
```

👉 `product_image_path` should be the **path to a valid image file** on your machine.

**Response (JSON):**

```json
{
  "success": true,
  "message": "Poster generated successfully",
  "poster_base64": "<base64 encoded PNG>"
}
```

You can decode `poster_base64` to save the poster image.

---

### 2️⃣ Generate Caption

```
POST /generate-caption
```

**Request Body (JSON):**

```json
{
  "product_name": "Luxury Watch",
  "price": "$499",
  "description": "Premium wristwatch with marble finish",
  "location": "New York",
  "industry": "Luxury"
}
```

**Response (JSON):**

```json
{
  "success": true,
  "message": "Caption generated successfully",
  "caption": "Timeless elegance on your wrist. This luxury watch, priced at $499, blends..."
}
```

---

## 📌 Example Usage

### Test Poster Generation (curl)

```bash
curl -X POST http://127.0.0.1:8080/generate-poster \
     -H "Content-Type: application/json" \
     -d '{
           "product_name": "Luxury Watch",
           "price": "$499",
           "description": "Premium wristwatch with marble finish",
           "location": "New York",
           "industry": "Luxury",
           "product_image_base64": base64
         }'
```

### Test Caption Generation (curl)

```bash
curl -X POST http://127.0.0.1:8080/generate-caption \
     -H "Content-Type: application/json" \
     -d '{
           "product_name": "Luxury Watch",
           "price": "$499",
           "description": "Premium wristwatch with marble finish",
           "location": "New York",
           "industry": "Luxury"
         }'
```

---

### Test with Python Client

```python
import requests, base64

# Generate Caption
resp = requests.post("http://127.0.0.1:8080/generate-caption", json={
    "product_name": "Luxury Watch",
    "price": "$499",
    "description": "Premium wristwatch with marble finish",
    "location": "New York",
    "industry": "Luxury"
})
print(resp.json())

# Generate Poster
resp = requests.post("http://127.0.0.1:8080/generate-poster", json={
    "product_name": "Luxury Watch",
    "price": "$499",
    "description": "Premium wristwatch with marble finish",
    "location": "New York",
    "industry": "Luxury",
    "product_image_base64": "YOUR-BASE64-STRING"
})
data = resp.json()

if data.get("poster_base64"):
    with open("poster.png", "wb") as f:
        f.write(base64.b64decode(data["poster_base64"]))
    print("Poster saved as poster.png")
```

---

## 🧪 Notes

* Opening `http://127.0.0.1:8080` in a browser will return **404**. Only **POST requests** are supported.
* `405` means you tried `GET` instead of `POST`.
* Ensure the `product_image_path` points to a valid image file.
* For production, use Docker + Gunicorn/Uvicorn (this is Flask dev server).


