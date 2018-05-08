$(function() {
  $("#get-value").submit(function(event){
    event.preventDefault()
    $.ajax({
      url: 'http://localhost:5000/getpairs',
      type: 'get',
      data: {key: event.target.sKey.value},
      success: function(data){
        $("#test").text(data)
      }
      })
    // $("ul").append("<li><div class='key-column'>har</div><div class='value-column'>hardyhar</div></li>")
  })
  $("#submit-pair").submit(function(event){
    event.preventDefault()
    $.ajax({
      url: 'http://localhost:5000/setpairs',
      type: 'post',
      data: {key: event.target.gKey.value, value: event.target.value.value},
      success: function(data){
        console.log('res, ', data)
      }
    })
  })
  $("#login-form").submit(function(event){
    event.preventDefault()
    $.ajax({
      url: 'http://localhost:5000/login',
      type: 'post',
      data: {username: event.target.username.value, password: event.target.password.value},
      success: function(data){
        window.location.reload()
      },
      error: function(data) {
        $("#password-failed").text('Incorrect Password')
      }
    })
  })
  $("#signup-form").submit(function(event){
    event.preventDefault()
    $.ajax({
      url: 'http://localhost:5000/signup',
      type: 'post',
      data: {username: event.target.username.value, password: event.target.password.value},
      success: function(data){
        window.location.reload()
      },
      error: function(data) {
        $("#signup-failed").text('username taken')
      }
    })
  })
})
// use .append on the ul #data-list, make sure it updates as we go

// handle returns?
