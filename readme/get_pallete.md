**Show Single Pallete**
----
  Returns json data about a single Pallete.

* **URL**

  `/api/v1/pallete/:pid`

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `pid`

* **Data Params**

  `None`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
```json
{
    "pid": "5",
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
    "accent_array": [
        0,
        0,
        1,
        1,
        0,
        0,
        0,
        0
    ],
    "dominant_array": [
        0,
        0,
        1,
        1,
        0,
        0,
        0,
        0
    ],
    "state": true,
    "name": "PalleteCynaPin",
    "owner": "admin",
    "user": "admin",
    "bookmark": null
}
```
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "Pallete doesn't exist" }`

  OR
<!-- 
  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }` -->



* **Sample Call:**
```
    curl http://"admin":"1234"@localhost:5000/api/v1/pallete/5
```