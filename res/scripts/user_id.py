import requests
import logging
from fake_useragent     import UserAgent
from .randomness        import number_between

# logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_user_id(__jwt: str) -> str:

    """
    Get the user ID from the PixAI website using the provided JWT token.
    """

    payload = {
        "query": "    query getUserInfo {  me {    ...UserBase    passwordEnabled  }}        fragment UserBase on User {  id  email  emailVerified  username  displayName  createdAt  updatedAt  avatarMedia {    ...MediaBase  }  coverMedia {    ...MediaBase  }  followedByMe  followingMe  followerCount  followingCount  inspiredCount  membership {    membershipId    tier  }  isAdmin}        fragment MediaBase on Media {  id  type  width  height  urls {    variant    url  }  imageType  fileUrl  duration  thumbnailUrl  hlsUrl  size  flag {    ...ModerationFlagBase  }}        fragment ModerationFlagBase on ModerationFlag {  status  isSensitive  isMinors  isRealistic  shouldBlur  isWarned  isAppealable}    ",
        "variables": {}
    }

    headers = {
        "User-Agent": f"{UserAgent().random}",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Authorization": f"Bearer {__jwt}",
        "Content-Type": "application/json",
        "Content-Length": f"{number_between(1, 100)}",
        "Origin": "https://pixai.art",
        "Connection": "keep-alive",
        "Referer": "https://pixai.art/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "TE": "trailers"
    }

    response = requests.post("https://api.pixai.art/graphql", json=payload, headers=headers)
    response.raise_for_status()

    logging.info(f"Successfully got user ID {response.json()['data']['me']['id']}.")

    return response.json()["data"]["me"]["id"]