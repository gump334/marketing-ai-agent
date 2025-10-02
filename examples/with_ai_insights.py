"""AI-Powered Analysis Example

This example shows how to use the AI-powered features of the Marketing AI Agent.
Requires OPENAI_API_KEY to be set in .env file.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.marketing_agent import MarketingAgent


def main():
    """Run AI-powered analysis example."""
    print("Marketing AI Agent - AI-Powered Analysis Example")
    print("=" * 70)
    print()
    
    # Check for API key
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("WARNING: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key to use AI features.")
        print("Example .env file content:")
        print("OPENAI_API_KEY=sk-your-api-key-here")
        print()
        print("Continuing with limited functionality...\n")
    
    # Initialize agent
    agent = MarketingAgent(api_key=api_key)
    
    # Example business with marketing challenges
    print("Analyzing: 'Green Thumb Landscaping'")
    print("-" * 70)
    
    report = agent.analyze_business(
        business_name="Green Thumb Landscaping",
        industry="Landscaping Services",
        website=None,  # No website - major issue
        social_media={},  # No social media presence
        monthly_revenue=12000,
        marketing_budget=300,
        target_audience="Homeowners in suburban areas",
        current_marketing_channels=["Flyers", "Word of mouth"],
        competitor_info=["Perfect Lawns", "Garden Masters", "Pro Landscape"],
        use_ai=True  # Enable AI insights
    )
    
    # Display scorecard
    scorecard = report['scorecard']
    print(f"\nBusiness: {scorecard['business_name']}")
    print(f"Overall Score: {scorecard['overall_score']}/100 ({scorecard['overall_rating']})")
    print(f"Revenue Impact: {scorecard['revenue_impact_assessment']['status']}")
    print(f"Potential Improvement: {scorecard['revenue_impact_assessment']['potential_improvement']}")
    
    # Display critical issues
    print("\n🚨 Critical Issues:")
    for issue in scorecard['critical_issues']:
        print(f"  • {issue}")
    
    # Display priority actions
    print("\n📋 Priority Actions:")
    for i, action in enumerate(scorecard['priority_actions'], 1):
        print(f"  {i}. {action}")
    
    # Display AI insights
    if report.get('ai_insights'):
        print("\n🤖 AI-Powered Insights:")
        print("-" * 70)
        ai_content = report['ai_insights'].get('ai_insights', 'No insights available')
        print(ai_content)
    
    # Display top solutions
    solutions = report['solutions']
    print("\n💡 Recommended Solutions:")
    print("-" * 70)
    print(f"Estimated Investment: {solutions['estimated_total_investment']}")
    print(f"Projected Revenue Impact: {solutions['projected_revenue_impact']}")
    
    if solutions['immediate_actions']:
        print("\nImmediate Actions:")
        for i, action in enumerate(solutions['immediate_actions'][:2], 1):
            print(f"\n{i}. {action['title']}")
            print(f"   Cost: {action['estimated_cost']}")
            print(f"   Timeline: {action['timeline']}")
            print(f"   Impact: {action['expected_impact']}")
    
    # Additional AI Features
    print("\n\n" + "=" * 70)
    print("Additional AI Features")
    print("=" * 70)
    
    # Get industry insights
    if api_key:
        print("\n📊 Industry Insights:")
        print("-" * 70)
        industry_insights = agent.get_industry_recommendations("Landscaping Services")
        print(industry_insights)
        
        # Get content ideas
        print("\n\n📝 Content Marketing Ideas:")
        print("-" * 70)
        content_ideas = agent.generate_content_strategy(
            business_name="Green Thumb Landscaping",
            industry="Landscaping Services",
            target_audience="Homeowners in suburban areas",
            num_ideas=5
        )
        for i, idea in enumerate(content_ideas, 1):
            print(f"{i}. {idea}")
    else:
        print("\nSkipping AI features (API key not configured)")
    
    print("\n" + "=" * 70)
    print("Analysis complete!")


if __name__ == "__main__":
    main()
