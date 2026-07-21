from jira import JIRA


def create_jira_issue(summary, description):
    """פתיחת כרטיס באג אוטומטי ב-Jira בעת כישלון טסט"""
    jira_options = {'server': 'https://your-domain.atlassian.net'}
    jira = JIRA(options=jira_options, basic_auth=('your-email@example.com', 'YOUR_JIRA_API_TOKEN'))

    issue_dict = {
        'project': {'key': 'QA'},
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Bug'},
    }
    new_issue = jira.create_issue(fields=issue_dict)
    print(f"🐞 נפתח באג אוטומטי ב-Jira: {new_issue.key}")
    return new_issue.key