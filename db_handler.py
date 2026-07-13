import mysql.connector
from mysql.connector import Error

def get_db_connection():
    """פונקציה המייצרת חיבור לבסיס הנתונים MySQL"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # שם המשתמש הדיפולטיבי במחשב
            password='1234',  # הסיסמה שלך ל-MySQL
            database='qa_project'
        )
        return connection
    except Error as e:
        print(f"❌ שגיאה בהתחברות ל-MySQL: {e}")
        return None

def insert_drama(name, genre):
    """פונקציה שמכניסה דרמה חדשה לטבלה בבסיס הנתונים"""
    connection = get_db_connection()
    if connection is None:
        return False

    try:
        cursor = connection.cursor()
        query = "INSERT INTO dramas (name, genre) VALUES (%s, %s)"
        values = (name, genre)

        cursor.execute(query, values)
        connection.commit()  # שמירת השינויים בבסיס הנתונים פיזית
        print(f"🚀 הסדרה '{name}' הוכנסה בהצלחה ל-DB!")
        return True
    except Error as e:
        print(f"❌ שגיאה בהכנסת נתונים: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_drama_by_name(name):
    """פונקציה ששולפת סדרה מתוך ה-DB לפי השם שלה"""
    connection = get_db_connection()
    if connection is None:
        return None

    try:
        cursor = connection.cursor(dictionary=True)  # מחזיר את השורה כמו מילון נוח
        query = "SELECT * FROM dramas WHERE name = %s"

        cursor.execute(query, (name,))
        result = cursor.fetchone()  # שליפת השורה הראשונה שנמצאה
        return result
    except Error as e:
        print(f"❌ שגיאה בשליפת נתונים: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def mark_drama_as_watched(name):
    """פונקציה המעדכנת סדרה כ'נצפתה' (watched = True) לפי השם שלה"""
    connection = get_db_connection()
    if connection is None:
        return False

    try:
        cursor = connection.cursor()
        query = "UPDATE dramas SET watched = TRUE WHERE name = %s"

        cursor.execute(query, (name,))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"📺 הסדרה '{name}' עודכנה כנצפתה!")
            return True
        else:
            print(f"⚠️ לא נמצאה סדרה בשם '{name}' לעדכון.")
            return False
    except Error as e:
        print(f"❌ שגיאה בעדכון נתונים: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# הרצת בדיקה ידנית של הקובץ
if __name__ == "__main__":
    insert_drama("Goblin", "Fantasy")