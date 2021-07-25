from src.cwarler.sinaComment import WeiboCommentScrapy
import yaml
import argparse
import pandas as pd


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'Cookie': '_T_WM=d3ed31a8ec8b0ca0fdfcac37c73a76ae; SUB=_2A25N_-60DeRhGeRP71EY9C_MyD6IHXVvA_L8rDV6PUJbktAKLUv1kW1NUC3zBRfdFyQVO25z6xV2O4UbV6TXGxUP; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5RQEjruSr1GKnnm9kLn3Xg5NHD95QEeKB01KBpeheEWs4DqcjlIrUAi--ciK.Ri-8sIrUA; SSOLoginState=1627102948'
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser("sina commet got config")
    parser.add_argument('--header',type=str,default='data/config.yaml')
    parser.add_argument('--wids',type=str,default='data/month7.csv')
    arg = parser.parse_args()
    with open(arg.header,'r') as f:
        header = f.read()
        f.close()
    header = yaml.load(header,Loader=yaml.FullLoader)
    getor = WeiboCommentScrapy(header=header)
    with open(arg.wids,'r') as f:
        data = f.readlines()
        f.close()
    data = [i.split('\n')[0] for i in data]
    for d in data:
        getor.scrapy(d)
