import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, session
from openai import OpenAI
import json
from datetime import datetime

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key')

# Initialize OpenAI client with custom base URL
client = OpenAI(
    base_url=os.getenv('OPENAI_BASE_URL', 'https://openai.vocareum.com/v1'),
    api_key=os.getenv('OPENAI_API_KEY')
)

class CultPassContentGenerator:
    def __init__(self):
        self.company_context = """
        CultPass is a B2B benefits card company that helps organizations offer their employees 
        access to cultural experiences including museums, art galleries, concerts, theater, 
        cultural festivals, art workshops, and historical tours. We focus on enhancing 
        employee wellbeing through cultural enrichment.
        """
    
    def generate_content(self, content_type, target_audience, cultural_focus, tone, additional_context=""):
        prompt = f"""
        You are a marketing expert for CultPass, a B2B company that provides cultural benefits cards to organizations.
        
        Company Context: {self.company_context}
        
        Create compelling {content_type} content with the following specifications:
        - Target Audience: {target_audience}
        - Cultural Focus: {cultural_focus}
        - Tone: {tone}
        - Additional Context: {additional_context}
        
        The content should:
        1. Highlight the value proposition for B2B clients
        2. Emphasize employee wellbeing and cultural enrichment
        3. Include specific cultural experience examples
        4. Be professional yet engaging
        5. Include a clear call-to-action
        
        Format the response appropriately for {content_type}.
        """
        
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # Updated to use the model from exercise
                messages=[
                    {"role": "system", "content": "You are an expert marketing content creator for CultPass."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating content: {str(e)}"
    
    def generate_campaign_strategy(self, campaign_objective, duration, budget_range):
        prompt = f"""
        Create a comprehensive marketing campaign strategy for CultPass with:
        - Objective: {campaign_objective}
        - Duration: {duration}
        - Budget Range: {budget_range}
        
        Include:
        1. Campaign timeline
        2. Content types and channels
        3. Key messaging themes
        4. Success metrics
        5. Cultural events to leverage
        """
        
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # Updated to use the model from exercise
                messages=[
                    {"role": "system", "content": "You are a strategic marketing consultant for CultPass."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1200,
                temperature=0.6
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating strategy: {str(e)}"

# Initialize content generator
content_generator = CultPassContentGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/content-generator')
def content_generator_page():
    return render_template('content_generator.html')

@app.route('/campaign-planner')
def campaign_planner_page():
    return render_template('campaign_planner.html')

@app.route('/api/generate-content', methods=['POST'])
def api_generate_content():
    data = request.get_json()
    
    content = content_generator.generate_content(
        content_type=data.get('content_type'),
        target_audience=data.get('target_audience'),
        cultural_focus=data.get('cultural_focus'),
        tone=data.get('tone'),
        additional_context=data.get('additional_context', '')
    )
    
    # Store in session for history
    if 'content_history' not in session:
        session['content_history'] = []
    
    session['content_history'].append({
        'timestamp': datetime.now().isoformat(),
        'type': data.get('content_type'),
        'content': content
    })
    
    return jsonify({'content': content, 'success': True})

@app.route('/api/generate-campaign', methods=['POST'])
def api_generate_campaign():
    data = request.get_json()
    
    strategy = content_generator.generate_campaign_strategy(
        campaign_objective=data.get('objective'),
        duration=data.get('duration'),
        budget_range=data.get('budget_range')
    )
    
    return jsonify({'strategy': strategy, 'success': True})

@app.route('/api/content-history')
def api_content_history():
    history = session.get('content_history', [])
    return jsonify({'history': history})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
