import base64
from groq import Groq

# Directly hardcoded GROQ API key
GROQ_API_KEY = "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"

# Convert image to base64
def encode_image(image_path):   
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Multimodal LLM query function
def analyze_image_with_query(query, model, encoded_image):
    client = Groq(api_key=GROQ_API_KEY)

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }
    ]

    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model
        )

        # print("✅ Full Chat Completion Object:\n", chat_completion)
        # print("\n🎨 AI Response:\n", chat_completion.choices[0].message.content)
        return chat_completion.choices[0].message.content


    except Exception as e:
        print("❌ Error occurred:", e)

# Main
if __name__ == "__main__":
    image_path = "acne.jpg"
    query = "Is there something wrong with my face?"
    model = "meta-llama/llama-4-scout-17b-16e-instruct"

    encoded_image = encode_image(image_path)
    analyze_image_with_query(query, model, encoded_image)
