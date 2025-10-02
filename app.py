"""Streamlit UI for Marketing AI Agent

This interactive web application provides a user-friendly interface for analyzing
business marketing effectiveness and generating actionable recommendations.
"""

import streamlit as st
import sys
import os
from typing import Dict, List, Optional

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.marketing_agent import MarketingAgent


def initialize_session_state():
    """Initialize session state variables."""
    if 'analysis_complete' not in st.session_state:
        st.session_state.analysis_complete = False
    if 'report' not in st.session_state:
        st.session_state.report = None


def render_header():
    """Render the application header."""
    st.title("🚀 Marketing AI Agent")
    st.markdown("""
    Welcome to the **Marketing AI Agent**! This tool helps small businesses identify 
    marketing weaknesses, provides comprehensive scorecards, and generates actionable 
    solutions to improve revenue.
    """)
    st.divider()


def render_business_info_form() -> Dict:
    """Render the business information form."""
    st.header("📋 Business Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        business_name = st.text_input(
            "Business Name *",
            placeholder="e.g., Green Thumb Landscaping",
            help="Enter your business name"
        )
        
        industry = st.text_input(
            "Industry *",
            placeholder="e.g., Landscaping Services",
            help="What industry is your business in?"
        )
        
        website = st.text_input(
            "Website URL",
            placeholder="https://example.com",
            help="Your business website (optional)"
        )
        
        monthly_revenue = st.number_input(
            "Monthly Revenue ($)",
            min_value=0,
            value=10000,
            step=1000,
            help="Approximate monthly revenue"
        )
    
    with col2:
        marketing_budget = st.number_input(
            "Monthly Marketing Budget ($)",
            min_value=0,
            value=500,
            step=100,
            help="How much do you spend on marketing per month?"
        )
        
        target_audience = st.text_area(
            "Target Audience",
            placeholder="e.g., Homeowners in suburban areas aged 35-55",
            help="Describe your ideal customer",
            height=100
        )
    
    return {
        'business_name': business_name,
        'industry': industry,
        'website': website if website else None,
        'monthly_revenue': monthly_revenue,
        'marketing_budget': marketing_budget,
        'target_audience': target_audience if target_audience else None
    }


def render_social_media_form() -> Dict:
    """Render the social media form."""
    st.header("📱 Social Media Presence")
    st.markdown("Enter your social media handles (leave blank if not applicable)")
    
    col1, col2 = st.columns(2)
    
    social_media = {}
    
    with col1:
        facebook = st.text_input("Facebook", placeholder="@yourbusiness")
        if facebook:
            social_media['facebook'] = facebook
            
        instagram = st.text_input("Instagram", placeholder="@yourbusiness")
        if instagram:
            social_media['instagram'] = instagram
            
        twitter = st.text_input("Twitter/X", placeholder="@yourbusiness")
        if twitter:
            social_media['twitter'] = twitter
    
    with col2:
        linkedin = st.text_input("LinkedIn", placeholder="company/yourbusiness")
        if linkedin:
            social_media['linkedin'] = linkedin
            
        youtube = st.text_input("YouTube", placeholder="@yourbusiness")
        if youtube:
            social_media['youtube'] = youtube
            
        tiktok = st.text_input("TikTok", placeholder="@yourbusiness")
        if tiktok:
            social_media['tiktok'] = tiktok
    
    return social_media


def render_marketing_channels_form() -> List[str]:
    """Render the marketing channels form."""
    st.header("📢 Current Marketing Channels")
    st.markdown("Select all channels you currently use for marketing")
    
    col1, col2, col3 = st.columns(3)
    
    channels = []
    
    with col1:
        if st.checkbox("Social Media"):
            channels.append("Social Media")
        if st.checkbox("Email Marketing"):
            channels.append("Email Marketing")
        if st.checkbox("SEO"):
            channels.append("SEO")
        if st.checkbox("Content Marketing"):
            channels.append("Content Marketing")
    
    with col2:
        if st.checkbox("Paid Advertising"):
            channels.append("Paid Advertising")
        if st.checkbox("Word of Mouth"):
            channels.append("Word of Mouth")
        if st.checkbox("Flyers/Print"):
            channels.append("Flyers/Print")
        if st.checkbox("Events"):
            channels.append("Events")
    
    with col3:
        if st.checkbox("Referral Program"):
            channels.append("Referral Program")
        if st.checkbox("Partnerships"):
            channels.append("Partnerships")
        if st.checkbox("Direct Mail"):
            channels.append("Direct Mail")
        if st.checkbox("Cold Calling"):
            channels.append("Cold Calling")
    
    # Allow custom channels
    custom_channels = st.text_input(
        "Other channels (comma-separated)",
        placeholder="e.g., Podcast, Webinars"
    )
    if custom_channels:
        channels.extend([ch.strip() for ch in custom_channels.split(',') if ch.strip()])
    
    return channels


