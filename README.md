# asvs-report-defect-dojo


Engagment Create Mode
1. Create New Engagement
2. Import Scan with existing Engagement with flag -id
3. Update Engagement with Argument -name if existing


# Generate requirements.txt
pip3 freeze > requirements.txt


# Generate Directory

python3 main.py generate_directory -url 'https://defectdojo.vira.sh' -token 'f59a685e5f318b175d8b3f485fb3a34efad88363'


# Import Scan Sample

python3 main.py upload_scans -name 'skywalker' -description 'Sabbzz' -version '1.0.0' -first_contacted '2022-01-01' -target_start '2022-01-01' -target_end '2022-01-01' -reason 'No Reason’ -tracker ‘https://pen-stage.udata.id/page/loginsdvc' -test_strategy 'https://pen-stage.udata.id/page/loginsdvc' -threat_model 'true' -api_test 'true' -pen_test 'true' -check_list 'true' -status 'Not Started' -engagement_type 'Interactive'  -build_id '1.0.0' -commit_hash '' -branch_tag '' -source_code_management_uri 'https://pen-stage.udata.id/page/loginsdvc' -deduplication_on_engagement 'true' -lead 1 -requester '' -preset '' -report_type '' -product 1 -build_server '' -source_code_management_server '' -orchestration_engine '' -scan_date '2021-12-08' -minimum_severity 'Medium' -active 'true' -verified 'true' -report_source 'reports' -url 'https://defectdojo.vira.sh' -token 'f59a685e5f318b175d8b3f485fb3a34efad88363'


# Import Scan Minimum

python3 main.py upload_scans -name 'Fifteen52' -description 'Sabbil 2' -first_contacted '2022-02-01' -target_start '2022-01-05' -target_end '2022-10-05' -product 1 -scan_date '2021-05-01' -minimum_severity 'Medium' -active 'true' -verified 'true' -report_source 'reports' -url 'https://defectdojo.vira.sh' -token 'f59a685e5f318b175d8b3f485fb3a34efad88363'


# Optional

* -close_old_findings
* -skip_duplicates
* -environment
* -service


# Add report.xml.settings, Remove payload if you dont use it

{
    "close_old_findings": true,
    "skip_duplicates": true,
    "tags": "test1,test2",
    "endpoint_to_add": 3,
    "push_to_jira": true,
    "environment": "Staging",
    "version": "7",
    "api_scan_configuration": "",
    "service": "",
    "group_by": "component_name"
}



python3 main.py upload_scans -name https://gitlab.playcourt.id/trace/backend/trace-inbox.git -tags https://gitlab.playcourt.id/trace/backend/trace-inbox.git -service https://gitlab.playcourt.id/trace/backend/trace-inbox.git -build_id 89 -branch_tag master -commit_hash 487636058a03ff577d35f59bc4546305d375f5d2 -deduplication_on_engagement true -source_code_management_uri https://gitlab.playcourt.id/trace/backend/trace-inbox.git -target_start 2021-12-22 -target_end 2021-12-22 -product 1 -scan_date 2021-12-22 -minimum_severity Info -status Completed -active true -verified false -report_source reports -token 'f59a685e5f318b175d8b3f485fb3a34efad88363' -url https://defectdojo.vira.sh