# 

# Run app in local

### create virtual environment

```
python -m venv venv
```

### activate venv

```
source venv/bin/activate
```

### create file .env from .env.example

```
cp .env.example .env
nano .env
# ganti host, port, dbuser, dbpassword, dbname
```

### install requirement

```
pip install -r requirements.txt
```

### run migration

```
alembic upgrade head
```

### run app

```
uvicorn app.main:app --reload
```

### open app

```
http://localhost:8000
```

### open documentation

```
http://localhost:8000/docs
```

### unit test

```
pytest
```


\

# Access Endpoint Demo

### Login

```bash
POST http://194.233.69.244:2040/token
Content-Type: multipart/form-data; 
username: admin
password: password
```

```bash
# response
{
    "message": "Login successful",
    "status_code": 200,
    "success": 1,
    "data": {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzY3NTA3MDksImRhdGEiOnsidXNlcm5hbWUiOiJhZG1pbiIsImlkIjoxLCJyb2xlIjoic3VwZXJhZG1pbiIsImNyZWF0ZWRfYnkiOm51bGwsInVwZGF0ZWRfYnkiOm51bGwsImZ1bGxuYW1lIjoiYWRtaW5pc3RyYXRvciIsImlzX2FjdGl2ZSI6ZmFsc2UsImNyZWF0ZWRfYXQiOiIyMDI1LTAxLTEzVDA0OjAyOjA0LjM2ODcwMiIsInVwZGF0ZWRfYXQiOiIyMDI1LTAxLTEzVDA0OjAyOjA0LjM2ODczOCJ9fQ.jxMtSlYbDi5KCFqVAILji94ra9qh7cPCqfCLdOomAJQ",
        "token_type": "bearer"
    }
}
```


## Content

untuk endpoint /content \nget & get by id → bisa diakses tanpa token\npost, put, delete by id →

### Get All

```json
GET http://194.233.69.244:2040/content
```

```json
# response 
{
    "message": "Get data successful",
    "status_code": 200,
    "success": 1,
    "data": [
        {
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. ",
            "is_active": false,
            "updated_by": null,
            "updated_at": "2025-01-13T04:54:31.336597",
            "slug": "lorem-ipsum",
            "id": 1,
            "title": "Lorem Ipsum",
            "created_by": null,
            "created_at": "2025-01-13T04:54:31.336542"
        }
    ]
}
```

### Get By Id

```json
GET http://194.233.69.244:2040/content/1
```

```json
# response 
{
    "message": "Get data successful",
    "status_code": 200,
    "success": 1,
    "data": {
        "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. ",
        "is_active": false,
        "updated_by": null,
        "updated_at": "2025-01-13T04:54:31.336597",
        "slug": "lorem-ipsum",
        "content": "<h1>HTML Ipsum Presents</h1><p><strong>Pellentesque habitant morbi tristique</strong> senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. <em>Aenean ultricies mi vitae est.</em> Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, <code>commodo vitae</code>, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. <a href=''>Donec non enim</a> in turpis pulvinar facilisis. Ut felis.</p><h2>Header Level 2</h2><ol> <li>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</li> <li>Aliquam tincidunt mauris eu risus.</li></ol><blockquote><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus magna. Cras in mi at felis aliquet congue. Ut a est eget ligula molestie gravida. Curabitur massa. Donec eleifend, libero at sagittis mollis, tellus est malesuada tellus, at luctus turpis elit sit amet quam. Vivamus pretium ornare est.</p></blockquote><h3>Header Level 3</h3><ul> <li>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</li> <li>Aliquam tincidunt mauris eu risus.</li></ul><pre><code>#header h1 a { display: block; width: 300px; height: 80px;}</code></pre>",
        "id": 1,
        "title": "Lorem Ipsum",
        "created_by": null,
        "created_at": "2025-01-13T04:54:31.336542"
    }
}
```

### Create

```json
POST http://194.233.69.244:2040/content
--header 'Authorization: bearer <token>'
```

