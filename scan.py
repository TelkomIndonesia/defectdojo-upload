import requests


def find_existing_test(base_url, token, engagement_id, scan_type, reportFileName):
    resp = requests.get(base_url + '/api/v2/tests/',
                        headers={"Authorization": "Token " + token},
                        params={"engagement": engagement_id})

    for test in resp.json()['results']:
        if test['scan_type'] != scan_type:
            continue
        if(reportFileName != test['title']):
            continue
        return test["id"]


def script(**var):

    scan_date = var['scan_date']
    minimum_severity = var['minimum_severity']
    active = var['active']
    verified = var['verified']
    scan_type = var['scan_type']
    reportFileName = var['reportFileName']
    reportFilePath = var['reportFilePath']
    file_type = var['file_type']
    engID = var['engID']
    base_url = var['base_url']
    token = var['token']
    dataSettings = var['dataSettings']
    lead = var['lead']
    build_id = var['build_id']
    branch_tag = var['branch_tag']
    commit_hash = var['commit_hash']
    close_old_findings = var['close_old_findings']
    skip_duplicates = var['skip_duplicates']
    tags = var['tags']
    service = var['service']
    environment = var['environment']
    reimport = var['reimport']

    payload = {'scan_date': scan_date,
               'minimum_severity': minimum_severity,
               'active': active,
               'verified': verified,
               'scan_type': scan_type,
               'engagement': engID,
               'lead': lead,
               'tags': tags,
               'build_id': build_id,
               'branch_tag': branch_tag,
               'commit_hash': commit_hash,
               'close_old_findings': close_old_findings,
               'environment': environment,
               'skip_duplicates': skip_duplicates,
               'service': service,
               'test_title': reportFileName
               }

    for dataSettingsVal in dataSettings:
        payload[dataSettingsVal] = dataSettings[dataSettingsVal]

    files = [
        ('file', (reportFileName, open(
            reportFilePath, 'rb'), file_type))
    ]
    headers = {
        "Authorization": "Token " + token,
    }

    testid = find_existing_test(
        base_url, token, engID, scan_type, reportFileName)

    if reimport and testid:
        payload["test"] = testid
        response = requests.post(
            base_url +
            '/api/v2/reimport-scan/',
            headers=headers,
            data=payload,
            files=files)
    else:
        response = requests.post(
            base_url +
            '/api/v2/import-scan/',
            headers=headers,
            data=payload,
            files=files)

    return response.text
