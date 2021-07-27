from rest_framework.response import Response
from rest_framework.views import APIView

import json
import requests
import datetime

class TrendsView(APIView):
    def get(self, request):
        response = []

        date = datetime.datetime.now().date()
        date_ago = datetime.timedelta(days = 10)
       
        trending_repos = requests.get(f"https://api.github.com/search/repositories?q=created:%3E{date - date_ago}&sort=stars&order=desc&per_page=3").json()
        
        for repo in trending_repos['items']:
            language_count = requests.get(f"https://api.github.com/search/repositories?q=language:{repo['language']}&per_page=0").json()
            response.append({
                "Full Repo. Name": repo['full_name'],
                "Repo. url": repo['html_url'],
                "Language": {
                    "Name": repo['language'],
                    f"Count": language_count['total_count']
                }
            })
        return Response(response)

