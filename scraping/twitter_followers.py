# This script is used to scrape the followers of a Twitter account.
# The script takes the account name as an argument and prints the followers of the account.
# run it like this, python3 twitter_followers.py {account_name} eg. python3 twitter_followers.py sequoia


import json
import sys
import requests

cookies = {
    "guest_id": "v1%3A171353782335253191",
    "kdt": "3ZKSjPiskgZ4C9RZmrOjul4XiUruIrWD3I6avXP2",
    "auth_token": "b27ab02b6fbcf00d1db8e7bf1a319d973084924b",
    "ct0": "59f68f861261d3437d0df807144367ee1032b72c3cdcff474f5eb3509a96fba0113ee7b870bb9eb2abd3e5c3b44500280c6b6ac6821ac1cd2089a1ccdd70447af2b8920a605f7a2bc149b5c9e47af494",
    "twid": "u%3D1663936852208898049",
    "att": "1-P5yldr2dC7Nx93mTtDiwLRPFsWs54e2aMykw99LD",
    "lang": "en",
    "d_prefs": "MjoxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw",
    "guest_id_marketing": "v1%3A171353782335253191",
    "guest_id_ads": "v1%3A171353782335253191",
    "personalization_id": '"v1_RpDwUXnw9jMd+cKgglNEGQ=="',
}

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.7",
    "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
    "content-type": "application/json",
    # 'cookie': 'guest_id=v1%3A171353782335253191; kdt=3ZKSjPiskgZ4C9RZmrOjul4XiUruIrWD3I6avXP2; auth_token=b27ab02b6fbcf00d1db8e7bf1a319d973084924b; ct0=59f68f861261d3437d0df807144367ee1032b72c3cdcff474f5eb3509a96fba0113ee7b870bb9eb2abd3e5c3b44500280c6b6ac6821ac1cd2089a1ccdd70447af2b8920a605f7a2bc149b5c9e47af494; twid=u%3D1663936852208898049; att=1-P5yldr2dC7Nx93mTtDiwLRPFsWs54e2aMykw99LD; lang=en; d_prefs=MjoxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; guest_id_marketing=v1%3A171353782335253191; guest_id_ads=v1%3A171353782335253191; personalization_id="v1_RpDwUXnw9jMd+cKgglNEGQ=="',
    "priority": "u=1, i",
    "referer": "https://twitter.com/sequoia/following",
    "sec-ch-ua": '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "x-client-transaction-id": "2O/jZAthe9nlWq6f0l4L39FhdetMLOYlN/miwJ+IhZ4CCL/Gi6hqtiuxMKZkXiAqDy2BANlC0dO4KNXCAWKXiCxMQgz42w",
    "x-client-uuid": "8fec3bd6-a49e-41b8-bb72-d0bd8ccc58b4",
    "x-csrf-token": "59f68f861261d3437d0df807144367ee1032b72c3cdcff474f5eb3509a96fba0113ee7b870bb9eb2abd3e5c3b44500280c6b6ac6821ac1cd2089a1ccdd70447af2b8920a605f7a2bc149b5c9e47af494",
    "x-twitter-active-user": "yes",
    "x-twitter-auth-type": "OAuth2Session",
    "x-twitter-client-language": "en",
}

acc_name_arg = sys.argv[1]

json_str = '{"variables": "{\\"screen_name\\":\\"sequoia\\",\\"withSafetyModeUserFields\\":true}"}'
acc_data = json.loads(json_str)
variables = json.loads(acc_data["variables"])
new_acc = acc_name_arg
variables["screen_name"] = new_acc
acc_data["variables"] = json.dumps(variables)
updated_json_str = json.dumps(
    acc_data,
)
data = json.loads(updated_json_str)
variables_str = data["variables"].replace('\\"', '"')
print(variables_str)
dis_name = json.loads(variables_str)

acc_response = requests.get(
    "https://twitter.com/i/api/graphql/qW5u-DAuXpMEG0zA1F7UGQ/UserByScreenName",
    params={
        "variables": f"{variables_str}",
        "features": '{"hidden_profile_likes_enabled":true,"hidden_profile_subscriptions_enabled":true,"rweb_tipjar_consumption_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"subscriptions_verification_info_is_identity_verified_enabled":true,"subscriptions_verification_info_verified_since_enabled":true,"highlights_tweets_tab_ui_enabled":true,"responsive_web_twitter_article_notes_tab_enabled":true,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}',
        "fieldToggles": '{"withAuxiliaryUserLabels":false}',
    },
    cookies=cookies,
    headers=headers,
)

acc_data = json.loads(acc_response.text)

# Navigate through the dictionary to get the required information
name = acc_data["data"]["user"]["result"]["legacy"]["name"]
followers_count = acc_data["data"]["user"]["result"]["legacy"]["followers_count"]
friends_count = acc_data["data"]["user"]["result"]["legacy"]["friends_count"]
request_id = acc_data["data"]["user"]["result"]["rest_id"]
# print(request_id)


json_str = '{"variables": "{\\"userId\\":\\"64844802\\",\\"count\\":20,\\"includePromotedContent\\":false}"}'
acc_data = json.loads(json_str)
variables = json.loads(acc_data["variables"])
new_user_id = request_id
variables["userId"] = new_user_id
acc_data["variables"] = json.dumps(variables)
updated_json_str = json.dumps(
    acc_data,
)
data = json.loads(updated_json_str)
variables_str = data["variables"].replace('\\"', '"')


params = {
    "variables": f"{variables_str}",
    "features": '{"rweb_tipjar_consumption_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"communities_web_enable_tweet_community_results_fetch":true,"c9s_tweet_anatomy_moderator_badge_enabled":true,"articles_preview_enabled":false,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":true,"tweet_awards_web_tipping_enabled":false,"creator_subscriptions_quote_tweet_preview_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"tweet_with_visibility_results_prefer_gql_media_interstitial_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_enhance_cards_enabled":false}',
}

response = requests.get(
    "https://twitter.com/i/api/graphql/ZxuX4tC6kWz9M8pe1i-Gdg/Following",
    params=params,
    cookies=cookies,
    headers=headers,
)

# json_data = json.loads(response.text)

data = json.loads(response.text)
# print(data)
# Extract instructions from the JSON data
instructions = data["data"]["user"]["result"]["timeline"]["timeline"]["instructions"]

print(
    f"Account name: {dis_name['screen_name']} | followers: {followers_count} | following: {friends_count}"
)
# print("-------------------------")
# print("⬇️ following ⬇️")
# print("-------------------------")

# Loop through the instructions and find 'TimelineAddEntries' type
for instruction in instructions:
    if instruction["type"] == "TimelineAddEntries":
        # Extract the entries from the instruction
        entries = instruction["entries"]
        # Loop through each entry and extract required information
        for entry in entries:
            content = entry["content"]
            try:
                user_result = content["itemContent"]["user_results"]["result"]
            except:
                continue
            name = user_result["legacy"]["name"]
            followers_count = user_result["legacy"]["followers_count"]
            friends_count = user_result["legacy"]["friends_count"]
            # Print extracted information
            # print(f"Name: {name}")
            # print(f"Followers: {followers_count}")
            # print(f"Following: {friends_count}")
            # print("-------------------------")
            full_data = {
                "follower_name": name,
                "followers_count": followers_count,
                "following_count": friends_count,
            }
            print(full_data)
