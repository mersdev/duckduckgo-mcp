from mcp.server.fastmcp import FastMCP
from duckduckgo_search import DDGS

# Create an MCP server
mcp = FastMCP("DuckDuckGo Search")

# Initialize DuckDuckGo search client
ddgs = DDGS()

@mcp.tool()
def search_github_code(topic: str) -> str:
    """
    Search for code related to a specific topic on GitHub using DuckDuckGo.

    Args:
        topic (str): The topic to search for code examples.

    Returns:
        str: A formatted string containing the search results.
    """
    # Use site:github.com to restrict search to GitHub
    query = f"site:github.com {topic} code"
    results = ddgs.text(query, max_results=5)
    
    if not results:
        return "No GitHub code results found."
    
    formatted_results = "GitHub Code Search Results:\n\n"
    for result in results:
        formatted_results += f"Title: {result['title']}\n"
        formatted_results += f"Link: {result['href']}\n"
        formatted_results += f"Description: {result['body']}\n\n"
    
    return formatted_results


@mcp.tool()
def search_malaysia_news(topic: str) -> str:
    """
    Search for Malaysia local news from NST website using DuckDuckGo.

    Args:
        topic (str): The topic to search for in Malaysia local news.

    Returns:
        str: A formatted string containing the NST news search results.
    """
    query = f"site:nst.com.my {topic}"
    results = ddgs.text(query, timelimit="y", max_results=5)
    
    if not results:
        return "No Malaysia news results found."
    
    formatted_results = "Malaysia Local News Results (NST):\n\n"
    for result in results:
        formatted_results += f"Title: {result['title']}\n"
        formatted_results += f"Link: {result['href']}\n"
        formatted_results += f"Description: {result['body']}\n\n"
    
    return formatted_results

@mcp.tool()
def search_azure_docs(topic: str) -> str:
    """
    Search for Azure resource documentation on learn.microsoft.com using DuckDuckGo.

    Args:
        topic (str): The Azure resource topic to search for documentation.

    Returns:
        str: A formatted string containing the Azure documentation search results.
    """
    query = f"site:learn.microsoft.com/en-us/azure {topic}"
    results = ddgs.text(query, max_results=5)
    
    if not results:
        return "No Azure documentation results found."
    
    formatted_results = "Azure Documentation Search Results:\n\n"
    for result in results:
        formatted_results += f"Title: {result['title']}\n"
        formatted_results += f"Link: {result['href']}\n"
        formatted_results += f"Description: {result['body']}\n\n"
    
    return formatted_results