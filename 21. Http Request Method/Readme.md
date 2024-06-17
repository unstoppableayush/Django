# What are HTTP Request Methods in Django (Get & Post)

## Get Method

- The GET Method sends the encoded user information appended to the page request. The page and the encoded information are seperated bt the ? charactrer.

- Ex - https://www.wscubetech.com/index.php?name1=value1&name2=value2

- Restricted to send upto `1024 characters` only.

- Never use GET method if you have `password` or `other sensitive information`.

- Cannot be used to send `binary data`, like images or word documents, to the server.


## POST Method

- The POST method transfer infromation via `HTTP headers`. The information is encoded as descibed in case of GET method and put into a header called QUERY_STRING.

- Does `not` have any `restriction on data size` to be sent.

- Can be used to send `ASCII` as well as `binary data`.

- The data sent by POST method goes through HTTP header so `security` depends on `HTTP protocol`.

- By using `secure HTTP` you can make sure that your information is secure.



