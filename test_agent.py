#!/usr/bin/env python3
"""
Simple test suite for the Marketing Agent
Run with: python test_agent.py
"""
from marketing_agent import MarketingAgent


def test_social_media_generation():
    """Test social media post generation"""
    agent = MarketingAgent()
    
    platforms = ['twitter', 'linkedin', 'facebook', 'instagram']
    for platform in platforms:
        result = agent.generate_social_media_post(
            platform=platform,
            topic="Test Topic",
            tone="professional"
        )
        assert result['platform'] == platform
        assert 'content' in result
        assert len(result['content']) <= result['char_limit']
        assert result['topic'] == "Test Topic"
    
    print("✓ Social media generation tests passed")


def test_email_campaign_generation():
    """Test email campaign generation"""
    agent = MarketingAgent()
    
    types = ['promotional', 'newsletter', 'welcome', 're-engagement']
    for campaign_type in types:
        result = agent.generate_email_campaign(
            campaign_type=campaign_type,
            target_audience="Test audience",
            key_message="Test message"
        )
        assert result['campaign_type'] == campaign_type
        assert 'subject' in result
        assert 'body' in result
        assert result['target_audience'] == "Test audience"
    
    print("✓ Email campaign generation tests passed")


def test_market_analysis():
    """Test market analysis"""
    agent = MarketingAgent()
    
    result = agent.analyze_market_trends(
        industry="Technology",
        focus_area="Marketing"
    )
    
    assert result['industry'] == "Technology"
    assert result['focus_area'] == "Marketing"
    assert 'trends' in result
    assert 'opportunities' in result
    assert 'recommendations' in result
    assert len(result['trends']) > 0
    
    print("✓ Market analysis tests passed")


def test_campaign_strategy():
    """Test campaign strategy creation"""
    agent = MarketingAgent()
    
    channels = ["LinkedIn", "Twitter", "Email"]
    result = agent.create_campaign_strategy(
        goal="leads",
        budget="$5000",
        duration="4 weeks",
        channels=channels
    )
    
    assert result['goal'] == "leads"
    assert result['budget'] == "$5000"
    assert result['duration'] == "4 weeks"
    assert result['channels'] == channels
    assert 'phases' in result
    assert 'kpis' in result
    assert 'budget_allocation' in result
    assert len(result['phases']) > 0
    
    print("✓ Campaign strategy tests passed")


def test_seo_recommendations():
    """Test SEO recommendations"""
    agent = MarketingAgent()
    
    keywords = ["keyword1", "keyword2"]
    result = agent.generate_seo_recommendations(
        website_type="blog",
        target_keywords=keywords
    )
    
    assert result['website_type'] == "blog"
    assert result['target_keywords'] == keywords
    assert 'on_page_seo' in result
    assert 'content_strategy' in result
    assert 'technical_seo' in result
    assert 'off_page_seo' in result
    assert len(result['on_page_seo']) > 0
    
    print("✓ SEO recommendations tests passed")


def test_history_tracking():
    """Test action history tracking"""
    agent = MarketingAgent()
    
    # Perform some actions
    agent.generate_social_media_post("twitter", "Test", "casual")
    agent.generate_email_campaign("promotional", "audience", "message")
    
    history = agent.get_history()
    assert len(history) == 2
    assert history[0]['action'] == 'generate_social_media_post'
    assert history[1]['action'] == 'generate_email_campaign'
    
    print("✓ History tracking tests passed")


def run_all_tests():
    """Run all tests"""
    print("=" * 50)
    print("Running AI Marketing Agent Tests")
    print("=" * 50)
    print()
    
    tests = [
        test_social_media_generation,
        test_email_campaign_generation,
        test_market_analysis,
        test_campaign_strategy,
        test_seo_recommendations,
        test_history_tracking
    ]
    
    failed = 0
    for test in tests:
        try:
            test()
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed += 1
    
    print()
    print("=" * 50)
    if failed == 0:
        print("All tests passed! ✓")
    else:
        print(f"{failed} test(s) failed ✗")
    print("=" * 50)
    
    return failed == 0


if __name__ == "__main__":
    import sys
    success = run_all_tests()
    sys.exit(0 if success else 1)
