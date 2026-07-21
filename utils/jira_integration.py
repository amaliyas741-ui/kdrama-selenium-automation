from jira import JIRA

JIRA_URL = "https://amaliya-kdrama.atlassian.net"
JIRA_EMAIL = "amaliyas741@gmail.com"  # המייל של החשבון שלך
JIRA_TOKEN = "ATATT3xFfGF0w8BTXJh5pVHTFmffjNHlGfhgCJIQzbldRtbjfizEKr4KrfBYkB67PvlbU_sr0eXY27CftbzQHBCxS52AETq5R7j2utW17H07XRBDBH5bvy4mEl5xXKuZiZDLZxqOt9xDgvj71HiW8qxH_TkugX2QOEaiV_J9aJ9OpdD35d3VTDk=384C5B38"
PROJECT_KEY = "SCRUM"


def create_jira_issue(summary, description):
    """פונקציה המייצרת כרטיס באג אוטומטי ב-Jira כאשר טסט נכשל"""
    try:
        jira_options = {'server': JIRA_URL}
        jira = JIRA(options=jira_options, basic_auth=(JIRA_EMAIL, JIRA_TOKEN))

        issue_dict = {
            'project': {'key': PROJECT_KEY},
            'summary': summary,
            'description': description,
            'issuetype': {'name': 'Bug'},
        }

        new_issue = jira.create_issue(fields=issue_dict)
        print(f"🐞 באג חדש נפתח בהצלחה ב-Jira! מספר כרטיס: {new_issue.key}")
        return new_issue.key

    except Exception as e:
        print(f"❌ שגיאה בפתיחת באג ב-Jira: {e}")
        return None


if __name__ == "__main__":
    create_jira_issue(
        summary="טסט אוטומטי נכשל: בדיקת חיבור מ-PyCharm",
        description="בדיקה זו נשלחה אוטומטית מקוד הפייתון של הפרויקט."
    )