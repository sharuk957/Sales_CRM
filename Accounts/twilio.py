
from twilio.rest import Client
from django.conf import settings

account_sid = settings.TWILIO_SID
auth_token = settings.TWILIO_TOKEN
serviceid = settings.TWILIO_SERVICES

client = Client(account_sid, auth_token)
def service_id_generator():
    service = client.verify.services.create(friendly_name='Hi, otp for salesCRM login is')
    return service

def send_sms(to_):
    print(serviceid,account_sid,auth_token)
    verification = client.verify \
                        .services(serviceid) \
                        .verifications \
                        .create(to=to_, channel='sms')
    print(verification.status)

    

def checking(to_,otp):

    verification_check = client.verify \
                            .services(serviceid) \
                            .verification_checks \
                            .create(to=to_, code=otp)
    return verification_check.status
