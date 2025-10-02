"""Scorecard Generator Module

Generates comprehensive scorecards for business marketing performance.
"""

from typing import Dict, List
from datetime import datetime


class ScorecardGenerator:
    """Generates marketing performance scorecards."""
    
    def __init__(self):
        """Initialize the Scorecard Generator."""
        self.rating_thresholds = {
            "excellent": 80,
            "good": 60,
            "fair": 40,
            "poor": 20,
            "critical": 0
        }
    
    def get_rating(self, score: float) -> str:
        """
        Convert numeric score to rating.
        
        Args:
            score: Numeric score (0-100)
            
        Returns:
            Rating string
        """
        if score >= self.rating_thresholds["excellent"]:
            return "EXCELLENT"
        elif score >= self.rating_thresholds["good"]:
            return "GOOD"
        elif score >= self.rating_thresholds["fair"]:
            return "FAIR"
        elif score >= self.rating_thresholds["poor"]:
            return "POOR"
        else:
            return "CRITICAL"
    
    def generate_scorecard(self, analysis_results: Dict) -> Dict[str, any]:
        """
        Generate a comprehensive scorecard from analysis results.
        
        Args:
            analysis_results: Results from BusinessAnalyzer
            
        Returns:
            Formatted scorecard dictionary
        """
        overall_score = analysis_results.get("overall_score", 0)
        rating = self.get_rating(overall_score)
        
        scorecard = {
            "business_name": analysis_results.get("business_name", "Unknown"),
            "assessment_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "overall_score": round(overall_score, 2),
            "overall_rating": rating,
            "categories": {},
            "critical_issues": analysis_results.get("critical_issues", []),
            "priority_actions": self._generate_priority_actions(analysis_results),
            "revenue_impact_assessment": self._assess_revenue_impact(overall_score)
        }
        
        # Add category scores
        detailed_analysis = analysis_results.get("detailed_analysis", {})
        for category, data in detailed_analysis.items():
            scorecard["categories"][category] = {
                "score": data.get("score", 0),
                "rating": self.get_rating(data.get("score", 0)),
                "issues": data.get("issues", []),
                "impact": data.get("impact", "UNKNOWN")
            }
        
        return scorecard
    
    def _generate_priority_actions(self, analysis_results: Dict) -> List[str]:
        """
        Generate prioritized action items based on analysis.
        
        Args:
            analysis_results: Results from BusinessAnalyzer
            
        Returns:
            List of priority actions
        """
        actions = []
        detailed_analysis = analysis_results.get("detailed_analysis", {})
        
        # Sort by score (lowest first - highest priority)
        sorted_categories = sorted(
            detailed_analysis.items(),
            key=lambda x: x[1].get("score", 100)
        )
        
        for category, data in sorted_categories:
            if data.get("score", 100) < 50:
                category_name = category.replace("_", " ").title()
                actions.append(f"Immediately address {category_name} (Score: {data.get('score', 0)})")
        
        if not actions:
            actions.append("Continue monitoring current marketing strategies")
        
        return actions
    
    def _assess_revenue_impact(self, overall_score: float) -> Dict[str, any]:
        """
        Assess potential revenue impact based on score.
        
        Args:
            overall_score: Overall marketing score
            
        Returns:
            Revenue impact assessment
        """
        if overall_score >= 80:
            return {
                "status": "POSITIVE",
                "description": "Strong marketing practices supporting revenue growth",
                "potential_improvement": "5-10% with optimization"
            }
        elif overall_score >= 60:
            return {
                "status": "NEUTRAL",
                "description": "Marketing practices are adequate but have room for improvement",
                "potential_improvement": "15-25% with strategic improvements"
            }
        elif overall_score >= 40:
            return {
                "status": "CONCERNING",
                "description": "Marketing weaknesses likely impacting revenue negatively",
                "potential_improvement": "30-50% with comprehensive improvements"
            }
        else:
            return {
                "status": "CRITICAL",
                "description": "Severe marketing deficiencies significantly impacting revenue",
                "potential_improvement": "50-100%+ with complete marketing overhaul"
            }
    
    def format_scorecard_text(self, scorecard: Dict) -> str:
        """
        Format scorecard as readable text.
        
        Args:
            scorecard: Scorecard dictionary
            
        Returns:
            Formatted text string
        """
        lines = [
            "=" * 70,
            f"MARKETING SCORECARD: {scorecard['business_name']}",
            "=" * 70,
            f"Assessment Date: {scorecard['assessment_date']}",
            f"Overall Score: {scorecard['overall_score']}/100",
            f"Overall Rating: {scorecard['overall_rating']}",
            "",
            "CATEGORY BREAKDOWN:",
            "-" * 70
        ]
        
        for category, data in scorecard['categories'].items():
            category_name = category.replace("_", " ").title()
            lines.extend([
                f"\n{category_name}:",
                f"  Score: {data['score']}/100 ({data['rating']})",
                f"  Impact: {data['impact']}",
                f"  Issues: {', '.join(data['issues'])}"
            ])
        
        lines.extend([
            "",
            "-" * 70,
            "CRITICAL ISSUES:",
            "-" * 70
        ])
        
        if scorecard['critical_issues']:
            for issue in scorecard['critical_issues']:
                lines.append(f"  • {issue}")
        else:
            lines.append("  No critical issues identified")
        
        lines.extend([
            "",
            "-" * 70,
            "PRIORITY ACTIONS:",
            "-" * 70
        ])
        
        for i, action in enumerate(scorecard['priority_actions'], 1):
            lines.append(f"  {i}. {action}")
        
        lines.extend([
            "",
            "-" * 70,
            "REVENUE IMPACT ASSESSMENT:",
            "-" * 70,
            f"  Status: {scorecard['revenue_impact_assessment']['status']}",
            f"  Description: {scorecard['revenue_impact_assessment']['description']}",
            f"  Potential Improvement: {scorecard['revenue_impact_assessment']['potential_improvement']}",
            "=" * 70
        ])
        
        return "\n".join(lines)
