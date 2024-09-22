from ics import Calendar, Event
import requests 
import json


query_args = {
    "group": "groupOid",
    "teacher": "lecturerOid",
    "auditorium": "auditoriumOid"
}
base_url = "https://www.ugrasu.ru/api/directory/lessons"

def request_lessons(Oid: int, fromdate: str, todate: str, timetableType: str, *args, **kwargs) -> list[object]:
    query = {
        query_args[timetableType]: Oid,
        'fromdate': fromdate,
        'todate': todate
    }
    lessons = requests.get(
        url=base_url,
        params=query
    )
    lessons.encoding = 'utf-8'
    lessons_json = json.loads(lessons.content.decode('utf-8'))
    return lessons_json

def subgroup_filter(record: dict, sub_group: int):
    if (group := record.get("subGroup")):
        return group.split("/")[1] == sub_group
    return True

def make_calendar(**kwargs):

    file_name = f"{kwargs.get('Oid')}-{kwargs.get('fromdate')}-{kwargs.get('todate')}.ics"

    lessons = request_lessons(**kwargs)
    if kwargs.get("subgroup") != '0' and kwargs.get('timetableType') == 'group':
        lessons = list(filter(lambda x: subgroup_filter(x, kwargs.get("subgroup")), lessons))
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
    