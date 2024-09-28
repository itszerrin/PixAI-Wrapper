from secrets        import randbelow
from fake_useragent import UserAgent
import logging
import requests

# logging configuration
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def claim_daily_credits(jwt: str) -> None:
    """
    Log into the PixAI website and claim the daily credits.

    :param jwt: Your auth token.

    :return: None
    """

    url: str = "https://api.pixai.art/graphql"

    headers = {
        "Host": "api.pixai.art",
        "User-Agent": UserAgent().random.__repr__(),
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Authorization": "Bearer " + jwt,
        "Content-Type": "application/json",
        "Content-Length": f"{randbelow(80)}",
        "Origin": "https://pixai.art",
        "DNT": "1",
        "Sec-GPC": "1",
        "Connection": "keep-alive",
        "Referer": "https://pixai.art/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Priority": "u=0",
        "TE": "trailers"
    }

    data = {
        "query": "\n    mutation dailyClaimQuota {\n  dailyClaimQuota\n}\n    "
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    # check inside the json if there's an error because the status code is still 200
    try:
        if response.json()['errors'][0]['extensions']['exception']['status'] == 403:
            logging.error(f"Failed to claim daily credits. Reason: {response.json()['errors'][0]['message']}")
    except KeyError:
        logging.info(f"Claimed daily credits. Response: {response.json()}")

    return None

