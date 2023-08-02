import requests
import pydig

# Ask to input domain. With Domainify app, might be a different method for input.
domain = input('Enter the domain name: ').lower()

# Function to get the generated UUID from uuidgenerator.net
def gen_uuid():
    uuid = requests.get('https://www.uuidgenerator.net/api/version1').text
    return uuid

# Uses pydig.query to get the TXT values of the domain and comparing it with the generated UUID. It has 1-2 minutes delay compared to Google Admin Toolbox. Using OpenSRS API may be better and faster.
def ver_txt(domain, uuid):
    txt = str(pydig.query('shopify-verify.' + domain, 'TXT'))
   
    if  uuid in txt:
         print(f'The UUID was found on the domain, this domain is verified! Go to: https://toolbox.googleapps.com/apps/dig/#TXT/shopify-verify.{domain} , to take a screenshot.')
    else:
        print(f'This domain is not verified! Please have the merchant add the {uuid} as a TXT value or try verifying again in a few minutes. You can check: https://toolbox.googleapps.com/apps/dig/#TXT/shopify-verify.{domain}' )
    return txt


uuid = gen_uuid()

# Test domain and uuid variable
#domain = 'karlveloso.com'
#uuid = '13738748-ece2-11ec-8ea0-0242ac120002'

print(f'This is your UUID: {uuid}')


# Prompt before verifying TXT
verify = input('Did the merchant add the UUID? (Y/N) ').lower()

if verify == 'y' or verify =='yes':
     ver_txt(domain, uuid)
else:
    print('Please have the merchant add the UUID as a TXT value in the domain and try again.')
