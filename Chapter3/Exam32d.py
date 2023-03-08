from bs4 import BeautifulSoup
Text = "<html><head><title>Khoa học dữ liệu</title><style>.call {background-color:black;} </style><script>getit</script></head><body>Là một ngành học<div>đáp ứng xu hướng việc làm trong tương lai.</div></body></html>"
 
# Function to remove tags
def remove_tags(html): 
    soup = BeautifulSoup(html, "html.parser") # parse html content
    for data in soup(['style', 'script']):
        data.decompose() # Remove tags
    return ' '.join(soup.stripped_strings)  # return data by retrieving the tag content
  
# Print the extracted data
print(remove_tags(Text))