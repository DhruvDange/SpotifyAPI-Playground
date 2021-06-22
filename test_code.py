#   Client Credentials Flow
        # auth_param = f"{self.client_id}:{self.client_secret}"
        # auth_param_b64 = base64.b64encode(auth_param.encode())
        # token_url = "https://accounts.spotify.com/api/token"
        # body_param = {
        #     "grant_type": "authorization_code",
        #     "code": ,
        #     "redirect_uri": redirect_uri
        # }
        # headers = {
        #     "Authorization": f"Basic {auth_param_b64.decode()}"
        # }

        # response = requests.post(
        #         token_url,
        #         data = body_param,
        #         headers = headers
        #     )
        # response_json = response.json()
        # self.api_key = response_json['access_token']
        # print(self.api_key)

# x = SpotifyClient(os.getenv("SPOTIFY_CLIENT_ID"), os.getenv("SPOTIFY_CLIENT_SECRET"))

# import webbrowser
# # webbrowser.open('http://127.0.0.1:8000', new=2)

# import requests
# import urllib.request
# webbrowser.open_new_tab(url)