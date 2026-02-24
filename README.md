# EPFL ENAC IT4R MCP

A [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) server to interact with a ENAC IT4R using natural language.

## Installation

### Dependencies

The Python project manager `uv` is required: see [uv documentation](https://docs.astral.sh/uv/).

Install the dependencies with:

```sh
make install
``` 

## Usage

Use [OpenCode](https://opencode.ai/docs/) as the AI agent prompt interface.

### From any folder

Install the IT4R MCP tool using `uv`:

```sh
uv tool install git+ssh://git@github.com/EPFL-ENAC/it4r-mcp
```

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

### From this project

Use OpenCode from this project folder: the IT4R MCP server is declared in the `opencode.json` configuration file.

Verify that the MCP is operational:

```sh
opencode mcp list
```

Start OpenCode and list servers available, open connection, assign tables etc.:

```sh
opencode
```

## Development

Start the MCP server manually:

```sh
make run-dev
```

Then go to http://localhost:6274/ and play with the web interface.