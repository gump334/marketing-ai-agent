"""Marketing AI Agent - Streamlit Web Interface

This Streamlit app provides a user-friendly web interface for the Marketing AI Agent,
allowing users to analyze their business marketing without writing any code.
"""

import streamlit as st
import sys
import os
from typing import Dict, List

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.marketing_agent import MarketingAgent


# Page configuration
st.set_page_config(
    page_title="Marketing AI Agent",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)


def main():
    """Main Streamlit application."""
    
    # Header
    st.title("🚀 Marketing AI Agent")
    st.markdown("### Comprehensive Business Marketing Analysis")
    st.markdown("---")
    
    # Sidebar for API configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        api_key = st.text_input(
            "OpenAI API Key (Optional)",
            type="password",
            help="Enter your OpenAI API key to enable AI-powered insights. Leave blank for basic analysis."
        )
        
        use_ai = st.checkbox(
            "Enable AI Insights",
            value=bool(api_key),
            disabled=not api_key,
            help="AI insights require an OpenAI API key"
        )
        
        st.markdown("---")
        st.markdown("### About")
        st.markdown("""
        This tool analyzes your business marketing across multiple dimensions:
        - Website Quality
        - Social Media Presence
        - Marketing ROI
        - And more...
        """)
        
        st.markdown("### Need Help?")
        st.markdown("[View Documentation](https://github.com/gump334/marketing-ai-agent)")
    
    # Main form
    st.header("📝 Business Information")
    
    with st.form("business_analysis_form"):
        # Required fields
        col1, col2 = st.columns(2)
        
        with col1:
            business_name = st.text_input(
                "Business Name *",
                placeholder="e.g., Joe's Pizza Shop",
                help="Enter your business name"
            )
            
            industry = st.text_input(
                "Industry *",
                placeholder="e.g., Restaurant, Technology, Retail",
                help="What industry is your business in?"
            )
            
            website = st.text_input(
                "Website URL",
                placeholder="https://www.example.com",
                help="Your business website (leave blank if none)"
            )
        
        with col2:
            monthly_revenue = st.number_input(
                "Monthly Revenue ($)",
                min_value=0.0,
                value=0.0,
                step=1000.0,
                help="Average monthly revenue in dollars"
            )
            
            marketing_budget = st.number_input(
                "Monthly Marketing Budget ($)",
                min_value=0.0,
                value=0.0,
                step=100.0,
                help="Monthly marketing budget in dollars"
            )
            
            target_audience = st.text_area(
                "Target Audience",
                placeholder="e.g., Women aged 25-45 interested in fashion",
                help="Describe your target audience",
                height=100
            )
        
        # Social media section
        st.subheader("📱 Social Media Presence")
        col3, col4 = st.columns(2)
        
        with col3:
            linkedin = st.text_input("LinkedIn", placeholder="company-name")
            twitter = st.text_input("Twitter/X", placeholder="@company")
            facebook = st.text_input("Facebook", placeholder="company-page")
        
        with col4:
            instagram = st.text_input("Instagram", placeholder="@company")
            youtube = st.text_input("YouTube", placeholder="channel-name")
            tiktok = st.text_input("TikTok", placeholder="@company")
        
        # Marketing channels
        st.subheader("📢 Current Marketing Channels")
        marketing_channels = st.multiselect(
            "Select all that apply",
            options=[
                "Email Marketing",
                "Social Media",
                "Content Marketing",
                "SEO",
                "Paid Advertising (Google Ads, Facebook Ads, etc.)",
                "LinkedIn",
                "Instagram",
                "Facebook",
                "Twitter/X",
                "YouTube",
                "TikTok",
                "Influencer Marketing",
                "Referral Programs",
                "Word of Mouth",
                "Local Advertising",
                "Direct Mail",
                "Events/Trade Shows",
                "Public Relations",
                "Podcast",
                "Webinars",
                "Other"
            ],
            help="Select all marketing channels you currently use"
        )
        
        # Competitors
        st.subheader("🏢 Competitor Information")
        competitors_text = st.text_area(
            "Competitor Names (one per line)",
            placeholder="Competitor 1\nCompetitor 2\nCompetitor 3",
            help="Enter competitor names, one per line",
            height=100
        )
        
        # Submit button
        st.markdown("---")
        submitted = st.form_submit_button("🔍 Analyze My Business", use_container_width=True, type="primary")
    
    # Process form submission
    if submitted:
        # Validate required fields
        if not business_name or not industry:
            st.error("❌ Please fill in all required fields (Business Name and Industry)")
            return
        
        # Show loading spinner
        with st.spinner("🔄 Analyzing your business... This may take a few moments."):
            try:
                # Initialize agent
                agent = MarketingAgent(api_key=api_key if api_key else None)
                
                # Prepare social media dict
                social_media = {}
                if linkedin: social_media['linkedin'] = linkedin
                if twitter: social_media['twitter'] = twitter
                if facebook: social_media['facebook'] = facebook
                if instagram: social_media['instagram'] = instagram
                if youtube: social_media['youtube'] = youtube
                if tiktok: social_media['tiktok'] = tiktok
                
                # Prepare competitors list
                competitors = [c.strip() for c in competitors_text.split('\n') if c.strip()]
                
                # Run analysis
                report = agent.analyze_business(
                    business_name=business_name,
                    industry=industry,
                    website=website if website else None,
                    social_media=social_media,
                    monthly_revenue=monthly_revenue if monthly_revenue > 0 else None,
                    marketing_budget=marketing_budget if marketing_budget > 0 else None,
                    target_audience=target_audience if target_audience else None,
                    current_marketing_channels=marketing_channels,
                    competitor_info=competitors,
                    use_ai=use_ai
                )
                
                # Display results
                display_results(report, use_ai)
                
            except Exception as e:
                st.error(f"❌ An error occurred during analysis: {str(e)}")
                st.exception(e)


