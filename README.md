# Marketing AI Agent

An intelligent AI-powered agent that helps small businesses identify marketing weaknesses, provides comprehensive scorecards, and generates actionable solutions to improve revenue.

## 🎯 Features

- **Interactive Web UI**: User-friendly Streamlit interface for easy data input and result visualization
- **Business Marketing Analysis**: Comprehensive evaluation of marketing practices across multiple dimensions
- **Scorecard Generation**: Detailed scoring system that rates current marketing effectiveness
- **Solution Engine**: Generates prioritized, actionable recommendations with cost and timeline estimates
- **AI-Powered Insights**: Uses LangChain and OpenAI to provide intelligent, context-aware recommendations
- **Revenue Impact Assessment**: Quantifies potential revenue improvements
- **Real-time Data Integration**: Built to integrate with APIs for live business data

## 🚀 Quick Start

### Installation

1. Clone the repository:
```bash
git clone https://github.com/gump334/marketing-ai-agent.git
cd marketing-ai-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

### Interactive UI (Streamlit)

Launch the interactive web interface:

```bash
streamlit run app.py
```

This will open a browser window with an intuitive form where you can:
- Enter your business information
- Specify social media presence
- Select marketing channels
- Add competitor information
- View comprehensive analysis results with visualizations

### Command Line Usage

```python
from src.marketing_agent import MarketingAgent

# Initialize the agent
agent = MarketingAgent()

# Quick assessment
result = agent.get_quick_assessment(
    business_name="Your Business Name",
    industry="Your Industry",
    has_website=True,
    social_media_count=2,
    monthly_revenue=10000,
    marketing_budget=1000
)

print(f"Overall Score: {result['overall_score']}/100")
print(f"Rating: {result['rating']}")
```

### Comprehensive Analysis

```python
# Generate full report
report = agent.generate_full_report(
    business_name="Your Business",
    industry="Technology",
    website="https://yoursite.com",
    social_media={
        "linkedin": "your-company",
        "twitter": "@yourcompany"
    },
    monthly_revenue=50000,
    marketing_budget=5000,
    target_audience="Small businesses",
    current_marketing_channels=["Email", "Social Media"],
    use_ai=True  # Enable AI insights
)

print(report)
```

## 📊 What Gets Analyzed

The agent evaluates businesses across multiple critical marketing dimensions:

1. **Website Quality**: Presence, design, user experience, and optimization
2. **Social Media Presence**: Platform coverage, engagement, and content strategy
3. **Marketing ROI**: Return on marketing investment and budget efficiency
4. **Content Marketing**: Content strategy and execution
5. **SEO Optimization**: Search engine visibility
6. **Customer Engagement**: Customer interaction and retention
7. **Brand Consistency**: Brand messaging and visual identity
8. **Target Audience Alignment**: Marketing effectiveness for target demographics

## 📈 Scorecard System

Businesses receive scores in each category (0-100):

- **90-100**: Excellent - Industry-leading practices
- **70-89**: Good - Solid marketing with minor improvements needed
- **50-69**: Fair - Significant room for improvement
- **30-49**: Poor - Major weaknesses requiring immediate attention
- **0-29**: Critical - Severe deficiencies threatening business viability

## 💡 Solution Generation

The agent provides three tiers of recommendations:

1. **Immediate Actions**: High-priority fixes to implement now
2. **Short-term Strategy**: 1-3 month improvement plans
3. **Long-term Strategy**: 3-12 month strategic initiatives

Each recommendation includes:
- Detailed description
- Priority level
- Estimated cost
- Implementation timeline
- Expected impact on revenue

## 🤖 AI-Powered Features

With an OpenAI API key configured, the agent provides:

- **Intelligent Insights**: Context-aware analysis of marketing challenges
- **Strategic Recommendations**: Tailored advice based on industry and situation
- **Content Ideas**: AI-generated content marketing suggestions
- **Competitor Analysis**: Insights on competitive positioning
- **Industry Trends**: Current best practices and emerging trends

## 📁 Project Structure

```
marketing-ai-agent/
├── src/
│   ├── __init__.py
│   ├── marketing_agent.py      # Main orchestrator
│   ├── business_analyzer.py    # Core analysis engine
│   ├── scorecard_generator.py  # Scorecard creation
│   ├── solution_engine.py      # Solution recommendations
│   └── ai_agent.py             # LangChain/LLM integration
├── examples/
│   ├── basic_usage.py          # Basic usage examples
│   └── with_ai_insights.py     # AI-powered examples
├── app.py                      # Streamlit web UI
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
└── README.md                  # This file
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Required for AI-powered features
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Add other API keys as needed
# GOOGLE_API_KEY=your_google_api_key
# SERPER_API_KEY=your_serper_api_key
```

### API Keys

- **OpenAI API**: Required for AI-powered insights and recommendations
  - Get your key at: https://platform.openai.com/api-keys
  - The agent uses GPT-3.5-turbo by default (cost-effective)

## 📚 Examples

### Example 1: Restaurant with No Online Presence

```python
agent = MarketingAgent()

