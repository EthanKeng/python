
## package: requests 

`python -m pip install requests` 

-----

## Sites 

- for REST API test:
https://jsonplaceholder.typicode.com/

- Windows cmd console: https://cmder.net/

-----

## Authentication

If you try to access the github API without authentication, you won't get the proper response. For example:
```
import requests
url="https://api.github.com/user"

```

- Go to github tokens setting :https://github.com/settings/tokens

- Generate new tokens
- Set expire days and note -- Grand "user" section
- Access with code below
```
import requests
url="https://api.github.com/user"
res = requests.get(url,headers={'Authorization':'Bearer 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'})
res.json()

```

Now you can see the response with correct info

----
