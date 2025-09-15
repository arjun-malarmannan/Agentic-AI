# Simple OpenAI API Test for CultPass
import os
from openai import OpenAI

print("🚀 Testing OpenAI API Connection for CultPass")
print("=" * 50)

# Test the OpenAI client initialization
try:
    client = OpenAI(
        base_url="https://openai.vocareum.com/v1",
        api_key="voc-00000000000000000000000000000000abcd.12345678"
    )
    print("✅ OpenAI client initialized successfully")
    
    # Test a simple API call
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for CultPass marketing."},
            {"role": "user", "content": "Write a short tagline for CultPass"}
        ],
        max_tokens=50,
        temperature=0.7
    )
    
    print("✅ API call successful!")
    print(f"Generated tagline: {response.choices[0].message.content}")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
    print("This might be due to:")
    print("1. Invalid API key")
    print("2. Network connectivity issues")
    print("3. API endpoint not accessible")

print("\n" + "=" * 50)
print("Test completed!")
