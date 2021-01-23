function submit_entry(){

  var home = document.getElementById("name");
  var away = document.getElementById("message");

  var entry = {
    home: home.value
    away: away.value
  };
  fetch('/create-entry',{
    method: "POST",
    credentials: 'include',
    body: JSON.stringify(entry),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json"
    })
  })

  .then(function (response){
    response.json().then(function(data){

      console.log(data)

    })
  })
    };