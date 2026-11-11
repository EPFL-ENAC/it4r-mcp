# EPFL ENAC IT4R MCP

A [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) server to interact with ENAC IT4R using natural language.

## Installation

### Dependencies

The Python project manager `uv` is required: see [uv documentation](https://docs.astral.sh/uv/).

Install the dependencies with:

```sh
make install
``` 

## Usage

Use [OpenCode](https://opencode.ai/docs/) or [Claude Code](https://code.claude.com/docs/) as the AI agent prompt interface.

To use the MCP server from any folder, first install the IT4R MCP tool using `uv`:

```sh
uv tool install git+ssh://git@github.com/EPFL-ENAC/it4r-mcp
```

### OpenCode

#### From any folder

Set up the `opencode.json` as follows:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "it4r": {
      "type": "local",
      "command": ["it4r-mcp"],
      "enabled": true
    }
  }
}
```

And verify it is working:

```sh
opencode mcp list
```

#### From this project

Use OpenCode from this project folder: the IT4R MCP server is declared in the `opencode.json` configuration file.

Verify that the MCP is operational:

```sh
opencode mcp list
```

Start OpenCode and use prompts etc.:

```sh
opencode
```

### Claude Code

#### From any folder

Register the installed IT4R MCP tool (use `--scope project` to write it to the folder's `.mcp.json` instead of your user settings):

```sh
claude mcp add --scope user it4r -- it4r-mcp
```

And verify it is working:

```sh
claude mcp list
```

#### From this project

Use Claude Code from this project folder: the IT4R MCP server is declared in the `.mcp.json` configuration file (approve it when prompted on first start).

Start Claude Code and verify that the MCP is operational with the `/mcp` command:

```sh
claude
```

## Development

Start the MCP server manually:

```sh
make run-dev
```

Then go to http://localhost:6274/ and play with the web interface.