```json
# payload
{  
    "title": "Lorem Ipsum 2",
    "slug": "lorem-ipsum-2",
    "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. ",
    "content": "<h1>HTML Ipsum Presents</h1><p><strong>Pellentesque habitant morbi tristique</strong> senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. <em>Aenean ultricies mi vitae est.</em> Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, <code>commodo vitae</code>, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. <a href=''>Donec non enim</a> in turpis pulvinar facilisis. Ut felis.</p><h2>Header Level 2</h2><ol> <li>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</li> <li>Aliquam tincidunt mauris eu risus.</li></ol><blockquote><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus magna. Cras in mi at felis aliquet congue. Ut a est eget ligula molestie gravida. Curabitur massa. Donec eleifend, libero at sagittis mollis, tellus est malesuada tellus, at luctus turpis elit sit amet quam. Vivamus pretium ornare est.</p></blockquote><h3>Header Level 3</h3><ul> <li>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</li> <li>Aliquam tincidunt mauris eu risus.</li></ul><pre><code>#header h1 a { display: block; width: 300px; height: 80px;}</code></pre>",
    "is_active": true
}
```

```json
# response
{
    "message": "Create data successful",
    "status_code": 200,
    "success": 1,
    "data": {
        "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. 2",
        "is_active": false,
        "updated_by": null,
        "updated_at": "2025-01-13T06:14:57.563428",
        "slug": "lorem-ipsum-2",
        "content": "<h1>HTML Ipsum Presents</h1><p><strong>Pellentesque habitant morbi tristique</strong> senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. <em>Aenean ultricies mi vitae est.</em> Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, <code>commodo vitae</code>, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. <a href=''>Donec non enim</a> in turpis pulvinar facilisis. Ut felis.</p><h2>Header Level 2</h2><ol> <li>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</li> <li>Aliquam tincidunt mauris eu risus.</li></ol><blockquote><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus magna. Cras in mi at felis aliquet congue. Ut a est eget ligula molestie gravida. Curabitur massa. Donec eleifend, libero at sagittis mollis, tellus est malesuada tellus, at luctus turpis elit sit amet quam. Vivamus pretium ornare est.</p></blockquote><h3>Header Level 3</h3><ul> <li>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</li> <li>Aliquam tincidunt mauris eu risus.</li></ul><pre><code>#header h1 a { display: block; width: 300px; height: 80px;}</code></pre>",
        "id": 2,
        "title": "Lorem Ipsum 2",
        "created_by": null,
        "created_at": "2025-01-13T06:14:57.563376"
    }
}
```

### Update By Id

```json
POST http://194.233.69.244:2040/content/1
--header 'Authorization: bearer <token>'
```

```json
# payload
{  
    "title": "Lorem Ipsum Change",
    "slug": "lorem-ipsum-change",
    "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. change",
    "content": "<h1>HTML Ipsum Presents</h1><p><strong>Pellentesque habitant morbi tristique</strong> senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. <em>Aenean ultricies mi vitae est.</em> Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, <code>commodo vitae</code>, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. <a href=''>Donec non enim</a> in turpis pulvinar facilisis. Ut felis.</p><h2>Header Level 2</h2><ol> <li>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</li> <li>Aliquam tincidunt mauris eu risus.</li></ol><blockquote><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus magna. Cras in mi at felis aliquet congue. Ut a est eget ligula molestie gravida. Curabitur massa. Donec eleifend, libero at sagittis mollis, tellus est malesuada tellus, at luctus turpis elit sit amet quam. Vivamus pretium ornare est.</p></blockquote><h3>Header Level 3</h3><ul> <li>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</li> <li>Aliquam tincidunt mauris eu risus.</li></ul><pre><code>#header h1 a { display: block; width: 300px; height: 80px;}</code></pre>",
    "is_active": false
}
```