def render_competitor_form() -> List[str]:
    """Render the competitor information form."""
    st.header("🎯 Competitor Information")
    st.markdown("List your main competitors (one per line)")
    
    competitors_text = st.text_area(
        "Competitor Names",
        placeholder="Perfect Lawns\nGarden Masters\nPro Landscape",
        help="Enter competitor names, one per line",
        height=100
    )
    
    competitors = []
    if competitors_text:
        competitors = [comp.strip() for comp in competitors_text.split('\n') if comp.strip()]
    
    return competitors


def render_ai_settings() -> Dict:
    """Render AI settings."""
    st.header("🤖 AI-Powered Analysis")
    
    use_ai = st.checkbox(
        "Enable AI-Powered Insights",
        value=True,
        help="Use OpenAI to generate intelligent, context-aware recommendations (requires API key)"
    )
    
    api_key = None
    if use_ai:
        api_key_input = st.text_input(
            "OpenAI API Key (optional)",
            type="password",
            help="Enter your OpenAI API key, or set OPENAI_API_KEY in .env file"
        )
        if api_key_input:
            api_key = api_key_input
    
    return {'use_ai': use_ai, 'api_key': api_key}


def display_scorecard(scorecard: Dict):
    """Display the scorecard results."""
    st.header("📊 Marketing Scorecard")
    
    # Overall metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Overall Score",
            f"{scorecard['overall_score']}/100",
            help="Your overall marketing effectiveness score"
        )
    
    with col2:
        st.metric(
            "Rating",
            scorecard['overall_rating'],
            help="Rating category based on your score"
        )
    
    with col3:
        revenue_impact = scorecard.get('revenue_impact_assessment', {})
        st.metric(
            "Revenue Potential",
            revenue_impact.get('potential_improvement', 'N/A'),
            help="Potential revenue improvement"
        )
    
    st.divider()
    
    # Category scores
    st.subheader("Category Breakdown")
    
    categories = scorecard.get('category_scores', {})
    if categories:
        col1, col2 = st.columns(2)
        
        half = len(categories) // 2 + len(categories) % 2
        items = list(categories.items())
        
        with col1:
            for category, score in items[:half]:
                progress = score / 100
                st.progress(progress, text=f"{category}: {score}/100")
        
        with col2:
            for category, score in items[half:]:
                progress = score / 100
                st.progress(progress, text=f"{category}: {score}/100")
    
    # Critical issues
    if scorecard.get('critical_issues'):
        st.divider()
        st.subheader("🚨 Critical Issues")
        for issue in scorecard['critical_issues']:
            st.error(f"• {issue}")
    
    # Priority actions
    if scorecard.get('priority_actions'):
        st.divider()
        st.subheader("📋 Priority Actions")
        for i, action in enumerate(scorecard['priority_actions'], 1):
            st.info(f"{i}. {action}")


def display_solutions(solutions: Dict):
    """Display the recommended solutions."""
    st.header("💡 Recommended Solutions")
    
    # Investment overview
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(
            "Estimated Investment",
            solutions.get('estimated_total_investment', 'N/A'),
            help="Total estimated investment needed"
        )
    
    with col2:
        st.metric(
            "Projected Revenue Impact",
            solutions.get('projected_revenue_impact', 'N/A'),
            help="Expected revenue improvement"
        )
    
    st.divider()
    
    # Immediate actions
    if solutions.get('immediate_actions'):
        st.subheader("⚡ Immediate Actions")
        st.markdown("*Start these right away for quick wins*")
        
        for i, action in enumerate(solutions['immediate_actions'], 1):
            with st.expander(f"{i}. {action['title']} - Priority: {action['priority']}"):
                st.markdown(f"**Description:** {action['description']}")
                st.markdown(f"**Cost:** {action['estimated_cost']}")
                st.markdown(f"**Timeline:** {action['timeline']}")
                st.markdown(f"**Expected Impact:** {action['expected_impact']}")
    
    # Short-term strategy
    if solutions.get('short_term_strategy'):
        st.divider()
        st.subheader("📅 Short-Term Strategy (1-3 Months)")
        
        for i, action in enumerate(solutions['short_term_strategy'], 1):
            with st.expander(f"{i}. {action['title']} - Priority: {action['priority']}"):
                st.markdown(f"**Description:** {action['description']}")
                st.markdown(f"**Investment:** {action['estimated_cost']}")
                st.markdown(f"**Timeline:** {action['timeline']}")
                st.markdown(f"**Expected Impact:** {action['expected_impact']}")
    
    # Long-term strategy
    if solutions.get('long_term_strategy'):
        st.divider()
        st.subheader("🎯 Long-Term Strategy (3-12 Months)")
        
        for i, action in enumerate(solutions['long_term_strategy'], 1):
            with st.expander(f"{i}. {action['title']} - Priority: {action['priority']}"):
                st.markdown(f"**Description:** {action['description']}")
                st.markdown(f"**Investment:** {action['estimated_cost']}")
                st.markdown(f"**Timeline:** {action['timeline']}")
                st.markdown(f"**Expected Impact:** {action['expected_impact']}")


