# CultPass Marketing Content Generator - OpenAI SDK Exercise
# Learning how to interact with LLMs programmatically

from openai import OpenAI
import json

# Step 1: Instantiate OpenAI client with your API Key
# Using the custom Vocareum endpoint as specified in the instructions
client = OpenAI(
    base_url="https://openai.vocareum.com/v1",
    api_key="voc-00000000000000000000000000000000abcd.12345678"  # Replace with your actual key
)

# Step 2: Define important parameters
# Model: the specific LLM you want to call
model = "gpt-4o-mini"

# Temperature: how random you want the responses to be (0.0 to 2.0)
# Lower values (closer to 0.0) = more consistent and focused
# Higher values (closer to 2.0) = more creative and random
temperature = 0.7  # Balanced creativity for marketing content

# Step 3: Tell the model how to behave - System Prompt
# For CultPass B2B marketing content creation
system_prompt = """
Act as an expert B2B content creator for CultPass, a company that provides cultural benefits cards to organizations.

CultPass helps companies offer their employees access to enriching cultural experiences including:
- Museums and art galleries
- Concerts and live performances  
- Theater shows and performances
- Art workshops and creative classes
- Cultural festivals and events
- Historical tours and experiences

Your role is to create compelling marketing content that:
1. Highlights the value proposition for B2B clients
2. Emphasizes employee wellbeing and cultural enrichment benefits
3. Shows ROI through improved employee satisfaction and retention
4. Adapts tone and style based on the target industry and channel
5. Includes clear calls-to-action appropriate for B2B decision makers

Always maintain a professional yet engaging tone that speaks to business leaders, HR managers, and employee benefits coordinators.
"""

# Step 4: Create a function to reuse LLM calls
def create_content(query: str,
                   client: OpenAI,
                   system_prompt: str,
                   model: str,
                   temperature: float) -> str:
    """
    Generate marketing content using OpenAI's API
    
    Args:
        query: The marketing analyst's content request
        client: OpenAI client instance
        system_prompt: Instructions for the AI's behavior
        model: The LLM model to use
        temperature: Creativity level (0.0-2.0)
    
    Returns:
        Generated content as string
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": query}  # Marketing analyst query
    ]
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
        )
        
        # Extract the content from the response
        content = response.choices[0].message.content
        
        # Optional: Print full response structure for learning
        print("=== FULL RESPONSE STRUCTURE ===")
        print(f"Model used: {response.model}")
        print(f"Total tokens: {response.usage.total_tokens}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Completion tokens: {response.usage.completion_tokens}")
        print(f"Finish reason: {response.choices[0].finish_reason}")
        print("================================\n")
        
        return content
        
    except Exception as e:
        return f"Error generating content: {str(e)}"

# Step 5: Call create_content function
# Marketing Analyst input examples
analyst_query = "Create an Instagram post for clients in the automotive industry"

content = create_content(
    query=analyst_query,
    client=client,
    system_prompt=system_prompt,
    model=model,
    temperature=temperature
)

print("GENERATED CONTENT:")
print("=" * 50)
print(content)
print("=" * 50)

# Step 6: Experiment with different scenarios
print("\n🧪 EXPERIMENTATION SECTION 🧪\n")

# Experiment 1: Different temperature values
print("1. TESTING DIFFERENT TEMPERATURE VALUES:")
print("-" * 40)

temperatures_to_test = [0.1, 0.7, 1.5]
query_temp_test = "Write a professional email to HR managers about CultPass benefits"

for temp in temperatures_to_test:
    print(f"\n🌡️ Temperature: {temp}")
    result = create_content(query_temp_test, client, system_prompt, model, temp)
    print(f"Result: {result[:100]}..." if len(result) > 100 else result)

# Experiment 2: Different system prompts
print("\n\n2. TESTING DIFFERENT SYSTEM PROMPTS:")
print("-" * 40)

creative_prompt = """
Act as a creative and energetic social media manager for CultPass. 
Write content that's fun, engaging, and uses emojis. 
Focus on making cultural experiences sound exciting and accessible.
"""

formal_prompt = """
Act as a formal business consultant writing for C-suite executives.
Use data-driven language, focus on ROI metrics, and maintain a corporate tone.
Emphasize strategic business benefits of cultural employee programs.
"""

query_prompt_test = "Create content about CultPass for the tech industry"

print("\n📝 Creative System Prompt:")
creative_result = create_content(query_prompt_test, client, creative_prompt, model, 0.8)
print(creative_result[:150] + "..." if len(creative_result) > 150 else creative_result)

print("\n💼 Formal System Prompt:")
formal_result = create_content(query_prompt_test, client, formal_prompt, model, 0.3)
print(formal_result[:150] + "..." if len(formal_result) > 150 else formal_result)

# Experiment 3: Different channels and industries
print("\n\n3. TESTING DIFFERENT CHANNELS AND INDUSTRIES:")
print("-" * 40)

test_scenarios = [
    "Create a LinkedIn post for healthcare companies",
    "Write a TikTok script for startups in the finance sector", 
    "Draft an email newsletter for manufacturing companies",
    "Create a brochure copy for educational institutions",
    "Write a press release for hospitality industry partnerships"
]

for scenario in test_scenarios:
    print(f"\n📋 Scenario: {scenario}")
    result = create_content(scenario, client, system_prompt, model, 0.6)
    print(f"Result: {result[:120]}..." if len(result) > 120 else result)

# Experiment 4: Inspecting the full response object
print("\n\n4. DETAILED RESPONSE OBJECT INSPECTION:")
print("-" * 40)

detailed_query = "Create a comprehensive marketing strategy summary for CultPass"
response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": detailed_query}
    ],
    temperature=0.5,
)

print("📊 RESPONSE OBJECT ANALYSIS:")
print(f"Response ID: {response.id}")
print(f"Object type: {response.object}")
print(f"Created timestamp: {response.created}")
print(f"Model used: {response.model}")
print(f"System fingerprint: {response.system_fingerprint}")

print("\n📈 USAGE STATISTICS:")
print(f"Prompt tokens: {response.usage.prompt_tokens}")
print(f"Completion tokens: {response.usage.completion_tokens}")
print(f"Total tokens: {response.usage.total_tokens}")

print("\n📝 CHOICE DETAILS:")
for i, choice in enumerate(response.choices):
    print(f"Choice {i}:")
    print(f"  - Index: {choice.index}")
    print(f"  - Finish reason: {choice.finish_reason}")
    print(f"  - Message role: {choice.message.role}")
    print(f"  - Content length: {len(choice.message.content)} characters")

print(f"\n📋 GENERATED CONTENT:\n{response.choices[0].message.content}")

# Advanced: Function to save content for later use
def save_content_to_file(content: str, filename: str = "generated_content.txt"):
    """Save generated content to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Generated on: {json.dumps({'timestamp': str(__import__('datetime').datetime.now())})}\n")
        f.write("=" * 60 + "\n")
        f.write(content)
    print(f"✅ Content saved to {filename}")

# Save the last generated content
save_content_to_file(response.choices[0].message.content, "cultpass_marketing_content.txt")

print("\n🎉 Exercise completed! You've successfully learned how to:")
print("✅ Import and instantiate the OpenAI client")
print("✅ Define model parameters and system prompts")
print("✅ Create reusable functions for LLM interactions")
print("✅ Experiment with different temperatures and prompts")
print("✅ Inspect response objects for detailed information")
print("✅ Apply the concepts to real-world marketing scenarios")
