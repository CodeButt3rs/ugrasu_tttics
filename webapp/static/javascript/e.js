var converter = new showdown.Converter()
var text = '# Как найти ID\n' +
    'Зайдя на сайт расписания, в строке поиска браузера вы увидите подобное:\n\n' +
    '```html \n' +
    'https://www.ugrasu.ru/timetable/group/2646\n' +
    '```\n' +
    '\nВам необходимо записать **последние цифры в данной строке**.\n' +
    '\nПолучается, что ID вашей группы - `2646`\n' +
    '\nЕго и необходимо использовать\nпри заполнении формы запроса файла\nрасписания.'
var html = converter.makeHtml(text);
$(document).ready(function () {
    $('#howToFindID').html(html);
});