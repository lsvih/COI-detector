"""
This file provides a simple crawler to fetch PC List from CMT system.
"""
import requests

# Modify the following variables according to your own account.
request_url = 'https://cmt3.research.microsoft.com/api/odata/ICASSP2023/Submissions(xxxx)/ConflictSelections'
request_cookie = ''

output_file = 'pc_list.txt'


def get_pc_list():
    response = requests.get(request_url, headers={'Cookie': request_cookie})
    if response.status_code == 200:
        print(len(response.json()['value']))
        with open(output_file, 'w') as f:
            for item in response.json()['value']:
                f.write(item['FirstName'] + '\t' + item['LastName'] + '\n')
        print('Crawled {} PC members. Save to {}.'.format(len(response.json()['value']), output_file))
    else:
        print('Failed to fetch PC list.')


if __name__ == '__main__':
    get_pc_list()
