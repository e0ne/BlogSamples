$(document).ready(function(){
    getUpdates();
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