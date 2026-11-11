from pathlib import Path
from mcp.server.fastmcp import FastMCP


# Create an MCP server
mcp = FastMCP("IT4R", json_response=True)

# Placeholder: replace with your own domain documentation
METHODOLOGY_PATH = Path(__file__).parent / "docs" / "methodology.md"


@mcp.prompt()
def methodology() -> str:
    """Placeholder prompt: methodology guide for the agent."""
    return METHODOLOGY_PATH.read_text()


@mcp.tool()
def get_methodology() -> str:
    """
    Placeholder tool: returns the recommended methodology.
    Call this at the start of any session to understand the expected workflow.
    """
    return METHODOLOGY_PATH.read_text()


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
