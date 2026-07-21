import time
from db_handler import insert_drama, get_drama_by_name, mark_drama_as_watched

# יצירת מזהה ייחודי מבוסס זמן
timestamp = time.strftime("%H%M%S")

def test_insert_new_drama_to_db():
    """טסט 1: בודק שהכנסת סדרה חדשה ל-DB מחזירה True"""
    drama_name = f"My Demon {timestamp}"
    genre = "Romance"

    result = insert_drama(drama_name, genre)
    assert result is True, f"הטסט נכשל: לא הצלחנו להכניס את הסדרה {drama_name} ל-DB"


def test_insert_and_verify_drama():
    """טסט 2: מכניס סדרה ומאמת שהיא קיימת ב-DB עם הג'אנר הנכון"""
    target_name = f"Vincenzo {timestamp}"
    target_genre = "Dark Comedy"

    insert_result = insert_drama(target_name, target_genre)
    assert insert_result is True, "נכשל בשלב הכנסת הסדרה ל-DB"

    db_data = get_drama_by_name(target_name)

    assert db_data is not None, f"הסדרה {target_name} לא נמצאה ב-DB לאחר ההכנסה"
    assert db_data['genre'] == target_genre, f"הג'אנר ב-DB הוא {db_data['genre']} ולא תואם"
    assert db_data['watched'] == 0, "ברירת המחדל של עמודת watched הייתה אמורה להיות 0"


def test_update_drama_watched_status():
    """טסט 3: מכניס סדרה, מעדכן אותה כ'נצפתה' ומאמת שהשינוי נשמר ב-DB"""
    drama_name = f"Alchemy of Souls {timestamp}"
    genre = "Fantasy"

    insert_result = insert_drama(drama_name, genre)
    assert insert_result is True, "נכשל בהכנסת הסדרה"

    update_result = mark_drama_as_watched(drama_name)
    assert update_result is True, "הפונקציה נכשלה בביצוע העדכון ב-DB"

    updated_data = get_drama_by_name(drama_name)

    assert updated_data is not None, "הסדרה לא נמצאה ב-DB"
    assert updated_data['watched'] == 1, f"הסטטוס ב-DB הוא {updated_data['watched']} במקום 1"