import requests
import engagement
import os
from argparse import ArgumentParser
from datetime import date
from time import sleep

today = date.today()
now_date = today.strftime("%Y-%m-%d")


cli = ArgumentParser()
subparsers = cli.add_subparsers(dest="subcommand")


def boolean_string(s):
    if s not in {'False', 'True'}:
        raise ValueError('Not a valid boolean string')
    return s == 'True'


def argument(*name_or_flags, **kwargs):
    return ([*name_or_flags], kwargs)


def subcommand(args=[], parent=subparsers):
    def decorator(func):
        parser = parent.add_parser(func.__name__, description=func.__doc__)
        for arg in args:
            parser.add_argument(*arg[0], **arg[1])
        parser.set_defaults(func=func)
    return decorator


@subcommand([argument("-url", type=str),
            argument("-token", nargs='?', default='', type=str), ])
def generate_directory(args):

    token = args.token
    url = args.url + '/api/v2/test_types/?limit=200'
    headers = {"Authorization": "Token " + token}

    response = requests.get(url, headers=headers)

    if(response.status_code == 403):
        print(response.json())
    else:
        scanType = response.json()['results']
        print(scanType)

        crReport = "reports"
        os.mkdir(crReport)

        for scanTypeName in scanType:
            os.mkdir(crReport + '/' + scanTypeName['name'])


@subcommand(
    [argument("-name", nargs='?', default='', type=str),
     argument("-description", nargs='?', default='', type=str),
     argument("-version", nargs='?', default='', type=str),
     argument("-first_contacted", nargs='?', default=now_date, type=str),
     argument("-target_start", nargs='?', default=now_date, type=str),
     argument("-target_end", nargs='?', default=now_date, type=str),
     argument("-reason", nargs='?', default='', type=str),
     argument("-tracker", nargs='?', default='', type=str),
     argument("-test_strategy", nargs='?', default='', type=str),
     argument("-threat_model", nargs='?', default='', type=str),
     argument("-api_test", nargs='?', default='', type=str),
     argument("-pen_test", nargs='?', default='', type=str),
     argument("-check_list", nargs='?', default='', type=str),
     argument("-status", nargs='?', default='', type=str),
     argument("-engagement_type", nargs='?', default='', type=str),
     argument("-build_id", nargs='?', default='', type=str),
     argument("-commit_hash", nargs='?', default='', type=str),
     argument("-branch_tag", nargs='?', default='', type=str),
     argument("-source_code_management_uri", nargs='?', default='', type=str),
     argument("-deduplication_on_engagement", nargs='?', default='', type=str),
     argument("-lead", nargs='?', default='', type=str),
     argument("-requester", type=str),
     argument("-preset", type=str),
     argument("-report_type", type=str),
     argument("-product", type=str),
     argument("-build_server", nargs='?', default='', type=str),
     argument("-source_code_management_server",
              nargs='?', default='', type=str),
     argument("-orchestration_engine", nargs='?', default='', type=str),

     argument("-scan_date", nargs='?', default='', type=str),
     argument("-minimum_severity", nargs='?', default='', type=str),
     argument("-active", nargs='?', default='', type=str),
     argument("-verified", nargs='?', default='', type=str),
     argument("-report_source", nargs='?', default='', type=str),
     argument("-url", type=str),
     argument("-url_import", type=str),
     argument("-token", nargs='?', default='', type=str),
     argument("-close_old_findings", nargs='?',
              default=True, type=boolean_string),
     argument("-skip_duplicates", nargs='?',
              default=False, type=boolean_string),

     argument("-tags", nargs='?', default=None, type=str),
     argument("-service", nargs='?', default='', type=str),
     argument("-environment", nargs='?', default='', type=str),
     argument("-close", nargs='?', default=False, type=boolean_string),
     argument('-no_reimport', action='store_false'),

     argument("-id", nargs='?', default=None, type=int)
     ])
def upload_scans(args):
    id = args.id
    name = args.name
    description = args.description
    version = args.version
    first_contacted = args.first_contacted
    target_start = args.target_start
    target_end = args.target_end
    reason = args.reason

    tracker = args.tracker
    test_strategy = args.test_strategy

    threat_model = args.threat_model  # 'true'
    api_test = args.api_test  # 'true'
    pen_test = args.pen_test  # 'true'
    check_list = args.check_list  # 'true'

    status = args.status  # Not Started
    engagement_type = args.engagement_type  # Interactive
    build_id = args.build_id
    commit_hash = args.commit_hash
    branch_tag = args.branch_tag

    # https://pen-stage.udata.id/page/loginsdvc
    source_code_management_uri = args.source_code_management_uri
    deduplication_on_engagement = args.deduplication_on_engagement  # true
    lead = args.lead  # 1
    requester = args.requester  # ''
    preset = args.preset  # ''

    report_type = args.report_type  # ''
    product = args.product  # 1 ******
    build_server = args.build_server  # ''
    source_code_management_server = args.source_code_management_server  # ''
    orchestration_engine = args.orchestration_engine  # ''

    scan_date = args.scan_date  # '2021-12-06'
    minimum_severity = args.minimum_severity  # Medium
    active = args.active  # true

    verified = args.verified  # true

    report_source = args.report_source  # Report File Path

    base_url = args.url
    url_import = args.url + '/api/v2/import-scan/'
    url = args.url + '/api/v2/engagements/'
    token = args.token

    close_old_findings = args.close_old_findings
    skip_duplicates = args.skip_duplicates

    tags = args.tags
    service = args.service
    environment = args.environment
    reimport = args.no_reimport

    close = args.close

    headers = {"Authorization": "Token " + token}
    data = {
        "tags": [
            tags
        ],
        "name": name,
        "description": description,
        "version": version,
        "first_contacted": first_contacted,
        "target_start": target_start,
        "target_end": target_end,
        "reason": reason,
        "tracker": tracker,
        "test_strategy": test_strategy,
        "threat_model": threat_model,
        "api_test": api_test,
        "pen_test": pen_test,
        "check_list": check_list,
        "status": status,
        "engagement_type": engagement_type,
        "build_id": build_id,
        "commit_hash": commit_hash,
        "branch_tag": branch_tag,
        "source_code_management_uri": source_code_management_uri,
        "deduplication_on_engagement": deduplication_on_engagement,
        "lead": lead,
        "requester": requester,
        "preset": preset,
        "report_type": report_type,
        "product": product,
        "build_server": build_server,
        "source_code_management_server": source_code_management_server,
        "orchestration_engine": orchestration_engine
    }

    if (tags == None):
        data.pop('tags')

    up_engagement = engagement.script(
        id=id,
        base_url=args.url,
        product=product,
        name=name,
        headers=headers,
        report_source=report_source,
        scan_date=scan_date,
        minimum_severity=minimum_severity,
        active=active,
        verified=verified,
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
        reimport=reimport,
        close=close,
        data=data)


if __name__ == "__main__":
    args = cli.parse_args()

    if args.subcommand is None:
        cli.print_help()
    else:
        args.func(args)
