
<h1>Сервис терминологии</h1>

<h2>Описание:</h2>

<h3>Технологии:</h3>
python 3<br>
django 2.2<br>
django rest framework 3.9.2<br>
vagrant 2.2.18<br>
<br>
<h3>Логин и пароль для входа в панель администрирования:</h3>

<b>login:</b> admin<br>
<b>password:</b> password


<h3>К сервису терминологии был разработан API имеющий следующие функции:</h3>
<h4>-Получение списка справочников.</h4>
<h5>Пример запроса:</h5>
<em>/directories</em>
<h5>Примеры ответа:</h5>
<p>
<pre>
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "ident": "1",
            "name": "Виды медицинской помощи",
            "short_name": "Виды медпомощи",
            "description": "Перечень видов медицинской помощи",
            "version": "1",
            "start_date": "2021-07-13"
        }
    ]
}
</pre>
<h4>-Получение списка справочников, актуальных на указанную дату</h4>
<h5>Параметры:</h5>
<table>
  <tr>
    <th>Name</th>
    <th>Type</th>
    <th>Required</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>start_date</td>
    <td>date</td>
    <td>No</td>
    <td>yyyy-mm-dd</td>
  </tr>
</table>
<h5>Пример запроса:</h5>

<em>/directories/2003-12-02</em>
<h5>Примеры ответа:</h5>
<p>
<pre>
[
    {
        "ident": "1",
        "name": "Виды медицинской помощи",
        "short_name": "Виды медпомощи",
        "description": "Перечень видов медицинской помощи",
        "version": "1",
        "start_date": "2021-07-13"
    }
]
</pre>
<h4>-Получение элементов заданного справочника текущей версии</h4>
<h5>Параметры:</h5>
<table>
  <tr>
    <th>Name</th>
    <th>Type</th>
    <th>Required</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>id</td>
    <td>varchar</td>
    <td>No</td>
    <td>id</td>
  </tr>
</table>
<h5>Пример запроса:</h5>

<em>/directory_items/1</em>
<h5>Примеры ответа:</h5>
<p>
<pre>
[
    {
        "id": 1,
        "parent": 1,
        "element_code": "1",
        "value": "первичная медико-санитарная помощь"
    },
    {
        "id": 2,
        "parent": 1,
        "element_code": "2",
        "value": "специализированная, в том числе высокотехнологичная, медицинская помощь"
    },
    {
        "id": 3,
        "parent": 1,
        "element_code": "3",
        "value": "скорая, в том числе скорая специализированная, медицинская помощь"
    },
    {
        "id": 4,
        "parent": 1,
        "element_code": "4",
        "value": "паллиативная медицинская помощь"
    }
]
</pre>
<h4>-Валидация элементов заданного справочника текущей версии</h4>
<h4>-Получение элементов заданного справочника указанной версии</h4>
<h4>-Валидация элемента заданного справочника по указанной версии</h4>

В API реализован постраничный вывод результата (по 10 элементов в странице)

Предусмотрена панель администрирования для добавления новых справочников, новых версий справочников.  
