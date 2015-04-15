# lolcomp/helpers.py

from ws.models import *
import os, re, json

# CONSTANTS
CST = {
    'lolcomp_analyzed_champs': 'Lolcomp_Analyzed_Champs',
    'config': 'Config',
    'tag_defs': 'Tag_Definitions',
    'relation_defs': 'Relation_Definitions',
    'urf_matches': 'Urf_Matches',
    'synergy': 'Synergy',
    'counter': 'Counter',
    'tag': 'Tag',
    'exception': 'Exception',
    'region': os.environ.get('DEFAULT_REGION', ''),
    'ver': os.environ.get('DEFAULT_VERSION', ''),
    'protocol': 'https',
    'host': 'global.api.pvp.net'
}

API = {
    'static_data': CST['protocol']+'://'+CST['host']+'/api/lol/static-data/'+CST['region']+CST['ver']+'champion'
}

# Helper Fn
def im_jarvan():
    return 'im helping'

def static_create(arg):
    new_singleton = Static(label=arg['label'], definition=arg['definition'])
    new_singleton.save()
    return

def get_info(champ, skill):
    champ = Champion.objects.filter(label=champ)[0]
    if(skill == 4):
        info_label = 'sanitizedDescription'
    else:
        info_label = 'sanitizedTooltip'
    info = json.loads(champ.skill_set.all()[skill].definition)[info_label]
        
    if(type(skill) == int):
        return info
    else:
        return champ

# from lolcomp.helpers import *; check_if_tag_qualifies(rule, info)
def check_if_tag_qualifies(rule, info):
    found = False
    for part in re.split(', *', rule):
        found_part = True
        for needle in re.split(' *AND *', part):
            match = re.search(needle, info)
            if(not match):
                found_part = False
                
            if found_part:
                found = True
                        
    return found