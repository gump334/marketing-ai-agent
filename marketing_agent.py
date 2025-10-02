"""
AI Marketing Agent - Helps businesses grow at scale with AI-powered marketing tools
"""
import os
import sys
from typing import Optional, Dict, List
from datetime import datetime
import json


class MarketingAgent:
    """
    AI-powered marketing agent that provides various marketing services
    including content generation, market analysis, and campaign strategy.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Marketing Agent
        
        Args:
            api_key: Optional API key for AI services (OpenAI, Anthropic, etc.)
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.history: List[Dict] = []
        
    def generate_social_media_post(
        self, 
        platform: str, 
        topic: str, 
        tone: str = "professional",
        include_hashtags: bool = True
    ) -> Dict[str, str]:
        """
        Generate a social media post for the specified platform
        
        Args:
            platform: Social media platform (twitter, linkedin, facebook, instagram)
            topic: Topic or theme for the post
            tone: Tone of the post (professional, casual, funny, inspirational)
            include_hashtags: Whether to include hashtags
            
        Returns:
            Dictionary with post content and metadata
        """
        platform = platform.lower()
        
        # Platform-specific guidelines
        char_limits = {
            "twitter": 280,
            "linkedin": 3000,
            "facebook": 63206,
            "instagram": 2200
        }
        
        limit = char_limits.get(platform, 280)
        
        # Generate content based on topic and tone
        post_templates = {
            "professional": f"Exploring {topic} and its impact on modern business. Here's what you need to know:",
            "casual": f"Let's talk about {topic}! Here's the scoop:",
            "funny": f"You know what's interesting about {topic}? Let me tell you:",
            "inspirational": f"Transform your business with {topic}. The journey starts here:"
        }
        
        base_content = post_templates.get(tone, post_templates["professional"])
        
        # Add platform-specific formatting
        if platform == "twitter":
            content = f"{base_content}\n\n🚀 Growth\n💡 Innovation\n📈 Results"
        elif platform == "linkedin":
            content = f"{base_content}\n\nKey Insights:\n• Drive engagement\n• Build relationships\n• Measure success\n\nWhat are your thoughts?"
        elif platform == "instagram":
            content = f"{base_content}\n\n✨ Discover\n💫 Engage\n🎯 Succeed"
        else:
            content = base_content
            
        # Add hashtags if requested
        if include_hashtags:
            hashtags = self._generate_hashtags(topic, platform)
            content += f"\n\n{hashtags}"
            
        result = {
            "platform": platform,
            "content": content[:limit],
            "char_count": len(content[:limit]),
            "char_limit": limit,
            "topic": topic,
            "tone": tone,
            "timestamp": datetime.now().isoformat()
        }
        
        self.history.append({"action": "generate_social_media_post", "result": result})
        return result
    
    def _generate_hashtags(self, topic: str, platform: str) -> str:
        """Generate relevant hashtags for a topic"""
        topic_words = topic.split()
        base_tags = ["#Marketing", "#Business", "#Growth"]
        
        # Add topic-specific tags
        topic_tags = [f"#{word.capitalize()}" for word in topic_words if len(word) > 3]
        
        # Platform-specific hashtag counts
        tag_counts = {
            "twitter": 3,
            "instagram": 10,
            "linkedin": 5,
            "facebook": 3
        }
        
        count = tag_counts.get(platform, 3)
        all_tags = base_tags + topic_tags
        return " ".join(all_tags[:count])
    
    def generate_email_campaign(
        self, 
        campaign_type: str, 
        target_audience: str,
        key_message: str
    ) -> Dict[str, str]:
        """
        Generate an email marketing campaign
        
        Args:
            campaign_type: Type of campaign (promotional, newsletter, welcome, re-engagement)
            target_audience: Description of target audience
            key_message: Main message or offer
            
        Returns:
            Dictionary with email subject, body, and metadata
        """
        campaign_type = campaign_type.lower()
        
        # Generate subject lines based on campaign type
        subjects = {
            "promotional": f"Exclusive Offer: {key_message}",
            "newsletter": f"This Week's Insights: {key_message}",
            "welcome": f"Welcome! Here's {key_message}",
            "re-engagement": f"We Miss You! {key_message}"
        }
        
        subject = subjects.get(campaign_type, f"Important Update: {key_message}")
        
        # Generate email body template
        body = f"""
Dear Valued Customer,

{self._get_email_opening(campaign_type)}

{key_message}

{self._get_email_cta(campaign_type)}

This email is tailored for: {target_audience}

Best regards,
Your Marketing Team

