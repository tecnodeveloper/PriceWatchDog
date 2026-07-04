# WebScrapping Fundamentals

- web scrapping is like getting data from website using tools like seliunum
- Html structure extraction is like parsing html DOM to find specific element.
  1. First HTML page is downloaded
  2. parsed HTML element into DOM
  3. if we want to extract table Then we search for specific data from page tag like `<table>` we target identifiers
  4. [Fetch URL]->[Extract Plain text]->[Build HTML DOM]->[Query Targets]->[Clean & Store]
- Static website are deliverd exactly as they stored in server no database connection is made like portfollio. Dynamic website are those in which data is fetched from database through api and rendered from server like draza.
- In server side rendering the web server process the data and build the complete html page before sending to user page. [Browser Request]->[Server Process the data from database]->[Build HTML page]->[Send html webpage back to browser]
- In client side rendering the browser download the blank html shell and javascript bundle from web server and then client browser runs the javascript and html page. [Browser request]->[webserver gives blank html + large bundle javascript]->[browser runs html and give Async API request + data payload to server]->[Data load on client DOM]
  [Client_Server Architecture](img/Client_Server Architecture.jpg)
- Api based data loading means getting data from outside server to your local application by using get post method.
- There are four http request that browser can make
  1. get is used to get data from database. it send data through url.
  2. post is used to store data in database it send data through request body, password and secrets keys are transfer through post
  3. put/patch put replaces entire resource and patch update the modification part only
  4. delete method delete the data
- [http header](https://blog.postman.com/what-are-http-headers/) are metadata that send with the request body to browser with every request you make on internet
- Cookies and sessions
  1. request headers
  - GET /signup
  - host: localhost
  - User Agent: Mazilla firefox 2.0..
  - accept: application/json
  - content Type: application/json
  - authorization: beaver tokken, jwt tokken...
  2. response header
  - HTTP/1.1 200
  - content length: 230
  - setCookie: sessionId
- learn status code that are important
  1. 200-succesfull request (Your request successfully reach server)
  2. 201-successfully created user (You have successfully created new user like post signup request)
  3. 404-Not found (when user have put random text in url then server don't find this route So it throw error)
  4. 500-Internal server error (It's mostly happen in server side like network connection or bug in app)
  5. 403-Forbidden (It's like authorization error if you have login as user role you cannot access the admin feature )
  6. 429-Rate limit (Mostly server has rate limiting like you can send 10 request from same ip address in one second your rate limit can be custom )
