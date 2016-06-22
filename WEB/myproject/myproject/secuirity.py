USERS = {'admin':'password',
          'foo':'12345'}
GROUPS = {'admin':['group:editors'], 'foo':['group:editors']}

def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])
