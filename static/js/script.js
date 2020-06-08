/*Link Test = document.getElementById("demo").innerHTML = 5 + 6;*/

/*$(document).ready(function() {
    $("#addnewround").click(function(){
        $("#clone-container").append($("#recordsubform").clone());
    }); 
});*/



$(document).ready(function() {

var x = 2;

    $("#addnewround").click(function(){
        var template = $("#recordtemplate")
              .clone().removeAttr("id")
              .html();

        console.log(template);

        
        template = $(template).attr("id", "recordsubform" + x.toString());
        $(template).addClass("container-fluid my-3 p-2 border sub-form");

        $(template).find("h6").html("Round " + x.toString());

        $("#clone-div").append(template)

        x++

    }); 
});