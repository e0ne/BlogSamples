$(document).ready(function(){
    getUpdates();
    getUpdates2();
});

function getUpdates(){
    $.ajax({
        url: "/updates",
        context: document.body,
        success: function(data, xhr){
            //$(this).addClass("done");
            $("#results").append(data);
            $("#results").append("<br/>");
            setTimeout(getUpdates, 0);
        },
        error: function(){
            $("#results").append("error");
            $("#results").append("<br/>");
            setTimeout(getUpdates, 5000);
        }
    });
}

function getUpdates2(){
    $.ajax({
        url: "/updates2",
        context: document.body,
        success: function(data, xhr){
            //$(this).addClass("done");
            $("#results").append(data);
            $("#results").append("<br/>");
            setTimeout(getUpdates2, 0);
        },
        error: function(){
            $("#results").append("error");
            $("#results").append("<br/>");
            setTimeout(getUpdates2, 5000);
        }
    });
}