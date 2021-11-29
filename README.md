### clone the file:
>git clone https://github.com/Nur-A-Alam1997/design.git 

* change to codesign directory

### installation:
>pip install -r requirement.txt

### create database (only ones):
>python setup.py

### build:
>python app.py

<!-- ### route:
>'http://127.0.0.1:5000/api/v1/dashboard'>

### login :
>'http://127.0.0.1:5000/api/v1/home'
* please use only predefined user for login

### logout :
>http://127.0.0.1:5000/logout
* keep password and login field empty and press sign sign in.
* go back to route  http://127.0.0.1:5000/api/v1/dashboard

### bookmark :
> <'http://127.0.0.1:5000/api/v1/bookmark/:pid> -->

### Problem Statement:
>* a REST API to create, manage, and share color palettes.

* **API Users will be able to**:
>* Browse public color palettes without login 

* **Features** <br>
`[1]`  `Create color palettes`<br>
`[2]`  `publish them to the public or make them private`<br>
`[3]`  `Save other’s palettes to favorite`<br>

* **A Palette consists of** <br>
`[1]`  `1 to 2 dominant color(s)`<br>
`[2]`  `2 to 4 accent colors(s)`<br>
`[3]`  `A name`<br>
`[4]`  `private or public state<br>`

## HTTP Response Codes
Each response will be returned with one of the following HTTP status codes:

* `200` `OK` The request was successful
* `400` `Bad Request` There was a problem with the request (security, malformed, data validation, etc.)
* `401` `Unauthorized` The supplied API credentials are invalid
* `403` `Forbidden` The credentials provided do not have permission to access the requested resource
* `404` `Not found` An attempt was made to access a resource that does not exist in the API
* `405` `Method not allowed` The resource being accessed doesn't support the method specified (GET, POST, etc.).
* `500` `Server Error` An error on the server occurred

* ** Predefined User Data to access Protected route**

```json
{
    "admin": "1234",
    "user1": "1234",
    "user2": "1234",
}
```

### Dashboard[]
- **[<code>GET</code> Dashboard list](/readme/dashboard.md)**

### Bookmark[]
- **[<code>GET</code> Bookmark list](/readme/bookmark.md)**
- **[<code>PUT</code> Update Bookmark](/readme/update_bookmark.md)**

### Pallete Resource[]
- **[<code>GET</code> GET pallete tray](/readme/create_pallete_resource.md)**

### Pallete[]
- **[<code>GET</code> Indivisual pallete](/readme/get_pallete.md)**
- **[<code>POST</code> Create pallete](/readme/create_pallete.md)**
- **[<code>PUT</code> Update pallete](/readme/update_pallete.md)**
- **[<code>DELETE</code> Delete pallete](/readme/delete_pallete.md)**
