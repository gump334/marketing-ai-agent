"""Basic Usage Example for Marketing AI Agent

This example demonstrates how to use the Marketing AI Agent to analyze a business.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.marketing_agent import MarketingAgent


def main():
    """Run basic usage example."""
    print("Marketing AI Agent - Basic Usage Example")
    print("=" * 70)
    print()
    
    # Initialize the agent
    # Note: For AI-powered insights, set OPENAI_API_KEY in .env file
    agent = MarketingAgent()
    
    # Example 1: Quick Assessment
    print("Example 1: Quick Assessment")
    print("-" * 70)
    
    quick_result = agent.get_quick_assessment(
        business_name="Joe's Pizza Shop",
        industry="Restaurant/Food Service",
        has_website=False,
        social_media_count=1,
        monthly_revenue=15000,
        marketing_budget=500
    )
    
    print(f"Business: {quick_result['business_name']}")
    print(f"Overall Score: {quick_result['overall_score']}/100")
    print(f"Rating: {quick_result['rating']}")
    print(f"Revenue Impact: {quick_result['revenue_impact']}")
    print(f"Priority Action: {quick_result['priority_action']}")
    print()
    
    # Example 2: Comprehensive Analysis
    print("\nExample 2: Comprehensive Analysis")
    print("-" * 70)
    
    full_report = agent.generate_full_report(
        business_name="TechStart Solutions",
        industry="Technology Consulting",
        website="https://techstart-solutions.com",
        social_media={
            "linkedin": "techstart-solutions",
            "twitter": "@techstart"
        },
        monthly_revenue=50000,
        marketing_budget=2000,
        target_audience="Small to medium-sized businesses needing IT consulting",
        current_marketing_channels=["LinkedIn", "Email Marketing", "Referrals"],
        competitor_info=["BigTech Consulting", "IT Solutions Inc"],
        use_ai=False  # Set to True if you have OpenAI API key configured
    )
    
    print(full_report)
    
    # Example 3: Detailed Analysis with all features
    print("\n\nExample 3: Detailed Business Analysis")
    print("-" * 70)
    
    report = agent.analyze_business(
        business_name="Bella's Boutique",
        industry="Retail Fashion",
        website=None,  # No website
        social_media={"instagram": "bellas_boutique"},
        monthly_revenue=8000,
        marketing_budget=200,
        target_audience="Women aged 25-45 interested in affordable fashion",
        current_marketing_channels=["Instagram", "Word of mouth"],
        competitor_info=["Fashion Forward", "Style Studio"],
        use_ai=False
    )
    
    scorecard = report['scorecard']
    print(f"\nBusiness: {scorecard['business_name']}")
    print(f"Assessment Date: {scorecard['assessment_date']}")
    print(f"Overall Score: {scorecard['overall_score']}/100 ({scorecard['overall_rating']})")
    print(f"\nRevenue Impact: {scorecard['revenue_impact_assessment']['status']}")
    print(f"Potential Improvement: {scorecard['revenue_impact_assessment']['potential_improvement']}")
    
    print("\nTop Priority Actions:")
    for i, action in enumerate(scorecard['priority_actions'][:3], 1):
        print(f"{i}. {action}")
    
    print("\n" + "=" * 70)
    print("Analysis complete! Check the full report above for detailed insights.")


if __name__ == "__main__":
    main()
