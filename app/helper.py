import uuid
import random
from dotenv import load_dotenv
import os
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

# load_dotenv()
load_dotenv("/home/100105/100105-DowellApiKey/.env")

SECRET_KEY = str(os.getenv('SECRET_KEY')) 

def generate_uuid():
    return str(uuid.uuid4())

def generate_voucher_code(number):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    otp = ""

    for _ in range(number):
        otp += random.choice(digits)

    return otp


def send_email(email, name, email_body):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = SECRET_KEY
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    subject = "API KEY for Dowell API service"
    html_content = email_body
    sender = {"name": "UX Living Lab", "email": "uxlivinglab@dowellresearch.sg"}
    to = [{"email": email, "name": name}]
    headers = {"Some-Custom-Name": "unique-id-1234"}
    print("---All the data is gathered and ready to send the email---")
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, headers=headers, html_content=html_content, sender=sender, subject=subject)
    
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        api_response_dict = api_response.to_dict()
        print("---The email has been sent successfully!---")
        return True
    except ApiException as e:
        print("---Failed to send the email: {}---".format(str(e)))
        return False




















# def post(self, request):
#         name = request.data.get('name')
#         email = request.data.get('email')
#         userDetails = request.data.get('userDetails')
#         api_services = request.data.get('api_services')
#         workspace_id = request.data.get('workspace_id')
#         print('---Generating API key---')
#         APIKey = generate_uuid()
#         field = {
#             "name": name,
#             "email": email,
#             "APIKey": APIKey,
#             "api_services" : api_services,
#             "workspace_id": workspace_id,
#             "userDetails": userDetails
#         }
#         serializer = ApiKeySerializer(data=field)
#         if serializer.is_valid():
#             serializer.save()
#             print("---All the data are saved to database---")
#             email_body = SendAPIKey.format(name, APIKey, api_services)
#             configuration = sib_api_v3_sdk.Configuration()
#             configuration.api_key['api-key'] = SECRET_KEY
#             api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
#             subject = "API KEY for Dowell API service"
#             html_content = email_body
#             sender = {"name": "UX Living Lab", "email": "uxlivinglab@dowellresearch.sg"}
#             to = [{"email": email, "name": name}]
#             headers = {"Some-Custom-Name": "unique-id-1234"}
#             print("---All the data are gethered and ready to send mail---")
#             send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, headers=headers,html_content=html_content, sender=sender, subject=subject)
#             try:
#                 api_response = api_instance.send_transac_email(send_smtp_email)
#                 api_response_dict = api_response.to_dict()
#                 print("---The mail has been sent ! Happy :D---")
#                 return Response({
#                     "success": True,
#                     "message":f"API key has been sent to your {email} , kindly check your inbox .",
#                 },status=status.HTTP_200_OK)
#             except ApiException as e:
#                 return Response({
#                     "success": False,
#                     "message":"Exception when calling SMTPApi->send_transac_email: %s\n" % e
#                 },status=status.HTTP_400_BAD_REQUEST)
            
#         else:
#             default_errors = serializer.errors
#             new_error = {}
#             for field_name, field_errors in default_errors.items():
#                 new_error[field_name] = field_errors[0]
#             return Response(new_error, status=status.HTTP_400_BAD_REQUEST)