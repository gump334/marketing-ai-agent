"""Solution Engine Module

Generates actionable solutions for businesses with marketing challenges.
"""

from typing import Dict, List


class SolutionEngine:
    """Generates customized marketing solutions based on business needs."""
    
    def __init__(self):
        """Initialize the Solution Engine."""
        self.solution_templates = self._initialize_solution_templates()
    
    def _initialize_solution_templates(self) -> Dict[str, Dict]:
        """
        Initialize solution templates for different marketing issues.
        
        Returns:
            Dictionary of solution templates
        """
        return {
            "website_quality": {
                "low_score_solutions": [
                    {
                        "title": "Website Development or Redesign",
                        "description": "Create a professional, mobile-responsive website",
                        "priority": "HIGH",
                        "estimated_cost": "$2,000-$10,000",
                        "timeline": "4-8 weeks",
                        "expected_impact": "Establish online credibility and reach new customers"
                    },
                    {
                        "title": "Basic SEO Optimization",
                        "description": "Optimize website for search engines to increase visibility",
                        "priority": "HIGH",
                        "estimated_cost": "$500-$2,000/month",
                        "timeline": "3-6 months for results",
                        "expected_impact": "Improve organic search rankings and traffic"
                    }
                ],
                "medium_score_solutions": [
                    {
                        "title": "Website Enhancement",
                        "description": "Improve user experience, loading speed, and conversion optimization",
                        "priority": "MEDIUM",
                        "estimated_cost": "$1,000-$5,000",
                        "timeline": "2-4 weeks",
                        "expected_impact": "Increase conversion rates by 20-30%"
                    }
                ]
            },
            "social_media_presence": {
                "low_score_solutions": [
                    {
                        "title": "Social Media Strategy Development",
                        "description": "Create accounts and content strategy for key platforms",
                        "priority": "HIGH",
                        "estimated_cost": "$1,000-$3,000 setup + $500-$2,000/month",
                        "timeline": "2-4 weeks setup, ongoing management",
                        "expected_impact": "Build brand awareness and customer engagement"
                    },
                    {
                        "title": "Content Creation Program",
                        "description": "Regular posting schedule with engaging content",
                        "priority": "HIGH",
                        "estimated_cost": "$500-$2,000/month",
                        "timeline": "Ongoing",
                        "expected_impact": "Grow followers and drive traffic to website"
                    }
                ],
                "medium_score_solutions": [
                    {
                        "title": "Social Media Advertising",
                        "description": "Targeted paid campaigns on social platforms",
                        "priority": "MEDIUM",
                        "estimated_cost": "$500-$5,000/month ad spend + management",
                        "timeline": "Ongoing",
                        "expected_impact": "Reach larger targeted audience quickly"
                    }
                ]
            },
            "marketing_roi": {
                "low_score_solutions": [
                    {
                        "title": "Marketing Analytics Implementation",
                        "description": "Set up tracking and analytics to measure marketing effectiveness",
                        "priority": "HIGH",
                        "estimated_cost": "$500-$2,000 setup",
                        "timeline": "1-2 weeks",
                        "expected_impact": "Identify what's working and optimize spending"
                    },
                    {
                        "title": "Marketing Budget Reallocation",
                        "description": "Shift resources to higher-performing channels",
                        "priority": "HIGH",
                        "estimated_cost": "No additional cost",
                        "timeline": "Immediate",
                        "expected_impact": "Improve ROI by 30-50%"
                    },
                    {
                        "title": "Customer Retention Program",
                        "description": "Focus on repeat customers (5x cheaper than new acquisition)",
                        "priority": "HIGH",
                        "estimated_cost": "$500-$2,000/month",
                        "timeline": "Ongoing",
                        "expected_impact": "Increase lifetime customer value"
                    }
                ]
            }
        }
    
    def generate_solutions(self, scorecard: Dict) -> Dict[str, any]:
        """
        Generate customized solutions based on scorecard results.
        
        Args:
            scorecard: Scorecard from ScorecardGenerator
            
        Returns:
            Dictionary of recommended solutions
        """
        solutions = {
            "business_name": scorecard.get("business_name", "Unknown"),
            "overall_score": scorecard.get("overall_score", 0),
            "immediate_actions": [],
            "short_term_strategy": [],
            "long_term_strategy": [],
            "estimated_total_investment": "$0",
            "projected_revenue_impact": ""
        }
        
        categories = scorecard.get("categories", {})
        
        # Generate solutions for each problematic category
        for category, data in categories.items():
            score = data.get("score", 100)
            
            if category in self.solution_templates:
                if score < 40:
                    # Critical - add immediate actions
                    category_solutions = self.solution_templates[category].get("low_score_solutions", [])
                    solutions["immediate_actions"].extend(category_solutions)
                elif score < 70:
                    # Moderate - add to short-term strategy
                    category_solutions = self.solution_templates[category].get("medium_score_solutions", [])
                    solutions["short_term_strategy"].extend(category_solutions)
        
        # Add general long-term strategies
        solutions["long_term_strategy"] = self._generate_long_term_strategies(scorecard)
        
        # Calculate estimated investment
        solutions["estimated_total_investment"] = self._calculate_investment(solutions)
        
        # Project revenue impact
        solutions["projected_revenue_impact"] = scorecard.get("revenue_impact_assessment", {}).get(
            "potential_improvement", "Unknown"
        )
        
        return solutions
    
    def _generate_long_term_strategies(self, scorecard: Dict) -> List[Dict]:
        """
        Generate long-term strategic recommendations.
        
        Args:
            scorecard: Scorecard dictionary
            
        Returns:
            List of long-term strategies
        """
        strategies = [
            {
                "title": "Build a Strong Brand Identity",
                "description": "Develop consistent brand messaging, visual identity, and voice",
                "priority": "MEDIUM",
                "estimated_cost": "$2,000-$10,000",
                "timeline": "3-6 months",
                "expected_impact": "Increase brand recognition and customer loyalty"
            },
            {
                "title": "Develop Content Marketing Strategy",
                "description": "Create valuable content to attract and engage target audience",
                "priority": "MEDIUM",
                "estimated_cost": "$1,000-$5,000/month",
                "timeline": "6-12 months for significant results",
                "expected_impact": "Establish thought leadership and drive organic traffic"
            },
            {
                "title": "Implement Customer Feedback System",
                "description": "Collect and act on customer feedback to improve offerings",
                "priority": "LOW",
                "estimated_cost": "$500-$2,000",
                "timeline": "Ongoing",
                "expected_impact": "Improve customer satisfaction and retention"
            }
        ]
        
        return strategies
    
    def _calculate_investment(self, solutions: Dict) -> str:
        """
        Calculate estimated total investment needed.
        
        Args:
            solutions: Solutions dictionary
            
        Returns:
            Estimated investment range as string
        """
        # This is a simplified calculation
        immediate_count = len(solutions.get("immediate_actions", []))
        short_term_count = len(solutions.get("short_term_strategy", []))
        
        if immediate_count >= 3:
            return "$5,000-$20,000 (first 3 months)"
        elif immediate_count >= 1:
            return "$2,000-$10,000 (first 3 months)"
        elif short_term_count >= 2:
            return "$1,000-$5,000 (first 3 months)"
        else:
            return "$500-$2,000 (first 3 months)"
    
    def format_solutions_text(self, solutions: Dict) -> str:
        """
        Format solutions as readable text.
        
        Args:
            solutions: Solutions dictionary
            
        Returns:
            Formatted text string
        """
        lines = [
            "=" * 70,
            f"MARKETING SOLUTION PLAN: {solutions['business_name']}",
            "=" * 70,
            f"Current Marketing Score: {solutions['overall_score']}/100",
            f"Projected Revenue Impact: {solutions['projected_revenue_impact']}",
            f"Estimated Investment: {solutions['estimated_total_investment']}",
            ""
        ]
        
        # Immediate Actions
        if solutions['immediate_actions']:
            lines.extend([
                "IMMEDIATE ACTIONS (Start Now):",
                "-" * 70
            ])
            for i, action in enumerate(solutions['immediate_actions'], 1):
                lines.extend([
                    f"\n{i}. {action['title']} [Priority: {action['priority']}]",
                    f"   Description: {action['description']}",
                    f"   Investment: {action['estimated_cost']}",
                    f"   Timeline: {action['timeline']}",
                    f"   Expected Impact: {action['expected_impact']}"
                ])
            lines.append("")
        
        # Short-term Strategy
        if solutions['short_term_strategy']:
            lines.extend([
                "SHORT-TERM STRATEGY (1-3 Months):",
                "-" * 70
            ])
            for i, action in enumerate(solutions['short_term_strategy'], 1):
                lines.extend([
                    f"\n{i}. {action['title']} [Priority: {action['priority']}]",
                    f"   Description: {action['description']}",
                    f"   Investment: {action['estimated_cost']}",
                    f"   Timeline: {action['timeline']}",
                    f"   Expected Impact: {action['expected_impact']}"
                ])
            lines.append("")
        
        # Long-term Strategy
        if solutions['long_term_strategy']:
            lines.extend([
                "LONG-TERM STRATEGY (3-12 Months):",
                "-" * 70
            ])
            for i, action in enumerate(solutions['long_term_strategy'], 1):
                lines.extend([
                    f"\n{i}. {action['title']} [Priority: {action['priority']}]",
                    f"   Description: {action['description']}",
                    f"   Investment: {action['estimated_cost']}",
                    f"   Timeline: {action['timeline']}",
                    f"   Expected Impact: {action['expected_impact']}"
                ])
        
        lines.extend([
            "",
            "=" * 70,
            "Next Steps:",
            "1. Review and prioritize these recommendations",
            "2. Set budget and timeline for implementation",
            "3. Begin with immediate actions",
            "4. Monitor progress and adjust strategy as needed",
            "=" * 70
        ])
        
        return "\n".join(lines)
