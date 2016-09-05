from lxml import html
import requests

import os
from slackclient import SlackClient


BOT_NAME = 'menubot'


page = requests.get('https://clients.eurest.ch/fr/rts-geneve/home')
tree = html.fromstring(page.content)

def s(a):
	return a.strip()

menu="\n".join(filter(lambda x: x, map(s, tree.xpath("//div[@class='todays-menu']//text()"))))

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
slack_client.api_call("chat.postMessage", channel="geneva", text=menu, as_user=True)
