from mcp.server import MCPServer

# Initialize MCPServer instance
mcp = MCPServer("Practice Weather MCP")

# Tools
@mcp.tool()
def get_weather(location: str) -> str:
    """Get Location based weather information"""
    return f"Weather information for {location}: Sunny, 25°C"

# Resources
@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Get Location based weather information"""
    return f"Weather information for {location}: Sunny, 25°C"

# Prompts
@mcp.prompt()
def weather_prompt(location: str) -> str:
    """Create a prompt for weather information"""
    return f"You are a weather reporter. Provide the current weather information for {location}"

# Server run
if __name__ == "__main__":
    mcp.run()