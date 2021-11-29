**Create Pallete**
----
  Returns json data about a single user.

* **URL**

  /api/v1/create

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
```json
{
    "dominant": [
        {
            "id": 1,
            "color": "red"
        },
        {
            "id": 2,
            "color": "blue"
        },
        {
            "id": 3,
            "color": "green"
        },
        {
            "id": 4,
            "color": "yellow"
        },
        {
            "id": 5,
            "color": "purple"
        },
        {
            "id": 6,
            "color": "indigo"
        },
        {
            "id": 7,
            "color": "orange"
        }
    ],
    "accent": [
        {
            "id": 1,
            "color": "red"
        },
        {
            "id": 2,
            "color": "blue"
        },
        {
            "id": 3,
            "color": "green"
        },
        {
            "id": 4,
            "color": "yellow"
        },
        {
            "id": 5,
            "color": "purple"
        },
        {
            "id": 6,
            "color": "indigo"
        },
        {
            "id": 7,
            "color": "orange"
        }
    ],
    "user": "user1"
}
``` 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

* **Sample Call:**

    ```
    curl  http://"user1":"1234"@localhost:5000/api/v1/create
    ```