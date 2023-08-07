import requests
import json

def get_skype_access_token(client_id, client_secret, tenant_id):
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "resource": "https://graph.microsoft.com"
    }

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        raise Exception("Failed to get access token.")

def get_group_chat_messages(access_token, group_id):
    url = f"https://graph.microsoft.com/v1.0/me/chats/{group_id}/messages"
    headers = {"Authorization": f"Bearer {access_token}"}

    print(access_token)
    response = requests.get(url, headers=headers)
    print(response)
    if response.status_code == 200:
        return response.json().get("value")
    else:
        raise Exception("Failed to get group chat messages.")

if __name__ == "__main__":
    #Replace these values with your own credentials and group ID
    client_id = "aa0c8e2e-8fae-4190-8da6-b1f8e4c109f0"
    client_secret = "KCK8Q~521g8Ks8YeLDlo9k-F6Wt5MrPXxzxdnb4G"
    tenant_id = "f8cdef31-a31e-4b4a-93e4-5f571e91255a"
    group_id = "r7zyweAEAcbD"

    # client_id = "aa0c8e2e-8fae-4190-8da6-b1f8e4c109f0"
    # client_secret = "KCK8Q~521g8Ks8YeLDlo9k-F6Wt5MrPXxzxdnb4G"
    # tenant_id = "f8cdef31-a31e-4b4a-93e4-5f571e91255a"
    # group_id = "r7zyweAEAcbD"

    # client_id = "aa0c8e2e-8fae-4190-8da6-b1f8e4c109f0"
    # client_secret = "f276143d-2f34-4380-bd64-4ceaa338e142"
    # tenant_id = "f8cdef31-a31e-4b4a-93e4-5f571e91255a"
    # group_id = "r7zyweAEAcbD"

    access_token = get_skype_access_token(client_id, client_secret, tenant_id)

    try:
        messages = get_group_chat_messages(access_token, group_id)
        with open("output.txt", "w", encoding="utf-8") as file:
            for message in messages:
                file.write(f"{message['from']['user']['displayName']}: {message['body']['content']}\n")
        print("Messages saved successfully.")
    except Exception as e:
        print("Error:", e)