---
Unsubscribe | Manage Preferences
        """.strip()
        
        result = {
            "campaign_type": campaign_type,
            "subject": subject,
            "body": body,
            "target_audience": target_audience,
            "timestamp": datetime.now().isoformat()
        }
        
        self.history.append({"action": "generate_email_campaign", "result": result})
        return result
    
    def _get_email_opening(self, campaign_type: str) -> str:
        """Get campaign-specific email opening"""
        openings = {
            "promotional": "We have an exciting offer just for you!",
            "newsletter": "Here's what's new and noteworthy this week.",
            "welcome": "Thank you for joining us! We're excited to have you.",
            "re-engagement": "It's been a while! We have something special for you."
        }
        return openings.get(campaign_type, "We wanted to reach out to you today.")
    
    def _get_email_cta(self, campaign_type: str) -> str:
        """Get campaign-specific call-to-action"""
        ctas = {
            "promotional": "Click here to claim your offer before it expires!",
            "newsletter": "Read more insights on our blog.",
            "welcome": "Get started by exploring our resources.",
            "re-engagement": "Come back and see what's new!"
        }
        return ctas.get(campaign_type, "Learn more on our website.")
    
    def analyze_market_trends(self, industry: str, focus_area: str) -> Dict[str, any]:
        """
        Provide market analysis and insights
        
        Args:
            industry: Industry to analyze
            focus_area: Specific area of focus
            
        Returns:
            Dictionary with market insights and recommendations
        """
        analysis = {
            "industry": industry,
            "focus_area": focus_area,
            "trends": [
                f"Digital transformation in {industry}",
                f"Customer-centric approaches for {focus_area}",
                f"Data-driven decision making",
                f"Personalization and automation"
            ],
            "opportunities": [
                f"Expand {focus_area} through digital channels",
                f"Leverage AI and automation in {industry}",
                "Build stronger customer relationships",
                "Optimize marketing spend with analytics"
            ],
            "recommendations": [
                f"Focus on content marketing for {industry}",
                f"Invest in SEO and organic growth",
                "Develop multi-channel strategy",
                "Implement customer feedback loops"
            ],
            "timestamp": datetime.now().isoformat()
        }
        
        self.history.append({"action": "analyze_market_trends", "result": analysis})
        return analysis
    
    def create_campaign_strategy(
        self, 
        goal: str, 
        budget: str, 
        duration: str,
        channels: List[str]
    ) -> Dict[str, any]:
        """
        Create a comprehensive marketing campaign strategy
        
        Args:
            goal: Campaign goal (awareness, leads, sales, engagement)
            budget: Budget range
            duration: Campaign duration
            channels: Marketing channels to use
            
        Returns:
            Dictionary with campaign strategy and timeline
        """
        strategy = {
            "goal": goal,
            "budget": budget,
            "duration": duration,
            "channels": channels,
            "phases": [
                {
                    "phase": "Planning & Research",
                    "duration": "Week 1-2",
                    "activities": [
                        "Define target audience personas",
                        "Competitor analysis",
                        "Content calendar creation",
                        "Asset preparation"
                    ]
                },
                {
                    "phase": "Launch & Execution",
                    "duration": "Week 3-4",
                    "activities": [
                        "Deploy campaigns across channels",
                        "Monitor initial performance",
                        "A/B testing",
                        "Quick optimizations"
                    ]
                },
                {
                    "phase": "Optimization & Scale",
                    "duration": "Week 5+",
                    "activities": [
                        "Analyze performance data",
                        "Scale successful campaigns",
                        "Refine targeting",
                        "Budget reallocation"
                    ]
                }
            ],
            "kpis": self._get_kpis_for_goal(goal),
            "budget_allocation": self._allocate_budget(channels),
            "timestamp": datetime.now().isoformat()
        }
        
        self.history.append({"action": "create_campaign_strategy", "result": strategy})
        return strategy
    
    def _get_kpis_for_goal(self, goal: str) -> List[str]:
        """Get relevant KPIs based on campaign goal"""
        kpi_map = {
            "awareness": ["Impressions", "Reach", "Brand mentions", "Share of voice"],
            "leads": ["Lead volume", "Cost per lead", "Conversion rate", "Lead quality score"],
            "sales": ["Revenue", "ROAS", "Customer acquisition cost", "Average order value"],
            "engagement": ["Engagement rate", "Comments", "Shares", "Time on site"]
        }
        return kpi_map.get(goal.lower(), ["Impressions", "Clicks", "Conversions", "ROI"])
    
    def _allocate_budget(self, channels: List[str]) -> Dict[str, str]:
        """Suggest budget allocation across channels"""
        allocation = {}
        percentage_per_channel = 100 // len(channels) if channels else 0
        
        for channel in channels:
            allocation[channel] = f"{percentage_per_channel}%"
            
        return allocation
    
    def generate_seo_recommendations(
        self, 
        website_type: str, 
        target_keywords: List[str]
    ) -> Dict[str, any]:
        """
        Generate SEO optimization recommendations
        
        Args:
            website_type: Type of website (blog, ecommerce, corporate, etc.)
            target_keywords: List of target keywords
            
        Returns:
            Dictionary with SEO recommendations
        """
        recommendations = {
            "website_type": website_type,
            "target_keywords": target_keywords,
            "on_page_seo": [
                "Optimize title tags with primary keywords",
                "Write compelling meta descriptions (150-160 characters)",
                "Use header tags (H1, H2, H3) hierarchically",
                "Optimize images with alt text",
                "Improve internal linking structure",
                "Ensure mobile responsiveness",
                "Improve page load speed"
            ],
            "content_strategy": [
                f"Create pillar content around: {', '.join(target_keywords[:3])}",
                "Develop topic clusters",
                "Focus on user intent",
                "Update old content regularly",
                "Add FAQ sections",
                "Include multimedia (images, videos)"
            ],
            "technical_seo": [
                "Submit XML sitemap to Google Search Console",
                "Implement schema markup",
                "Fix broken links and 404 errors",
                "Optimize robots.txt",
                "Ensure HTTPS security",
                "Improve crawlability"
            ],
            "off_page_seo": [
                "Build high-quality backlinks",
                "Guest posting on relevant sites",
                "Social media engagement",
                "Local SEO optimization (if applicable)",
                "Online reputation management"
            ],
            "timestamp": datetime.now().isoformat()
        }
        
        self.history.append({"action": "generate_seo_recommendations", "result": recommendations})
        return recommendations
    
    def get_history(self) -> List[Dict]:
        """Get the history of all actions performed"""
        return self.history
    
    def save_history(self, filename: str = "marketing_history.json"):
        """Save action history to a file"""
        with open(filename, 'w') as f:
            json.dump(self.history, f, indent=2)
        return f"History saved to {filename}"


def print_formatted_dict(data: Dict, indent: int = 0):
    """Pretty print a dictionary"""
    prefix = "  " * indent
    for key, value in data.items():
        if isinstance(value, dict):
            print(f"{prefix}{key}:")
            print_formatted_dict(value, indent + 1)
        elif isinstance(value, list):
            print(f"{prefix}{key}:")
            for item in value:
                if isinstance(item, dict):
                    print_formatted_dict(item, indent + 1)
                    print()
                else:
                    print(f"{prefix}  - {item}")
        else:
            print(f"{prefix}{key}: {value}")


if __name__ == "__main__":
    print("=== AI Marketing Agent ===")
    print("Helping businesses grow at scale\n")
    
    # Initialize agent
    agent = MarketingAgent()
    
    # Example usage
    print("1. Generating Social Media Post for LinkedIn...")
    print("-" * 50)
    post = agent.generate_social_media_post(
        platform="linkedin",
        topic="AI in Marketing",
        tone="professional",
        include_hashtags=True
    )
    print_formatted_dict(post)
    print("\n")
    
    print("2. Creating Email Campaign...")
    print("-" * 50)
    email = agent.generate_email_campaign(
        campaign_type="promotional",
        target_audience="Small business owners",
        key_message="Transform your marketing with AI tools"
    )
    print_formatted_dict(email)
    print("\n")
    
    print("3. Analyzing Market Trends...")
    print("-" * 50)
    analysis = agent.analyze_market_trends(
        industry="Technology",
        focus_area="Digital Marketing"
    )
    print_formatted_dict(analysis)
    print("\n")
    
    print("4. Creating Campaign Strategy...")
    print("-" * 50)
    strategy = agent.create_campaign_strategy(
        goal="leads",
        budget="$5,000-$10,000",
        duration="8 weeks",
        channels=["LinkedIn", "Google Ads", "Content Marketing", "Email"]
    )
    print_formatted_dict(strategy)
    print("\n")
    
    print("5. Generating SEO Recommendations...")
    print("-" * 50)
    seo = agent.generate_seo_recommendations(
        website_type="blog",
        target_keywords=["AI marketing", "marketing automation", "digital strategy"]
    )
    print_formatted_dict(seo)
    print("\n")
    
    print("=" * 50)
    print(f"Completed {len(agent.get_history())} marketing operations")
    print("History saved to marketing_history.json")
    agent.save_history()
