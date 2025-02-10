# DPP Experience API - Python Implementation
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
        self.accessToken = ''
        self.mediaType = ''
        self.bearerToken = ''

    # Switch between sandbox and production environments.
    def switchEnv(self):
        
        if self.env == 'sandbox':
            self.env = 'production'
            self.url = "https://api.deluxe.com/dpp/v1/gateway/"
            self.token_url = "https://api.deluxe.com/secservices/oauth2/v2/token"
        else:
            self.env = 'sandbox'
            self.url = "https://sandbox.api.deluxe.com/dpp/v1/gateway/"
            self.token_url = "https://sandbox.api.deluxe.com/secservices/oauth2/v2/token"


    # Refreshes bearer token and expiry, must be called prior to making a request.
    def getBearerToken(self, clientId, clientSecret):

        body = {
            "grant_type": "client_credentials",
            "scope": "mulesoft_scope"
        }
        
        response = requests.post(self.token_url, auth=(clientId, clientSecret), data=body)

        try:
            response.raise_for_status()
            self.bearerToken = response.json()['access_token']
            self.bearerTokenExpiry = response.json()['tokenExpiry_time']
        
        except requests.exceptions.HTTPError as err:
            return err

    # Master method for making calls to the API, should not be called invoked directly.
    def performRequest(self):
        
        headers = {
            "Authorization": "Bearer " + self.bearerToken,
            "PartnerToken": self.accessToken,
            "Content-Type": "application/json",
        }

            if self.mediaType == 'post':
                response = requests.post(self.req_url, data=json.dumps(self.requestData), headers=headers)
            elif self.mediaType == 'patch':
                response = requests.patch(self.req_url, data=json.dumps(self.requestData), headers=headers)
            elif self.mediaType == 'get':
                response = requests.get(self.req_url, headers=headers)
            else:
                return "Unsupported operation"

        # Reset mediaType
        self.mediaType = ''
        
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            return err

    # Methods for all endpoints as of 09/23/24
    # Requirements outlined in DPP Experience API documentation: https://developer.deluxe.com/s/dpp-api-reference

    def createPayment(self, accessToken, requestData):

        self.req_url = self.url + 'payments'
        self.requestData = requestData
        self.accessToken = accessToken
        self.mediaType = 'post'
        
        return Gateway.performRequest(self)

    def cancelPayment(self, accessToken, requestData):
        
        self.req_url = self.url + 'payments/cancel'
        self.requestData = requestData
        self.accessToken = accessToken
        self.mediaType = 'post'
        
        return Gateway.performRequest(self)

    def completePayment(self, accessToken, requestData):
        
        self.req_url = self.url + 'payments/complete'
        self.requestData = requestData
        self.accessToken = accessToken
        self.mediaType = 'post'
        
        return Gateway.performRequest(self)

    def authorizePayment(self, accessToken, requestData):
        
        self.req_url = self.url + 'payments/authorize'
        self.requestData = requestData
        self.accessToken = accessToken
        self.mediaType = 'post'
        
        return Gateway.performRequest(self)

    def searchPayment(self, accessToken, requestData):
        
        self.req_url = self.url + 'payments/search'
        self.requestData = requestData
        self.accessToken = accessToken
        self.mediaType = 'post'
        
        return Gateway.performRequest(self)

    def refundPayment(self, accessToken, requestData):
        
        self.req_url = self.url + 'refunds'
        self.requestData = requestData
        self.accessToken = accessToken
        self.mediaType = 'post'
        
        return Gateway.performRequest(self)

    def createSubscription(self, accessToken, requestData):
        
        self.req_url = self.url + 'subscriptions'
        self.requestData = requestData
        self.accessToken = accessToken
        self.mediaType = 'post'
        
        return Gateway.performRequest(self)

    def modifySubscription(self, accessToken, requestData, id):
        
        self.req_url = self.url + 'subscriptions/' + str(id)
        self.requestData = requestData
        self.accessToken = accessToken
        self.mediaType = 'patch'
        
        return Gateway.performRequest(self)

    def createPaymentMethod(self, accessToken, requestData):
        
        self.req_url = self.url + 'paymentmethods'
        self.requestData = requestData
        self.accessToken = accessToken
        self.mediaType = 'post'
        
        return Gateway.performRequest(self)

    def modifyPaymentMethod(self, accessToken, requestData, id):
        
        self.req_url = self.url + 'paymentmethods/' + str(id)
        self.requestData = requestData
        self.accessToken = accessToken
        self.mediaType = 'patch'
        
        return Gateway.performRequest(self)

    def generateToken(self, accessToken, requestData):
        
        self.req_url = self.url + 'paymentmethods/token'
        self.requestData = requestData
        self.accessToken = accessToken
        self.mediaType = 'post'
        
        return Gateway.performRequest(self)

    def createCustomer(self, accessToken, requestData):
        
        self.req_url = self.url + 'customers'
        self.requestData = requestData
        self.accessToken = accessToken
        self.mediaType = 'post'

        return Gateway.performRequest(self)

    def getCustomers(self, accessToken):

        self.req_url = self.url + 'customers'
        self.accessToken = accessToken
        self.mediaType = 'get'

        return Gateway.performRequest(self)

    def getCustomer(self, accessToken, id):

        self.req_url = self.url + 'customers/' + str(id)
        self.accessToken = accessToken
        self.mediaType = 'get'

        return Gateway.performRequest(self)

    def modifyCustomer(self, accessToken, requestData, id):
        
        self.req_url = self.url + 'customers/' + str(id)
        self.requestData = requestData
        self.accessToken = accessToken
        self.mediaType = 'patch'

        return Gateway.performRequest(self)

    def closeBatch(self, accessToken, requestData):

        self.req_url = self.url + 'batches'
        self.requestData = requestData
        self.accessToken = accessToken
        self.mediaType = 'post'

        return Gateway.performRequest(self)

    def retrieveReport(self, accessToken, requestData):

        self.req_url = self.url + 'reports'
        self.requestData = requestData
        self.accessToken = accessToken
        self.mediaType = 'post'

        return Gateway.performRequest(self)

    def createPaymentLink(self, accessToken, requestData):

        self.req_url = self.url + 'paymentlinks'
        self.requestData = requestData
        self.accessToken = accessToken
        self.mediaType = 'post'

        return Gateway.performRequest(self)

    def subscribeEvent(self, accessToken, requestData):

        self.req_url = self.url + 'events/subscribe'
        self.requestData = requestData
        self.accessToken = accessToken
        self.mediaType = 'post'

        return Gateway.performRequest(self)

    def unsubscribeEvent(self, accessToken, requestData):

        self.req_url = self.url + 'events/unsubscribe'
        self.requestData = requestData
        self.accessToken = accessToken
        self.mediaType = 'post'

        return Gateway.performRequest(self)

    def testEvent(self, accessToken, requestData):

        self.req_url = self.url + 'events/test'
        self.requestData = requestData
        self.accessToken = accessToken
        self.mediaType = 'post'

        return Gateway.performRequest(self)

    def resendEvent(self, accessToken, requestData):

        self.req_url = self.url + 'events/resend'
        self.requestData = requestData
        self.accessToken = accessToken
        self.mediaType = 'post'

        return Gateway.performRequest(self)
