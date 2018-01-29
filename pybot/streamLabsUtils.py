import requests, re
import cfg

"""def getAccessCodeFromAuth(authcode):
    url = "https://streamlabs.com/api/v1.0/token" # API Get Stuff
    grant_type = "authorization_code"
    querystring = {"grant_type":grant_type,"client_id":cfg.STREAMLABSID,"client_secret":cfg.CLIENTSECRET,"redirect_uri":cfg.STREAMLABSREDIRECTURI,"code":authcode}
    response = requests.request("POST", url, data=querystring)
    accesscode = response.text[17:57]
    refreshcode = response.text[116:156]
    f = open('codeBackup.txt','w') # Save the Refresh Code to a file to use next time this command is triggered
    f.write(refreshcode)
    f.close() """

def getAccessCode():
    f = open('codeBackup.txt','r') # Get the old Refresh Code from the file we saved
    refresh_token = f.read()
    f.close()

    url = "https://streamlabs.com/api/v1.0/token" # API Get Stuff
    grant_type = "refresh_token"
    querystring = {"grant_type":grant_type,"client_id":cfg.STREAMLABSID,"client_secret":cfg.CLIENTSECRET,"redirect_uri":cfg.STREAMLABSREDIRECTURI,"refresh_token":refresh_token}
    response = requests.request("POST", url, data=querystring)

    accesscode = response.text[17:57]
    refreshcode = response.text[116:156]

    f = open('codeBackup.txt','w') # Save the Refresh Code to a file to use next time this command is triggered
    f.write(refreshcode)
    f.close()

    return(accesscode) # Return the Access_Token

def customAlert(message, alerttype):
    url = "https://streamlabs.com/api/v1.0/alerts"
    access_token = getAccessCode()
    querystring = {"access_token":access_token,"type":alerttype,"message":message}
    response = requests.request("POST", url, data=querystring)
    print(response.text)

def testAlert(alerttype):
    url = "https://streamlabs.com/api/v1.0/alerts/send_test_alert"
    access_token = getAccessCode()
    querystring = {"access_token":access_token,"type":alerttype}
    response = requests.request("POST", url, data=querystring)
    print(response.text)

def getPoints(username):
    url = "https://streamlabs.com/api/v1.0/points"
    access_token = getAccessCode()
    querystring = {"access_token":access_token,"username":username,"channel":"octamouselabs"}
    response = requests.request("GET", url, params=querystring)
    print(response.text)

def createDonation(name, amount):
    url = "https://streamlabs.com/api/v1.0/donations"
    access_token = getAccessCode()
    querystring = {"access_token":access_token,"name":name,"identifier":"Test","amount":amount,"currency":"USD"}
    response = requests.request("POST", url, data=querystring)
    print(response.text)

def getDonations():
    url = "https://streamlabs.com/api/v1.0/donations"
    access_token = getAccessCode()
    querystring = {"access_token":access_token}
    response = requests.request("GET", url, params=querystring)
    print(response.text)
"""    for donation in response:
        name = ['data'][donation]['name']
        message = ['data'][donation]['message']
        amount = ['data'][donation]['amount']
        f = open('DonationLog.txt','a')
        f.write("Name: "+name+"\nMessage: "+message+"\nAmount: "+amount)
        f.close() """

def getSocketCode():
    url = "https://streamlabs.com/api/v1.0/socket/token"
    access_token = getAccessCode()
    querystring = {"access_token":access_token}
    response = requests.request("GET", url, params=querystring)
    print(response.text)
