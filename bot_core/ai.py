"""##########################
# Imports
##########################"""
#from echo.response import echo_response
#from folder.file import echo_response

"""##########################
# Bot Core
##########################"""
#create a function to determine which database to read from
def post_response(text, raw_text):
  message = {}
  
  if 'test' in text:
    message = "Broken I am"

  #elif echo_response(text): 
     #message = echo_response(text)
  
  elif '#yoda' in text:
    echo = raw_text
    message = echo
    
  
  return message

