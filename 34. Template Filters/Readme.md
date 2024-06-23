## Implementation and Logics of Custom Template Filter in Django

- Safe Filter : To show the actual tags

 `<h1> {{n.service_icon | safe }} | {{n.service_title | safe }} | {{n.service_des | safe }}  </h1>`

- upper : convert text to upper case. (`{{n.service_icon | upper }}`)
- lower : convert text to lower case. (`{{n.service_icon | lower }}`)
- first : gives the first letter
- wordcount : counts the word
- length : total no of letters
