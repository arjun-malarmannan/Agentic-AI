"""
Test suite for CultPass Marketing Hub
"""
import pytest
from app_demo import app, content_generator

def test_app_creation():
    """Test Flask app creation"""
    assert app is not None
    assert app.config['TESTING'] is not None

def test_content_generator_initialization():
    """Test content generator class"""
    assert content_generator is not None
    assert hasattr(content_generator, 'generate_content')
    assert hasattr(content_generator, 'generate_campaign_strategy')

def test_content_generation():
    """Test content generation with sample data"""
    content = content_generator.generate_content(
        content_type="email_marketing",
        target_audience="hr_managers", 
        cultural_focus="museums_galleries",
        tone="professional_formal",
        additional_context="Test context"
    )
    assert content is not None
    assert len(content) > 0
    assert "CultPass" in content

def test_campaign_strategy_generation():
    """Test campaign strategy generation"""
    strategy = content_generator.generate_campaign_strategy(
        campaign_objective="brand_awareness",
        duration="3_months",
        budget_range="50k_100k"
    )
    assert strategy is not None
    assert len(strategy) > 0
    assert "CAMPAIGN" in strategy

def test_flask_routes():
    """Test Flask application routes"""
    with app.test_client() as client:
        # Test home page
        response = client.get('/')
        assert response.status_code == 200
        
        # Test content generator page
        response = client.get('/content-generator')
        assert response.status_code == 200
        
        # Test campaign planner page
        response = client.get('/campaign-planner')
        assert response.status_code == 200

def test_api_content_generation():
    """Test API content generation endpoint"""
    with app.test_client() as client:
        response = client.post('/api/generate-content', 
                             json={
                                 'content_type': 'social_media_post',
                                 'target_audience': 'startups',
                                 'cultural_focus': 'concerts',
                                 'tone': 'friendly_approachable'
                             })
        assert response.status_code == 200
        data = response.get_json()
        assert data['success'] is True
        assert 'content' in data

if __name__ == '__main__':
    pytest.main([__file__])
