# Quick Start Guide

Get started with the AI Marketing Agent in 5 minutes!

## Installation

```bash
# Clone the repository
git clone https://github.com/gump334/marketing-ai-agent.git
cd marketing-ai-agent

# Install dependencies
pip install -r requirements.txt
```

## Your First Marketing Task

### 1. Generate a Social Media Post

```bash
python cli.py social-post --platform linkedin --topic "AI in Business" --tone professional
```

### 2. Create an Email Campaign

```bash
python cli.py email --type welcome --audience "new users" --message "Welcome to our platform"
```

### 3. Run the Complete Demo

```bash
python cli.py demo
```

This will showcase all 5 core features of the agent.

## Common Use Cases

### Building a Product Launch Campaign

1. **Market Research**
```bash
python cli.py market-analysis --industry "SaaS" --focus "Product Launch"
```

2. **Campaign Planning**
```bash
python cli.py campaign-strategy --goal awareness --budget "$10000" --duration "6 weeks" --channels "LinkedIn,Twitter,Email"
```

3. **Create Launch Content**
```bash
python cli.py social-post --platform twitter --topic "New Product Launch" --tone inspirational
python cli.py email --type newsletter --audience "existing customers" --message "Check out our new features"
```

4. **SEO Optimization**
```bash
python cli.py seo --website-type corporate --keywords "innovative product,SaaS solution,productivity tool"
```

### Running a Seasonal Promotion

1. **Create promotional content**
```bash
python cli.py email --type promotional --audience "subscribers" --message "Holiday Sale - 40% off"
python cli.py social-post --platform instagram --topic "Holiday Specials" --tone inspirational
```

2. **Plan the campaign**
```bash
python cli.py campaign-strategy --goal sales --budget "$5000" --duration "2 weeks" --channels "Facebook,Instagram,Email"
```

## Using the Python API

For more control, use the Python API directly:

```python
from marketing_agent import MarketingAgent

# Initialize
agent = MarketingAgent()

# Generate content
post = agent.generate_social_media_post(
    platform="linkedin",
    topic="Digital Transformation",
    tone="professional"
)

print(post['content'])

# Save your work
agent.save_history("my_campaign.json")
```

## Next Steps

- Check out `examples.py` for more advanced use cases
- Read the full `README.md` for detailed documentation
- Customize the agent for your specific needs

## Need Help?

- Run `python cli.py --help` to see all available commands
- Run `python cli.py [command] --help` for command-specific help
- Check the examples in `examples.py`

Happy Marketing! 🚀