def display_results(report: Dict, use_ai: bool):
    """Display analysis results in a formatted way."""
    
    st.success("✅ Analysis Complete!")
    st.markdown("---")
    
    # Extract data
    scorecard = report['scorecard']
    solutions = report['solutions']
    ai_insights = report.get('ai_insights')
    
    # Overall Score Section
    st.header("📊 Overall Marketing Score")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Overall Score",
            f"{scorecard['overall_score']:.1f}/100",
            help="Overall marketing effectiveness score"
        )
    
    with col2:
        # Color code the rating
        rating = scorecard['overall_rating']
        if rating == "Excellent":
            rating_color = "🟢"
        elif rating == "Good":
            rating_color = "🟡"
        elif rating == "Fair":
            rating_color = "🟠"
        else:
            rating_color = "🔴"
        
        st.metric(
            "Rating",
            f"{rating_color} {rating}",
            help="Performance rating"
        )
    
    with col3:
        impact = scorecard['revenue_impact_assessment']
        st.metric(
            "Revenue Impact",
            impact['status'],
            impact['potential_improvement'],
            help="Potential revenue improvement"
        )
    
    # Category Breakdown
    st.markdown("---")
    st.header("📈 Category Analysis")
    
    categories = scorecard.get('categories', {})
    if categories:
        cols = st.columns(3)
        for idx, (category, data) in enumerate(categories.items()):
            with cols[idx % 3]:
                category_name = category.replace('_', ' ').title()
                score = data.get('score', 0)
                rating = data.get('rating', 'Unknown')
                
                # Color code based on score
                if score >= 70:
                    color = "🟢"
                elif score >= 50:
                    color = "🟡"
                else:
                    color = "🔴"
                
                st.subheader(f"{color} {category_name}")
                st.progress(score / 100)
                st.text(f"Score: {score:.1f}/100 ({rating})")
                
                # Show issues if any
                issues = data.get('issues', [])
                if issues:
                    with st.expander("View Issues"):
                        for issue in issues:
                            st.write(f"• {issue}")
    
    # Critical Issues
    st.markdown("---")
    st.header("🚨 Critical Issues")
    
    critical_issues = scorecard.get('critical_issues', [])
    if critical_issues:
        for issue in critical_issues:
            st.warning(f"⚠️ {issue}")
    else:
        st.success("✅ No critical issues found!")
    
    # Priority Actions
    st.markdown("---")
    st.header("🎯 Priority Actions")
    
    priority_actions = scorecard.get('priority_actions', [])
    if priority_actions:
        for idx, action in enumerate(priority_actions, 1):
            st.info(f"{idx}. {action}")
    
    # Solutions Section
    st.markdown("---")
    st.header("💡 Recommended Solutions")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            "Estimated Investment",
            solutions.get('estimated_total_investment', 'N/A')
        )
    with col2:
        st.metric(
            "Projected Revenue Impact",
            solutions.get('projected_revenue_impact', 'N/A')
        )
    
    # Immediate Actions
    immediate_actions = solutions.get('immediate_actions', [])
    if immediate_actions:
        st.subheader("🔥 Immediate Actions (Start Now)")
        for action in immediate_actions:
            with st.expander(f"📌 {action['title']}"):
                st.write(f"**Description:** {action['description']}")
                st.write(f"**Priority:** {action['priority']}")
                st.write(f"**Cost:** {action['estimated_cost']}")
                st.write(f"**Timeline:** {action['timeline']}")
                st.write(f"**Expected Impact:** {action['expected_impact']}")
    
    # Short-term Strategy
    short_term = solutions.get('short_term_strategy', [])
    if short_term:
        st.subheader("📅 Short-term Strategy (1-3 months)")
        for action in short_term:
            with st.expander(f"📋 {action['title']}"):
                st.write(f"**Description:** {action['description']}")
                st.write(f"**Priority:** {action['priority']}")
                st.write(f"**Cost:** {action['estimated_cost']}")
                st.write(f"**Timeline:** {action['timeline']}")
                st.write(f"**Expected Impact:** {action['expected_impact']}")
    
    # Long-term Strategy
    long_term = solutions.get('long_term_strategy', [])
    if long_term:
        st.subheader("🎯 Long-term Strategy (3-12 months)")
        for action in long_term:
            with st.expander(f"🎪 {action['title']}"):
                st.write(f"**Description:** {action['description']}")
                st.write(f"**Priority:** {action['priority']}")
                st.write(f"**Cost:** {action['estimated_cost']}")
                st.write(f"**Timeline:** {action['timeline']}")
                st.write(f"**Expected Impact:** {action['expected_impact']}")
    
    # AI Insights Section
    if use_ai and ai_insights:
        st.markdown("---")
        st.header("🤖 AI-Powered Insights")
        
        ai_content = ai_insights.get('ai_insights', '')
        if ai_content and ai_content != 'No insights available':
            st.markdown(ai_content)
        else:
            st.info("No AI insights available at this time.")
    
    # Export options
    st.markdown("---")
    st.header("📥 Export Results")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Create downloadable text report
        text_report = create_text_report(report)
        st.download_button(
            label="📄 Download Text Report",
            data=text_report,
            file_name=f"{scorecard['business_name']}_marketing_analysis.txt",
            mime="text/plain"
        )
    
    with col2:
        # Create downloadable JSON
        import json
        json_report = json.dumps(report, indent=2, default=str)
        st.download_button(
            label="📋 Download JSON Report",
            data=json_report,
            file_name=f"{scorecard['business_name']}_marketing_analysis.json",
            mime="application/json"
        )


