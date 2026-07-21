import os
from jira import JIRA

# קריאת הנתונים ממשתני הסביבה (אם לא קיימים, ישתמש בברירת המחדל)
JIRA_URL = os.getenv("JIRA_URL", "https://amaliya-kdrama.atlassian.net")
JIRA_EMAIL = os.getenv("JIRA_EMAIL", "amaliyas741@gmail.com")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")  # מגיע בבטחה מ-GitHub Secrets או מהסביבה המקומית
PROJECT_KEY = "SCRUM"


def create_jira_issue(summary, description):
    """פונקציה המייצרת כרטיס באג אוטומטי ב-Jira כאשר טסט נכשל"""
    if not JIRA_TOKEN:
        print("⚠️ אזהרה: JIRA_TOKEN אינו מוגדר במערכת. לא ניתן לפתוח באג ב-Jira.")
        return None

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