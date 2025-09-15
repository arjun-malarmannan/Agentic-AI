# 🎯 CultPass Marketing Assistant - Complete OpenAI SDK Exercise
# This demonstrates all the concepts from the exercise with proper implementation

from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("🎨 CultPass Marketing Content Generator")
print("=" * 60)
print("Learning OpenAI SDK for B2B Marketing Content Creation")
print("=" * 60)

# STEP 1: Import and instantiate OpenAI client
print("\n📚 STEP 1: Client Instantiation")
print("-" * 30)

client = OpenAI(
    base_url="https://openai.vocareum.com/v1",
    api_key="voc-00000000000000000000000000000000abcd.12345678"  # Use your actual key
)
print("✅ OpenAI client instantiated with custom Vocareum endpoint")

# STEP 2: Define important parameters
print("\n⚙️ STEP 2: Parameter Definition")
print("-" * 30)

model = "gpt-4o-mini"
print(f"✅ Model: {model}")

# Fixed temperature - should be a single float value, not a list
temperature = 0.7  # This was the error in the original exercise
print(f"✅ Temperature: {temperature} (balanced creativity)")

# STEP 3: System prompt for CultPass
print("\n🎭 STEP 3: System Prompt Definition")
print("-" * 30)

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
print("✅ System prompt defined for CultPass B2B marketing")

# STEP 4: Create reusable function
print("\n🔧 STEP 4: Function Creation")
print("-" * 30)

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
        {"role": "user", "content": query}  # This was missing in the original exercise
    ]
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
        )
        
        # Return just the content for this demo
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Error generating content: {str(e)}"

print("✅ Content generation function created")

# STEP 5: Call the function with proper parameters
print("\n🚀 STEP 5: Function Execution")
print("-" * 30)

# Marketing Analyst input
analyst_query = "Create an Instagram post for clients in the automotive industry"
print(f"📝 Query: {analyst_query}")

# Fixed function call - all parameters properly provided
content = create_content(
    query=analyst_query,
    client=client,
    system_prompt=system_prompt,
    model=model,
    temperature=temperature
)

print("\n✨ Generated Content:")
print("-" * 30)
print(content)

# STEP 6: Experimentation
print("\n\n🧪 STEP 6: Experimentation")
print("=" * 60)

# Experiment 1: Different temperatures
print("\n1️⃣ Testing Different Temperatures:")
temperatures = [0.2, 0.7, 1.2]
test_query = "Write a short email subject line for tech companies"

for temp in temperatures:
    print(f"\n🌡️ Temperature {temp}:")
    result = create_content(test_query, client, system_prompt, model, temp)
    print(f"Result: {result}")

# Experiment 2: Different system prompts
print("\n\n2️⃣ Testing Different System Prompts:")

casual_prompt = "Act as a fun, casual social media manager. Use emojis and trendy language for CultPass."
formal_prompt = "Act as a formal business consultant writing executive-level content for CultPass."

query = "Create content about CultPass benefits"

print("\n😄 Casual Prompt:")
casual_result = create_content(query, client, casual_prompt, model, 0.8)
print(casual_result[:150] + "..." if len(casual_result) > 150 else casual_result)

print("\n💼 Formal Prompt:")
formal_result = create_content(query, client, formal_prompt, model, 0.3)
print(formal_result[:150] + "..." if len(formal_result) > 150 else formal_result)

# Experiment 3: Different channels and industries
print("\n\n3️⃣ Testing Different Channels and Industries:")

scenarios = [
    "Create a LinkedIn post for healthcare companies",
    "Write a TikTok script for startups", 
    "Draft an email for manufacturing companies",
    "Create brochure copy for educational institutions"
]

for scenario in scenarios:
    print(f"\n📋 {scenario}:")
    result = create_content(scenario, client, system_prompt, model, 0.6)
    print(f"Result: {result[:100]}..." if len(result) > 100 else result)

print("\n\n🎉 Exercise Complete!")
print("=" * 60)
print("You've successfully learned:")
print("✅ How to import and use the OpenAI SDK")
print("✅ How to instantiate a client with custom endpoints")
print("✅ How to define model parameters correctly")
print("✅ How to create effective system prompts")
print("✅ How to build reusable functions for LLM calls")
print("✅ How to experiment with different parameters")
print("✅ How to apply AI to real-world marketing scenarios")
print("\n🚀 Ready to build amazing AI-powered applications!")