def create_text_report(report: Dict) -> str:
    """Create a text report from the analysis results."""
    
    scorecard = report['scorecard']
    solutions = report['solutions']
    
    lines = []
    lines.append("=" * 70)
    lines.append("MARKETING AI AGENT - ANALYSIS REPORT")
    lines.append("=" * 70)
    lines.append("")
    lines.append(f"Business: {scorecard['business_name']}")
    lines.append(f"Assessment Date: {scorecard['assessment_date']}")
    lines.append("")
    lines.append("OVERALL SCORE")
    lines.append("-" * 70)
    lines.append(f"Score: {scorecard['overall_score']:.1f}/100")
    lines.append(f"Rating: {scorecard['overall_rating']}")
    lines.append(f"Revenue Impact: {scorecard['revenue_impact_assessment']['status']}")
    lines.append(f"Potential Improvement: {scorecard['revenue_impact_assessment']['potential_improvement']}")
    lines.append("")
    
    # Category Scores
    lines.append("CATEGORY BREAKDOWN")
    lines.append("-" * 70)
    for category, data in scorecard.get('categories', {}).items():
        category_name = category.replace('_', ' ').title()
        lines.append(f"{category_name}: {data['score']:.1f}/100 ({data['rating']})")
    lines.append("")
    
    # Critical Issues
    if scorecard.get('critical_issues'):
        lines.append("CRITICAL ISSUES")
        lines.append("-" * 70)
        for issue in scorecard['critical_issues']:
            lines.append(f"• {issue}")
        lines.append("")
    
    # Priority Actions
    lines.append("PRIORITY ACTIONS")
    lines.append("-" * 70)
    for idx, action in enumerate(scorecard.get('priority_actions', []), 1):
        lines.append(f"{idx}. {action}")
    lines.append("")
    
    # Solutions
    lines.append("RECOMMENDED SOLUTIONS")
    lines.append("-" * 70)
    lines.append(f"Estimated Investment: {solutions['estimated_total_investment']}")
    lines.append(f"Projected Revenue Impact: {solutions['projected_revenue_impact']}")
    lines.append("")
    
    if solutions.get('immediate_actions'):
        lines.append("Immediate Actions:")
        for action in solutions['immediate_actions']:
            lines.append(f"  • {action['title']}")
            lines.append(f"    Cost: {action['estimated_cost']}, Timeline: {action['timeline']}")
        lines.append("")
    
    if solutions.get('short_term_strategy'):
        lines.append("Short-term Strategy (1-3 months):")
        for action in solutions['short_term_strategy']:
            lines.append(f"  • {action['title']}")
            lines.append(f"    Cost: {action['estimated_cost']}, Timeline: {action['timeline']}")
        lines.append("")
    
    if solutions.get('long_term_strategy'):
        lines.append("Long-term Strategy (3-12 months):")
        for action in solutions['long_term_strategy']:
            lines.append(f"  • {action['title']}")
            lines.append(f"    Cost: {action['estimated_cost']}, Timeline: {action['timeline']}")
        lines.append("")
    
    # AI Insights
    if report.get('ai_insights'):
        lines.append("AI-POWERED INSIGHTS")
        lines.append("-" * 70)
        lines.append(report['ai_insights'].get('ai_insights', 'No insights available'))
        lines.append("")
    
    lines.append("=" * 70)
    lines.append("End of Report")
    lines.append("=" * 70)
    
    return "\n".join(lines)


if __name__ == "__main__":
    main()
