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
# url = "https://accounts.spotify.com/authorize?client_id=f5de6d932e734c108d504646c0e30f88&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A8000&scope=user-read-private%20user-read-email&state=34fFs29kd09"

# response = urllib.request.urlopen("https://accounts.spotify.com/authorize?client_id=f5de6d932e734c108d504646c0e30f88&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A8000&scope=user-read-private%20user-read-email&state=34fFs29kd09")

#  # https://stackoverflow.com/questions/27554994/spotify-api-authentication-with-python
# webbrowser.open_new_tab(url)