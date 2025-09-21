from flask import Flask, request, jsonify
import base64
from poster_generator import generate_marketing_poster

app = Flask(__name__)

@app.route("/generate-poster", methods=["POST"])
def generate_poster_api():
    data = request.json
    result = generate_marketing_poster(
        product_name=data.get("product_name"),
        price=data.get("price"),
        description=data.get("description"),
        location=data.get("location"),
        industry=data.get("industry"),
        product_image_base64=data.get("product_image_base64")
    )

    if result["success"]:
        encoded_image = base64.b64encode(result["poster_bytes"]).decode("utf-8")
        return jsonify({
            "success": True,
            "message": result["message"],
            "poster_base64": encoded_image
        })
    else:
        return jsonify(result), 500


@app.route("/generate-caption", methods=["POST"])
def generate_caption_api():
    data = request.json
    result = generate_product_caption(
        product_name=data.get("product_name"),
        price=data.get("price"),
        description=data.get("description"),
        location=data.get("location"),
        industry=data.get("industry")
    )
    if result["success"]:
        encoded_image = base64.b64encode(result["poster_bytes"]).decode("utf-8")
        return jsonify({
            "success": True,
            "message": result["message"],
            "poster_base64": encoded_image
        })
    else:
        return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
