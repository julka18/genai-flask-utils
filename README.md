
# 📢 Poster Generation API — Developer Guide

This project provides a **Flask API** for generating marketing posters using **Google GenAI (Gemini)**.
It takes product details + an image path and returns a **poster (base64 encoded)**.

---

## 🛠 Setup Instructions (Developer Machine)

### 1. Unzip the project

Unzip the `poster_api.zip` you received into a folder, e.g.:

```
poster_api/
 ├── app.py
 ├── poster_generator.py
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

This will install:

* `flask`
* `pillow`
* `google-genai`

---

### 4. Set API Key

In **poster\_generator.py**, replace:

```python
client = genai.Client(api_key="YOUR_API_KEY")
```

with your **Google API Key**.
⚠️ Keep this private — never commit/share your real key.

---

### 5. Run the API

```bash
python app.py
```

The API will start at:

```
http://127.0.0.1:8080
```

---

## 📡 Usage

### Endpoint

```
POST /generate-poster
```

### Request Body (JSON)

```json
{
  "product_name": "Luxury Watch",
  "price": "$499",
  "description": "Premium wristwatch with marble finish",
  "location": "New York",
  "industry": "Luxury",
  "product_image_path": "watch.png"
}
```

👉 `product_image_path` should be the path to an existing image file on your machine (e.g. `watch.png` in the same folder).

---

### Example with curl

```bash
curl -X POST http://127.0.0.1:8080/generate-poster \
     -H "Content-Type: application/json" \
     -d '{
           "product_name": "Luxury Watch",
           "price": "$499",
           "description": "Premium wristwatch with marble finish",
           "location": "New York",
           "industry": "Luxury",
           "product_image_path": "watch.png"
         }'
```

---

### Example with Python

```python
import requests, base64

resp = requests.post("http://127.0.0.1:8080/generate-poster", json={
    "product_name": "Luxury Watch",
    "price": "$499",
    "description": "Premium wristwatch with marble finish",
    "location": "New York",
    "industry": "Luxury",
    "product_image_path": "watch.png"
})

print(resp.json()["message"])
poster_base64 = resp.json().get("poster_base64")

if poster_base64:
    with open("poster.png", "wb") as f:
        f.write(base64.b64decode(poster_base64))
    print("Poster saved as poster.png")
```

---

## 🧪 Notes

* If you open `http://127.0.0.1:8080` in a browser, you’ll see **404** — this is expected. Use a **POST request** only.
* Make sure the image path you pass (`product_image_path`) points to a valid file on your PC.
* This setup uses Flask’s development server — fine for local testing. For production, we’d use Docker + Gunicorn/Cloud Run.

---

✅ That’s it! You can now generate posters by sending product details + an image to the API.

