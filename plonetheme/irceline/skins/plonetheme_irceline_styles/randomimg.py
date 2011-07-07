## Script (Python) "randomimg"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=randomimg
##
from random import choice
# Import a standard function, and get the HTML request and response objects.
from Products.PythonScripts.standard import html_quote

request = container.REQUEST
RESPONSE = request.RESPONSE
RESPONSE.setHeader('Content-Type','image/jpg')

# Get list of images in randomimages folder
images = context.randomimages.getFolderContents({'portal_type':'Image'}) 

# Return a random choice of one of the images
return choice(images).getObject().data
