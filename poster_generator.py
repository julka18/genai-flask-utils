from google import genai
from PIL import Image
from io import BytesIO
import traceback
import base64

# Initialize client once (reuse across requests)
client = genai.Client(api_key="YOUR_API_KEY")

def generate_marketing_poster(product_name: str, price: str, description: str, location: str, industry: str, product_image_base64: str):
    try:
        prompt = (
            f"Don’t just create a poster. Create a story. This isn’t about decoration — it’s about making people feel something the moment they see it.\n\n"
            f"Here’s the product you’re working with:\n"
            f"- Product Name: {product_name}\n"
            f"- Price: {price}\n"
            f"- Description: {description}\n"
            f"- Location: {location}\n"
            f"- Industry: {industry}\n\n"
            f"Now, design a marketing poster that is iconic. It must be clean, minimalistic, and emotionally powerful. "
            f"The product should be the hero of the poster. Use whitespace and typography masterfully — every element must have a reason to exist. "
            f"Highlight the product name and price with absolute clarity, and let the design whisper confidence and trust.\n"
            f"Avoid clutter. Avoid clichés. Make it timeless. The result should look like it could be on a billboard in New York City or in an Apple keynote. "
            f"Something people instantly remember, something people believe in.\n"
            f"Create the highest-resolution, modern, industry-relevant poster possible, blending design thinking with storytelling. Make it extraordinary. Make it unforgettable."
        )

        product_image_path = BytesIO(base64.b64decode(product_image_base64))
        product_image = Image.open(product_image_path)

        response = client.models.generate_content(
            model="gemini-2.5-flash-image-preview",
            contents=[prompt, product_image],
        )

        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                poster_image = Image.open(BytesIO(part.inline_data.data))
                output_buffer = BytesIO()
                poster_image.save(output_buffer, format="PNG")
                return {
                    "success": True,
                    "message": "Poster generated successfully",
                    "poster_bytes": output_buffer.getvalue()
                }

        return {"success": False, "message": "No image generated in response", "poster_bytes": None}

    except Exception as e:
        return {"success": False, "message": f"Error: {str(e)} | Trace: {traceback.format_exc()}", "poster_bytes": None}


def generate_product_caption(product_name: str, price: str, description: str, location: str, industry: str):
    """
    Generate a storytelling caption for a product in marketplaces using Google GenAI.

    Args:
        product_name (str): Name of the product.
        price (str): Price of the product.
        description (str): Product description.
        location (str): Target market location.
        industry (str): Industry or niche.

    Returns:
        dict: {
            "success": bool,
            "message": str,
            "caption": str (if success else None)
        }
    """
    try:
        # Build prompt for storytelling caption
        prompt = (
            f"Write a captivating, storytelling product description suitable for marketplaces like Amazon or Flipkart. "
            f"Use 4-5 engaging lines. Highlight the product's uniqueness and value, "
            f"make it relatable to the target audience, and subtly include the price.\n\n"
            f"Product Details:\n"
            f"- Name: {product_name}\n"
            f"- Price: {price}\n"
            f"- Description: {description}\n"
            f"- Location: {location}\n"
            f"- Industry: {industry}\n\n"
            f"Output a concise, memorable, and persuasive description in natural language."
        )

        # Call Gemini API
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[prompt]
        )

        # Extract text output
        for part in response.candidates[0].content.parts:
            if part.text:
                return {
                    "success": True,
                    "message": "Caption generated successfully",
                    "caption": part.text.strip()
                }

        return {
            "success": False,
            "message": "No caption generated in response",
            "caption": None
        }

    except Exception as e:
        return {
            "success": False,
            "message": f"Error: {str(e)} | Trace: {traceback.format_exc()}",
            "caption": None
        }
