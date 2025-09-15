# Simple test script for OpenAI API integration
from openai import OpenAI

# Step 1: Import and instantiate OpenAI client
print("🚀 Testing OpenAI SDK Integration for CultPass Marketing")
print("=" * 60)

client = OpenAI(
    base_url="https://openai.vocareum.com/v1",
    api_key="voc-00000000000000000000000000000000abcd.12345678"  # Replace with your actual key
)

# Step 2: Define parameters
model = "gpt-4o-mini"
temperature = 0.7

# Step 3: System prompt for CultPass
system_prompt = """
Act as an expert B2B content creator for CultPass, a company that provides cultural benefits cards to organizations.

CultPass helps companies offer their employees access to enriching cultural experiences including museums, art galleries, concerts, theater, cultural festivals, art workshops, and historical tours.

Create compelling marketing content that highlights the value proposition for B2B clients and emphasizes employee wellbeing through cultural enrichment.
"""

# Step 4: Create content function
def create_content(query: str, client: OpenAI, system_prompt: str, model: str, temperature: float) -> str:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": query}
    ]
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Step 5: Test the function
analyst_query = "Create an Instagram post for clients in the automotive industry"

print(f"📝 Query: {analyst_query}")
print("-" * 60)

content = create_content(
    query=analyst_query,
    client=client,
    system_prompt=system_prompt,
    model=model,
    temperature=temperature
)

print("✨ Generated Content:")
print(content)
print("\n" + "=" * 60)
print("✅ Test completed successfully!")

# Additional test scenarios
test_scenarios = [
    "Write a professional email subject line for healthcare companies",
    "Create a LinkedIn post for tech startups about employee benefits"
]

print("\n🧪 Additional Test Scenarios:")
for i, scenario in enumerate(test_scenarios, 1):
    print(f"\n{i}. {scenario}")
    result = create_content(scenario, client, system_prompt, model, 0.5)
    print(f"Result: {result[:100]}..." if len(result) > 100 else result)
