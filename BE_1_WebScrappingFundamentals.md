# WebScrapping Fundamentals

- web scrapping is like getting data from website using tools like seliunum
- Html structure extraction is like parsing html DOM to find specific element.
  1. First HTML page is downloaded
  2. parsed HTML element into DOM
  3. if we want to extract table Then we search for specific data from page tag like `<table>` we target identifiers
  4. [Fetch URL]->[Extract Plain text]->[Build HTML DOM]->[Query Targets]->[Clean & Store]
- Static website are deliverd exactly as they stored in server no database connection is made like portfollio. Dynamic website are those in which data is fetched from database and rendered from server like draza.
- In server side rendering the web server process the data and build the complete html page before sending to user page. [Browser Request]->[Server Process the data from database]->[Build HTML page]->[Send html webpage back to browser]
- In client side rendering the browser download the blank html shell and javascript bundle from web server and then client browser runs the javascript and html page. [Browser request]->[webserver gives blank html + large bundle javascript]->[browser runs html and give Async API request + data payload to server]->[Data load on client DOM]
