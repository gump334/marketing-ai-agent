# AI Marketing Agent

An intelligent AI-powered marketing agent designed to help businesses grow at scale. This tool provides comprehensive marketing services including content generation, market analysis, campaign strategy, and SEO optimization.

## Features

- **Social Media Content Generation**: Create engaging posts for Twitter, LinkedIn, Facebook, and Instagram
- **Email Campaign Creation**: Generate professional email campaigns for various purposes
- **Market Analysis**: Get insights on industry trends and opportunities
- **Campaign Strategy**: Develop comprehensive marketing campaign strategies
- **SEO Recommendations**: Receive actionable SEO optimization suggestions
- **Session History**: Track and save all your marketing operations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/gump334/marketing-ai-agent.git
cd marketing-ai-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Configure API keys:
```bash
cp .env.example .env
# Edit .env and add your API keys
```

## Usage

### Running the Demo

To see all features in action:
```bash
python marketing_agent.py
```

Or using the CLI:
```bash
python cli.py demo
```

### CLI Commands

#### Generate Social Media Post
```bash
python cli.py social-post --platform linkedin --topic "AI Marketing" --tone professional
```

Options:
- `--platform`: twitter, linkedin, facebook, instagram
- `--topic`: Topic for the post
- `--tone`: professional, casual, funny, inspirational
- `--no-hashtags`: Exclude hashtags (optional)

#### Create Email Campaign
```bash
python cli.py email --type promotional --audience "small businesses" --message "Special offer"
```

Options:
- `--type`: promotional, newsletter, welcome, re-engagement
- `--audience`: Target audience description
- `--message`: Key message or offer

#### Analyze Market Trends
```bash
python cli.py market-analysis --industry "Technology" --focus "Digital Marketing"
```

Options:
- `--industry`: Industry to analyze
- `--focus`: Specific focus area

#### Create Campaign Strategy
```bash
python cli.py campaign-strategy --goal leads --budget "$5000" --duration "8 weeks" --channels "LinkedIn,Google Ads,Email"
```

Options:
- `--goal`: awareness, leads, sales, engagement
- `--budget`: Budget range
- `--duration`: Campaign duration
- `--channels`: Comma-separated list of channels

#### Generate SEO Recommendations
```bash
python cli.py seo --website-type blog --keywords "AI marketing,automation,strategy"
```

Options:
- `--website-type`: Type of website (blog, ecommerce, corporate, etc.)
- `--keywords`: Comma-separated list of target keywords

### Python API

You can also use the agent programmatically:

```python
from marketing_agent import MarketingAgent

# Initialize the agent
agent = MarketingAgent()

# Generate a social media post
post = agent.generate_social_media_post(
    platform="linkedin",
    topic="AI in Marketing",
    tone="professional",
    include_hashtags=True
)
print(post['content'])

# Create an email campaign
email = agent.generate_email_campaign(
    campaign_type="promotional",
    target_audience="Small business owners",
    key_message="Transform your marketing with AI"
)
print(email['subject'])
print(email['body'])

# Analyze market trends
analysis = agent.analyze_market_trends(
    industry="Technology",
    focus_area="Digital Marketing"
)
print(analysis['trends'])

# Create campaign strategy
strategy = agent.create_campaign_strategy(
    goal="leads",
    budget="$5,000-$10,000",
    duration="8 weeks",
    channels=["LinkedIn", "Google Ads", "Content Marketing"]
)
print(strategy['phases'])

# Generate SEO recommendations
seo = agent.generate_seo_recommendations(
    website_type="blog",
    target_keywords=["AI marketing", "marketing automation"]
)
print(seo['on_page_seo'])

# Save your session history
agent.save_history("my_marketing_session.json")
```

## Project Structure

```
marketing-ai-agent/
├── marketing_agent.py    # Core marketing agent implementation
├── cli.py               # Command-line interface
├── requirements.txt     # Python dependencies
├── .env.example        # Example environment configuration
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Requirements

- Python 3.7+
- Dependencies listed in `requirements.txt`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Future Enhancements

- Integration with real AI APIs (OpenAI, Anthropic)
- Advanced analytics and reporting
- Multi-language support
- Template customization
- CRM integration
- A/B testing suggestions
- ROI calculators
- Competitor analysis tools

## Support

For questions or issues, please open an issue on GitHub.
