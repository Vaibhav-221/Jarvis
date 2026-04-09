from google import genai

client = genai.Client(api_key="AIzaSyAkcwG_3ymmFfbo0KHnZ9_TJdRjJLQDN8k")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works in a few words"
)

print(response.text)