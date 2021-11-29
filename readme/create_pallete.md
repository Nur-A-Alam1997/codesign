**Create Pallete**
----
  Returns json data about a single user.

* **URL**

  /api/v1/create

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**
 

* **Data Params**

  ```json
  {
      "name": "PalleteCynaPin",
      "dominant": ['1','3'],
      "accent": ['2','4'],
      "state" : true
}
 ```

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
```json
{
    "message":"pallete created"
}
```
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

* **Sample Call:**

  ```
curl -X POST -H 'Content-Type: application/json'\
 -d '{"name": "PalleteCynaPin",\
 "dominant": ['1','3'],\
 "accent": ['2','4'],\
 "state" : true}'\
  http://"admin":"1234"@localhost:5000/api/v1/create
  ```