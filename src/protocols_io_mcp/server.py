import os
import importlib
from fastmcp import FastMCP
from fastmcp.server.auth import OAuthProxy
from fastmcp.server.auth.providers.debug import DebugTokenVerifier
from dotenv import load_dotenv
load_dotenv()

auth = None
if {"PROTOCOLS_IO_CLIENT_ID", "PROTOCOLS_IO_CLIENT_SECRET", "PROTOCOLS_IO_MCP_BASE_URL"}.issubset(os.environ):
    auth = OAuthProxy(
        upstream_authorization_endpoint="https://www.protocols.io/api/v3/oauth/authorize",
        upstream_token_endpoint="https://www.protocols.io/api/v3/oauth/token",
        upstream_client_id=os.getenv("PROTOCOLS_IO_CLIENT_ID"),
        upstream_client_secret=os.getenv("PROTOCOLS_IO_CLIENT_SECRET"),
        token_verifier=DebugTokenVerifier(),
        base_url=os.getenv("PROTOCOLS_IO_MCP_BASE_URL"),
        valid_scopes=["readwrite"],
        forward_pkce=False,
        token_endpoint_auth_method="client_secret_post"
    )
mcp = FastMCP(
    name="protocols-io-mcp",
    instructions="""
        This server helps you interact with data from protocols.io.
    """,
    auth=auth
)
importlib.import_module('protocols_io_mcp.tools')