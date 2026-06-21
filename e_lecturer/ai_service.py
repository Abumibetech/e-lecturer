from google import genai
from groq import Groq
from django.conf import settings


def ask_ai(prompt):
    # Try Gemini first
    try:
        gemini = genai.Client(api_key=settings.GEMINI_API_KEY)

        response = gemini.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=prompt,
        )

        # response may vary by SDK; attempt to return common attributes
        if hasattr(response, "text"):
            return response.text
        if hasattr(response, "content"):
            return response.content
        return str(response)

    except Exception as gemini_error:
        # Log and fall back to Groq
        print("Gemini failed:", gemini_error)

        groq = Groq(api_key=settings.GROQ_API_KEY)

        response = groq.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
        )

        # Normalize groq response
        try:
            return response.choices[0].message.content
        except Exception:
            return str(response)

