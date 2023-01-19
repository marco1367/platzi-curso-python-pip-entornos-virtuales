import requests

def get_categories():
    path = 'https://api.escuelajs.co/api/v1/categories'

    r = requests.get(path)
    
    # print('status => ', r.status_code)
    print('categories =>', r.text)
    
    categories = r.json()
    # print(type(categories))
    # print(type(categories[0]))
    # print (categories)
    for category in categories:
        # print(category['name'])
        print(category)
        print('*'.center(10, '*'))
