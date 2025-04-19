import requests

def fetch_random_data_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"] ["username"]
        country = user_data["location"]["country"]
        picture = user_data["picture"]["medium"]

        return username, country, picture
    else:
        raise Exception("Failed to fetch data")
    

def main():
    try:
        username, country, picture = fetch_random_data_freeapi()
        print(f"username: {username} \n country: {country} \n picture: {picture}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()