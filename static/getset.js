$(function() {
  $("#get-value").submit(function(event){
    event.preventDefault()
    $.ajax({
      url: 'http://localhost:5000/getpairs',
      type: 'get',
      data: {key: event.target.sKey.value},
      success: function(data){
        $("#get-result").text(data)
      },
      error: function(){
        $("#get-result").text('There was an error trying to retrieve the data')
      }
      })
  })
  $("#submit-pair").submit(function(event){
    event.preventDefault()
    $.ajax({
      url: 'http://localhost:5000/setpairs',
      type: 'post',
      data: {key: event.target.gKey.value, value: event.target.value.value},
      success: function(data){
        $("#set-result").text(data)
      },
      error: function(){
        $("#set-result").text('There was an error trying to retrieve the data')
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
        $("#signup-failed").text('Username Already Taken')
      }
    })
  })
})
