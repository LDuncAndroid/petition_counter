import requests

url = "https://petition.parliament.uk/petitions/180642.json"


def main():
    response = requests.request("GET", url)
    outside_gb_count = 0
    print(response.text)
    for country in response.json()['data']['attributes']['signatures_by_country']:
        # If the country is not Great Britain
        if country['code'] != 'GB':
            outside_gb_count += country['signature_count']

    print('{} votes outside Great Britain'.format(outside_gb_count))

    outside_scot_count = 0
    for constituency in response.json()['data']['attributes']['signatures_by_constituency']:
        # If the constituency is not in Scotland
        if constituency['ons_code'][:1] != 'S':
            outside_scot_count += constituency['signature_count']

    print('{} votes outside Scotland'.format(outside_scot_count))

    total_count_outside_scotland = outside_gb_count + outside_scot_count

    print('{} votes that don\'t matter to this petition'.format(total_count_outside_scotland))


if __name__ == "__main__":
    main()
