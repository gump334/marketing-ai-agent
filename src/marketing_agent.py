"""Main Marketing AI Agent Orchestrator

This module orchestrates all components to provide comprehensive marketing analysis and solutions.
"""

from typing import Dict, Optional
from .business_analyzer import BusinessAnalyzer, BusinessData
from .scorecard_generator import ScorecardGenerator
from .solution_engine import SolutionEngine
from .ai_agent import MarketingAIAgent


class MarketingAgent:
    """
    Main orchestrator for the Marketing AI Agent system.
    
    This agent coordinates analysis, scorecard generation, solution creation,
    and AI-powered insights to help small businesses improve their marketing.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Marketing Agent.
        
        Args:
            api_key: OpenAI API key for AI-powered features (optional)
        """
        self.analyzer = BusinessAnalyzer()
        self.scorecard_gen = ScorecardGenerator()
        self.solution_engine = SolutionEngine()
        self.ai_agent = MarketingAIAgent(api_key=api_key)
    
    def analyze_business(
        self,
        business_name: str,
        industry: str,
        website: Optional[str] = None,
        social_media: Optional[Dict[str, str]] = None,
        monthly_revenue: Optional[float] = None,
        marketing_budget: Optional[float] = None,
        target_audience: Optional[str] = None,
        current_marketing_channels: Optional[list] = None,
        competitor_info: Optional[list] = None,
        use_ai: bool = True
    ) -> Dict:
        """
        Perform comprehensive business marketing analysis.
        
        Args:
            business_name: Name of the business
            industry: Industry/sector
            website: Business website URL
            social_media: Dictionary of social media handles
            monthly_revenue: Monthly revenue in dollars
            marketing_budget: Monthly marketing budget in dollars
            target_audience: Description of target audience
            current_marketing_channels: List of current marketing channels
            competitor_info: List of competitor names/info
            use_ai: Whether to use AI-powered insights
            
        Returns:
            Complete analysis report dictionary
        """
        # Step 1: Collect business data
        business_data = self.analyzer.collect_business_data(
            business_name=business_name,
            industry=industry,
            website=website,
            social_media=social_media or {},
            monthly_revenue=monthly_revenue,
            marketing_budget=marketing_budget,
            target_audience=target_audience,
            current_marketing_channels=current_marketing_channels or [],
            competitor_info=competitor_info or []
        )
        
        # Step 2: Perform analysis
        analysis_results = self.analyzer.perform_comprehensive_analysis(business_data)
        
        # Step 3: Generate scorecard
        scorecard = self.scorecard_gen.generate_scorecard(analysis_results)
        
        # Step 4: Generate solutions
        solutions = self.solution_engine.generate_solutions(scorecard)
        
        # Step 5: Get AI insights (if enabled)
        ai_insights = None
        if use_ai:
            ai_insights = self.ai_agent.analyze_business_with_ai(
                business_data.__dict__,
                analysis_results
            )
        
        # Compile complete report
        report = {
            "business_data": business_data.__dict__,
            "scorecard": scorecard,
            "solutions": solutions,
            "ai_insights": ai_insights
        }
        
        return report
    
    def generate_full_report(
        self,
        business_name: str,
        industry: str,
        **kwargs
    ) -> str:
        """
        Generate a complete formatted text report.
        
        Args:
            business_name: Name of the business
            industry: Industry/sector
            **kwargs: Additional business data
            
        Returns:
            Formatted text report
        """
        # Perform analysis
        report = self.analyze_business(
            business_name=business_name,
            industry=industry,
            **kwargs
        )
        
        # Format report sections
        sections = []
        
        # Header
        sections.append("\n" + "=" * 70)
        sections.append("COMPREHENSIVE MARKETING ANALYSIS REPORT")
        sections.append("=" * 70 + "\n")
        
        # Scorecard section
        sections.append(self.scorecard_gen.format_scorecard_text(report['scorecard']))
        sections.append("\n")
        
        # Solutions section
        sections.append(self.solution_engine.format_solutions_text(report['solutions']))
        sections.append("\n")
        
        # AI Insights section
        if report.get('ai_insights'):
            sections.append("=" * 70)
            sections.append("AI-POWERED INSIGHTS & RECOMMENDATIONS")
            sections.append("=" * 70)
            sections.append(report['ai_insights'].get('ai_insights', 'No insights available'))
            sections.append("\n")
        
        return "\n".join(sections)
    
    def get_quick_assessment(
        self,
        business_name: str,
        industry: str,
        has_website: bool = False,
        social_media_count: int = 0,
        monthly_revenue: Optional[float] = None,
        marketing_budget: Optional[float] = None
    ) -> Dict:
        """
        Perform a quick assessment with minimal data.
        
        Args:
            business_name: Name of the business
            industry: Industry/sector
            has_website: Whether business has a website
            social_media_count: Number of active social media platforms
            monthly_revenue: Monthly revenue in dollars
            marketing_budget: Monthly marketing budget in dollars
            
        Returns:
            Quick assessment dictionary
        """
        # Build minimal social media dict
        social_media = {}
        if social_media_count > 0:
            for i in range(social_media_count):
                social_media[f"platform_{i+1}"] = "active"
        
        # Perform analysis
        report = self.analyze_business(
            business_name=business_name,
            industry=industry,
            website="https://example.com" if has_website else None,
            social_media=social_media,
            monthly_revenue=monthly_revenue,
            marketing_budget=marketing_budget,
            use_ai=False
        )
        
        scorecard = report['scorecard']
        
        # Return simplified results
        return {
            "business_name": business_name,
            "overall_score": scorecard['overall_score'],
            "rating": scorecard['overall_rating'],
            "top_issues": scorecard['critical_issues'][:3] if scorecard['critical_issues'] else [],
            "priority_action": scorecard['priority_actions'][0] if scorecard['priority_actions'] else "Continue monitoring",
            "revenue_impact": scorecard['revenue_impact_assessment']['status']
        }
    
    def get_industry_recommendations(self, industry: str) -> str:
        """
        Get industry-specific marketing recommendations.
        
        Args:
            industry: Industry name
            
        Returns:
            Industry-specific recommendations
        """
        return self.ai_agent.get_industry_insights(industry)
    
    def generate_content_strategy(
        self,
        business_name: str,
        industry: str,
        target_audience: str,
        num_ideas: int = 10
    ) -> list:
        """
        Generate content marketing strategy ideas.
        
        Args:
            business_name: Name of the business
            industry: Industry/sector
            target_audience: Description of target audience
            num_ideas: Number of content ideas to generate
            
        Returns:
            List of content ideas
        """
        business_data = {
            'business_name': business_name,
            'industry': industry,
            'target_audience': target_audience
        }
        
        return self.ai_agent.generate_content_ideas(business_data, num_ideas)
