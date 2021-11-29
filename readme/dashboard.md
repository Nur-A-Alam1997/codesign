**Dashboard**
----
  Returns json data about all available palletes.

* **URL**

  /api/v1/dashboard

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
    ``` json
        {
            "pallete": [
                {
                    "id": 1,
                    "owner": "user1",
                    "name": "my favourite pallete",
                    "dominant": "['1', '3', '5']",
                    "accent": "['1', '2', '5']",
                    "state": true
                },
                {
                    "id": 2,
                    "owner": "user1",
                    "name": "Pallete",
                    "dominant": "['1']",
                    "accent": "['1', '2']",
                    "state": true
                }
            ]
        }
```
 
* **Error Response:**


* **Sample Call:**

    ```
    curl http://"user1":"1234"@localhost:5000/api/v1/dashboard
    ```