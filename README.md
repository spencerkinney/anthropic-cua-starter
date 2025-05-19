# Anthropic+Orgo Computer-Use Starter

Control a computer with Claude.

## What's This?

The purpose of this repo is to help you quickly set up Anthropic's Computer Use with Orgo.

Orgo provides a free cloud-based desktop environment for AI computer use.

This code is like a "Hello World". Not going into anything super complicated.

## Prerequisites

- Python 3.7+
- [Anthropic API key](https://console.anthropic.com/)
- [Orgo API key](https://orgo.ai/start)

## Quick Setup

1. Clone this repo:
```bash
git clone https://github.com/spencerkinney/anthropic-cua-starter
cd anthropic-cua-starter
```

2. Create a virtual environment:
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your API keys:
```
ANTHROPIC_API_KEY=your_anthropic_api_key
ORGO_API_KEY=your_orgo_api_key
```

5. Run the script:
```bash
python run.py
```

Ideally, Claude will now open Firefox and visit a website. That's about it.

## How Does It Work?

The `run.py` script creates a virtual desktop through Orgo and lets Claude control it using the `prompt()` method:

```python
computer = Computer()
computer.prompt("Open Firefox and search for 'Anthropic Claude'")
```

Behind the scenes:
- Orgo provides the virtual desktop environment
- Claude examines screenshots to understand the desktop
- Claude executes actions like clicking and typing to accomplish the task

## Alternative Methods

If you don't want to use natural language, you can directly control the computer:

```python
computer.left_click(200, 200)  # Click at x,y coordinates
computer.type("Hello world")   # Type text
computer.key("ctrl+c")         # Press key combinations
computer.screenshot()          # Take a screenshot
```

## Self-hosting Option

Instead of using Orgo, you can also locally self-host using Anthropic's Docker image from [their quickstarts repo](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo).

## Video Tutorial

[![Anthropic Computer Use Setup in 30 Seconds](https://img.youtube.com/vi/JTbgxry--Fk/0.jpg)](https://www.youtube.com/watch?v=JTbgxry--Fk)

Click the image above to watch a 30-second video showing how to set this up.

## Resources

- [Anthropic Computer Use Docs](https://docs.anthropic.com/en/docs/agents-and-tools/computer-use)
- [Orgo Documentation](https://www.orgo.ai/docs)
- [OS-World Leaderboard](https://os-world.github.io/) - AI model performance on computer tasks