from pathlib import Path
from mcp.server.fastmcp import FastMCP


# Create an MCP server
mcp = FastMCP("IT4R", json_response=True)

PICO_METHODOLOGY_PATH = Path(__file__).parent / "docs" / "datashield-pico.md"


@mcp.prompt()
def pico_methodology() -> str:
    """PICO methodology guide for DataSHIELD analysis."""
    return PICO_METHODOLOGY_PATH.read_text()


@mcp.tool()
def get_analysis_methodology() -> str:
    """
    Returns the recommended methodology for conducting a DataSHIELD analysis.
    Call this at the start of any analysis session to understand the PICO framework
    and the correct sequence of operations.
    """
    return PICO_METHODOLOGY_PATH.read_text()


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
