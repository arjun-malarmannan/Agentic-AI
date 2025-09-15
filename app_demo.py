import os
from flask import Flask, render_template, request, jsonify, session
import json
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'demo-secret-key'

class CultPassContentGenerator:
    def __init__(self):
        self.company_context = """
        CultPass is a B2B benefits card company that helps organizations offer their employees 
        access to cultural experiences including museums, art galleries, concerts, theater, 
        cultural festivals, art workshops, and historical tours. We focus on enhancing 
        employee wellbeing through cultural enrichment.
        """
    
    def generate_content(self, content_type, target_audience, cultural_focus, tone, additional_context=""):
        """
        Demo version with simulated content generation
        In production, this would use the OpenAI API
        """
        
        # Simulated content based on parameters
        content_templates = {
            "email_marketing": {
                "subject": f"Transform {target_audience.replace('_', ' ').title()} Wellbeing with {cultural_focus.replace('_', ' ').title()}",
                "body": f"""
Dear HR Manager,

Enhance your {target_audience.replace('_', ' ')} team's wellbeing with CultPass cultural benefits!

Our {cultural_focus.replace('_', ' ')} experiences provide:
✓ Increased employee satisfaction
✓ Enhanced creativity and innovation  
✓ Stronger team bonding
✓ Improved work-life balance

{additional_context}

Schedule a demo today to see how CultPass transforms workplace culture.

Best regards,
The CultPass Team
                """.strip()
            },
            "social_media_post": f"""
🌟 Attention {target_audience.replace('_', ' ').title()}! 

Transform your workplace with CultPass {cultural_focus.replace('_', ' ')} experiences! 

🎭 {cultural_focus.replace('_', ' ').title()} for your team
📈 Measurable wellbeing improvements
💼 Easy B2B implementation
🎯 Tailored for {target_audience.replace('_', ' ')}

Ready to elevate your company culture? 

#CultPass #EmployeeBenefits #CompanyCulture #{target_audience.title()}
            """.strip(),
            
            "brochure_copy": f"""
CULTPASS: CULTURAL BENEFITS FOR {target_audience.replace('_', ' ').upper()}

Transform Your Workplace Culture
Make {cultural_focus.replace('_', ' ')} accessible to your entire team with CultPass benefits card.

WHY CHOOSE CULTPASS?
• Comprehensive {cultural_focus.replace('_', ' ')} access
• Flexible employee benefits solution
• Proven ROI through enhanced engagement
• Easy integration with existing benefits

PERFECT FOR: {target_audience.replace('_', ' ').title()}
TONE: {tone.replace('_', ' ').title()}

{additional_context}

Contact us today: hello@cultpass.com | 1-800-CULTPASS
            """.strip()
        }
        
        if content_type in content_templates:
            if isinstance(content_templates[content_type], dict):
                return f"Subject: {content_templates[content_type]['subject']}\n\n{content_templates[content_type]['body']}"
            else:
                return content_templates[content_type]
        else:
            return f"""
{content_type.replace('_', ' ').title()} Content for CultPass

Target Audience: {target_audience.replace('_', ' ').title()}
Cultural Focus: {cultural_focus.replace('_', ' ').title()}  
Tone: {tone.replace('_', ' ').title()}

CultPass transforms workplace culture by providing employees with access to enriching {cultural_focus.replace('_', ' ')} experiences. 

Our B2B solution is specifically designed for {target_audience.replace('_', ' ')} who want to enhance employee wellbeing and retention through cultural benefits.

Key Benefits:
• Increased employee satisfaction and engagement
• Enhanced creativity and innovation
• Stronger team bonding and collaboration
• Improved work-life balance and mental health

{additional_context}

Ready to elevate your company culture? Contact CultPass today!
            """.strip()
    
    def generate_campaign_strategy(self, campaign_objective, duration, budget_range):
        """
        Demo campaign strategy generator
        """
        return f"""
CULTPASS MARKETING CAMPAIGN STRATEGY

CAMPAIGN OVERVIEW
Objective: {campaign_objective.replace('_', ' ').title()}
Duration: {duration.replace('_', ' ').title()}
Budget: {budget_range.replace('_', ' ').title()}

CAMPAIGN TIMELINE
Phase 1 (Month 1): Brand Awareness & Lead Generation
• Launch multi-channel content campaign
• Target HR managers and benefits coordinators
• Focus on employee wellbeing messaging

Phase 2 (Month 2-3): Engagement & Conversion  
• Demo scheduling and follow-up campaigns
• Case studies and success stories
• Industry-specific content targeting

Phase 3 (Ongoing): Retention & Expansion
• Customer success stories
• Referral programs
• Account expansion opportunities

CONTENT TYPES & CHANNELS
• LinkedIn: Professional B2B content
• Email: Nurture sequences and newsletters
• Website: Landing pages and case studies
• Brochures: Sales enablement materials
• Webinars: Educational content and demos

KEY MESSAGING THEMES
1. Employee Wellbeing = Business Success
2. Cultural Enrichment Drives Innovation
3. Easy Implementation, Measurable Results
4. Tailored Solutions for Every Industry

SUCCESS METRICS
• Lead generation: 500+ qualified leads
• Conversion rate: 15% demo-to-close
• Customer satisfaction: 90%+ NPS score
• Revenue growth: 25% quarter-over-quarter

CULTURAL EVENTS TO LEVERAGE
• Museum Week (Spring)
• International Jazz Day (April)
• Arts in the Workplace Month (October)
• Cultural Heritage Month (Various)
• Local festival partnerships

BUDGET ALLOCATION
• Content creation: 30%
• Digital advertising: 40%  
• Events and partnerships: 20%
• Tools and analytics: 10%

This comprehensive strategy positions CultPass as the leading cultural benefits solution for forward-thinking organizations.
        """.strip()

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
    print("🚀 Starting CultPass Marketing Hub...")
    print("=" * 50)
    print("✅ Demo mode enabled (simulated AI responses)")
    print("🌐 Open your browser to: http://localhost:5000")
    print("📱 Features available:")
    print("   • Content Generator")
    print("   • Campaign Planner") 
    print("   • Content History")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)
