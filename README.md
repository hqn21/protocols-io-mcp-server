# Protocols.io MCP Server

A Model Context Protocol (MCP) server that enables MCP clients like Claude Desktop to interact with [protocols.io](https://www.protocols.io), a popular platform for sharing scientific protocols and methods.

## Available Tools

The server provides the following tools that can be used by MCP clients:

### Search and Retrieval
- `search_public_protocols` - Search for public protocols by keyword
- `get_protocol` - Get basic protocol information by ID
- `get_protocol_steps` - Get detailed steps for a specific protocol
- `get_my_protocols` - Retrieve all protocols from your account

### Protocol Creation and Management
- `create_protocol` - Create a new protocol with title and description
- `update_protocol_title` - Update the title of an existing protocol
- `update_protocol_description` - Update the description of an existing protocol

### Step Management
- `set_protocol_steps` - Replace all steps in a protocol
- `add_protocol_step` - Add a single step to the end of a protocol
- `delete_protocol_step` - Delete a specific step from a protocol

## Requirements

- Python 3.10 or higher
- protocols.io account with API credentials
- MCP client (such as Claude Desktop)

### Obtain Protocols.io API Credentials

1. Visit [protocols.io/developers](https://www.protocols.io/developers)
2. Sign in to your account
3. Navigate to the **API Clients** section
4. Click **ADD CLIENT** to create a new application
5. Configure and copy the credentials based on your use case:
   - **Client Access Token**: Copy the generated token for simple authentication (suitable for local STDIO transport)
   - **Client ID** and **Client Secret**: For OAuth 2.0 authentication (suitable for remote HTTP/SSE transport):
     - Set the redirect URL to `{your_mcp_base_url}/auth/callback`
     - Copy the Client ID and Client Secret

## Installation

### Quick Start with Docker

```bash
docker run -d -p 8000:8000 -e PROTOCOLS_IO_CLIENT_ID="your_client_id" -e PROTOCOLS_IO_CLIENT_SECRET="your_client_secret" -e PROTOCOLS_IO_MCP_BASE_URL="https://example.com" --name protocols-io-mcp --restart always ghcr.io/hqn21/protocols-io-mcp:latest
```

The server will be accessible at `http://0.0.0.0:8000/mcp` with HTTP transport

### Install via pip

```bash
pip install protocols-io-mcp
```

#### Set Environment Variables

##### STDIO Transport

```bash
export PROTOCOLS_IO_CLIENT_ACCESS_TOKEN="your_client_access_token"
```

##### HTTP/SSE Transport

```bash
export PROTOCOLS_IO_CLIENT_ID="your_client_id"
export PROTOCOLS_IO_CLIENT_SECRET="your_client_secret"
export PROTOCOLS_IO_MCP_BASE_URL="https://example.com"
```

## Usage

### Command Line Interface

Run the MCP server with various transport options:

```bash
# Default: STDIO transport
protocols-io-mcp

# HTTP transport
protocols-io-mcp --transport http --host 127.0.0.1 --port 8000

# SSE transport
protocols-io-mcp --transport sse --host 127.0.0.1 --port 8000
```

#### CLI Options

```
Usage: protocols-io-mcp [OPTIONS]

  Run the protocols.io MCP server.
    
Options:
  --transport [stdio|http|sse]  Transport protocol to use [default: stdio]
  --host TEXT                   Host to bind to when using http and sse
                                transport [default: 127.0.0.1]
  --port INTEGER                Port to bind to when using http and sse
                                transport [default: 8000]
  --help                        Show this message and exit.
```

### Integration with Claude Desktop

To use this server with Claude Desktop, add the following configuration to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "protocols-io": {
      "command": "protocols-io-mcp",
      "env": {
        "PROTOCOLS_IO_CLIENT_ACCESS_TOKEN": "your_client_access_token"
      }
    }
  }
}
```

#### Troubleshooting

##### MCP protocols-io: spawn protocols-io-mcp ENOENT

This error indicates that Claude Desktop cannot find the `protocols-io-mcp` command. To resolve this:
1. Make sure you have installed the `protocols-io-mcp` package globally using pip.
2. Change the `command` field in your `claude_desktop_config.json` to the full path of the `protocols-io-mcp` executable. You can find the path by running:
   ```bash
   which protocols-io-mcp
   ```
3. Your final configuration should look like:
   ```json
   {
     "mcpServers": {
       "protocols-io": {
         "command": "/full/path/to/protocols-io-mcp",
         "env": {
           "PROTOCOLS_IO_CLIENT_ACCESS_TOKEN": "your_client_access_token"
         }
       }
     }
   }
   ```

## Development

### Running Tests

Ensure you have set the `PROTOCOLS_IO_CLIENT_ACCESS_TOKEN` environment variable, then run:

```bash
pytest
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.