report = agent.analyze_business(
    business_name="Joe's Pizza Shop",
    industry="Restaurant",
    website=None,
    social_media={},
    monthly_revenue=15000,
    marketing_budget=500,
    target_audience="Local families and young professionals",
    current_marketing_channels=["Word of mouth", "Local ads"]
)

# Typical results:
# - Overall Score: 25/100 (Critical)
# - Key Issue: No online presence
# - Top Recommendation: Create website and social media accounts
# - Potential Revenue Impact: 50-100% improvement
```

### Example 2: Tech Startup with Good Foundation

```python
report = agent.analyze_business(
    business_name="TechStart Solutions",
    industry="Technology Consulting",
    website="https://techstart.com",
    social_media={"linkedin": "techstart", "twitter": "@techstart"},
    monthly_revenue=50000,
    marketing_budget=5000,
    target_audience="Small to medium businesses",
    current_marketing_channels=["LinkedIn", "Content Marketing", "Email"]
)

# Typical results:
# - Overall Score: 65/100 (Fair)
# - Key Issue: Moderate marketing ROI
# - Top Recommendation: Optimize conversion funnel
# - Potential Revenue Impact: 15-25% improvement
```

## 🛠️ Advanced Usage

### Custom Analysis Criteria

```python
from src.business_analyzer import BusinessAnalyzer, BusinessData

analyzer = BusinessAnalyzer()

# Create custom business data
business_data = analyzer.collect_business_data(
    business_name="Custom Business",
    industry="Custom Industry",
    website="https://example.com",
    # ... add more fields
)

# Perform analysis
results = analyzer.perform_comprehensive_analysis(business_data)
```

### Generating Only Solutions

```python
from src.solution_engine import SolutionEngine

engine = SolutionEngine()

# Assuming you have a scorecard
solutions = engine.generate_solutions(scorecard)
formatted_text = engine.format_solutions_text(solutions)
print(formatted_text)
```

## 🧪 Testing

### Interactive UI Testing

Launch the Streamlit web interface:

```bash
streamlit run app.py
```

Then fill in the form with your business details and click "Analyze My Business" to see the results.

### Command Line Testing

Run the example scripts to test functionality:

```bash
# Basic usage (works without API key)
python examples/basic_usage.py

# AI-powered features (requires API key)
python examples/with_ai_insights.py
```

## 🤝 Contributing

Contributions are welcome! Areas for enhancement:

1. Integration with real-time data APIs (Google Analytics, social media APIs)
2. Web scraping for competitor analysis
3. Additional analysis dimensions
4. Support for more LLM providers
5. Visualization and reporting features
6. Multi-language support

## 📝 Use Cases

- **Small Business Consultants**: Quickly assess client marketing needs
- **Business Owners**: Self-evaluate marketing effectiveness
- **Marketing Agencies**: Automate initial client assessments
- **Startup Accelerators**: Screen and help portfolio companies
- **Freelancers**: Offer value-add services to clients

## 🔒 Privacy & Security

- No business data is stored permanently
- API keys should be kept secure in `.env` file
- All analysis is performed locally except LLM API calls
- Consider data sensitivity when using cloud LLM services

## 📄 License

This project is open source and available under the MIT License.

## 🙋 Support

For questions, issues, or feature requests, please open an issue on GitHub.

## 🗺️ Roadmap

- [ ] Integration with Google Analytics API
- [ ] Social media API integration (Facebook, Instagram, LinkedIn)
- [ ] Web scraping for competitor analysis
- [ ] Website analysis with Lighthouse
- [ ] PDF report generation
- [x] Dashboard UI (Streamlit)
- [ ] Database for tracking improvements over time
- [ ] Email reporting capabilities
- [ ] Multi-business batch analysis

## 💪 Built With

- **Python 3.8+**
- **Streamlit**: Interactive web UI framework
- **LangChain**: LLM orchestration framework
- **OpenAI GPT-3.5**: AI-powered insights
- **Pydantic**: Data validation
- **python-dotenv**: Environment management

---

Made to help small businesses grow at scale. 🚀
