import requests
import os
import mimetypes
import scan
import json
import re


def script(**var):
    id = var['id']
    base_url = var['base_url']
    product = var['product']
    name = var['name']
    headers = var['headers']
    report_source = var['report_source']
    scan_date = var['scan_date']
    minimum_severity = var['minimum_severity']
    active = var['active']
    verified = var['verified']
    token = var['token']
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
    close = var['close']
    data = var['data']

    try:
        engID = preparingEngID(base_url, product, name,
                               headers, data, id, close, token)
        import_scans(
            report_source=report_source,
            scan_date=scan_date,
            minimum_severity=minimum_severity,
            active=active,
            verified=verified,
            engID=engID,
            base_url=base_url,
            token=token,
            lead=lead,
            build_id=build_id,
            branch_tag=branch_tag,
            commit_hash=commit_hash,
            close_old_findings=close_old_findings,
            skip_duplicates=skip_duplicates,
            tags=tags,
            service=service,
            environment=environment,
            reimport=reimport)
    except Exception as error:
        print('Exception', error)


def preparingEngID(base_url, product, name, headers, data, id, close, token):
    urlCheck = base_url + '/api/v2/engagements/?product=' + product + '&name=' + name
    responseCheck = requests.get(urlCheck, headers=headers)
    engFound = responseCheck.json()

    # if id not set
    if(id is None):
        # if name & product not found Create New
        if(engFound['count'] == 0):
            print("Create New Engagement ...")
            url = base_url + '/api/v2/engagements/'
            response = requests.post(url, data=data, headers=headers)
            response.raise_for_status()
            engID = response.json()['id']

            # if close true = Close Eng
            if(close):
                engID = str(response.json()['id'])
                urlClose = base_url + '/api/v2/engagements/' + engID + '/close/'
                responseClose = requests.post(urlClose, headers=headers)

        # If name & product found Replace
        else:
            print("Update Patch ...")

            engID = engFound['results'][0]['id']

            data.pop('first_contacted')
            data.pop('target_start')

            url = base_url + '/api/v2/engagements/' + str(engID) + '/'
            response = requests.patch(url, data=data, headers=headers)
            response.raise_for_status()

    # If id is set insert existing Engagement
    else:
        print("Insert Existing ...")
        engID = id

    return engID


def import_scans(**var):

    report_source = var['report_source']
    scan_date = var['scan_date']
    minimum_severity = var['minimum_severity']
    active = var['active']
    verified = var['verified']
    engID = var['engID']
    base_url = var['base_url']
    token = var['token']
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

    reportsTypeArr = [name for name in os.listdir(report_source)]
    for reportsType in reportsTypeArr:
        if reportsType.startswith('.'):
            continue

        scan_type = reportsType
        reportsFile = [name for name in os.listdir(
            'reports/' + reportsType)]
        if not (reportsFile):
            continue

        for reportsFile in reportsFile:
            if reportsFile.startswith('.'):
                continue

            x = re.search("\\.settings$", reportsFile)
            if (x):
                continue

            reportFileName = reportsFile
            reportFilePath = 'reports/' + reportsType + '/' + reportsFile
            reportFilePathSettings = 'reports/' + \
                reportsType + '/' + reportsFile + '.settings'

            fileExists = os.path.exists(
                reportFilePathSettings)

            if(fileExists):
                f = open(reportFilePathSettings)
                dataSettings = json.load(f)
            else:
                dataSettings = {}

            print("Uploading " + reportFileName + ' ...')
            file_type = mimetypes.guess_type(
                reportFilePath)[0]
            resputScan = scan.script(
                scan_date=scan_date,
                minimum_severity=minimum_severity,
                active=active,
                verified=verified,
                scan_type=scan_type,
                reportFileName=reportFileName,
                reportFilePath=reportFilePath,
                file_type=file_type,
                engID=engID,
                base_url=base_url,
                token=token,
                dataSettings=dataSettings,
                lead=lead,
                build_id=build_id,
                branch_tag=branch_tag,
                commit_hash=commit_hash,
                close_old_findings=close_old_findings,
                skip_duplicates=skip_duplicates,
                tags=tags,
                service=service,
                environment=environment,
                reimport=reimport)

            print(resputScan + '\nUpload ' +
                  reportFileName + ' Complete\n')
