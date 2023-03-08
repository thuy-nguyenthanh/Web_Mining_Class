from bs4 import BeautifulSoup
 
# HTML Document
HTML_DOC = """
              <html>
                <head>
                    <title> Geeksforgeeks </title>
                    <style>.call {background-color:black;} </style>
                    <script>getit</script>
                </head>
                <body>
                    is a
                    <div>Computer Science portal.</div>
                </body>
              </html>
            """
 
# Function to remove tags
def remove_tags(html): 
    # parse html content
    soup = BeautifulSoup(html, "html.parser") 
    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose() 
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)
  
# Print the extracted data
print(remove_tags(HTML_DOC))