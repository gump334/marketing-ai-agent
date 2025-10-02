#!/usr/bin/env python3
"""
CLI interface for the AI Marketing Agent
"""
import sys
import argparse
from marketing_agent import MarketingAgent, print_formatted_dict


def main():
    parser = argparse.ArgumentParser(
        description="AI Marketing Agent - Help your business grow at scale",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate a social media post
  python cli.py social-post --platform linkedin --topic "AI Marketing" --tone professional
  
  # Create an email campaign
  python cli.py email --type promotional --audience "small businesses" --message "Special offer"
  
  # Analyze market trends
  python cli.py market-analysis --industry "Technology" --focus "Digital Marketing"
  
  # Create campaign strategy
  python cli.py campaign-strategy --goal leads --budget "$5000" --duration "8 weeks" --channels "LinkedIn,Google Ads"
  
  # Generate SEO recommendations
  python cli.py seo --website-type blog --keywords "AI marketing,automation"
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Social media post command
    social_parser = subparsers.add_parser('social-post', help='Generate a social media post')
    social_parser.add_argument('--platform', required=True, 
                              choices=['twitter', 'linkedin', 'facebook', 'instagram'],
                              help='Social media platform')
    social_parser.add_argument('--topic', required=True, help='Topic for the post')
    social_parser.add_argument('--tone', default='professional',
                              choices=['professional', 'casual', 'funny', 'inspirational'],
                              help='Tone of the post')
    social_parser.add_argument('--no-hashtags', action='store_true',
                              help='Exclude hashtags from the post')
    
    # Email campaign command
    email_parser = subparsers.add_parser('email', help='Generate an email campaign')
    email_parser.add_argument('--type', required=True,
                             choices=['promotional', 'newsletter', 'welcome', 're-engagement'],
                             help='Type of email campaign')
    email_parser.add_argument('--audience', required=True, help='Target audience description')
    email_parser.add_argument('--message', required=True, help='Key message or offer')
    
    # Market analysis command
    market_parser = subparsers.add_parser('market-analysis', help='Analyze market trends')
    market_parser.add_argument('--industry', required=True, help='Industry to analyze')
    market_parser.add_argument('--focus', required=True, help='Specific focus area')
    
    # Campaign strategy command
    campaign_parser = subparsers.add_parser('campaign-strategy', help='Create campaign strategy')
    campaign_parser.add_argument('--goal', required=True,
                                choices=['awareness', 'leads', 'sales', 'engagement'],
                                help='Campaign goal')
    campaign_parser.add_argument('--budget', required=True, help='Budget range')
    campaign_parser.add_argument('--duration', required=True, help='Campaign duration')
    campaign_parser.add_argument('--channels', required=True,
                                help='Comma-separated list of marketing channels')
    
    # SEO recommendations command
    seo_parser = subparsers.add_parser('seo', help='Generate SEO recommendations')
    seo_parser.add_argument('--website-type', required=True,
                           help='Type of website (e.g., blog, ecommerce, corporate)')
    seo_parser.add_argument('--keywords', required=True,
                           help='Comma-separated list of target keywords')
    
    # Demo command
    subparsers.add_parser('demo', help='Run a full demo of all features')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Initialize agent
    agent = MarketingAgent()
    
    print("=== AI Marketing Agent ===\n")
    
    try:
        if args.command == 'social-post':
            result = agent.generate_social_media_post(
                platform=args.platform,
                topic=args.topic,
                tone=args.tone,
                include_hashtags=not args.no_hashtags
            )
            print("Social Media Post Generated:")
            print("-" * 50)
            print_formatted_dict(result)
            
        elif args.command == 'email':
            result = agent.generate_email_campaign(
                campaign_type=args.type,
                target_audience=args.audience,
                key_message=args.message
            )
            print("Email Campaign Generated:")
            print("-" * 50)
            print_formatted_dict(result)
            
        elif args.command == 'market-analysis':
            result = agent.analyze_market_trends(
                industry=args.industry,
                focus_area=args.focus
            )
            print("Market Analysis:")
            print("-" * 50)
            print_formatted_dict(result)
            
        elif args.command == 'campaign-strategy':
            channels = [ch.strip() for ch in args.channels.split(',')]
            result = agent.create_campaign_strategy(
                goal=args.goal,
                budget=args.budget,
                duration=args.duration,
                channels=channels
            )
            print("Campaign Strategy:")
            print("-" * 50)
            print_formatted_dict(result)
            
        elif args.command == 'seo':
            keywords = [kw.strip() for kw in args.keywords.split(',')]
            result = agent.generate_seo_recommendations(
                website_type=args.website_type,
                target_keywords=keywords
            )
            print("SEO Recommendations:")
            print("-" * 50)
            print_formatted_dict(result)
            
        elif args.command == 'demo':
            print("Running full demo of all features...\n")
            
            print("1. Social Media Post (LinkedIn)")
            print("=" * 50)
            post = agent.generate_social_media_post("linkedin", "AI Marketing", "professional")
            print_formatted_dict(post)
            print("\n")
            
            print("2. Email Campaign (Promotional)")
            print("=" * 50)
            email = agent.generate_email_campaign("promotional", "Small business owners", 
                                                  "Transform your marketing with AI")
            print_formatted_dict(email)
            print("\n")
            
            print("3. Market Analysis")
            print("=" * 50)
            analysis = agent.analyze_market_trends("Technology", "Digital Marketing")
            print_formatted_dict(analysis)
            print("\n")
            
            print("4. Campaign Strategy")
            print("=" * 50)
            strategy = agent.create_campaign_strategy("leads", "$5,000-$10,000", "8 weeks",
                                                     ["LinkedIn", "Google Ads", "Email"])
            print_formatted_dict(strategy)
            print("\n")
            
            print("5. SEO Recommendations")
            print("=" * 50)
            seo = agent.generate_seo_recommendations("blog", 
                                                    ["AI marketing", "automation", "strategy"])
            print_formatted_dict(seo)
            print("\n")
            
            print("=" * 50)
            print(f"Demo complete! Performed {len(agent.get_history())} operations")
            
        # Save history
        print("\n" + "=" * 50)
        print("Saving session history...")
        filename = agent.save_history()
        print(filename)
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
