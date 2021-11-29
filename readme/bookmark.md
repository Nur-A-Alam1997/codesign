**Bookmarks**
----
  Returns json data about a single user.

* **URL**

  /api/v1/my_bookmark

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
    "pallete": [
        {
            "id": 1,
            "owner": "user1",
            "name": "my favourite pallete"
        },
        {
            "id": 2,
            "owner": "user1",
            "name": "Pallete"
        }
    ]
}

 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "bookmark doesn't exist" }`

  OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

* **Sample Call:**
```
curl  http://"user1":"1234"@localhost:5000/api/v1/my_bookmark
