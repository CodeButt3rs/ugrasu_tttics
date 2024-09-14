from ics import Calendar, Event
import requests 
import json

base_url = "https://www.ugrasu.ru/api/directory/lessons"

def request_lessons(groupOid: int, fromdate: str, todate: str) -> list[object]:
    query = {
        'groupOid': groupOid,
        'fromdate': fromdate,
        'todate': todate
    }

    base_url = "https://www.ugrasu.ru/api/directory/lessons"
    lessons = requests.get(
        url=base_url,
        params=query
    )
    lessons.encoding = 'utf-8'
    lessons_json = json.loads(lessons.content.decode('utf-8'))
    return lessons_json

def make_calendar(**kwargs):

    file_name = f"{kwargs.get('groupOid')}-{kwargs.get('fromdate')}-{kwargs.get('todate')}.ics"

    lessons = request_lessons(**kwargs)
    calendar = Calendar()

    for i in lessons:
        e = Event()
        e.name = f"{i['discipline']} - {i['kindOfWork']} - {i['auditorium']}"
        e.begin = f"{i['date'].replace('.','-')}T{i['beginLesson']}:00+05:00"
        e.end = f"{i['date'].replace('.','-')}T{i['endLesson']}:00+05:00"
        calendar.events.add(e)

    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(calendar.serialize_iter())
    return file_name
    