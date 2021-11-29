**Edit Pallete**
----
  Returns json data about a single pallete.

* **URL**

  /api/v1/pallete/:pid

* **Method:**

  `PUT`
  
*  **URL Params**

   **Required:**
 
   `pid`

* **Data Params**
```json
{
      "name": "PalleteCynaPin",
      "dominant": ['1','3'],
      "accent": ['2','4'],
      "state" : true
 }


* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
```json
{
  "message": "Pallete edited"
}

 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ message : "Pallete doesn't exist" }`

  OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

* **Sample Call:**

    ```
    curl -X PUT  -H 'Content-Type:application/json'
    -d '{"name": "PalleteCynaPin",\
    "dominant": ['1','3'],\
    "accent": ['2','4'],\
    "state" : true}'\
    http://"admin":"1234"@localhost:5000/api/v1/pallete/1
    ```