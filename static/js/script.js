/*Link Test = document.getElementById("demo").innerHTML = 5 + 6;*/

let roundCalc = function($won, $lost) {
  if (
    $($won).val() == 2 ||
    ($($won).val() == 1 && $($lost).val() == 0)
  ) {
    return "won";
  } else if ($($won).val() == 1 && $($lost).val() == 1) {
    return "draw";
  } else if ($($won).val() == "" && $($lost).val() == "") {
    return "undefined";
  } else {
    return "loss";
  }
}

$(document).ready(function () {
  $(".check-fields").on("click", function () {
    var reqlength = $(".form_box").length;

    var value = $(".form_box").filter(function () {
      return this.value != "";
    });

    if (value.length >= 0 && value.length !== reqlength) {
      content = "Incomplete";
    } else {
      content = "Complete";
    }

    $("#eventstatusinput").val(content);

    var results = [];

    results.push(roundCalc(first_w, first_l), roundCalc(second_w, second_l), roundCalc(third_w, third_l), roundCalc(fourth_w, fourth_l), roundCalc(fifth_w, fifth_l));
    console.log(results);

    var roundswon = $.grep(results, function (elem) {
      return elem === "won";
    }).length;

    var roundsdrawn = $.grep(results, function (elem) {
      return elem === "draw";
    }).length;

    var roundslost = $.grep(results, function (elem) {
      return elem === "loss";
    }).length;

    $("#eventrecordinput").val(
      roundswon + " - " + roundsdrawn + " - " + roundslost
    );

    var gameswon = 0;
    $(".wonnumber").each(function () {
      gameswon = parseInt($(this).val() || 0) + gameswon;
    });

    var gamesplayed = 0;
    $(".boxnumber").each(function () {
      gamesplayed = parseInt($(this).val() || 0) + gamesplayed;
    });

    gamewinpercentage = ((gameswon / gamesplayed) * 100).toFixed(2) + "%";

    $("#eventgamewin").val(gamewinpercentage);
  });

  $("#playerhistory").on("click", function () {
    player_name = $("#playername").val();
    if (player_name.length === 0) {
      $("#myModal").modal("show");
    } else {
      window.location.href = "/player_history/" + player_name;
    }
  });
});
