from ravenrpc import Ravencoin
import json
import requests

rvn = Ravencoin('user', 'B4bgfdWk11e')

def get_price():
    markets = json.loads(requests.get('https://tradeogre.com/api/v1/markets').content.decode('utf-8')) 
    for market in markets:
        try:
            rvn_btc = market['BTC-RVN']['price']
            break
        except KeyError:
            continue

    return f'The price of Ravencoin in satoshis is **{rvn_btc}**'

def beautify_json(j):
    j = j['result']
    try:
        del j['warnings']
        del j['error']
    except:
        pass
    j = json.dumps(j, sort_keys=True, indent=4).replace('{', '').replace('}', '').replace('"', '').replace(',', '')
    return '```' + j + '```'

def blockchain_info():
    return beautify_json(rvn.getblockchaininfo())

def get_help(command):
    return '```' + rvn.help(command)['result'] + '```'