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
    console.log('key:::', event.target.gKey.value)
    $.ajax({
      url: 'http://localhost:5000/setpairs',
      type: 'post',
      data: {key: event.target.gKey.value, value: event.target.value.value},
      success: function(data){
        console.log('res, ', data)
      }
    })
  })
})
// use .append on the ul #data-list


// need a submit function defined here, attached to the form. have it do the set, then do another get so we have an updated version

// then we add log in

// and also look more into the database persistence then, maybe same time as login
