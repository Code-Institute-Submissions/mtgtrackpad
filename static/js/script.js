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
        /*$(template).addClass("container-fluid my-3 p-2 border sub-form");*/

        $(template).find("h6").html("Event Round " + x.toString());

        console.log("#recordsubform" + x.toString() +" :input")

        $("#clone-div").append(template)

        $("#recordsubform" + x.toString() +" input").each(function(){
            num = x
            this.id = this.id + num.toString();
            this.name = this.name + num.toString();
        });

        $("#recordsubform" + x.toString() +" label").each(function(){
            var id = $(this).attr('for');
            num = x
            console.log(id);
            $(this).attr('for', id + num.toString());
            
        });

        x++

    }); 

    $("#deletelastround").click(function(){
        i = x-1
        $("#recordsubform" + i.toString()).remove();
        x--
    });


});