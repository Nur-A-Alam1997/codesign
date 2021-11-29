**Update Pallete**
----
  Returns json data about a single user.

* **URL**

  `/api/v1/pallete/:pid`

* **Method:**

  `PUT`
  
*  **URL Params**

   **Required:**
   `pid`

* **Data Params**

```json
{
      "name": "Pallete-Cyna-Pin",
      "dominant": ['1','3','5'],
      "accent": ['2','4'],
      "state" : true
}
```

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**
    `{'message': 'Pallete edited'}`
 
* **Error Response:**
    
  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "message': 'you are not authorized to or does not exists.." }`

* **Sample Call:**

    ```
    curl  http://"user1":"1234"@localhost:5000/api/v1/create
    ```