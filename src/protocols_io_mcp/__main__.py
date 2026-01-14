import click
from protocols_io_mcp.server import mcp
from protocols_io_mcp.utils import config

@click.command()
@click.option("--transport", default="stdio", type=click.Choice(['stdio', 'http', 'sse']), help="Transport protocol to use [default: stdio]")
@click.option("--host", default="127.0.0.1", help="Host to bind to when using http and sse transport [default: 127.0.0.1]")
@click.option("--port", default=8000, help="Port to bind to when using http and sse transport [default: 8000]")
def main(transport: str, host: str, port: int):
    """Run the protocols.io MCP server."""
    config.TRANSPORT_TYPE = transport
    print("Starting protocols.io MCP server...")
    if transport == "stdio":
        mcp.run(transport=transport)
    else:
        mcp.run(transport=transport, host=host, port=port)

if __name__ == "__main__":
    main()