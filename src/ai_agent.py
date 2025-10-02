"""AI Agent Module using LangChain

This module uses LangChain and LLMs to provide intelligent analysis and recommendations.
"""

import os
from typing import Dict, Optional

try:
    from dotenv import load_dotenv
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False
    def load_dotenv():
        pass

try:
    from langchain_openai import ChatOpenAI
    from langchain.prompts import ChatPromptTemplate
    from langchain.schema import HumanMessage, SystemMessage
    LANGCHAIN_AVAILABLE = True
except ImportError:
    LANGCHAIN_AVAILABLE = False
    print("Warning: LangChain not installed. AI features will be limited.")


class MarketingAIAgent:
    """AI-powered marketing analysis agent using LangChain."""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Marketing AI Agent.
        
        Args:
            api_key: OpenAI API key (optional, will try to load from environment)
        """
        load_dotenv()
        
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.llm = None
        
        if LANGCHAIN_AVAILABLE and self.api_key:
            try:
                self.llm = ChatOpenAI(
                    model="gpt-3.5-turbo",
                    temperature=0.7,
                    openai_api_key=self.api_key
                )
            except Exception as e:
                print(f"Warning: Could not initialize LLM: {e}")
    
    def analyze_business_with_ai(self, business_data: Dict, analysis_results: Dict) -> Dict[str, str]:
        """
        Use AI to provide enhanced analysis and insights.
        
        Args:
            business_data: Business data dictionary
            analysis_results: Results from BusinessAnalyzer
            
        Returns:
            AI-generated insights dictionary
        """
        if not self.llm:
            return {
                "ai_insights": "AI insights unavailable (API key not configured)",
                "strategic_recommendations": "Please configure OpenAI API key for AI-powered insights"
            }
        
        # Create analysis prompt
        system_message = SystemMessage(content="""You are an expert marketing consultant specializing in helping small businesses improve their marketing strategies and revenue. 
Analyze the provided business data and marketing scorecard, then provide:
1. Key insights about their marketing challenges
2. Strategic recommendations tailored to their specific situation
3. Quick wins they can implement immediately
Be concise, actionable, and focus on ROI.""")
        
        human_message = HumanMessage(content=f"""
Business Information:
- Name: {business_data.get('business_name', 'Unknown')}
- Industry: {business_data.get('industry', 'Unknown')}
- Monthly Revenue: ${business_data.get('monthly_revenue', 'Unknown')}
- Marketing Budget: ${business_data.get('marketing_budget', 'Unknown')}
- Current Channels: {', '.join(business_data.get('current_marketing_channels', []))}

Marketing Score Analysis:
- Overall Score: {analysis_results.get('overall_score', 0)}/100
- Critical Issues: {', '.join(analysis_results.get('critical_issues', []))}

Please provide:
1. Top 3 insights about their marketing situation
2. Top 3 strategic recommendations
3. Top 3 quick wins they can implement this week
""")
        
        try:
            response = self.llm.invoke([system_message, human_message])
            return {
                "ai_insights": response.content,
                "model_used": "gpt-3.5-turbo"
            }
        except Exception as e:
            return {
                "ai_insights": f"Error generating AI insights: {str(e)}",
                "strategic_recommendations": "Please check your API configuration"
            }
    
    def generate_competitor_analysis(self, business_data: Dict) -> str:
        """
        Generate AI-powered competitor analysis.
        
        Args:
            business_data: Business data dictionary
            
        Returns:
            Competitor analysis insights
        """
        if not self.llm:
            return "AI competitor analysis unavailable (API key not configured)"
        
        competitors = business_data.get('competitor_info', [])
        if not competitors:
            return "No competitor information provided for analysis"
        
        system_message = SystemMessage(content="""You are a competitive intelligence analyst. 
Analyze the competitor information provided and identify opportunities for the business to differentiate and compete effectively.""")
        
        human_message = HumanMessage(content=f"""
Business: {business_data.get('business_name', 'Unknown')}
Industry: {business_data.get('industry', 'Unknown')}
Competitors: {', '.join(competitors)}

Provide:
1. Competitive positioning opportunities
2. Differentiation strategies
3. Market gaps to exploit
""")
        
        try:
            response = self.llm.invoke([system_message, human_message])
            return response.content
        except Exception as e:
            return f"Error generating competitor analysis: {str(e)}"
    
    def generate_content_ideas(self, business_data: Dict, num_ideas: int = 5) -> list:
        """
        Generate content marketing ideas using AI.
        
        Args:
            business_data: Business data dictionary
            num_ideas: Number of content ideas to generate
            
        Returns:
            List of content ideas
        """
        if not self.llm:
            return ["AI content generation unavailable (API key not configured)"]
        
        system_message = SystemMessage(content="""You are a content marketing strategist. 
Generate creative, engaging content ideas that will resonate with the target audience and drive business results.""")
        
        human_message = HumanMessage(content=f"""
Business: {business_data.get('business_name', 'Unknown')}
Industry: {business_data.get('industry', 'Unknown')}
Target Audience: {business_data.get('target_audience', 'Unknown')}

Generate {num_ideas} content marketing ideas that would:
1. Engage their target audience
2. Showcase their expertise
3. Drive traffic and conversions

Format: Just list the ideas, one per line, numbered.
""")
        
        try:
            response = self.llm.invoke([system_message, human_message])
            content = response.content.strip()
            ideas = [line.strip() for line in content.split('\n') if line.strip()]
            return ideas
        except Exception as e:
            return [f"Error generating content ideas: {str(e)}"]
    
    def get_industry_insights(self, industry: str) -> str:
        """
        Get AI-powered industry-specific insights.
        
        Args:
            industry: Industry name
            
        Returns:
            Industry insights and trends
        """
        if not self.llm:
            return "AI industry insights unavailable (API key not configured)"
        
        system_message = SystemMessage(content="""You are an industry analyst with deep knowledge of marketing trends and best practices across different sectors.""")
        
        human_message = HumanMessage(content=f"""
Provide key marketing insights and trends for the {industry} industry:
1. Current marketing trends
2. Effective marketing channels
3. Common challenges and solutions
4. Best practices for small businesses

Keep it concise and actionable.
""")
        
        try:
            response = self.llm.invoke([system_message, human_message])
            return response.content
        except Exception as e:
            return f"Error generating industry insights: {str(e)}"
