import logging
import requests
from django.conf import settings
from django.shortcuts import render

logger = logging.getLogger(__name__)

def instagram_home(request):
    access_token = settings.INSTAGRAM_ACCESS_TOKEN
    url = f'https://graph.instagram.com/me/media?fields=id,caption,media_type,media_url,thumbnail_url,permalink&access_token={access_token}'

    logger.debug(f"Request URL: {url}")
    
    try:
        response = requests.get(url)
        logger.debug(f"API Response Status Code: {response.status_code}")
        logger.debug(f"API Response Text: {response.text}")
        
        response.raise_for_status()  # This will raise an error for HTTP status codes 4xx/5xx

        if response.status_code == 200:
            data = response.json()
            logger.debug(f"API Response JSON: {data}")
            if 'data' in data and len(data['data']) > 0:
                latest_post = data['data'][0]
                return render(request, 'insta/instagram_home.html', {'latest_post': latest_post})

    except requests.RequestException as e:
        logger.error(f"Request failed: {e}")

    return render(request, 'insta/instagram_home.html', {'latest_post': None})

