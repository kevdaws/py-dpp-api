# DPP Experience API Sandbox - Python Implementation
# Kevin Dawson - 09/23/24

import os
import requests
import json

class Gateway:

    # Initialize gateway instance, defaults to sandbox environment.
    def __init__(self):
        
        self.url = "https://sandbox.api.deluxe.com/dpp/v1/gateway/"
        self.token_url = "https://sandbox.api.deluxe.com/secservices/oauth2/v2/token"
        self.env = 'sandbox'
        self.constants = {
            "grant_type": "client_credentials",
            "scope": "mulesoft_scope"
        }
        self.clientId = os.getenv("CLIENT_ID")
        self.clientSecret = os.getenv("CLIENT_SECRET")
        self.partnerToken = os.getenv("ACCESS_TOKEN")
        self.mediaType = ''
        self.bearerToken = ''

    # Switch between sandbox and production environments.
    def switchEnv(self):
        
        if self.env = 'sandbox':
            self.env = 'production'
            self.url = "https://api.deluxe.com/dpp/v1/gateway/"
            self.token_url = "https://api.deluxe.com/secservices/oauth2/v2/token"
        else:
            self.env = 'sandbox'
            self.url = "https://sandbox.api.deluxe.com/dpp/v1/gateway/"
            self.token_url = "https://sandbox.api.deluxe.com/secservices/oauth2/v2/token"


    # Refreshes bearer token, returns token and expiry time.
    def getBearerToken(self):

        response = requests.post(self.token_url, auth=(self.clientId, self.clientSecret), data=self.constants).json()
        self.bearerToken = response['access_token']
        bearerTokenExpiry = response['tokenExpiry_time']

        return "Bearer token refreshed, expires at " + str(bearerTokenExpiry)

    # Master method for making calls to the API, should not be called invoked directly.
    def performRequest(self):
        
        headers = {
            "Authorization": "Bearer " + self.bearerToken,
            "PartnerToken": self.partnerToken,
            "Content-Type": "application/json"
        }

        if self.mediaType == 'post':
            response = requests.post(self.req_url, data=json.dumps(self.requestData), headers=headers)
        elif self.mediaType == 'patch':
            response = requests.patch(self.req_url, data=json.dumps(self.requestData), headers=headers)
        elif self.mediaType == 'get':
            response = requests.get(self.req_url, headers=headers)
        else:
            return "Unsupported Media Type"
        
        return response.json()

    # Methods for all endpoints as of 09/23/24
    # Requirements outlined in DPP Experience API documentation: https://developer.deluxe.com/s/dpp-api-reference

    def createPayment(self, requestData):

        self.req_url = self.url + 'payments'
        self.requestData = requestData
        self.mediaType = 'post'
        
        return Gateway.performRequest(self)

    def cancelPayment(self, requestData):
        
        self.req_url = self.url + 'payments/cancel'
        self.requestData = requestData
        self.mediaType = 'post'
        
        return Gateway.performRequest(self)

    def completePayment(self, requestData):
        
        self.req_url = self.url + 'payments/complete'
        self.requestData = requestData
        self.mediaType = 'post'
        
        return Gateway.performRequest(self)

    def authorizePayment(self, requestData):
        
        self.req_url = self.url + 'payments/authorize'
        self.requestData = requestData
        self.mediaType = 'post'
        
        return Gateway.performRequest(self)

    def searchPayment(self, requestData):
        
        self.req_url = self.url + 'payments/search'
        self.requestData = requestData
        self.mediaType = 'post'
        
        return Gateway.performRequest(self)

    def refundPayment(self, requestData):
        
        self.req_url = self.url + 'refunds'
        self.requestData = requestData
        self.mediaType = 'post'
        
        return Gateway.performRequest(self)

    def createSubscription(self, requestData):
        
        self.req_url = self.url + 'subscriptions'
        self.requestData = requestData
        self.mediaType = 'post'
        
        return Gateway.performRequest(self)

    def modifySubscription(self, requestData, id):
        
        self.req_url = self.url + 'subscriptions/' + str(id)
        self.requestData = requestData
        self.mediaType = 'patch'
        
        return Gateway.performRequest(self)

    def createPaymentMethod(self, requestData):
        
        self.req_url = self.url + 'paymentmethods'
        self.requestData = requestData
        self.mediaType = 'post'
        
        return Gateway.performRequest(self)

    def modifyPaymentMethod(self, requestData, id):
        
        self.req_url = self.url + 'paymentmethods/' + str(id)
        self.requestData = requestData
        self.mediaType = 'patch'
        
        return Gateway.performRequest(self)

    def generateToken(self, requestData):
        
        self.req_url = self.url + 'paymentmethods/token'
        self.requestData = requestData
        self.mediaType = 'post'
        
        return Gateway.performRequest(self)

    def createCustomer(self, requestData):
        
        self.req_url = self.url + 'customers'
        self.requestData = requestData
        self.mediaType = 'post'

        return Gateway.performRequest(self)

    def getCustomers(self):

        self.req_url = self.url + 'customers'
        self.mediaType = 'get'

        return Gateway.performRequest(self)

    def getCustomer(self, id):

        self.req_url = self.url + 'customers/' + str(id)
        self.mediaType = 'get'

        return Gateway.performRequest(self)

    def modifyCustomer(self, requestData, id):
        
        self.req_url = self.url + 'customers/' + str(id)
        self.requestData = requestData
        self.mediaType = 'patch'

        return Gateway.performRequest(self)

    def closeBatch(self, requestData):

        self.req_url = self.url + 'batches'
        self.requestData = requestData
        self.mediaType = 'post'

        return Gateway.performRequest(self)

    def retrieveReport(self, requestData):

        self.req_url = self.url + 'reports'
        self.requestData = requestData
        self.mediaType = 'post'

        return Gateway.performRequest(self)

    def createPaymentLink(self, requestData):

        self.req_url = self.url + 'paymentlinks'
        self.requestData = requestData
        self.mediaType = 'post'

        return Gateway.performRequest(self)

    def subscribeEvent(self, requestData):

        self.req_url = self.url + 'events/subscribe'
        self.requestData = requestData
        self.mediaType = 'post'

        return Gateway.performRequest(self)

    def unsubscribeEvent(self, requestData):

        self.req_url = self.url + 'events/unsubscribe'
        self.requestData = requestData
        self.mediaType = 'post'

        return Gateway.performRequest(self)

    def testEvent(self, requestData):

        self.req_url = self.url + 'events/test'
        self.requestData = requestData
        self.mediaType = 'post'

        return Gateway.performRequest(self)

    def resendEvent(self, requestData):

        self.req_url = self.url + 'events/resend'
        self.requestData = requestData
        self.mediaType = 'post'

        return Gateway.performRequest(self)

