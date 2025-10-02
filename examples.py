#!/usr/bin/env python3
"""
Example use cases for the AI Marketing Agent
"""
from marketing_agent import MarketingAgent, print_formatted_dict


def example_social_media_campaign():
    """Example: Create a multi-platform social media campaign"""
    print("=" * 60)
    print("Example 1: Multi-Platform Social Media Campaign")
    print("=" * 60)
    
    agent = MarketingAgent()
    platforms = ['twitter', 'linkedin', 'facebook', 'instagram']
    topic = "Sustainable Business Practices"
    
    print(f"\nGenerating posts for topic: '{topic}'\n")
    
    for platform in platforms:
        print(f"\n{platform.upper()}:")
        print("-" * 40)
        post = agent.generate_social_media_post(
            platform=platform,
            topic=topic,
            tone='professional'
        )
        print(post['content'])
        print(f"\nCharacter count: {post['char_count']}/{post['char_limit']}")


def example_email_sequence():
    """Example: Create a welcome email sequence"""
    print("\n\n" + "=" * 60)
    print("Example 2: Welcome Email Sequence")
    print("=" * 60)
    
    agent = MarketingAgent()
    sequence_types = ['welcome', 'newsletter', 'promotional']
    
    for email_type in sequence_types:
        print(f"\n\n{email_type.upper()} EMAIL:")
        print("-" * 40)
        email = agent.generate_email_campaign(
            campaign_type=email_type,
            target_audience="New subscribers",
            key_message="Get started with our platform"
        )
        print(f"Subject: {email['subject']}")
        print(f"\n{email['body']}")


def example_complete_campaign():
    """Example: Plan a complete marketing campaign"""
    print("\n\n" + "=" * 60)
    print("Example 3: Complete Campaign Planning")
    print("=" * 60)
    
    agent = MarketingAgent()
    
    # Step 1: Market Analysis
    print("\n\nStep 1: Market Analysis")
    print("-" * 40)
    analysis = agent.analyze_market_trends(
        industry="SaaS",
        focus_area="Customer Acquisition"
    )
    print("\nKey Trends:")
    for trend in analysis['trends'][:3]:
        print(f"  • {trend}")
    
    print("\nOpportunities:")
    for opp in analysis['opportunities'][:3]:
        print(f"  • {opp}")
    
    # Step 2: Campaign Strategy
    print("\n\nStep 2: Campaign Strategy")
    print("-" * 40)
    strategy = agent.create_campaign_strategy(
        goal="leads",
        budget="$10,000-$20,000",
        duration="12 weeks",
        channels=["LinkedIn", "Google Ads", "Content Marketing", "Email", "SEO"]
    )
    
    print(f"Goal: {strategy['goal']}")
    print(f"Budget: {strategy['budget']}")
    print(f"Duration: {strategy['duration']}")
    
    print("\nPhases:")
    for phase in strategy['phases']:
        print(f"\n  {phase['phase']} ({phase['duration']})")
        for activity in phase['activities'][:2]:
            print(f"    - {activity}")
    
    print("\nKPIs to Track:")
    for kpi in strategy['kpis']:
        print(f"  • {kpi}")
    
    # Step 3: SEO Optimization
    print("\n\nStep 3: SEO Recommendations")
    print("-" * 40)
    seo = agent.generate_seo_recommendations(
        website_type="corporate",
        target_keywords=["SaaS platform", "customer acquisition", "business software"]
    )
    
    print("\nOn-Page SEO (Top 3):")
    for rec in seo['on_page_seo'][:3]:
        print(f"  • {rec}")
    
    print("\nContent Strategy (Top 3):")
    for rec in seo['content_strategy'][:3]:
        print(f"  • {rec}")


def example_seasonal_campaign():
    """Example: Create a seasonal marketing campaign"""
    print("\n\n" + "=" * 60)
    print("Example 4: Seasonal Campaign (Holiday Season)")
    print("=" * 60)
    
    agent = MarketingAgent()
    
    # Social media for holiday campaign
    print("\n\nHoliday Social Media Posts:")
    print("-" * 40)
    
    platforms = ['instagram', 'facebook']
    for platform in platforms:
        post = agent.generate_social_media_post(
            platform=platform,
            topic="Holiday Special Offers",
            tone='inspirational',
            include_hashtags=True
        )
        print(f"\n{platform.upper()}:")
        print(post['content'])
    
    # Holiday promotional email
    print("\n\nHoliday Email Campaign:")
    print("-" * 40)
    email = agent.generate_email_campaign(
        campaign_type='promotional',
        target_audience='Existing customers',
        key_message='Exclusive holiday discounts - up to 40% off'
    )
    print(f"Subject: {email['subject']}")
    print(f"\n{email['body'][:300]}...")


def example_startup_launch():
    """Example: Marketing strategy for a startup launch"""
    print("\n\n" + "=" * 60)
    print("Example 5: Startup Launch Marketing Strategy")
    print("=" * 60)
    
    agent = MarketingAgent()
    
    # Pre-launch strategy
    print("\n\nPre-Launch Campaign Strategy:")
    print("-" * 40)
    strategy = agent.create_campaign_strategy(
        goal="awareness",
        budget="$5,000-$8,000",
        duration="6 weeks",
        channels=["LinkedIn", "Twitter", "Product Hunt", "Content Marketing"]
    )
    
    print(f"Campaign Goal: {strategy['goal'].upper()}")
    print(f"Budget: {strategy['budget']}")
    print(f"Timeline: {strategy['duration']}")
    
    print("\nBudget Allocation:")
    for channel, allocation in strategy['budget_allocation'].items():
        print(f"  {channel}: {allocation}")
    
    # Launch announcement email
    print("\n\nLaunch Announcement:")
    print("-" * 40)
    email = agent.generate_email_campaign(
        campaign_type='newsletter',
        target_audience='Beta users and early subscribers',
        key_message="We're officially live! Check out our new features"
    )
    print(f"Subject: {email['subject']}")
    
    # SEO for startup website
    print("\n\nWebsite SEO Strategy:")
    print("-" * 40)
    seo = agent.generate_seo_recommendations(
        website_type='corporate',
        target_keywords=['innovative startup', 'tech solution', 'digital transformation']
    )
    print("Top Technical SEO Priorities:")
    for priority in seo['technical_seo'][:4]:
        print(f"  • {priority}")


def main():
    """Run all examples"""
    print("\n" + "=" * 60)
    print("AI MARKETING AGENT - EXAMPLE USE CASES")
    print("=" * 60)
    
    examples = [
        example_social_media_campaign,
        example_email_sequence,
        example_complete_campaign,
        example_seasonal_campaign,
        example_startup_launch
    ]
    
    for example in examples:
        try:
            example()
        except Exception as e:
            print(f"\nError in {example.__name__}: {e}")
    
    print("\n\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