def display_ai_insights(ai_insights: Optional[Dict]):
    """Display AI-powered insights."""
    if not ai_insights:
        return
    
    st.header("🤖 AI-Powered Insights")
    
    insights_content = ai_insights.get('ai_insights', '')
    if insights_content:
        st.markdown(insights_content)
    else:
        st.info("No AI insights available. Make sure your OpenAI API key is configured.")


def main():
    """Main application function."""
    # Configure page
    st.set_page_config(
        page_title="Marketing AI Agent",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize session state
    initialize_session_state()
    
    # Sidebar
    with st.sidebar:
        st.image("https://via.placeholder.com/150x50/4CAF50/FFFFFF?text=Marketing+AI", use_container_width=True)
        st.markdown("### About")
        st.markdown("""
        This AI-powered tool analyzes your business marketing effectiveness 
        and provides actionable recommendations to improve revenue.
        
        **Features:**
        - Comprehensive marketing scorecard
        - Prioritized action items
        - Cost and timeline estimates
        - AI-powered strategic insights
        """)
        
        st.divider()
        
        st.markdown("### Resources")
        st.markdown("[📖 Documentation](https://github.com/gump334/marketing-ai-agent)")
        st.markdown("[💡 Examples](https://github.com/gump334/marketing-ai-agent/tree/main/examples)")
        
        st.divider()
        
        if st.button("🔄 Start New Analysis"):
            st.session_state.analysis_complete = False
            st.session_state.report = None
            st.rerun()
    
    # Main content
    render_header()
    
    if not st.session_state.analysis_complete:
        # Input form
        with st.form("business_analysis_form"):
            # Business info
            business_info = render_business_info_form()
            
            st.divider()
            
            # Social media
            social_media = render_social_media_form()
            
            st.divider()
            
            # Marketing channels
            marketing_channels = render_marketing_channels_form()
            
            st.divider()
            
            # Competitors
            competitors = render_competitor_form()
            
            st.divider()
            
            # AI settings
            ai_settings = render_ai_settings()
            
            # Submit button
            st.divider()
            submitted = st.form_submit_button("🚀 Analyze My Business", use_container_width=True)
            
            if submitted:
                # Validate required fields
                if not business_info['business_name'] or not business_info['industry']:
                    st.error("Please fill in required fields: Business Name and Industry")
                else:
                    with st.spinner("Analyzing your business... This may take a moment."):
                        try:
                            # Initialize agent
                            agent = MarketingAgent(api_key=ai_settings.get('api_key'))
                            
                            # Run analysis
                            report = agent.analyze_business(
                                business_name=business_info['business_name'],
                                industry=business_info['industry'],
                                website=business_info['website'],
                                social_media=social_media,
                                monthly_revenue=business_info['monthly_revenue'],
                                marketing_budget=business_info['marketing_budget'],
                                target_audience=business_info['target_audience'],
                                current_marketing_channels=marketing_channels,
                                competitor_info=competitors,
                                use_ai=ai_settings['use_ai']
                            )
                            
                            # Store in session state
                            st.session_state.report = report
                            st.session_state.analysis_complete = True
                            st.rerun()
                            
                        except Exception as e:
                            st.error(f"An error occurred during analysis: {str(e)}")
                            st.exception(e)
    
    else:
        # Display results
        report = st.session_state.report
        
        if report:
            # Scorecard
            display_scorecard(report['scorecard'])
            
            st.divider()
            
            # Solutions
            display_solutions(report['solutions'])
            
            st.divider()
            
            # AI Insights
            display_ai_insights(report.get('ai_insights'))
            
            # Download option
            st.divider()
            st.info("💾 **Tip:** Use your browser's print function (Ctrl+P or Cmd+P) to save this report as a PDF.")


if __name__ == "__main__":
    main()
