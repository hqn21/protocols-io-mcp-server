import os
import click
from protocols_io_mcp.server import mcp
from protocols_io_mcp.utils import config
from dotenv import load_dotenv
load_dotenv()

@click.command()
@click.option("--transport", default="stdio", type=click.Choice(['stdio', 'http', 'sse']), help="Transport protocol to use [default: stdio]")
@click.option("--host", default="127.0.0.1", help="Host to bind to when using http and sse transport [default: 127.0.0.1]")
@click.option("--port", default=8000, help="Port to bind to when using http and sse transport [default: 8000]")
def main(transport: str, host: str, port: int):
    """Run the protocols.io MCP server."""
    config.TRANSPORT_TYPE = transport
    print("Starting protocols.io MCP server...")
    if transport == "stdio":
        if not {"PROTOCOLS_IO_CLIENT_ACCESS_TOKEN"}.issubset(os.environ):
            raise ValueError("Missing required environment variable for stdio transport: PROTOCOLS_IO_CLIENT_ACCESS_TOKEN")
        mcp.run(transport=transport)
    else:
        required = {"PROTOCOLS_IO_CLIENT_ID", "PROTOCOLS_IO_CLIENT_SECRET", "PROTOCOLS_IO_MCP_BASE_URL"}
        missing = required - os.environ.keys()
        if missing:
            raise ValueError(f"Missing required environment variables for {transport} transport: {', '.join(missing)}")
        mcp.run(transport=transport, host=host, port=port)

if __name__ == "__main__":
    main()