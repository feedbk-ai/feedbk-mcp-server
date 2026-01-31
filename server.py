"""
Minimal FastMCP server for feedbk.ai interview skills.

Serves skills from the ./skills directory via MCP protocol.
Uses streamable-http transport for compatibility with Claude, ChatGPT, and Gemini.
"""

import os
from pathlib import Path
from fastmcp import FastMCP
from fastmcp.server.providers.skills import SkillsDirectoryProvider

# Configuration from environment
HOST = os.getenv("MCP_HOST", "0.0.0.0")
PORT = int(os.getenv("MCP_PORT", "8888"))

# Create the MCP server
mcp = FastMCP("feedbk-skills")

# Skills directory (relative to this file)
SKILLS_DIR = Path(__file__).parent / "skills"

# Add the skills provider
mcp.add_provider(
    SkillsDirectoryProvider(
        roots=SKILLS_DIR,
        supporting_files="resources",  # Expose supporting files as resources
        reload=True,  # Re-scan on each request for development
    )
)


def main():
    """Entry point for the server."""
    mcp.run(transport="streamable-http", host=HOST, port=PORT)


if __name__ == "__main__":
    main()
