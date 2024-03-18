import requests
import json

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

with open("dubaidentist.json", "r") as f:
    leads = f.readlines()
# with open("montdent.txt", "r") as f:
#     leads = f.readlines()

message = "مرحبًا! 👋 أنا أحمد من خدمات الويب الكويتية (https://kuwaitwebservices.com). نحن متخصصون في إنشاء مواقع ويب عصرية وذات محتوى عالٍ لعيادات الأسنان مثل عيادتكم. تركز مواقعنا على التصميم النظيف لتعزيز الاحترافية وتحقيق تصنيف متميز على جوجل. هل ترغبون في تدقيق موقع الويب مجانًا أو مناقشة موقع مصمم خصيصًا لعيادتكم؟ أخبروني! يمكنكم أيضًا مراسلتي عبر البريد الإلكتروني على info@kuwaitwebservices.com."

for lead in leads:
    lead = json.loads(lead)
    if lead.get("telephone") is None:
        continue
    # if lead == "NaN":
    #     continue
    # print(lead.get("telephone"))
    params = {
        # "phone": f"{lead.strip()[1:].replace(' ', '').replace('-', '')}",
        "phone": f"{lead.get('telephone').strip()[1:].replace(' ', '').replace('-', '')}",
        "session": "default",
    }
    # print(params.get("phone"))
    json_data = {
        # "chatId": f"{lead[1:].strip().replace(' ', '').replace('-', '')}",
        "chatId": f"{lead.get('telephone')[1:].strip().replace(' ', '').replace('-', '')}",
        "text": f"{message}",
        "session": "default",
    }
    print(json_data.get("chatId"))

    response = requests.get(
        "http://[::1]:3000/api/contacts/check-exists", params=params, headers=headers
    )

    if response.json().get("numberExists") is True:
        # response = requests.post(
        #     "http://[::1]:3000/api/sendText", headers=headers, json=json_data
        # )
        print("Number exists")
    else:
        print("Nope, number does not exist")
        continue

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
# data = '{\n  "chatId": "233243265106",\n  "text": "Bulk text",\n  "session": "default"\n}'
# response = requests.post('http://[::1]:3000/api/sendText', headers=headers, data=data)
