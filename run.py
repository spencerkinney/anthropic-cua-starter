from orgo import Computer
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create computer instance
computer = Computer()

# Prompt Claude to control the computer
computer.prompt("Open Firefox and search for 'Anthropic Claude'")

# Direct control methods:
# computer.left_click(200, 200)  # Click at coordinates
# computer.type("Hello world")   # Type text
# computer.key("ctrl+c")         # Press key combination
# computer.screenshot()          # Take a screenshot