```json
# response
{
    "message": "Update data successful",
    "status_code": 200,
    "success": 1,
    "data": {
        "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. change",
        "is_active": false,
        "updated_by": null,
        "updated_at": "2025-01-13T04:54:31.336597",
        "slug": "lorem-ipsum-change",
        "content": "<h1>HTML Ipsum Presents</h1><p><strong>Pellentesque habitant morbi tristique</strong> senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. <em>Aenean ultricies mi vitae est.</em> Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, <code>commodo vitae</code>, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. <a href=''>Donec non enim</a> in turpis pulvinar facilisis. Ut felis.</p><h2>Header Level 2</h2><ol> <li>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</li> <li>Aliquam tincidunt mauris eu risus.</li></ol><blockquote><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus magna. Cras in mi at felis aliquet congue. Ut a est eget ligula molestie gravida. Curabitur massa. Donec eleifend, libero at sagittis mollis, tellus est malesuada tellus, at luctus turpis elit sit amet quam. Vivamus pretium ornare est.</p></blockquote><h3>Header Level 3</h3><ul> <li>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</li> <li>Aliquam tincidunt mauris eu risus.</li></ul><pre><code>#header h1 a { display: block; width: 300px; height: 80px;}</code></pre>",
        "id": 1,
        "title": "Lorem Ipsum Change",
        "created_by": null,
        "created_at": "2025-01-13T04:54:31.336542"
    }
}
```

### Delete By Id

```json
DELETE http://194.233.69.244:2040/content/1
--header 'Authorization: bearer <token>'
```


## User

untuk endpoint /user\nsemua method get, post, put, delete memerlukan token

### Get All

```json
GET http://194.233.69.244:2040/user
--header 'Authorization: bearer <token>'
```

```json
# response
{
    "message": "Get data successful",
    "status_code": 200,
    "success": 1,
    "data": [
        {
            "id": 1,
            "role": "superadmin",
            "created_by": null,
            "updated_by": null,
            "fullname": "administrator",
            "username": "admin",
            "is_active": false,
            "created_at": "2025-01-13T04:02:04.368702",
            "updated_at": "2025-01-13T04:02:04.368738"
        }
    ]
}
```

### Get By Id

```json
GET http://194.233.69.244:2040/user/1
--header 'Authorization: bearer <token>'
```

```json
# response
{
    "message": "Get data successful",
    "status_code": 200,
    "success": 1,
    "data": {
        "id": 1,
        "role": "superadmin",
        "created_by": null,
        "updated_by": null,
        "fullname": "administrator",
        "username": "admin",
        "is_active": false,
        "created_at": "2025-01-13T04:02:04.368702",
        "updated_at": "2025-01-13T04:02:04.368738"
    }
}
```

### Create

```json
POST http://194.233.69.244:2040/user
--header 'Authorization: bearer <token>'
```

```json
# payload
{  
    "username": "gelar",
    "password": "password",
    "fullname": "gelar aditya",
    "role": "viewer",
    "is_active": true
}
```

```json
# response 
{
    "message": "Create data successful",
    "status_code": 200,
    "success": 1,
    "data": {
        "id": 2,
        "role": "viewer",
        "created_by": null,
        "updated_by": null,
        "fullname": "gelar aditya",
        "username": "gelar",
        "is_active": false,
        "created_at": "2025-01-13T06:37:34.845259",
        "updated_at": "2025-01-13T06:37:34.845367"
    }
}
```

### Update by Id

```json
Put http://194.233.69.244:2040/user/2
--header 'Authorization: bearer <token>'
```

```json
# payload
{  
    "username": "gelar2",
    "password": "password2",
    "fullname": "gelar aditya 2",
    "role": "viewer",
    "is_active": true
}
```

```json
# response
{
    "message": "Update data successful",
    "status_code": 200,
    "success": 1,
    "data": {
        "id": 2,
        "role": "viewer",
        "created_by": null,
        "updated_by": null,
        "fullname": "gelar aditya 2",
        "username": "gelar2",
        "is_active": false,
        "created_at": "2025-01-13T06:37:34.845259",
        "updated_at": "2025-01-13T06:37:34.845367"
    }
}
```

### Delete By Id

```json
DELETE http://194.233.69.244:2040/user/2
--header 'Authorization: bearer <token>'
```


\

\
# Developer notes

### add env to file requirements

```
pip freeze > requirements.txt
```

### alembic init

```
alembic init alembic
```

### create migration

```
alembic revision --autogenerate -m "migration message"
```

### run migration

```
alembic upgrade head
```