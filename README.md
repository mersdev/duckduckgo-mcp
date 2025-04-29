# DuckDuckGo Search MCP

A Python-based MCP (Machine Comprehension Protocol) server that provides specialized search functionality using DuckDuckGo's search engine. This implementation offers three distinct search tools:

- GitHub Code Search
- Malaysia News Search (NST)
- Azure Documentation Search

## Features

### 1. GitHub Code Search
Search for code examples and repositories on GitHub related to specific topics.
- Automatically filters results to GitHub domain
- Returns top 5 relevant results with titles, links, and descriptions

### 2. Malaysia News Search
Search for local news articles from New Straits Times (NST) Malaysia.
- Specifically targets nst.com.my domain
- Includes results from the past year
- Returns top 5 news articles with titles, links, and descriptions

### 3. Azure Documentation Search
Search for official Azure documentation on Microsoft Learn.
- Focuses on Azure-specific documentation
- Returns top 5 relevant documentation pages with titles, links, and descriptions

## Installation

1. Ensure you have Python 3.11 or later installed

2. Clone the repository:
```bash
git clone <repository-url>
cd duckduckgo-mcp
```

3. Install dependencies using pip:
```bash
pip install -r requirements.txt
```

Required dependencies:
- duckduckgo-search>=4.1.1
- mcp[cli]>=1.6.0

## Usage

1. Start the MCP server:
```bash
python search.py
```

2. The server will initialize with three available search tools:
   - `search_github_code(topic: str)`
   - `search_malaysia_news(topic: str)`
   - `search_azure_docs(topic: str)`

3. Each search function accepts a topic string and returns formatted results including titles, links, and descriptions.

## Example Usage

```python
# Search for Python asyncio code examples on GitHub
search_github_code("Python asyncio")

# Search for technology news in Malaysia
search_malaysia_news("technology startup")

# Search for Azure Kubernetes Service documentation
search_azure_docs("AKS cluster creation")
```

## Project Setup

### Using uv Package Manager (Recommended)

1. If you haven't installed uv yet, install it first:
```bash
pip install uv
```

2. Create a new MCP project:
```bash
uv init duckduckgo-mcp
cd duckduckgo-mcp
```

3. Add MCP to your project dependencies:
```bash
uv add "mcp[cli]"
```

4. Run the MCP server:
```bash
uv run mcp
```

### Using pip (Alternative)

Alternatively, you can use pip to install dependencies:

```bash
pip install "mcp[cli]"
```

## Development

### Basic Development
The project uses FastMCP for creating the MCP server and DuckDuckGo Search API for performing searches. Each search function is decorated with `@mcp.tool()` to make it available as an MCP tool.

### Development Mode
The fastest way to test and debug your server is with the MCP Inspector:

```bash
# Run server in development mode
mcp dev search.py --with duckduckgo-search
```

Development mode provides:
- Interactive debugging interface
- Hot reload for code changes
- Real-time tool testing
- Dependency management
- Local code mounting for development

### Cline Extension Integration

To integrate the DuckDuckGo Search MCP with CLine extension, add the following configuration to your CLine settings:

```json
"duckduckgo-search": {
    "autoApprove": [],
    "disabled": false,
    "timeout": 60,
    "command": "uv",
    "args": [
        "run",
        "--with",
        "mcp[cli]",
        "--with",
        "duckduckgo-search",
        "mcp",
        "run",
        "/path/to/example/search.py"
    ],
    "transportType": "stdio"
}
```

This configuration:
- Uses `uv` package manager to run the MCP server
- Sets a 60-second timeout for operations
- Automatically loads required dependencies (mcp[cli] and duckduckgo-search)
- Configures stdio transport for communication
- Specifies the path to your search.py implementation