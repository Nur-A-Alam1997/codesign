**Update bookmark**
----
  Returns json data about a bookmark.

* **URL**

  /api/v1/bookmark:pid

* **Method:**

  `PUT`
  
*  **URL Params**

   **Required:**
 
   `pid`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
```json
{
  "message": "successful changes"
}
```    

 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

* **Sample Call:**

  ```
  curl -X PUT -H "Content-Type : application/json"\
    -d'{pid:1}' http://"user1":"1234"@localhost:5000/api/v1/bookmark/1


  