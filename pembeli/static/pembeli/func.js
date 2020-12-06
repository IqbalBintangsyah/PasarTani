function change1()
{
    var elem = document.getElementById("btn1");
    if (elem.value=="subscribe") elem.value = "unsubscribe";
    else elem.value = "subscribe";
}

function change2()
{
    var elem = document.getElementById("btn2");
    if (elem.value=="subscribe") elem.value = "unsubscribe";
    else elem.value = "subscribe";
}

function change3()
{
    var elem = document.getElementById("btn3");
    if (elem.value=="subscribe") elem.value = "unsubscribe";
    else elem.value = "subscribe";
}

$.ajax({
    // points to the url where your data will be posted
    url:'/postendpoint/$',
    // post for security reason
    type: "POST",
    // data that you will like to return 
    data: {stock : stock},
    // what to do when the call is success 
    success:function(response){},
    // what to do when the call is complete ( you can right your clean from code here)
    complete:function(){},
    // what to do when there is an error
    error:function (xhr, textStatus, thrownError){}
});