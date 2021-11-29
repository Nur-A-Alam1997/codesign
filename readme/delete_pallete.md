**Delete Pallete**
----
  Returns json data about confirmation of deleted pallete.

* **URL**

  `/api/v1/pallete/:pid`

* **Method:**

  `DELETE`
  
*  **URL Params**

   **Required:**
 
   `pid`

* **Data Params**

  `None`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
```JSON{
  "message": "Pallete deleted"
  }
```

* **Error Response:**
  * **Code:** 404 NOT AVAILABLE <br />

```JSON
{
  "message": "not found"
}
```

* **Code:** 401 UNAUTHORIZED <br />
    **Content:** 
```JSON
{ 
        "error" : "You are unauthorized to make this request." 
        }
```

* **Sample Call:**
  ```
  curl -X DELETE http://"admin":"1234"@localhost:5000/api/v1/pallete/5
  ```