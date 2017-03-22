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

    scot_count = 0
    eng_count = 0
    wales_count = 0
    ni_count = 0

    country_codes = []

    for constituency in response.json()['data']['attributes']['signatures_by_constituency']:
        country_code = constituency['ons_code'][:1]
        constituency_count = constituency['signature_count']

        if country_code not in country_codes:
            country_codes.append(country_code)

        if country_code == 'S':
            scot_count += constituency_count
        elif country_code == 'E':
            eng_count += constituency_count
        elif country_code == 'W':
            wales_count += constituency_count
        elif country_code == 'N':
            ni_count += constituency_count

    total_signatures = response.json()['data']['attributes']['signature_count']

    print('{} Scottish Votes'.format(scot_count))
    print('{} English Votes'.format(eng_count))
    print('{} Welsh Votes'.format(wales_count))
    print('{} N.I Votes'.format(ni_count))

    total_count_outside_scotland = outside_gb_count + eng_count + wales_count + ni_count

    print('{} votes OUTSIDE Scotland'.format(total_count_outside_scotland))


if __name__ == "__main__":
    main()
